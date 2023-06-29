#!/usr/bin/env python3

import argparse
import asyncio
import os
from typing import Dict, List, Tuple

import conf
import preprocess
from builder import build_markdown_file
from logger import Logger
from model import OpenAIHandler


async def main(api_key: str, output: str, repository: str) -> None:
    """Main entrypoint for README-AI application."""
    conf.ApiConfig.validate_api_key(api_key)
    conf.GitConfig.validate_repository(repository)
    config.git = conf.GitConfig(repository=repository)
    config.paths.readme = output

    LOGGER.info("Model: %s", dict(config.api, api_key=("*" * 16)))
    LOGGER.info("Repository: %s", config.git)

    llm = OpenAIHandler(config)
    await generate_readme(llm)


async def generate_readme(llm: OpenAIHandler) -> None:
    """Orchestrates the README file generation process."""
    name, repository = config.git.name, config.git.repository
    scanner = preprocess.RepositoryParserWrapper(config, config_helper)
    dependencies, file_text = get_dependencies(scanner, repository)

    LOGGER.info(f"Dependencies: {dependencies}")
    LOGGER.info(f"Total files: {len(file_text)}")

    code_summary, slogan, overview, features = {}, "", "", ""
    try:
        code_summary = await generate_code_to_text(llm, file_text)
        slogan, overview, features = await generate_markdown_text(
            llm, repository, code_summary
        )
    except Exception as excinfo:
        LOGGER.error(f"Exception: {excinfo}")
    finally:
        await llm.close()

    format_markdown_sections(name, slogan, overview, features)
    build_markdown_file(config, config_helper, dependencies, code_summary)


def format_markdown_sections(
    name: str, slogan: str, overview: str, features: str
) -> None:
    """Updates config.md.header and config.md.intro."""
    config.md.header = config.md.header.format(name, slogan)
    config.md.intro = config.md.intro.format(overview, features)


async def generate_code_to_text(llm: OpenAIHandler, file_text: str) -> Dict[str, str]:
    """Generates code_to_text using llm."""
    return await llm.code_to_text(
        config_helper.ignore_files, file_text, config.prompts.code_summary
    )


async def generate_markdown_text(
    llm: OpenAIHandler, repository: str, code_summary: str
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


if __name__ == "__main__":
    LOGGER = Logger(__name__)
    LOGGER.info("README-AI is now executing.")

    parser = argparse.ArgumentParser(
        description="Generates a README.md file for a given repository."
    )
    parser.add_argument(
        "-k",
        "--api-key",
        default=os.environ["OPENAI_API_KEY"],
        help="OpenAI API secret key.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="readme-ai.md",
        help="README.md output file path.",
    )
    parser.add_argument(
        "-r",
        "--repository",
        help="Repository URL or directory path.",
    )
    parser.add_argument(
        "-t",
        "--template",
        help="Template to use for README.md file.",
    )
    parser.add_argument(
        "-l",
        "--language",
        help="Language to write README.md file in.",
    )
    args = parser.parse_args()
    config = conf.load_config()
    config_model = conf.AppConfigModel(app=config)
    config_helper = conf.load_config_helper(config_model)

    asyncio.run(main(args.api_key, args.output, args.repository))

    LOGGER.info("README-AI execution complete.\n")
