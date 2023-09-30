#!/usr/bin/env python3

"""Main entrypoint for the readme-ai application."""

__package__ = "readmeai"

import asyncio
import shutil

from . import builder, conf, logger, model, preprocess, utils

logger = logger.Logger(__name__)


async def run_app(
    config: conf.AppConfig, config_helper: conf.ConfigHelper
) -> None:
    """Orchestrates the README file generation process."""
    llm = model.OpenAIHandler(config)
    logger.info("README-AI is now executing.")
    logger.info(f"Repository: {config.git.repository}")
    logger.info(f"OpenAI Model: {config.api.model}")

    name = config.git.name
    repository = config.git.repository
    placeholder = config.md.default

    try:
        temp_dir = await asyncio.to_thread(
            utils.clone_repo_to_temp_dir, repository
        )
        temp_dir = utils.clone_repo_to_temp_dir(repository)
        tree_str = builder.generate_tree(temp_dir, repository)
        tree = builder.format_tree(name, tree_str)
        config.md.tree = config.md.tree.format(tree)
        logger.info(f"Directory tree: {config.md.tree}")

        parser = preprocess.RepositoryParser(config, config_helper)
        dependencies, file_text = parser.get_dependencies(temp_dir)
        logger.info(f"Dependencies: {dependencies}")

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
                config.prompts.features.format(repository, code_summary),
            ]
            slogan, overview, features = await llm.chat_to_text(prompts)

        else:
            config.md.tables = builder.build_recursive_tables(
                repository, temp_dir, placeholder
            )
            code_summary = placeholder
            slogan, overview, features = (
                config.md.default,
                config.md.default,
                config.md.default,
            )

        config.md.header = config.md.header.format(name, slogan)
        config.md.intro = config.md.intro.format(overview, features)
        builder.build_readme_file(
            config, config_helper, dependencies, code_summary
        )

    except Exception as excinfo:
        logger.error(f"Exception: {excinfo}")
    finally:
        await llm.close()
        await asyncio.to_thread(shutil.rmtree, temp_dir)

    logger.info("README-AI execution complete.")
