#!/usr/bin/env python3
"""Main entrypoint for README-AI application."""

import argparse
import asyncio
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import builder
import conf
import preprocess
import utils
from logger import Logger
from model import OpenAIHandler

CONF = conf.load_config()
CONF_HELPER = conf.load_config_helper(CONF)
LOGGER = Logger(__name__)


def validate_api_key(api_key: str) -> None:
    """Handles validation of the user's OpenAI API key."""
    if not api_key:
        raise argparse.ArgumentTypeError("Invalid or missing OpenAI API key.")
    os.environ["OPENAI_API_KEY"] = api_key


def validate_repository(repository: str) -> None:
    """Handles validation of the user's repository URL or path."""
    if repository is None:
        repository = CONF.git.repository

    if not utils.is_valid_git_repo(repository):
        raise ValueError(f"Invalid git repository: {repository}")

    if not repository or (
        not str(repository).startswith("http") and not Path(str(repository)).exists()
    ):
        raise argparse.ArgumentTypeError("Invalid or missing code repository.")

    name = CONF.git.get_repository_name(repository)
    CONF.git.name = name
    CONF.git.repository = repository


async def main(api_key: str, output: str, repository: Optional[str]) -> None:
    """Main entrypoint for README-AI application."""
    LOGGER.info("README-AI is now executing.")
    CONF.paths.readme = output
    validate_api_key(api_key)
    validate_repository(repository)
    gpt = OpenAIHandler(CONF)
    await generate_readme(gpt)


async def generate_readme(gpt: OpenAIHandler) -> None:
    """Orchestrates the README file generation process."""
    name, repository = CONF.git.name, CONF.git.repository
    scanner = preprocess.RepositoryParserWrapper(CONF, CONF_HELPER)
    dependencies, file_text = get_dependencies(scanner, repository)
    code_summary, slogan, overview, features = {}, "", "", ""
    try:
        code_summary = await generate_code_to_text(gpt, file_text)
        slogan, overview, features = await generate_markdown_text(
            gpt, repository, code_summary
        )
    except Exception as exc:
        LOGGER.error(f"Exception: {exc}")
    finally:
        await gpt.close()

    format_text_to_markdown(name, slogan, overview, features)
    builder.build_markdown(CONF, CONF_HELPER, dependencies, code_summary)
    LOGGER.info("README-AI execution complete.\n")


def get_dependencies(
    scanner: preprocess.RepositoryParserWrapper, repository: str
) -> Tuple[List[str], str]:
    """Extracts dependencies and file_text using the scanner."""
    dependencies, file_text = scanner.get_dependencies(repository)
    LOGGER.info(f"Codebase dependencies: {dependencies}")
    LOGGER.info(f"Total files: {len(file_text)}")
    return dependencies, file_text


async def generate_code_to_text(gpt: OpenAIHandler, file_text: str) -> Dict[str, str]:
    """Generates code_to_text using gpt."""
    return await gpt.code_to_text(
        CONF_HELPER.ignore_files, file_text, CONF.prompts.code_summary
    )


async def generate_markdown_text(
    gpt: OpenAIHandler, repository: str, code_summary: str
) -> Tuple[str, str, str]:
    """Generates slogan, overview and features using gpt."""
    prompts = [
        CONF.prompts.slogan.format(CONF.git.name),
        CONF.prompts.overview.format(repository, code_summary),
        CONF.prompts.features.format(repository, code_summary),
    ]
    responses = await gpt.chat_to_text(prompts)
    return responses[:3]


def format_text_to_markdown(
    name: str, slogan: str, overview: str, features: str
) -> None:
    """Updates CONF.md.header and CONF.md.intro."""
    CONF.md.header = CONF.md.header.format(name, slogan)
    CONF.md.intro = CONF.md.intro.format(overview, features)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generates a README.md file for a given repository."
    )
    parser.add_argument(
        "-k",
        "--api-key",
        default=os.environ["OPENAI_API_KEY"],
        help="OpenAI API key.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="readme_ai.md",
        help="README.md file output path.",
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="URL or path to repository.",
    )
    parser.add_argument(
        "-t",
        "--template",
        help="Template to use for README.md file.",
    )
    args = parser.parse_args()

    asyncio.run(main(args.api_key, args.output, args.repository))
