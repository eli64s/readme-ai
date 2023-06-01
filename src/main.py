"""Generates README.md file for your repository using OpenAI's GPT APIs."""

import asyncio
import os
from pathlib import Path
from typing import Optional, Tuple

import openai
import typer

import builder
import conf
import model
import preprocess
from logger import Logger

LOGGER = Logger("readmeai_logger")
CONF = conf.load_config()
CONF_HELPER = conf.load_config_helper(CONF)

app = typer.Typer()


def validate_api_key(api_key: Optional[str]) -> None:
    """Validates and sets the OpenAI API key provided by the user."""
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        typer.echo("Error: Invalid or missing OpenAI API key.")
        raise typer.Exit(code=1)

    openai.api_key = api_key


def validate_repository(repository: Optional[str]) -> Tuple[str, str]:
    """Validates the repository URL or path provided by the user."""
    if repository is None:
        repository = CONF.git.repository
    if repository is None or (
        not str(repository).startswith("http")
        and not Path(str(repository)).exists()
    ):
        typer.echo("Error: Invalid or missing repository URL or path.")
        raise typer.Exit(code=1)

    CONF.git.name = CONF.git.get_repository_name(CONF.git.hosts, repository)
    CONF.git.repository = repository


@app.command()
def main(
    api_key: Optional[str] = typer.Option(None, help="Your OpenAI API key."),
    output: str = typer.Option(
        "README_AI.md", help="Path to your README file."
    ),
    repository: Optional[str] = typer.Option(
        None, help="Repository url or directory."
    ),
) -> None:
    """Typer command-line interface for entry point."""
    CONF.paths.readme = output
    validate_api_key(api_key)
    validate_repository(repository)
    api_handler = model.OpenAIHandler(CONF)
    asyncio.run(generate_readme(api_handler))


async def generate_readme(api_handler: model.OpenAIHandler) -> None:
    """Generate README.md file for your repository using OpenAI's GPT APIs."""
    LOGGER.info("README-AI is now executing.")

    name = CONF.git.name
    repository = CONF.git.repository

    file_contents = preprocess.get_repository(repository)
    dependencies = preprocess.extract_dependencies(
        CONF.git.hosts, CONF_HELPER.language_names, repository
    )

    LOGGER.info(f"Total files to document: {len(file_contents)}")
    LOGGER.info(f"\nProject dependencies list: {dependencies}\n")

    summaries, overview, features, slogan = None, None, None, None
    try:
        summaries = await generate_text(
            file_contents, CONF.prompts.code_summary, api_handler
        )
        prompts = [
            CONF.prompts.overview.format(repository, summaries),
            CONF.prompts.features.format(repository, summaries),
            CONF.prompts.slogan.format(name),
        ]
        responses = await get_summary_text(prompts, api_handler)
        overview, features, slogan = responses[:3]

    except openai.OpenAIError as exc:
        LOGGER.error(f"OpenAI API Error: {exc}")

    except Exception as exc:
        LOGGER.error(f"Error: {exc}")

    finally:
        await api_handler.close()

    CONF.md.header = CONF.md.header.format(name, slogan)
    CONF.md.intro = CONF.md.intro.format(overview, features)
    builder.build(CONF, CONF_HELPER, dependencies, summaries)

    LOGGER.info("README-AI execution complete.\n")


async def generate_text(
    file_contents: list, prompt: str, api_handler: model.OpenAIHandler
) -> list:
    """Generate summary text for code files using OpenAI's GPT-3."""
    summaries = await api_handler.code_to_text(
        CONF_HELPER.ignore_files, file_contents, prompt
    )
    return summaries


async def get_summary_text(
    prompt: str, api_handler: model.OpenAIHandler
) -> str:
    """Generate text using prompts and OpenAI's GPT-3."""
    summary_text = await api_handler.summary_text_gen(prompt)
    return summary_text


if __name__ == "__main__":
    app()
