#!/usr/bin/env python3

"""Main entrypoint for the readme-ai application."""

__package__ = "readmeai"

import asyncio
import traceback

from readmeai.config.settings import (
    AppConfig,
    AppConfigModel,
    ConfigHelper,
    GitConfig,
    load_config,
    load_config_helper,
)
from readmeai.core import logger, model, preprocess
from readmeai.markdown import headers, tables, tree
from readmeai.services import version_control as vcs
from readmeai.utils import utils

logger = logger.Logger(__name__)


def main(
    api_key: str,
    badges: str,
    emojis: bool,
    offline: bool,
    model: str,
    output: str,
    repository: str,
    temperature: float,
) -> None:
    """Entrypoint for the readme-ai application."""
    conf = load_config()
    conf_model = AppConfigModel(app=conf)
    conf_helper = load_config_helper(conf_model)
    conf.api.model = model
    conf.cli.badges = badges
    conf.cli.emojis = emojis
    conf.api.model = model
    conf.cli.offline = offline
    conf.paths.output = output
    conf.api.temperature = temperature
    conf.git = GitConfig(repository=repository, name=None)
    conf.git.name = vcs.get_user_repository_name(repository)[1]
    logger.info(f"Configuration: {conf.git}")
    asyncio.run(readme_agent(conf, conf_helper))


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    logger.info("README-AI is now executing.")
    logger.info(f"User Repository: {conf.git.repository}")
    logger.info(f"Output File: {conf.paths.output}")
    logger.info(f"Model Engine:  {conf.api.model}")

    name = conf.git.name
    placeholder = conf.md.default
    repository = conf.git.repository

    llm = model.OpenAIHandler(conf)

    try:
        temp_dir = vcs.clone_repo_to_temp_dir(repository)
        tree_generator = tree.TreeGenerator(
            conf_helper,
            temp_dir,
            repository,
            project_name="readmeai",
            max_depth=3,
        )
        tree_str = tree_generator.generate_and_format_tree()
        conf.md.tree = conf.md.tree.format(tree_str)
        logger.info(f"Repository tree: {conf.md.tree}")

        parser = preprocess.RepositoryParser(conf, conf_helper)
        dependencies, files = parser.get_dependencies(temp_dir)
        logger.info(f"Dependencies: {dependencies}")

        # Generate codebase file summaries and README.md text via LLMs.
        if conf.cli.offline is False:
            code_summary = await llm.code_to_text(
                files,
                conf_helper.ignore_files,
                conf.prompts.summaries,
                tree_str,
            )
            prompts = [
                conf.prompts.slogan.format(conf.git.name),
                conf.prompts.overview.format(
                    repository, tree_str, dependencies, code_summary
                ),
                conf.prompts.features.format(
                    repository, tree_str, dependencies, code_summary
                ),
            ]
            slogan, overview, features = await llm.chat_to_text(prompts)
        else:
            conf.md.tables = tables.build_recursive_tables(
                repository, temp_dir, placeholder
            )
            code_summary = placeholder
            slogan, overview, features = (
                conf.md.default,
                conf.md.default,
                conf.md.default,
            )

        # Generate README.md file.
        conf.prompts.slogan = slogan
        conf.md.header = conf.md.header.format(name.upper(), slogan)
        conf.md.intro = conf.md.intro.format(overview, features)
        headers.build_readme_md(conf, conf_helper, dependencies, code_summary)

    except Exception as excinfo:
        logger.error(
            f"Exception: {excinfo}\nStacktrace: {traceback.format_exc()}"
        )
    finally:
        await llm.close()

    logger.info("README-AI execution complete.")
