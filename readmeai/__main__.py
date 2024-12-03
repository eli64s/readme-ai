#!/usr/bin/env python3

"""Orchestrates the pipeline for the README.md file generation."""

__package__ = "readmeai"

import asyncio
import contextlib
import tempfile
from collections.abc import Generator

from readmeai.config.constants import ImageOptions, LLMService
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.errors import ReadmeGeneratorError
from readmeai.generators.builder import MarkdownBuilder
from readmeai.ingestion.models import RepositoryContext
from readmeai.ingestion.pipeline import RepositoryProcessor
from readmeai.logger import get_logger
from readmeai.models.dalle import DalleHandler
from readmeai.models.factory import ModelFactory
from readmeai.postprocessor import response_cleaner
from readmeai.readers.git.repository import load_data
from readmeai.utils.file_handler import FileHandler

_logger = get_logger(__name__)


@contextlib.contextmanager
def error_handler() -> Generator[None, None, None]:
    """Error handler wrapper for the README generation process."""
    try:
        yield
    except Exception as e:
        raise ReadmeGeneratorError(e) from e


def readme_agent(config: ConfigLoader, output_file: str) -> None:
    """Wrap asyncronous README generation process with context manager."""
    with error_handler():
        asyncio.run(readme_generator(config, output_file))


async def readme_generator(settings: ConfigLoader, output_file: str) -> None:
    """Processes the repository and builds the README file."""
    config = settings.config

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_path = await load_data(config.git.repository, temp_dir)

        processor: RepositoryProcessor = RepositoryProcessor(settings=settings)

        context: RepositoryContext = await processor.process_repository(
            repo_path=repo_path
        )

        log_repository_context(context)

        async with ModelFactory.get_backend(
            settings, context
        ).use_api() as llm:
            responses = await llm.batch_request()
            (
                file_summaries,
                features,
                overview,
                tagline,
            ) = responses
            config.md.features = config.md.features.format(
                response_cleaner.format_markdown_table(features),
            )
            config.md.overview = config.md.overview.format(
                response_cleaner.process_markdown(overview),
            )
            config.md.tagline = response_cleaner.remove_quotes(tagline)

        if should_generate_image(config):
            await generate_image(config)
        if config.md.image in [None, "", ImageOptions.LLM.value]:
            config.md.image = ImageOptions.BLUE.value

        markdown_content = MarkdownBuilder(
            settings, context, file_summaries, temp_dir
        ).build()

        FileHandler().write(output_file, markdown_content)

        log_process_completion(output_file)


async def generate_image(config: Settings) -> None:
    """Generates an image using the DALL-E model."""
    async with DalleHandler(config) as dalle:
        image_url = await dalle._make_request()
        config.md.image = await dalle.download(image_url)


def should_generate_image(config: Settings) -> bool:
    """Determines if the user enabled LLM image generation."""
    return (
        config.md.image == ImageOptions.LLM.value
        and config.llm.api != LLMService.OFFLINE.value
    )


def log_repository_context(context: RepositoryContext) -> None:
    """Logs a snippet of the processed repository context data."""
    _logger.info(f"Total files analyzed: {len(context.files)}")
    _logger.info(f"Metadata extracted: {context.metadata}")
    _logger.info(f"Dependencies: {context.dependencies}")
    _logger.info(f"Languages: {context.language_counts}")


def log_process_completion(output_file: str) -> None:
    """Logs the completion of the README generation process."""
    _logger.info("README.md file generated successfully.")
    _logger.info(f"Output file saved @ {output_file}")
    _logger.info("Share with us @ github.com/eli64s/readme-ai/discussions")
