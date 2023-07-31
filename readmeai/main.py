#!/usr/bin/env python3

"""Main entrypoint for README-AI application."""

import asyncio
import os
from typing import Dict, List, Optional, Tuple

import click

from . import builder, conf, logger, model, preprocess

logger = logger.Logger(__name__)
config = conf.load_config()
config_model = conf.AppConfigModel(app=config)
config_helper = conf.load_config_helper(config_model)


async def main(api_key: str, output: str, repository: str) -> None:
    """Main entrypoint for README-AI application."""
    conf.ApiConfig.validate_api_key(api_key)
    conf.GitConfig.validate_repository(repository)
    config.git = conf.GitConfig(repository=repository)
    config.paths.readme = output
    logger.info("Model: %s", dict(config.api, api_key="*" * 16))
    logger.info("Repository: %s", config.git)
    llm = model.OpenAIHandler(config)
    await generate_readme(llm)


async def generate_readme(llm: model.OpenAIHandler) -> None:
    """Orchestrates the README file generation process."""
    name, repository = config.git.name, config.git.repository
    scanner = preprocess.RepositoryParserWrapper(config, config_helper)
    dependencies, file_text = get_dependencies(scanner, repository)

    logger.info(f"Dependencies: {dependencies}")
    logger.info(f"Total files: {len(file_text)}")

    code_summary, slogan, overview, features = {}, "", "", ""
    try:
        code_summary = await generate_code_to_text(llm, file_text)
        slogan, overview, features = await generate_markdown_text(
            llm, repository, code_summary
        )
    except Exception as excinfo:
        logger.error(f"Exception: {excinfo}")
    finally:
        await llm.close()

    format_markdown_sections(name, slogan, overview, features)
    builder.build_markdown_file(config, config_helper, dependencies, code_summary)


def format_markdown_sections(
    name: str, slogan: str, overview: str, features: str
) -> None:
    """Updates config.md.header and config.md.intro."""
    config.md.header = config.md.header.format(name, slogan)
    config.md.intro = config.md.intro.format(overview, features)


async def generate_code_to_text(
    llm: model.OpenAIHandler, file_text: str
) -> Dict[str, str]:
    """Generates code_to_text using llm."""
    return await llm.code_to_text(
        config_helper.ignore_files, file_text, config.prompts.code_summary
    )


async def generate_markdown_text(
    llm: model.OpenAIHandler, repository: str, code_summary: str
) -> Tuple[str, str, str]:
    """Generates slogan, overview and features using llm."""
    prompts = [
        config.prompts.slogan.format(config.git.name),
        config.prompts.overview.format(repository, code_summary),
        config.prompts.features.format(repository, code_summary),
    ]
    responses = await llm.chat_to_text(prompts)
    return responses[:3]


def get_dependencies(
    scanner: preprocess.RepositoryParserWrapper, repository: str
) -> Tuple[List[str], str]:
    """Extracts dependencies and file_text using the scanner."""
    dependencies, file_text = scanner.get_dependencies(repository)
    return dependencies, file_text


@click.command()
@click.option(
    "-k",
    "--api-key",
    default=os.environ.get("OPENAI_API_KEY", None),
    help="OpenAI API secret key.",
)
@click.option(
    "-o",
    "--output",
    default="readme-ai.md",
    help="README.md output file path.",
)
@click.option(
    "-r",
    "--repository",
    required=True,
    help="Repository URL or directory path.",
)
@click.option(
    "-t",
    "--template",
    help="Template to use for README.md file.",
)
@click.option(
    "-l",
    "--language",
    help="Language to write README.md file in.",
)
def cli(
    api_key: str,
    output: str,
    repository: str,
    template: Optional[int],
    language: Optional[str],
) -> None:
    """Cli entrypoint for readme-ai pypi package."""
    logger.info("README-AI is now executing.")
    asyncio.run(main(api_key, output, repository))
    logger.info("README-AI execution complete.")


if __name__ == "__main__":
    cli()
