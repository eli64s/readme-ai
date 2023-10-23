"""CLI entrypoint for readme-ai."""

from typing import Optional

import click

from readmeai.cli import options
from readmeai.main import main


@click.command()
@options.api_key
@options.badges
@options.emojis
@options.offline
@options.model
@options.output
@options.repository
@options.temperature
@options.language
@options.style
def commands(
    api_key: str,
    badges: Optional[str],
    emojis: Optional[bool],
    offline: Optional[bool],
    model: Optional[str],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    language: Optional[str],
    style: Optional[int],
):
    """CLI entrypoint for readme-ai."""
    main(
        badges=badges,
        emojis=emojis,
        offline=offline,
        model=model,
        output=output,
        repository=repository,
        temperature=temperature,
    )


if __name__ == "__main__":
    commands()
