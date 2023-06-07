"""Generates README.md file for your repository using OpenAI's GPT APIs."""

import asyncio
import os
from pathlib import Path
from typing import Optional, Tuple

import openai
import typer

import builder
import conf
import utils
from logger import Logger
from model import OpenAIHandler
from preprocess import RepositoryParser

CONF = conf.load_config()
CONF_HELPER = conf.load_config_helper(CONF)
LOGGER = Logger("readmeai_logger")

app = typer.Typer()


def validate_api_key(api_key: str) -> None:
    """Validates and sets the OpenAI API key provided by the user."""
    if not api_key:
        typer.echo("Error: Invalid or missing OpenAI API key.")
        raise typer.Exit(code=1)
    openai.api_key = api_key


def validate_repository(repository: Optional[str]) -> Tuple[str, str]:
    """Validates the repository URL or path provided by the user."""
    if repository is None:
        repository = CONF.git.repository
    if not repository or (
        not str(repository).startswith("http")
        and not Path(str(repository)).exists()
    ):
        typer.echo("Error: Invalid or missing repository URL or path.")
        raise typer.Exit(code=1)

    CONF.git.name = CONF.git.get_repository_name(CONF.git.hosts, repository)
    CONF.git.repository = repository


@app.command()
def main(
    api_key: str = typer.Option(
        os.environ["OPENAI_API_KEY"], help="OpenAI API key."
    ),
    output: str = typer.Option(
        "README_AI.md", help="Output file path for README.md."
    ),
    repository: Optional[str] = typer.Option(
        None, help="URL or path of the repository."
    ),
) -> None:
    """Typer command-line interface for entry point."""
    CONF.paths.readme = output
    validate_api_key(api_key)
    validate_repository(repository)
    api_handler = OpenAIHandler(CONF)
    asyncio.run(generate_readme(api_handler))


async def generate_readme(api_handler: OpenAIHandler) -> None:
    """Generate README.md file for your repository using OpenAI's GPT APIs."""
    LOGGER.info("README-AI is now executing.")

    name = CONF.git.name
    repository = CONF.git.repository
    analyzer = RepositoryParser(
        CONF_HELPER.ignore_files["directories"],
        CONF_HELPER.ignore_files["files"],
        CONF_HELPER.ignore_files["extensions"],
        CONF_HELPER.language_names,
        CONF_HELPER.language_setup,
    )

    contents = analyzer.analyze(repository, is_remote=True)
    dependencies = analyzer.get_dependency_file_contents(contents)
    dependencies.append(contents["extension"].unique().tolist())
    dependencies.append(contents["language"].unique().tolist())
    dependencies.append(contents["name"].unique().tolist())
    dependencies = list(set(utils.flatten_list(dependencies)))
    file_contents = dict(zip(contents["path"], contents["content"]))

    LOGGER.info(f"Repository dependencies: {dependencies}")
    LOGGER.info(f"Total files to process: {file_contents}")

    summaries, overview, features, slogan = None, None, None, None
    try:
        summaries = await generate_code_summaries(
            file_contents, CONF.prompts.code_summary, api_handler
        )
        LOGGER.info(f"Code summaries: {summaries}")
        chat_prompts = [
            CONF.prompts.slogan.format(name),
            CONF.prompts.overview.format(repository, summaries),
            CONF.prompts.features.format(repository, summaries),
        ]
        responses = await generate_chat_text(chat_prompts, api_handler)
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


async def generate_code_summaries(
    file_contents: list, prompt: str, api_handler: OpenAIHandler
) -> list:
    """Generate summary text for code files using OpenAI's GPT-3."""
    summaries = await api_handler.code_to_text(
        CONF_HELPER.ignore_files, file_contents, prompt
    )
    return summaries


async def generate_chat_text(prompts: str, api_handler: OpenAIHandler) -> str:
    """Generate text using prompts and OpenAI's GPT-3."""
    summary_texts = await api_handler.chat_to_text(prompts)
    return summary_texts


if __name__ == "__main__":
    app()
