#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import os
import tempfile
import traceback
from pathlib import Path
from typing import Optional, Tuple

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
from readmeai.core.factory import FileHandler
from readmeai.core.logger import Logger
from readmeai.core.model import ModelHandler
from readmeai.core.preprocess import process_repository
from readmeai.exceptions import ReadmeGeneratorError
from readmeai.markdown.builder import build_readme_md
from readmeai.services.git_utils import clone_repository

logger = Logger(__name__)


def readme_agent(
    align: Optional[str],
    api_key: Optional[str],
    badges: Optional[str],
    badge_color: Optional[str],
    emojis: Optional[bool],
    image: Optional[str],
    # language: Optional[str],
    max_tokens: Optional[int],
    model: Optional[str],
    offline: Optional[bool],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    # template: Optional[str],
    tree_depth: Optional[int],
    vertex_ai: Optional[Tuple[str, str]],
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
                if image != ImageOptions.CUSTOM.name
                else prompt_for_image(None, None, image),
            }
        )
        conf.llm.model = model
        conf.llm.offline = offline
        conf.llm.temperature = temperature
        conf.llm.tokens_max = max_tokens

        logger.info(f"Repository validation: {conf.git}")
        logger.info(f"LLM API validation: {conf.llm}")

        setup_environment(conf, api_key)

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

            logger.info(f"Dependencies:\n{dependencies}")
            logger.info(f"Directory Tree:\n{tree}")

            if conf.llm.offline is False:
                async with ModelHandler(conf).use_api() as llm:
                    responses = await llm.batch_request(
                        dependencies, raw_files
                    )
                    (
                        summaries,
                        features,
                        overview,
                        slogan,
                    ) = responses
                    conf.md.features = conf.md.features.format(features)
                    conf.md.overview = conf.md.overview.format(overview)
                    conf.md.slogan = slogan
            else:
                (
                    summaries,
                    conf.md.features,
                    conf.md.overview,
                    conf.md.slogan,
                ) = (
                    [
                        (str(file_path), conf.md.default)
                        for file_path, _ in raw_files
                    ],
                    conf.md.features.format(conf.md.default),
                    conf.md.overview.format(conf.md.default),
                    conf.md.default,
                )

        md_contents = build_readme_md(
            conf, conf_helper, dependencies, summaries, temp_dir
        )
        FileHandler().write(Path(output), md_contents)

        logger.info(f"README file successfully generated @ {output}")
        logger.info(
            "Share your README with the community @ https://github.com/eli64s/readme-ai/discussions"
        )

    except Exception as exc:
        raise ReadmeGeneratorError(traceback.format_exc()) from exc


def setup_environment(config: AppConfig, api_key: str) -> None:
    """Set environment variables for the CLI application."""
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        logger.info("LLM API key exported to environment.")
    elif "OPENAI_API_KEY" in os.environ:
        logger.info("LLM API key found in environment.")
    else:
        config.llm.offline = True
        logger.warning("LLM API key not found. Running in offline mode.")
