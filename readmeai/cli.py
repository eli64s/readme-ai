"""CLI commands for readme-ai."""

import asyncio
import os
from typing import Optional

import click

from . import conf, main


@click.command()
@click.option(
    "-k",
    "--api-key",
    default=os.environ.get("OPENAI_API_KEY", None),
    help="OpenAI API secret key.",
)
@click.option(
    "-c",
    "--encoding",
    default="cl100k_base",
    help="Encodings specify how text is converted into tokens.",
)
@click.option(
    "--endpoint",
    default="https://api.openai.com/v1/chat/completions",
    help="OpenAI API endpoint.",
)
@click.option(
    "-m",
    "--model",
    default="gpt-3.5-turbo",
    help="OpenAI language model engine to use.",
)
@click.option(
    "-f",
    "--offline-mode",
    is_flag=True,
    default=False,
    help="Run the tool in offline mode without calling the OpenAI API.",
)
@click.option(
    "-o",
    "--output",
    default="readme-ai.md",
    help="README.md output file path.",
)
@click.option(
    "-r",
    "--repository",
    required=True,
    help="Repository URL or directory path.",
)
@click.option(
    "-t",
    "--temperature",
    default=1.1,
    help="OpenAI's temperature parameter, a higher value increases randomness.",
)
@click.option(
    "-l",
    "--language",
    help="Language to write README.md file in.",
)
@click.option(
    "-s",
    "--style",
    help="Template to use for README.md file.",
)
def cli(
    api_key: str,
    encoding: Optional[str],
    endpoint: Optional[str],
    offline_mode: Optional[bool],
    model: Optional[str],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    language: Optional[str],
    style: Optional[int],
):
    """CLI entrypoint for readme-ai."""
    config = conf.load_config()
    config_model = conf.AppConfigModel(app=config)
    config_helper = conf.load_config_helper(config_model)
    config.api.model = model
    config.paths.readme = output
    config.api.temperature = temperature
    config.api.offline_mode = offline_mode
    config.git = conf.GitConfig(repository=repository)
    if api_key is None and offline_mode is False:
        config.api.offline_mode = offline_mode

    asyncio.run(main.run_app(config, config_helper))


if __name__ == "__main__":
    cli()
