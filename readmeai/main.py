#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import os
import shutil
import tempfile
import traceback

from readmeai.cli.options import prompt_for_custom_image
from readmeai.config.settings import (
    AppConfig,
    AppConfigModel,
    ConfigHelper,
    GitSettings,
    ImageOptions,
    load_config,
    load_config_helper,
)
from readmeai.core.logger import Logger
from readmeai.core.model import ModelHandler
from readmeai.core.preprocess import RepoProcessor
from readmeai.markdown.headers import build_readme_md
from readmeai.markdown.tree import TreeGenerator
from readmeai.services.git_operations import clone_repo_to_temp_dir

logger = Logger(__name__)


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    repo_url = conf.git.repository
    temp_dir = await asyncio.to_thread(tempfile.mkdtemp)
    try:
        await clone_repo_to_temp_dir(repo_url, temp_dir)

        tree_command(conf, conf_helper, temp_dir)

        parser = RepoProcessor(conf, conf_helper)
        dependencies, file_context = parser.get_dependencies(temp_dir)
        summaries = [(path, content) for path, content in file_context.items()]

        logger.info(f"Project dependencies: {dependencies}")
        logger.info(f"Project structure:\n{conf.md.tree}")

        async with ModelHandler(conf).use_api() as llm:
            if conf.cli.offline is False:
                prompts = [
                    {
                        "type": "summaries",
                        "context": {
                            "repo": repo_url,
                            "tree": conf.md.tree,
                            "dependencies": dependencies,
                            "summaries": summaries,
                        },
                    },
                    {
                        "type": "features",
                        "context": {
                            "repo": repo_url,
                            "tree": conf.md.tree,
                            "dependencies": dependencies,
                            "summaries": summaries,
                        },
                    },
                    {
                        "type": "overview",
                        "context": {
                            "name": conf.git.name,
                            "repo": repo_url,
                            "summaries": summaries,
                        },
                    },
                    {
                        "type": "slogan",
                        "context": {
                            "repo": repo_url,
                            "summaries": summaries,
                        },
                    },
                ]
                responses = await llm.batch_text_generator(prompts)
                (
                    summaries_response,
                    features_response,
                    overview_response,
                    slogan_response,
                ) = (response for response in responses)
                summaries = summaries_response
                conf.md.features = conf.md.features.format(features_response)
                conf.md.overview = conf.md.overview.format(overview_response)
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
                        for file_path, _ in file_context.items()
                    ],
                    conf.md.features.format(conf.md.default),
                    conf.md.overview.format(conf.md.default),
                    conf.md.default,
                )

        build_readme_md(conf, conf_helper, dependencies, summaries)

    except Exception as exc_info:
        logger.error(
            f"Error generating README: {exc_info}\n{traceback.format_exc()}"
        )
    finally:
        shutil.rmtree(temp_dir)

    logger.info(f"README file successfully generated at {conf.files.output}")


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
        export_to_environment(conf, api_key)

        log_settings(conf)

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


def export_to_environment(config: AppConfig, api_key: str) -> None:
    """Set environment variables for the CLI application."""
    if api_key is not None:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        config.cli.offline = True


def tree_command(
    conf: AppConfig, conf_helper: ConfigHelper, temp_dir: str
) -> None:
    """Updates the markdown tree configuration."""
    tree_generator = TreeGenerator(
        conf_helper=conf_helper,
        root_dir=temp_dir,
        repo_url=conf.git.repository,
        repo_name=conf.git.name,
    )
    conf.md.tree = conf.md.tree.format(tree_generator.run())


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
