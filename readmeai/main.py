#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import os
import tempfile
import traceback
from typing import List

from readmeai.cli.options import prompt_for_custom_image
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
from readmeai.core.preprocess import FileData, process_repository
from readmeai.exceptions import ReadmeGeneratorError
from readmeai.markdown.builder import build_readme_md
from readmeai.services.git_utils import clone_to_temporary_directory

logger = Logger(__name__)


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    repo_url = conf.git.repository

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            await clone_to_temporary_directory(repo_url, temp_dir)
            (
                file_context,
                dependencies,
                summaries,
                tree,
            ) = process_repository(conf, conf_helper, temp_dir)

            log_file_data(file_context, list(dependencies), tree)

            async with ModelHandler(conf).use_api() as llm:
                if conf.cli.offline is False:
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
            f"README.md file generated successfully @ {conf.files.output}"
        )

    except Exception as exc:
        raise ReadmeGeneratorError(traceback.format_exc()) from exc


def main(
    align: str,
    api_key: str,
    badges: str,
    emojis: bool,
    image: str,
    max_tokens: int,
    model: str,
    offline: bool,
    output: str,
    repository: str,
    temperature: float,
) -> None:
    """Main method of the readme-ai CLI application."""
    try:
        conf = load_config()
        conf_model = AppConfigModel(app=conf)
        conf_helper = load_config_helper(conf_model)
        conf.git = GitSettings(repository=repository)
        conf.files.output = output
        conf.cli.emojis = emojis
        conf.cli.offline = offline
        conf.llm.tokens_max = max_tokens
        conf.llm.model = model
        conf.llm.temperature = temperature
        conf.md.align = align
        conf.md.badge_style = badges
        conf.md.image = (
            image
            if image != ImageOptions.CUSTOM.name
            else prompt_for_custom_image(None, None, image)
        )
        log_settings(conf)

        setup_environment(conf, api_key)

        asyncio.run(readme_agent(conf, conf_helper))

    except Exception as exc:
        raise ReadmeGeneratorError(exc, traceback.format_exc()) from exc


def setup_environment(config: AppConfig, api_key: str) -> None:
    """Set environment variables for the CLI application."""
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        logger.info("API key exported to environment.")
    elif "OPENAI_API_KEY" in os.environ:
        logger.info("API key found in environment.")
    else:
        config.cli.offline = True
        logger.warning("API key not found. Running in offline mode.")


def log_settings(conf: AppConfig) -> None:
    """Log the settings for the CLI application."""
    logger.info("Starting README-AI processing...")
    logger.info(f"Processing repository: {conf.git.repository}")
    logger.info(f"LLM model engine: {conf.llm.model}")
    logger.info(f"LLM temperature: {conf.llm.temperature}")
    logger.info(f"Badge style: {conf.md.badge_style}")
    logger.info(f"Image style: {conf.md.image}")
    logger.info(f"Header alignment: {conf.md.align}")
    logger.info(f"Using emojis: {conf.cli.emojis}")
    logger.info(f"Offline mode: {conf.cli.offline}")
    logger.info(
        f"""Repository pydantic validations:\n\
        Repository URL: {conf.git.repository}\n\
        Full Name: {conf.git.full_name}\n\
        Project Name: {conf.git.name}\n\
        Host: {conf.git.source}\n\
        Host Name: {conf.git.host}"""
    )


def log_file_data(context: list[FileData], deps: List[str], tree: str) -> None:
    """Log the processed file data from the repository."""
    for file_data in context:
        logger.info(
            f"""
            File: {file_data.path}\n\
            Language: {file_data.language} ({file_data.extension})\n\
            Tokens: {file_data.tokens}\n\
            Dependencies: {file_data.dependencies}"""
        )
    logger.info(f"Dependencies: {deps}")
    logger.info(f"Project structure:\n{tree}")
