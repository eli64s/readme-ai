#!/usr/bin/env python3

"""
Runs the README.md file generation process.
"""

__package__ = "readmeai"

import asyncio
import tempfile
import traceback
from pathlib import Path
from typing import Optional

from readmeai._exceptions import ReadmeGeneratorError
from readmeai.cli.options import ImageOptions, ModelOptions
from readmeai.config.settings import ConfigLoader, GitSettings
from readmeai.core.logger import Logger
from readmeai.core.preprocess import preprocessor
from readmeai.core.utils import get_environment
from readmeai.generators.builder import MarkdownBuilder
from readmeai.models.dalle import DalleHandler
from readmeai.models.factory import ModelFactory
from readmeai.services.git import clone_repository
from readmeai.utils.file_handler import FileHandler

_logger = Logger(__name__)


def readme_agent(
    alignment: Optional[str],
    api: Optional[str],
    badge_color: Optional[str],
    badge_style: Optional[str],
    base_url: Optional[str],
    context_window: Optional[int],
    emojis: Optional[bool],
    image: Optional[str],
    # language: Optional[str],
    model: Optional[str],
    output_file: Optional[str],
    rate_limit: Optional[int],
    repository: str,
    temperature: Optional[float],
    # template: Optional[str],
    tree_depth: Optional[int],
    top_p: Optional[float],
) -> None:
    """Configures and runs the README file generator agent."""
    try:
        conf = ConfigLoader()
        api, model = get_environment(api, model)
        conf.config.api.rate_limit = rate_limit
        conf.config.llm = conf.config.llm.copy(
            update={
                "api": api,
                "base_url": base_url,
                "context_window": context_window,
                "model": model,
                "temperature": temperature,
                "top_p": top_p,
            }
        )
        conf.config.md = conf.config.md.copy(
            update={
                "alignment": alignment,
                "badge_color": badge_color,
                "badge_style": badge_style,
                "emojis": emojis,
                "image": image,
                "tree_depth": tree_depth,
            }
        )
        conf.config.git = GitSettings(repository=repository)
        _logger.info(f"Repository validated: {conf.config.git}")
        _logger.info(f"LLM API settings: {conf.config.llm}")
        asyncio.run(readme_generator(conf, output_file))

    except Exception as exc:
        raise ReadmeGeneratorError(exc, traceback.format_exc()) from exc


async def readme_generator(conf: ConfigLoader, output_file: Path) -> None:
    """Orchestrates the README.md file generation process."""
    with tempfile.TemporaryDirectory() as temp_dir:
        await clone_repository(conf.config.git.repository, temp_dir)
        (
            dependencies,
            raw_files,
        ) = preprocessor(conf, temp_dir)
        _logger.info(f"Total files analyzed: {len(raw_files)}")
        _logger.info(f"Dependencies found: {dependencies}")

        async with ModelFactory.model_handler(conf).use_api() as llm:
            responses = await llm.batch_request(dependencies, raw_files)
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
            conf.config.md.width = "60%"
            dalle = DalleHandler(conf)
            image_url = dalle.run()
            conf.config.md.image = dalle.download(image_url)
        elif (
            conf.config.md.image == ImageOptions.LLM.value
            and conf.config.llm.api == ModelOptions.OFFLINE.value
        ):
            conf.config.md.image = ImageOptions.BLUE.value

        readme_md = MarkdownBuilder(
            conf, dependencies, summaries, temp_dir
        ).build()
        FileHandler().write(output_file, readme_md)
        _logger.info("README generation process completed successfully!")
        _logger.info(f"README.md file saved to: {output_file}")
        _logger.info("Share it @ github.com/eli64s/readme-ai/discussions")
