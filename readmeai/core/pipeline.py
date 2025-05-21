#!/usr/bin/env python3

"""Orchestrates the pipeline for the README.md file generation."""

__package__ = "readmeai"

import asyncio
import contextlib
import tempfile
from collections.abc import Generator

from readmeai.config.settings import ConfigLoader
from readmeai.core.errors import ReadmeGeneratorError
from readmeai.core.logger import get_logger
from readmeai.extractors.analyzer import RepositoryAnalyzer
from readmeai.extractors.models import RepositoryContext
from readmeai.generators.builder import MarkdownBuilder
from readmeai.generators.enums import CustomLogos, DefaultLogos
from readmeai.models.dalle import DalleHandler
from readmeai.models.enums import LLMProviders
from readmeai.models.factory import ModelFactory
from readmeai.postprocessor import markdown_to_html, response_cleaner
from readmeai.retrievers.git.repository import load_data
from readmeai.utilities.file_handler import FileHandler

_logger = get_logger(__name__)


@contextlib.contextmanager
def error_handler() -> Generator[None, None, None]:
    """Error handler wrapper for the README generation process."""
    try:
        yield
    except Exception as e:
        raise ReadmeGeneratorError(str(e)) from e


def readme_agent(config: ConfigLoader, output_file: str) -> None:
    """Wrap asyncronous README generation process with context manager."""
    with error_handler():
        asyncio.run(readme_generator(config, output_file))


async def readme_generator(config: ConfigLoader, output_file: str) -> None:
    """Processes the repository and builds the README file."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        repo_path = await load_data(config.config.git.repository, tmp_dir)
        processor: RepositoryAnalyzer = RepositoryAnalyzer(config=config)
        context: RepositoryContext = await processor.process_repository(
            repo_path=repo_path
        )

        log_repository_context(context)

        async with ModelFactory.get_backend(config, context).use_api() as llm:
            responses = await llm.batch_request()
            (
                file_summaries,
                features,
                overview,
                tagline,
            ) = responses
            summaries = [
                (path, markdown_to_html.convert(response_cleaner.process_text(summary)))
                for path, summary in file_summaries
            ]
            cleand_tagline = response_cleaner.extract_text_between_tags(
                tagline,
                "<tagline>",
                "</tagline>",
            )
            config.config.md.tagline = response_cleaner.remove_quotes(cleand_tagline)
            cleaned_intro = response_cleaner.extract_text_between_tags(
                overview,
                "<overview>",
                "</overview>",
            )
            config.config.md.overview = config.config.md.overview.format(cleaned_intro)
            config.config.md.features = config.config.md.features.format(
                response_cleaner.format_markdown_table(features),
            )
        if should_generate_image(config):
            await generate_image(config)
        if config.config.md.logo in [None, "", DefaultLogos, CustomLogos]:
            config.config.md.logo = DefaultLogos.PURPLE.value

        section_contents = MarkdownBuilder(config, context, summaries, tmp_dir).build()

        FileHandler().write(output_file, section_contents)

        log_process_completion(output_file)


async def generate_image(config: ConfigLoader) -> None:
    """Generates an image using the DALL-E model."""
    async with DalleHandler(config) as dalle:
        image_url = await dalle._make_request()
        config.config.md.logo = await dalle.download(image_url)


def should_generate_image(config: ConfigLoader) -> bool:
    """Determines if the user enabled LLM image generation."""
    return (
        config.config.md.logo == CustomLogos.LLM.value
        and config.config.llm.api != LLMProviders.OFFLINE.value
    )


def log_repository_context(context: RepositoryContext) -> None:
    """Logs a snippet of the processed repository context data."""
    _logger.debug(f"Total files analyzed: {len(context.files)}")
    _logger.debug(f"Metadata extracted: {context.metadata}")
    _logger.debug(f"Dependencies: {context.dependencies}")
    _logger.debug(f"Languages: {context.language_counts}")
    _logger.debug(f"Languages detected: {context.languages}")
    _logger.debug(f"Extensions detected: {context.metadata}")
    _logger.debug(f"Quickstart: {context.quickstart.model_dump()}")


def log_process_completion(output_file: str) -> None:
    """Logs the completion of the README generation process."""
    _logger.info("README.md file generated successfully.")
    _logger.info(f"Output file saved @ {output_file}")
    _logger.info("Share with us @ github.com/eli64s/readme-ai/discussions")
