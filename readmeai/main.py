#!/usr/bin/env python3

"""Main module for the README-AI CLI application."""

__package__ = "readmeai"

import asyncio
import os
import traceback

from readmeai.cli.options import prompt_for_custom_image
from readmeai.config.settings import (
    AppConfig,
    AppConfigModel,
    ConfigHelper,
    GitConfig,
    ImageOptions,
    load_config,
    load_config_helper,
)
from readmeai.core import logger, model, preprocess
from readmeai.markdown import headers, tree
from readmeai.services import git_operations as vcs

logger = logger.Logger(__name__)


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
    logger.info("EXECUTING README-AI CLI APPLICATION...")
    conf = load_config()
    conf_model = AppConfigModel(app=conf)
    conf_helper = load_config_helper(conf_model)
    conf.git = GitConfig(repository=repository)
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

    if api_key is not None:
        os.environ["OPENAI_API_KEY"] = api_key
    elif "OPENAI_API_KEY" not in os.environ:
        conf.cli.offline = True

    asyncio.run(readme_agent(conf, conf_helper))


async def readme_agent(conf: AppConfig, conf_helper: ConfigHelper) -> None:
    """Orchestrates the README file generation process."""
    logger.info(f"PROCESSING REPOSITORY: {conf.git.repository}")
    logger.info(f"README OUTPUT FILE PATH: {conf.files.output}")
    logger.info(f"GPT LANGUAGE MODEL ENGINE: {conf.llm.model}")

    try:
        llm = model.LlmApiHandler(conf)
        name = conf.git.name
        repo = conf.git.repository
        temp_dir = vcs.clone_repo_to_temp_dir(repo)

        conf.md.tree = conf.md.tree.format(
            tree.TreeGenerator(
                conf_helper=conf_helper,
                root_directory=temp_dir,
                repo_url=repo,
                project_name=name,
            ).generate_and_format_tree()
        )
        parser = preprocess.RepositoryParser(conf, conf_helper)
        dependencies, file_context = parser.get_dependencies(temp_dir)
        summaries = [
            (file_path, file_content)
            for file_path, file_content in file_context.items()
        ]

        logger.info(f"REPOSITORY {name.upper()} DEPENDENCIES:")
        for dep in dependencies:
            logger.info(f"- {dep}")
        logger.info(f"DIRECTORY TREE STRUCTURE:\n{conf.md.tree}")
        logger.info("PREPARING TO GENERATE LLM PROMPT RESPONSES...")

        context = {
            "name": repo,
            "tree": conf.md.tree,
            "deps": dependencies,
            "summaries": summaries,
        }
        if conf.cli.offline is False:
            summaries = await llm.prompt_processor("summaries", context)
            context["summaries"] = summaries
            features_response = await llm.prompt_processor("features", context)
            overview_response = await llm.prompt_processor("overview", context)
            slogan_response = await llm.prompt_processor("slogan", context)
            features = features_response["features"]
            overview = overview_response["overview"]
            slogan = slogan_response["slogan"]
        else:
            logger.debug(
                "OFFLINE MODE ENABLED, SKIPPING LLM PROMPT PROCESSING..."
            )
            summaries, features, overview, slogan = (
                [
                    (file_path.as_posix(), conf.md.default)
                    for file_path, _ in file_context.items()
                ],
                conf.md.default,
                conf.md.default,
                conf.md.default,
            )

        logger.info(f"FILE SUMMARIES: {summaries[0:3]}")
        logger.info(f"TOTAL SUMMARIES GENERATED: {len(summaries)}")
        logger.info("BUILDING AND FORMATTING MARKDOWN SECTIONS...")

        conf.md.header = conf.md.header.format(
            conf.md.align, conf.md.image, name.upper(), slogan
        )
        conf.md.intro = conf.md.intro.format(overview, features)
        conf.prompts.slogan = slogan
        headers.build_readme_md(conf, conf_helper, dependencies, summaries)

    except Exception as exc_info:
        logger.error(f"EXCEPTION PROCESSING REPOSITORY {name}: {exc_info}")
        logger.error(f"TRACEBACK: {traceback.format_exc()}")
    finally:
        await llm.close()

    logger.info("README-AI EXECUTION COMPLETE...")
    logger.info(f"README FILE OUTPUT PATH: {conf.files.output}")
