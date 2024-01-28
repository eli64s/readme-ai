#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import tempfile
import traceback
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
    vertex_ai: Optional[Tuple[str, str]],
) -> None:
    """Main method of the readme-ai CLI application."""
    try:
        conf = load_config()
        conf_model = AppConfigModel(app=conf)
        conf_helper = load_config_helper(conf_model)

        conf.files.output = output
        conf.git = GitSettings(repository=repository)
        conf.llm = conf.llm.copy(
            update={
                "api_key": api_key,
                "model": model,
                "offline": offline,
                "temperature": temperature,
                "tokens_max": max_tokens,
            }
        )
        image = (
            image
            if image != ImageOptions.CUSTOM.name
            else prompt_for_image(None, None, image)
        )
        conf.md = conf.md.copy(
            update={
                "align": align,
                "badges": badges,
                "emojis": emojis,
                "image": image,
            }
        )

        logger.info(f"Repository validation: {conf.git}")
        logger.info(f"LLM API validation: {conf.llm}")

        asyncio.run(readme_generator(conf, conf_helper))

    except Exception as exc:
        raise ReadmeGeneratorError(exc, traceback.format_exc()) from exc


async def readme_generator(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            await clone_repository(conf.git.repository, temp_dir)
            (
                file_context,
                dependencies,
                summaries,
                tree,
            ) = process_repository(conf, conf_helper, temp_dir)

            for fn in file_context:
                if fn.file_name == "Dockerfile":
                    logger.info(f"File Context:\n{fn}")
            logger.info(f"Dependencies:\n{dependencies}")
            logger.info(f"Directory Tree:\n{tree}")

            if conf.llm.offline is False:
                async with ModelHandler(conf).use_api() as llm:
                    responses = await llm.batch_request(
                        file_context, dependencies, summaries
                    )
                    (
                        summaries_response,
                        features_response,
                        overview_response,
                        slogan_response,
                    ) = responses
                    summaries = summaries_response
                    conf.md.features = conf.md.features.format(
                        features_response
                    )
                    conf.md.overview = conf.md.overview.format(
                        overview_response
                    )
                    conf.md.slogan = slogan_response
            else:
                (
                    summaries,
                    conf.md.features,
                    conf.md.overview,
                    conf.md.slogan,
                ) = (
                    [
                        (str(file_path), conf.md.default)
                        for file_path, _ in summaries
                    ],
                    conf.md.features.format(conf.md.default),
                    conf.md.overview.format(conf.md.default),
                    conf.md.default,
                )

        build_readme_md(conf, conf_helper, dependencies, summaries, temp_dir)

        logger.info(
            f"README file generated successfully @ {conf.files.output}"
        )

    except Exception as exc:
        raise ReadmeGeneratorError(traceback.format_exc()) from exc
