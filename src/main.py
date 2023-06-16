"""Generates README.md file for your repository using OpenAI's GPT APIs."""

import asyncio
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import openai
import typer

import builder
import conf
import preprocess
from logger import Logger
from model import OpenAIHandler

CONF = conf.load_config()
CONF_HELPER = conf.load_config_helper(CONF)
LOGGER = Logger(__name__)

app = typer.Typer()


def validate_api_key(api_key: str) -> None:
    """Handles validation of the user's OpenAI API key."""
    if not api_key:
        typer.echo("Error: Invalid or missing OpenAI API key.")
        raise typer.Exit(code=1)
    openai.api_key = api_key


def validate_repository(repository: Optional[str]) -> Tuple[str, str]:
    """Handles validation of the user's repository URL or path."""
    if repository is None:
        repository = CONF.git.repository
    if not repository or (
        not str(repository).startswith("http") and not Path(str(repository)).exists()
    ):
        typer.echo("Error: Invalid or missing repository URL or path.")
        raise typer.Exit(code=1)

    name = CONF.git.get_repository_name(CONF.git.hosts, repository)
    CONF.git.name = name
    CONF.git.repository = repository


@app.command()
def main(
    api_key: str = typer.Option(os.environ["OPENAI_API_KEY"], help="OpenAI API key."),
    output: str = typer.Option("readme_ai.md", help="Output path of the README."),
    repository: Optional[str] = typer.Option(None, help="URL or path to repository."),
) -> None:
    """Typer command-line interface entry point."""
    LOGGER.info("README-AI is now executing.")
    CONF.paths.readme = output
    validate_api_key(api_key)
    validate_repository(repository)
    api_handler = OpenAIHandler(CONF)
    asyncio.run(generate_readme(api_handler))


async def generate_code_summaries(
    api_handler: OpenAIHandler, file_text: list, prompt: str
) -> Dict[str, str]:
    """Converts code to natural language using large language models."""
    summaries = await api_handler.code_to_text(
        CONF_HELPER.ignore_files,
        file_text,
        prompt,
    )
    return summaries


async def generate_chat_text(api_handler: OpenAIHandler,
                             prompts: List[str]) -> List[str]:
    """Generate general text giving various prompts to OpenAI's API."""
    summary_texts = await api_handler.chat_to_text(prompts)
    return summary_texts


async def generate_readme(api_handler: OpenAIHandler) -> None:
    """Orchestrates the README file generation process."""
    name = CONF.git.name
    repository = CONF.git.repository
    scanner = preprocess.RepositoryParserWrapper(CONF, CONF_HELPER)
    dependencies, file_text = scanner.get_dependencies(repository)
    LOGGER.info(f"Total dependencies: {len(dependencies)}")
    LOGGER.info(f"Total files: {len(file_text)}")

    try:
        summaries, overview, features, slogan = None, None, None, None
        summaries = await generate_code_summaries(
            api_handler,
            file_text,
            CONF.prompts.code_summary,
        )
        chat_prompts = [
            CONF.prompts.slogan.format(name),
            CONF.prompts.overview.format(repository, summaries),
            CONF.prompts.features.format(repository, summaries),
        ]
        responses = await generate_chat_text(api_handler, chat_prompts)
        slogan, overview, features = responses[:3]

    except openai.OpenAIError as exc:
        LOGGER.error(f"OpenAI API Error: {exc}")

    except Exception as exc:
        LOGGER.error(f"Error: {exc}")

    finally:
        await api_handler.close()

    CONF.md.header = CONF.md.header.format(name, slogan)
    CONF.md.intro = CONF.md.intro.format(overview, features)
    builder.build_readme(CONF, CONF_HELPER, dependencies, summaries)
    LOGGER.info("README-AI execution complete.\n")


if __name__ == "__main__":
    app()
