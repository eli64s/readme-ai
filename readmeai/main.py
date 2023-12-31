#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import os
import shutil
import tempfile
import traceback
from pathlib import Path

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
from readmeai.core import logger, model, preprocess
from readmeai.markdown import headers, tree
from readmeai.services.git_operations import clone_repo_to_temp_dir

logger = logger.Logger(__name__)


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    logger.info(f"Processing repository: {conf.git.repository}")
    logger.info(f"GPT language model engine: {conf.llm.model}")

    llm = model.LlmApiHandler(conf)
    repo_name = conf.git.name.upper()
    repo_url = conf.git.repository
    temp_dir = await asyncio.to_thread(tempfile.mkdtemp)

    try:
        await clone_repo_to_temp_dir(repo_url, temp_dir)

        conf.md.tree = conf.md.tree.format(
            tree.TreeGenerator(
                conf_helper=conf_helper,
                root_directory=Path(temp_dir),
                repo_url=repo_url,
                repo_name=repo_name,
            ).generate_and_format_tree()
        )
        parser = preprocess.RepositoryParser(conf, conf_helper)
        dependencies, file_context = parser.get_dependencies(temp_dir)
        summaries = [
            (file_path, file_content)
            for file_path, file_content in file_context.items()
        ]

        logger.info(f"Dependencies and software: {dependencies}")
        logger.info(f"Directory tree structure:\n{conf.md.tree}")

        async with llm.use_api() as api:
            context = {
                "repo": repo_url,
                "tree": conf.md.tree,
                "dependencies": dependencies,
                "summaries": summaries,
            }
            if conf.cli.offline is False:
                context["summaries"] = await api.prompt_processor(
                    "summaries", context
                )
                features_response = await api.prompt_processor(
                    "features", context
                )
                overview_response = await api.prompt_processor(
                    "overview", context
                )
                slogan_response = await api.prompt_processor("slogan", context)
                summaries = context["summaries"]
                conf.md.features = conf.md.features.format(
                    features_response["features"]
                )
                conf.md.overview = conf.md.overview.format(
                    overview_response["overview"]
                )
                conf.md.slogan = slogan_response["slogan"]
            else:
                logger.warning("Offline mode enabled, skipping API calls.")
                (
                    summaries,
                    conf.md.features,
                    conf.md.overview,
                    conf.md.slogan,
                ) = (
                    [
                        (file_path.as_posix(), conf.md.default)
                        for file_path, _ in file_context.items()
                    ],
                    conf.md.features.format(conf.md.default),
                    conf.md.overview.format(conf.md.default),
                    conf.md.default,
                )

        headers.build_readme_md(conf, conf_helper, dependencies, summaries)
        logger.info("README file successfully created: {conf.files.output}")

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

        if image == ImageOptions.CUSTOM.name:
            conf.md.image = prompt_for_custom_image(None, None, image)
        else:
            conf.md.image = image

        _set_environment_vars(conf, api_key)

        asyncio.run(readme_agent(conf, conf_helper))

    except Exception as exc_info:
        logger.error(
            f"Exception during README generation: {exc_info}\n{traceback.format_exc()}"
        )


def _set_environment_vars(config: AppConfig, api_key: str) -> None:
    """Set environment variables for the CLI application."""
    if api_key is not None:
        os.environ["OPENAI_API_KEY"] = api_key

    elif "OPENAI_API_KEY" not in os.environ:
        config.cli.offline = True
