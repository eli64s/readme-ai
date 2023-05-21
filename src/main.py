"""Generates README.md file for your repository using OpenAI's GPT APIs."""

import asyncio
import os
from pathlib import Path
from typing import Optional

import dacite
import openai
import pandas as pd
import typer

import builder
import model
import preprocess
from conf import AppConfig, load_configuration_helper
from factory import FileHandler
from logger import Logger

app = typer.Typer()

LOGGER = Logger("readmeai_logger")


def set_openai_api_key(api_key: Optional[str]) -> str:
    """Validates and sets the OpenAI API key provided by the user."""
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
    if api_key is None:
        typer.echo("Error: Invalid or missing OpenAI API key.")
        raise typer.Exit(code=1)
    return api_key


def validate_repository(repository: Optional[str]) -> str:
    """Validates the repository URL or path provided by the user."""
    if repository is None or (
        not repository.startswith("http") and not Path(repository).exists()
    ):
        typer.echo("Error: Invalid or missing repository URL or path.")
        raise typer.Exit(code=1)
    return repository


def get_configuration(config_path: str) -> AppConfig:
    """Load README-AI configuration from TOML file."""
    handler = FileHandler()
    conf_dict = handler.read(config_path)
    return dacite.from_dict(AppConfig, conf_dict)


@app.command()
def main(
    api_key: Optional[str] = typer.Option(None, help="Your OpenAI API key."),
    output: str = typer.Option(
        "README_AI.md", help="Path to your README file."
    ),
    repository: Optional[str] = typer.Option(
        None, help="Repository url or path."
    ),
) -> None:
    api_key = set_openai_api_key(api_key)
    openai.api_key = api_key

    repository = validate_repository(repository)

    asyncio.run(generate_readme(output, repository))


async def generate_readme(output: str, repository: str) -> None:
    """Generate README.md file for your repository using OpenAI's GPT APIs."""
    LOGGER.info("README-AI is now executing.")
    conf_path = Path("conf/conf.toml")

    conf = get_configuration(conf_path)
    conf_helper = load_configuration_helper(conf)

    conf.paths.md = output
    conf.git.repository = repository
    conf.git.name = preprocess.get_repository_name(repository)
    file_contents = preprocess.get_repository(repository)
    dependency_list = preprocess.extract_dependencies(
        conf_helper.dependency_files, conf_helper.language_names, repository
    )

    LOGGER.info(f"Total files to document: {len(file_contents)}")
    LOGGER.info(f"\nProject dependencies list: {dependency_list}\n")

    summaries = await llm_text_gen(
        conf, file_contents, conf_helper.ignore_files
    )
    summaries = pd.DataFrame(summaries, columns=["Module", "Summary"])
    summaries.to_csv(conf.paths.docs, index=False)

    LOGGER.info(f"OpenAI LLM generated code summaries:\n\n{summaries}\n")

    builder.build(conf, conf_helper, dependency_list, summaries)

    LOGGER.info("README-AI execution complete.\n")


async def llm_text_gen(
    conf: AppConfig, file_contents: list, ignore_files: list
) -> list:
    """Generate summary text for code files using OpenAI's GPT-3."""
    name = conf.git.name
    prompt_intro = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan
    prompt_code = conf.api.prompt_code_to_text
    code_summaries = await model.code_to_text(
        ignore_files, file_contents, prompt_code
    )
    intro = model.generate_summary_text(prompt_intro.format(name))
    slogan = model.generate_summary_text(prompt_slogan.format(name))
    conf.md.intro = conf.md.intro.format(intro)
    conf.md.slogan = conf.md.slogan.format(slogan)

    return code_summaries


if __name__ == "__main__":
    app()
