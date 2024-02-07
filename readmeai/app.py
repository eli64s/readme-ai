#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import tempfile
import traceback
from pathlib import Path
from typing import Optional

from readmeai.cli.options import prompt_for_image
from readmeai.config.enums import ImageOptions
from readmeai.config.settings import (
    AppConfig,
    AppConfigModel,
    ConfigHelper,
    GitSettings,
    load_config,
    load_config_helper,
)
from readmeai.core.file_io import FileHandler
from readmeai.core.logger import Logger
from readmeai.core.preprocess import process_repository
from readmeai.core.utils import setup_environment
from readmeai.exceptions import ReadmeGeneratorError
from readmeai.llms.registry import model_handler
from readmeai.markdown.builder import build_readme_md
from readmeai.services.git_utils import clone_repository

logger = Logger(__name__)


def readme_agent(
    align: Optional[str],
    api: str,
    badges: Optional[str],
    badge_color: Optional[str],
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
        conf = load_config()
        conf_model = AppConfigModel(app=conf)
        conf_helper = load_config_helper(conf_model)
        conf.git = GitSettings(repository=repository)
        conf.md = conf.md.copy(
            update={
                "align": align,
                "badges": badges,
                "badge_color": badge_color,
                "emojis": emojis,
                "tree_depth": tree_depth,
                "image": image
                if image != ImageOptions.URL.name
                else prompt_for_image(None, None, image),
            }
        )
        conf.llm = conf.llm.copy(
            update={
                "api": api,
                "model": model,
                "temperature": temperature,
                "tokens_max": max_tokens,
            }
        )
        logger.info(f"Repository validation: {conf.git}")
        logger.info(f"LLM API validation: {conf.llm}")

        setup_environment(conf, api)
        asyncio.run(readme_generator(conf, conf_helper, output))

    except Exception as exc:
        raise ReadmeGeneratorError(exc, traceback.format_exc()) from exc


async def readme_generator(
    conf: AppConfig, conf_helper: ConfigHelper, output: str
) -> None:
    """Orchestrates the README file generation process."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            await clone_repository(conf.git.repository, temp_dir)
            (
                file_context,
                dependencies,
                raw_files,
                tree,
                dependency_dict,
            ) = process_repository(conf, conf_helper, temp_dir)
            logger.info(f"Dependency Files:\n{dependency_dict}")
            logger.info(f"Dependencies:\n{dependencies}")
            logger.info(f"Directory Tree:\n{tree}")

            async with model_handler(conf).use_api() as llm:
                responses = await llm.batch_request(dependencies, raw_files)
                (
                    summaries,
                    features,
                    overview,
                    slogan,
                ) = responses
                conf.md.features = conf.md.features.format(features)
                conf.md.overview = conf.md.overview.format(overview)
                conf.md.slogan = slogan

        markdown_content = build_readme_md(
            conf, conf_helper, dependencies, summaries, temp_dir
        )
        FileHandler().write(Path(output), markdown_content)

        logger.info(f"README file successfully generated @ {output}")
        logger.info(f"Share your README with us @ {conf.git.discussions}")

    except Exception as exc:
        raise ReadmeGeneratorError(traceback.format_exc()) from exc
