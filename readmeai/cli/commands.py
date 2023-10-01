"""CLI commands for readme-ai."""

from typing import Optional

import click

from readmeai.cli import options
from readmeai.main import main


@click.command()
@options.api_key
@options.badges
@options.encoding
@options.endpoint
@options.offline_mode
@options.model
@options.output
@options.repository
@options.temperature
@options.language
@options.style
def commands(
    api_key: str,
    badges: Optional[str],
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
    main(
        api_key=api_key,
        badges=badges,
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
    commands()
