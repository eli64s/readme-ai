"""Automate README.md generation for your codebase using OpenAI's API."""

import asyncio
import os
from pathlib import Path

import dacite
import openai
import pandas as pd
import typer

import builder
import model
import preprocess
from conf import AppConf, load_conf_helper
from file_factory import FileHandler
from logger import Logger

app = typer.Typer()
CONFIG_FILE = "conf/conf.toml"
LOGGER = Logger("readmeai_logger")


@app.command()
def main(
    api_key: str = typer.Option(None, help="Your OpenAI API key."),
    local: str = typer.Option(None, help="Path to local codebase directory."),
    output: str = typer.Option("docs/README.md", help="Path to output README.md file."),
    remote: str = typer.Option(None, help="URL of remote GitHub repository."),
):
    if not os.getenv("OPENAI_API_KEY") and not api_key:
        typer.echo("Error: Please provide your OpenAI API key.")
        raise typer.Exit(code=1)

    if not local and not remote:
        typer.echo(
            "Error: Please provide either a local directory path or a remote repository URL."
        )
        raise typer.Exit(code=1)

    asyncio.run(generate_readme(api_key, local, output, remote))


async def generate_readme(api_key: str, local: str, output: str, remote: str) -> None:
    LOGGER.info("README-AI is now executing.")

    # Load configuration
    conf_path = Path(CONFIG_FILE).resolve()
    conf = load_configuration(conf_path)
    conf_helper = load_conf_helper(conf)

    # Set command line arguments
    if api_key:
        openai.api_key = api_key
    if output:
        conf.paths.md = output
    if local:
        conf.github.local = local
    if remote:
        conf.github.remote = remote

    # Process repository
    if local:
        LOGGER.info(f"Using local directory: {conf.github.local}")
        conf.github.path = conf.github.local
        repo_contents = preprocess.get_codebase_local(conf.github.local)
    else:
        LOGGER.info(f"Using GitHub remote repository: {conf.github.remote}")
        conf.github.path = conf.github.remote
        repo_contents = preprocess.get_codebase_remote(conf.github.remote)

    repo = conf.github.path
    name = preprocess.get_repo_name(repo)
    conf.github.name = name
    file_exts = conf_helper.file_extensions
    file_names = conf_helper.file_names
    ignore_files = conf_helper.ignore_files
    dependencies = preprocess.get_project_dependencies(repo, file_exts, file_names)

    LOGGER.info(f"Creating README.md for the repository: {name}")
    LOGGER.info(f"Total files to document: {len(repo_contents)}")
    LOGGER.info(f"\nProject dependencies list: {dependencies}\n")

    # Use OpenAI API to generate documentation
    prompt_intro = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan
    codebase_docs = await model.code_to_text(ignore_files, repo_contents)
    introduction = model.generate_summary_text(prompt_intro.format(name))
    intro_slogan = model.generate_summary_text(prompt_slogan.format(name))
    conf.md.intro = conf.md.intro.format(introduction)
    documentation = pd.DataFrame(codebase_docs, columns=["Module", "Summary"])

    LOGGER.info(f"OpenAI generated codebase summaries:\n\n{documentation}\n")

    # Build README.md
    documentation.to_csv(conf.paths.docs, index=False)
    builder.build(conf, conf_helper, dependencies, documentation, intro_slogan)

    LOGGER.info("README-AI execution complete.\n")


def load_configuration(config_path):
    handler = FileHandler()
    conf_dict = handler.read(config_path)
    return dacite.from_dict(AppConf, conf_dict)


if __name__ == "__main__":
    app()
