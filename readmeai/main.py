#!/usr/bin/env python3

"""Main method for the readme-ai cli application."""

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
from readmeai.markdown import headers, tree
from readmeai.services import git_operations as vcs

logger = logger.Logger(__name__)


def main(
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
    conf.git = GitConfig(repository=repository)
    conf.api.temperature = temperature
    conf.api.model = model
    conf.cli.emojis = emojis
    conf.cli.offline = offline
    conf.paths.output = output
    conf.md.badge_style = badges
    asyncio.run(readme_agent(conf, conf_helper))


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    logger.info("Starting readme-ai execution.")
    logger.info(f"Processing {conf.git.source}: {conf.git.repository}")
    logger.info(f"Setting LLM engine to: {conf.api.model}")
    logger.info(f"Saving output file as: {conf.paths.output}")

    llm = model.OpenAIHandler(conf)
    name = conf.git.name
    repository = conf.git.repository

    try:
        temp_dir = vcs.clone_repo_to_temp_dir(repository)
        repo_tree = tree.TreeGenerator(
            conf_helper=conf_helper,
            root_directory=temp_dir,
            repo_url=repository,
            project_name=name,
        ).generate_and_format_tree()
        conf.md.tree = conf.md.tree.format(repo_tree)
        logger.info(f"Directory tree structure: {conf.md.tree}")

        parser = preprocess.RepositoryParser(conf, conf_helper)
        dependencies, files = parser.get_dependencies(temp_dir)
        logger.info(f"Dependencies: {dependencies}")

        # Generate README.md file contents via OpenAI API.
        if conf.cli.offline is False:
            code_summary = await llm.code_to_text(
                files,
                conf_helper.ignore_files,
                conf.prompts.summaries,
                repo_tree,
            )
            prompts = [
                conf.prompts.slogan.format(conf.git.name),
                conf.prompts.overview.format(
                    repository, repo_tree, dependencies, code_summary
                ),
                conf.prompts.features.format(
                    repository, repo_tree, dependencies, code_summary
                ),
            ]
            slogan, overview, features = await llm.chat_to_text(prompts)
        else:
            code_summary = [
                (str(file_path), conf.md.default)
                for file_path, _ in files.items()
            ]
            slogan, overview, features = (
                conf.md.default,
                conf.md.default,
                conf.md.default,
            )

        # Build README.md file with extracted and generated data.
        conf.prompts.slogan = slogan
        conf.md.header = conf.md.header.format(name.upper(), slogan)
        conf.md.intro = conf.md.intro.format(overview, features)
        headers.build_readme_md(conf, conf_helper, dependencies, code_summary)

    except Exception as exc_info:
        logger.error(
            f"Exception: {exc_info}\nStacktrace: {traceback.format_exc()}"
        )
    finally:
        await llm.close()

    logger.info("Finished readme-ai execution.")
