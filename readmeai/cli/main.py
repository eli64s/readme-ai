"""CLI commands for readme-ai."""

import asyncio
from typing import Optional

import click

from readmeai.cli import options

from .. import app, conf


@click.command()
@options.api_key
@options.encoding
@options.endpoint
@options.offline_mode
@options.model
@options.output
@options.repository
@options.temperature
@options.language
@options.style
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

    asyncio.run(app.run_model(config, config_helper))


if __name__ == "__main__":
    cli()
