#!/usr/bin/env python3

"""Orchestrates the README file generation process."""

__package__ = "readmeai"

import asyncio
import tempfile
import traceback
from pathlib import Path
from typing import Optional

from readmeai.cli.options import prompt_for_image
from readmeai.config.enums import ImageOptions
from readmeai.config.settings import (
    ConfigLoader,
    GitSettings,
)
from readmeai.core.preprocess import preprocessor
from readmeai.core.utils import set_model_engine
from readmeai.exceptions import ReadmeGeneratorError
from readmeai.generators.builder import build_markdown
from readmeai.models.factory import model_handler
from readmeai.services.git import clone_repository
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.logger import Logger

_logger = Logger(__name__)


def readme_agent(
    alignment: Optional[str],
    api: str,
    badge_color: Optional[str],
    badge_style: Optional[str],
    emojis: Optional[bool],
    image: Optional[str],
    # language: Optional[str],
    max_tokens: Optional[int],
    model: Optional[str],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    # template: Optional[str],
    tree_depth: Optional[int],
) -> None:
    """Main method of the readme-ai CLI application."""
    try:
        config_loader = ConfigLoader()
        config = config_loader.config
        config.git = GitSettings(repository=repository)

        try:
            config.git.host_domain = config.git.repository.host
        except Exception:
            config.git.host_domain = "LOCAL"

        config.llm.api = api
        config.llm.model = model
        config.llm.temperature = temperature
        config.llm.tokens_max = max_tokens

        config.md.alignment = alignment or config.md.alignment
        config.md.badge_color = badge_color
        config.md.badge_style = badge_style
        config.md.emojis = emojis
        config.md.tree_depth = tree_depth or 3
        config.md.image = (
            image
            if image not in [ImageOptions.CUSTOM.name, ImageOptions.LLM.name]
            else prompt_for_image(image)
        )

        config.output_file = output or config.output_file

        _logger.info(f"Repository settings validated: {config.git}")
        _logger.info(f"LLM API settings validated: {config.llm}")

        set_model_engine(config)
        asyncio.run(readme_generator(config_loader))

    except Exception as exc:
        raise ReadmeGeneratorError(exc, traceback.format_exc()) from exc


async def readme_generator(config_loader: ConfigLoader) -> None:
    """Orchestrates the README file generation process."""
    config = config_loader.config

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            await clone_repository(config.git.repository, temp_dir)
            (
                dependencies,
                raw_files,
                dependencies_dict,
            ) = preprocessor(config_loader, temp_dir)

            _logger.info(f"Dependencies extracted: {dependencies}")

            async with model_handler(config, config_loader).use_api() as llm:
                responses = await llm.batch_request(dependencies, raw_files)
                (
                    summaries,
                    features,
                    overview,
                    slogan,
                    features_synthesized,
                ) = responses
                config.md.features = config.md.features.format(features)
                config.md.overview = config.md.overview.format(overview)
                config.md.slogan = slogan

        md_content = build_markdown(
            config_loader, dependencies, summaries, temp_dir
        )

        FileHandler().write(Path(config.output_file), md_content)

        _logger.info(f"README file generated @ {config.output_file}")
        _logger.info(f"Share it with us @ {config.discussions} !")

    except Exception as exc:
        raise ReadmeGeneratorError(traceback.format_exc()) from exc
