#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import os
import shutil
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
from readmeai.core.preprocess import FileData, RepoProcessor
from readmeai.markdown.builder import ReadmeBuilder, build_readme_md
from readmeai.services.git_operations import clone_repo_to_temp_dir

logger = Logger(__name__)


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    repo_url = conf.git.repository

    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            await clone_repo_to_temp_dir(repo_url, temp_dir)

            repo_processor = RepoProcessor(conf, conf_helper)
            file_context = repo_processor.generate_contents(temp_dir)
            file_context = repo_processor.language_mapper(file_context)
            file_context = repo_processor.tokenize_content(file_context)

            dependencies = set()
            for file_data in file_context:
                dependencies.update(file_data.dependencies)
                dependencies.add(file_data.language)
                dependencies.add(file_data.name)
                dependencies.add(file_data.extension)

            dependencies = list(dependencies)
            code_files = [(data.path, data.content) for data in file_context]
            summaries = code_files.copy()
            conf.md.tree = ReadmeBuilder(
                conf, conf_helper, dependencies, summaries, temp_dir
            ).md_tree

            log_file_data(file_context, list(dependencies), conf.md.tree)

            async with ModelHandler(conf).use_api() as llm:
                if not conf.cli.offline:
                    prompts = await generate_prompts(
                        conf, file_context, dependencies, summaries
                    )
                    responses = await llm.batch_text_generator(prompts)
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

            build_readme_md(
                conf, conf_helper, dependencies, summaries, temp_dir
            )

            logger.info(
                f"README.md file generated successfully @ {conf.files.output}"
            )

    except Exception as exc_info:
        logger.error(
            f"Error generating README: {exc_info}\n{traceback.format_exc()}"
        )


async def generate_prompts(
    conf: AppConfig,
    file_context: list[FileData],
    dependencies: List[str],
    summaries: List[str],
) -> List[dict]:
    """Generates the prompts to be used by the LLM API."""
    return [
        {"type": prompt_type, "context": context}
        for prompt_type, context in [
            (
                "summaries",
                {
                    "repo": conf.git.repository,
                    "tree": conf.md.tree,
                    "dependencies": file_context,
                    "summaries": summaries,
                },
            ),
            (
                "features",
                {
                    "repo": conf.git.repository,
                    "dependencies": dependencies,
                    "files": file_context,
                },
            ),
            (
                "overview",
                {
                    "name": conf.git.name,
                    "repo": conf.git.repository,
                    "summaries": summaries,
                },
            ),
            (
                "slogan",
                {
                    "name": conf.git.name,
                    "repo": conf.git.repository,
                    "summaries": summaries,
                },
            ),
        ]
    ]


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
        conf = update_settings(
            conf,
            align,
            badges,
            emojis,
            image,
            max_tokens,
            model,
            offline,
            output,
            repository,
            temperature,
        )
        log_settings(conf)

        setup_environment(conf, api_key)

        asyncio.run(readme_agent(conf, conf_helper))

    except Exception as exc_info:
        logger.error(
            f"Error generating README: {exc_info}\n{traceback.format_exc()}"
        )


def update_settings(
    conf: AppConfig,
    align: str,
    badges: str,
    emojis: bool,
    image: str,
    max_tokens: int,
    model: str,
    offline: bool,
    output: str,
    repository: str,
    temperature: float,
) -> AppConfig:
    """Sets up the application configuration."""
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
    return conf


def setup_environment(config: AppConfig, api_key: str) -> None:
    """Set environment variables for the CLI application."""
    if api_key is not None:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
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
