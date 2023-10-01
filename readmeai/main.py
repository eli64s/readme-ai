#!/usr/bin/env python3

"""Main entrypoint for the readme-ai application."""

__package__ = "readmeai"

import asyncio
import shutil

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
from readmeai.utils import github

logger = logger.Logger(__name__)


def main(
    api_key: str,
    badges: str,
    encoding: str,
    endpoint: str,
    offline_mode: bool,
    model: str,
    output: str,
    repository: str,
    temperature: float,
    language: str,
    style: int,
) -> None:
    """Orchestrates the README file generation process."""
    config = load_config()
    config_model = AppConfigModel(app=config)
    config_helper = load_config_helper(config_model)
    config.api.model = model
    config.paths.output = output
    config.api.temperature = temperature
    config.api.offline_mode = offline_mode
    config.git = GitConfig(repository=repository)
    if api_key is None and offline_mode is False:
        config.api.offline_mode = offline_mode
    asyncio.run(md_agent(badges, config, config_helper))


async def md_agent(
    badges: str, config: AppConfig, config_helper: ConfigHelper
) -> None:
    """Orchestrates the README file generation process."""
    logger.info("README-AI is now executing.")
    logger.info(f"Repository: {config.git.repository}")
    logger.info(f"Model:  {config.api.model}")
    logger.info(f"Output: {config.paths.output}")
    name = config.git.name
    placeholder = config.md.default
    repository = config.git.repository
    llm = model.OpenAIHandler(config)
    temp_dir = None

    try:
        temp_dir = await asyncio.to_thread(
            github.clone_repo_to_temp_dir, repository
        )
        temp_dir = github.clone_repo_to_temp_dir(repository)
        tree_str = tree.generate_tree(temp_dir, repository)
        tree_str = tree.format_tree(name, tree_str)
        config.md.tree = config.md.tree.format(tree_str)
        logger.info(f"Directory tree: {config.md.tree}")

        parser = preprocess.RepositoryParser(config, config_helper)
        dependencies, file_text = parser.get_dependencies(temp_dir)
        logger.info(f"Dependencies: {dependencies}")
        logger.info(f"File text: {file_text}")

        if config.api.offline_mode is False:
            # Generates codebase file summaries using large language models.
            code_summary = await llm.code_to_text(
                config_helper.ignore_files,
                file_text,
                config.prompts.code_summary,
            )
            logger.info(f"Code summaries returned:\n{code_summary[:10]}")

            # Generates slogan, overview and features using llm.
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

        config.prompts.slogan = slogan
        config.md.header = config.md.header.format(name, slogan)
        config.md.intro = config.md.intro.format(overview, features)
        headers.build(
            badges, config, config_helper, dependencies, code_summary
        )

    except Exception as excinfo:
        logger.error(f"Exception: {excinfo}")
        import traceback

        logger.error(f"Stacktrace: {traceback.format_exc()}")
    finally:
        await llm.close()
        if temp_dir:
            await asyncio.to_thread(shutil.rmtree, temp_dir)

    logger.info("README-AI execution complete.")
