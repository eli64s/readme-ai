#!/usr/bin/env python3

"""
Main module for the README file generator agent.
"""

__package__ = "readmeai"

import asyncio
import contextlib
import tempfile
import traceback
from collections.abc import Generator

from readmeai._exceptions import ReadmeGeneratorError
from readmeai.cli.options import ImageOptions, ModelOptions
from readmeai.config.settings import ConfigLoader, GitSettings
from readmeai.core.logger import Logger
from readmeai.core.preprocess import preprocessor
from readmeai.core.utils import get_environment
from readmeai.generators.builder import MarkdownBuilder
from readmeai.models.dalle import DalleHandler
from readmeai.models.factory import ModelRegistry
from readmeai.utils.file_handler import FileHandler
from readmeai.vcs.ingestor import retrieve_repository

_logger = Logger(__name__)


@contextlib.contextmanager
def error_handler() -> Generator:
    """
    Exception handler for the README generation process.
    """
    try:
        yield
    except Exception as exc:
        _logger.error(f"Error in README generation process: {exc}")
        raise ReadmeGeneratorError(exc, traceback.format_exc()) from exc


def readme_agent(
    repository: str,
    align: str,
    api: str,
    badge_color: str,
    badge_style: str,
    base_url: str,
    context_window: int,
    emojis: bool,
    header_style: str,
    image: str,
    model: str,
    output: str,
    rate_limit: int,
    temperature: float,
    toc_style: str,
    top_p: float,
    tree_depth: int,
) -> None:
    """
    Configures and runs the README file generator agent.
    """
    with error_handler():
        api, model = get_environment(api, model)

        conf = ConfigLoader()

        conf.config.api.rate_limit = rate_limit
        conf.config.llm = conf.config.llm.model_copy(
            update={
                "api": api,
                "base_url": base_url,
                "context_window": context_window,
                "model": model,
                "temperature": temperature,
                "top_p": top_p,
            },
        )
        conf.config.md = conf.config.md.model_copy(
            update={
                "align": align,
                "badge_color": badge_color,
                "badge_style": badge_style,
                "emojis": emojis,
                "header_style": header_style,
                "image": image,
                "toc_style": toc_style,
                "tree_depth": tree_depth,
            },
        )
        conf.config.git = GitSettings(repository=repository)

        _logger.info(f"Repository settings updated: {conf.config.git}")
        _logger.info(f"LLM API settings updated: {conf.config.llm}")

        asyncio.run(readme_generator(conf, output))


async def readme_generator(conf: ConfigLoader, output_file: str) -> None:
    """
    Processes the repository and generates the README file.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        await retrieve_repository(conf.config.git.repository, tmp_dir)
        deps, raw_files = preprocessor(conf, tmp_dir)

        _logger.info(f"Total files analyzed: {len(raw_files)}")
        _logger.info(f"Dependencies extracted: {deps}")

        async with ModelRegistry.get_backend(conf).use_api() as llm:
            responses = await llm.batch_request(deps, raw_files)
            (
                summaries,
                features,
                overview,
                slogan,
            ) = responses
            conf.config.md.features = conf.config.md.features.format(features)
            conf.config.md.overview = conf.config.md.overview.format(overview)
            conf.config.md.slogan = slogan

        if (
            conf.config.md.image == ImageOptions.LLM.value
            and conf.config.llm.api != ModelOptions.OFFLINE.value
        ):
            with DalleHandler(conf).use_api() as dalle:
                image_url = dalle._make_request()
                conf.config.md.image = dalle.download(image_url)
                if conf.config.md.image == ImageOptions.LLM.value:
                    conf.config.md.image = ImageOptions.BLUE.value

        readme_md = MarkdownBuilder(conf, deps, summaries, tmp_dir).build()

        FileHandler().write(output_file, readme_md)

        _logger.info(f"README.md file saved to: {output_file}")
        _logger.info("README generation process completed successfully!")
        _logger.info("Share it @ github.com/eli64s/readme-ai/discussions")
