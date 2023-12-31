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
    log_cli_settings(conf)

    llm = ModelHandler(conf)
    repo_name = conf.git.name
    repo_url = conf.git.repository
    temp_dir = await asyncio.to_thread(tempfile.mkdtemp)

    try:
        await clone_repo_to_temp_dir(repo_url, temp_dir)
        conf.md.tree = conf.md.tree.format(
            TreeGenerator(
                conf_helper=conf_helper,
                root_dir=temp_dir,
                repo_url=repo_url,
                repo_name=repo_name,
            ).run_tree()
        )
        parser = RepoProcessor(conf, conf_helper)
        dependencies, file_context = parser.get_dependencies(temp_dir)
        summaries = [
            (file_path, file_content)
            for file_path, file_content in file_context.items()
        ]
        logger.info(f"Project dependencies: {dependencies}")
        logger.info(f"Project structure:\n{conf.md.tree}")

        async with llm.use_api() as api:
            if conf.cli.offline is False:
                prompts = [
                    {
                        "type": "summaries",
                        "context": {
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
                responses = await api.batch_text_generator(prompts)
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

    finally:
        shutil.rmtree(temp_dir)


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
        conf.md.badges_style = badges
        conf.md.image = image
        if image == ImageOptions.CUSTOM.name:
            conf.md.image = prompt_for_custom_image(None, None, image)

        export_to_environment(conf, api_key)

        asyncio.run(readme_agent(conf, conf_helper))

    except Exception as exc_info:
        logger.error(
            f"Error generating README: {exc_info}\n{traceback.format_exc()}"
        )

    logger.info(
        "README-AI processing complete. File saved as - {conf.files.output}"
    )


def export_to_environment(config: AppConfig, api_key: str) -> None:
    """Set environment variables for the CLI application."""
    if api_key is not None:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        config.cli.offline = True


def log_cli_settings(conf: AppConfig) -> None:
    """Log the settings for the CLI application."""
    logger.info("Starting README-AI processing...")
    logger.info(f"Processing repository: {conf.git.repository}")
    logger.info(f"GPT API model engine: {conf.llm.model}")
    logger.info(f"Temperature: {conf.llm.temperature}")
    logger.info(f"Badge style: {conf.md.badges_style}")
    logger.info(f"Image style: {conf.md.image}")
    logger.info(f"Header alignment: {conf.md.align}")
