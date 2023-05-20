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
from conf import AppConfig, ConfigHelper, load_configuration_helper
from file_factory import FileHandler
from logger import Logger

app = typer.Typer()
CONFIG = Path("conf/conf.toml")
LOGGER = Logger("readmeai_logger")


def set_api_key(api_key: Optional[str]) -> None:
    """
    Validate OpenAI API key exists as an
    environment variable or as an argument.
    """
    if api_key:
        openai.api_key = api_key
    else:
        api_key = os.environ["OPENAI_API_KEY"]
        if api_key:
            openai.api_key = api_key
        else:
            typer.echo("Error: Invalid or missing OpenAI API key.")
            raise typer.Exit(code=1)


def validate_repository(repository: Optional[str]) -> None:
    """Validates the repository argument."""
    if repository:
        if not repository.startswith("http"):
            if not Path(repository).exists():
                typer.echo("Error: Path to repository does not exist.")
                raise typer.Exit(code=1)
    else:
        typer.echo("Error: Invalid or missing repository URL or path.")
        raise typer.Exit(code=1)


@app.command()
def main(
    api_key: Optional[str] = typer.Option(None, help="Your OpenAI API key."),
    output: str = typer.Option("README_AI.md", help="Path to your README file."),
    repository: Optional[str] = typer.Option(None, help="Repository url or path."),
) -> None:
    """Generates README.md file for your repository using OpenAI's GPT APIs."""
    set_api_key(api_key)
    validate_repository(repository)
    asyncio.run(generate_readme(output, repository))


async def generate_readme(output: str, repository: str) -> None:
    """Orchestrates the execution of the README-AI application."""
    LOGGER.info("README-AI is now executing.")

    conf = load_configuration(CONFIG)
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

    summaries = await llm_text_generation(conf, file_contents, conf_helper.ignore_files)
    summaries = pd.DataFrame(summaries, columns=["Module", "Summary"])

    LOGGER.info(f"OpenAI LLM generated code summaries:\n\n{summaries}\n")

    build_readme(conf, conf_helper, dependency_list, summaries)

    LOGGER.info("README-AI execution complete.\n")


async def llm_text_generation(
    conf: AppConfig, file_contents: list, ignore_files: list
) -> list:
    """Generate code summaries for all files in a repository."""
    name = conf.git.name
    prompt_intro = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan
    prompt_code = conf.api.prompt_code_to_text
    code_summaries = await model.code_to_text(ignore_files, file_contents, prompt_code)
    intro = model.generate_summary_text(prompt_intro.format(name))
    slogan = model.generate_summary_text(prompt_slogan.format(name))
    conf.md.intro = conf.md.intro.format(intro)
    conf.md.slogan = conf.md.slogan.format(slogan)

    return code_summaries


def build_readme(
    conf: AppConfig,
    conf_helper: ConfigHelper,
    dependency_list: list,
    summaries: pd.DataFrame,
) -> None:
    """Builds the README Markdown file."""
    summaries.to_csv(conf.paths.docs, index=False)
    builder.build(conf, conf_helper, dependency_list, summaries)


def load_configuration(config_path: str) -> AppConfig:
    """Loads the configuration file."""
    handler = FileHandler()
    conf_dict = handler.read(config_path)
    return dacite.from_dict(AppConfig, conf_dict)


if __name__ == "__main__":
    app()
