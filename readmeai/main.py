#!/usr/bin/env python3

"""Main entrypoint for the readme-ai application."""

__package__ = "readmeai"

import asyncio
import traceback

from readmeai.core import logger, model, preprocess
from readmeai.core.config import (
    AppConfig,
    AppConfigModel,
    ConfigHelper,
    GitConfig,
    load_config,
    load_config_helper,
)
from readmeai.md_builder import headers, tables, tree
from readmeai.utils import git

logger = logger.Logger(__name__)


def main(
    api_key: str,
    badges: str,
    emojis: bool,
    offline_mode: bool,
    model: str,
    output: str,
    repository: str,
    temperature: float,
    language: str,
    style: int,
) -> None:
    """Main entrypoint for the readme-ai application."""
    config = load_config()
    config_model = AppConfigModel(app=config)
    config_helper = load_config_helper(config_model)
    config.api.model = model
    config.cli.emojis = emojis
    config.paths.output = output
    config.api.temperature = temperature
    config.api.offline_mode = offline_mode
    config.git = GitConfig(repository=repository)
    _, config.git.name = git.get_user_repository_name(repository)

    if api_key is None and offline_mode is False:
        config.api.offline_mode = offline_mode

    if badges == "shields":
        config.md.badges_style = "style=for-the-badge"

    asyncio.run(readme_agent(badges, config, config_helper))


async def readme_agent(
    badges: str, config: AppConfig, config_helper: ConfigHelper
) -> None:
    """Orchestrates the README file generation process."""
    logger.info("README-AI is now executing.")
    logger.info(f"User Repository: {config.git.repository}")
    logger.info(f"Output README File: {config.paths.output}")
    logger.info(f"LLM Engine:  {config.api.model}")

    name = config.git.name
    placeholder = config.md.default
    repository = config.git.repository

    llm = model.OpenAIHandler(config)

    try:
        temp_dir = git.clone_repo_to_temp_dir(repository)
        tree_str = tree.generate_tree(temp_dir, repository)
        tree_str = tree.format_tree(name, tree_str)
        config.md.tree = config.md.tree.format(tree_str)
        logger.info(f"Directory tree: {config.md.tree}")

        parser = preprocess.RepositoryParser(config, config_helper)
        dependencies, file_text = parser.get_dependencies(temp_dir)
        logger.info(f"Dependencies: {dependencies}")

        # Generate codebase file summaries and README.md text via LLMs.
        if config.api.offline_mode is False:
            code_summary = await llm.code_to_text(
                config_helper.ignore_files,
                file_text,
                config.prompts.code_summary,
            )
            logger.info(f"Code summaries returned:\n{code_summary[:5]}")
            prompts = [
                config.prompts.slogan.format(config.git.name),
                config.prompts.overview.format(repository, code_summary),
                config.prompts.features.format(repository, tree),
            ]
            slogan, overview, features = await llm.chat_to_text(prompts)

        else:
            config.md.tables = tables.build_recursive_tables(
                repository, temp_dir, placeholder
            )
            code_summary = placeholder
            slogan, overview, features = (
                config.md.default,
                config.md.default,
                config.md.default,
            )

        # Update configuration Markdown templates with LLM generated text.
        config.prompts.slogan = slogan
        config.md.header = config.md.header.format(name.upper(), slogan)
        config.md.intro = config.md.intro.format(overview, features)

        # Generate README.md file.
        headers.build_readme_md(
            badges, config, config_helper, dependencies, code_summary
        )

    except Exception as excinfo:
        logger.error(
            f"Exception: {excinfo}\nStacktrace: {traceback.format_exc()}"
        )

    finally:
        await llm.close()

    logger.info("README-AI execution complete.")
