"""Generates README.md file for your repository using OpenAI's GPT APIs."""

import asyncio
import os
from pathlib import Path
from typing import Optional

import openai
import pandas as pd
import typer

import builder
import model
import preprocess
from conf import AppConfig, load_config, load_config_helper
from logger import Logger

CONF = Path("conf/conf.toml")
LOGGER = Logger("readmeai_logger")

app = typer.Typer()
conf = load_config(CONF)
conf_helper = load_config_helper(conf)


def set_openai_api_key(api_key: Optional[str]) -> None:
    """Validates and sets the OpenAI API key provided by the user."""
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        typer.echo("Error: Invalid or missing OpenAI API key.")
        raise typer.Exit(code=1)

    openai.api_key = api_key


def validate_repository(repository: Optional[str]) -> str:
    """Validates the repository URL or path provided by the user."""
    if repository is None:
        repository = conf.git.repository
    if repository is None or (
        not repository.startswith("http") and not Path(repository).exists()
    ):
        typer.echo("Error: Invalid or missing repository URL or path.")
        raise typer.Exit(code=1)
    return repository


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
    set_openai_api_key(api_key)
    repository = validate_repository(repository)

    conf.git.repository = repository
    conf.paths.output = output

    asyncio.run(generate_readme(repository))


async def generate_readme(repository: str) -> None:
    """Generate README.md file for your repository using OpenAI's GPT APIs."""
    LOGGER.info("README-AI is now executing.")

    conf.git.name = preprocess.get_repository_name(repository)
    file_contents = preprocess.get_repository(repository)
    dependency_list = preprocess.extract_dependencies(
        conf_helper.dependency_files, conf_helper.language_names, repository
    )

    LOGGER.info(f"Total files to document: {len(file_contents)}")
    LOGGER.info(f"\nProject dependencies list: {dependency_list}\n")

    summaries = await generate_text(file_contents, conf_helper.ignore_files)
    summaries = pd.DataFrame(summaries, columns=["Module", "Summary"])
    summaries.to_csv(conf.paths.docs, index=False)

    LOGGER.info(f"OpenAI LLM generated code summaries:\n\n{summaries}\n")

    builder.build(conf, conf_helper, dependency_list, summaries)

    LOGGER.info("README-AI execution complete.\n")


async def generate_text(file_contents: list, ignore_files: list) -> list:
    """Generate summary text for code files using OpenAI's GPT-3."""

    code_to_text = conf.prompts.code_to_text
    intro = conf.prompts.intro
    features = conf.prompts.features
    slogan = conf.prompts.slogan
    name = conf.git.name
    repo = conf.git.repository

    summaries = await model.code_to_text(
        ignore_files, file_contents, code_to_text
    )
    prompt_summaries = "\n".join(str(s) for s in summaries)

    intro = model.generate_summary_text(
        intro.format(name, repo, prompt_summaries)
    )
    features = model.generate_summary_text(
        features.format(name, repo, prompt_summaries)
    )
    slogan = model.generate_summary_text(slogan.format(name))

    conf.md.intro = conf.md.intro.format(intro, features)
    conf.md.slogan = conf.md.slogan.format(slogan)

    return summaries


if __name__ == "__main__":
    app()
