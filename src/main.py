"""Generates README.md file for your repository using OpenAI's GPT APIs."""

import asyncio
import os
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
CONFIG_FILE = "conf/conf.toml"
LOGGER = Logger("readmeai_logger")


@app.command()
def main(
    api_key: Optional[str] = typer.Option(None, help="Your OpenAI API key."),
    local: Optional[str] = typer.Option(None, help="Path to local repository."),
    output: str = typer.Option("README_AI.md", help="Path to your README file."),
    remote: Optional[str] = typer.Option(None, help="URL to remote repository."),
) -> None:
    """Generates README.md file for your repository using OpenAI's GPT APIs."""

    check_arguments(api_key, local, remote)
    asyncio.run(generate_readme(api_key, local, output, remote))


def check_arguments(
    api_key: Optional[str], local: Optional[str], remote: Optional[str]
) -> None:
    """Validates the command line arguments."""

    if not os.getenv("OPENAI_API_KEY") and not api_key:
        typer.echo("Error: Please provide your OpenAI API key.")
        raise typer.Exit(code=1)

    if not local and not remote:
        typer.echo("Error: Please provide a local path or remote url.")
        raise typer.Exit(code=1)


async def generate_readme(
    api_key: Optional[str], local: Optional[str], output: str, remote: Optional[str]
) -> None:
    """Orchestrates the execution of the README-AI application."""

    LOGGER.info("README-AI is now executing.")

    conf = load_configuration(CONFIG_FILE)
    conf_helper = load_configuration_helper(conf)

    set_command_line_arguments(api_key, conf, local, output, remote)

    repo = conf.git.path
    repo_contents = preprocess.get_codebase(repo)
    conf.git.name = preprocess.get_repo_name(repo)
    dependency_list = preprocess.get_project_dependencies(
        repo, conf_helper.language_names, conf_helper.dependency_files
    )

    LOGGER.info(f"Total files to document: {len(repo_contents)}")
    LOGGER.info(f"\nProject dependencies list: {dependency_list}\n")

    summaries = await generate_code_summaries(
        conf, conf_helper.ignore_files, repo_contents
    )
    code_summaries = pd.DataFrame(summaries, columns=["Module", "Summary"])

    LOGGER.info(f"OpenAI LLM generated code summaries:\n\n{code_summaries}\n")

    build_readme(conf, conf_helper, code_summaries, dependency_list)

    LOGGER.info("README-AI execution complete.\n")


def set_command_line_arguments(
    api_key: Optional[str],
    conf: AppConfig,
    local: Optional[str],
    output: str,
    remote: Optional[str],
) -> None:
    """Set the command line arguments according."""

    if api_key:
        openai.api_key = api_key
    if output:
        conf.paths.md = output
    if local:
        conf.git.path, conf.git.local = local, local
        LOGGER.info(f"Using local repository: {conf.git.local}")
    if remote:
        conf.git.path, conf.git.remote = remote, remote
        LOGGER.info(f"Using remote repository: {conf.git.remote}")


async def generate_code_summaries(
    conf: AppConfig, ignore_files: list, repo_contents: list
) -> list:
    """Generate code summaries for all files in a repository."""

    name = conf.git.name
    prompt_intro = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan

    code_summaries = await model.code_to_text(ignore_files, repo_contents)
    intro = model.generate_summary_text(prompt_intro.format(name))
    slogan = model.generate_summary_text(prompt_slogan.format(name))
    conf.md.intro = conf.md.intro.format(intro)
    conf.md.slogan = conf.md.slogan.format(slogan)

    return code_summaries


def build_readme(
    conf: AppConfig,
    conf_helper: ConfigHelper,
    docs: pd.DataFrame,
    dependencies: list,
) -> None:
    """Generates the README.md file."""

    docs.to_csv(conf.paths.docs, index=False)
    builder.build(conf, conf_helper, docs, dependencies)


def load_configuration(config_path: str) -> AppConfig:
    """Loads the configuration file."""

    handler = FileHandler()
    conf_dict = handler.read(config_path)
    return dacite.from_dict(AppConfig, conf_dict)


if __name__ == "__main__":
    app()
