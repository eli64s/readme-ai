"""CLI commands for readme-ai."""

from typing import Optional

import click

from readmeai.cli import options

from readmeai.app import run_app


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
    run_app(
        api_key=api_key,
        encoding=encoding,
        endpoint=endpoint,
        offline_mode=offline_mode,
        model=model,
        output=output,
        repository=repository,
        temperature=temperature,
        language=language,
        style=style,
    )


if __name__ == "__main__":
    cli()
