"""CLI entrypoint for readme-ai."""

from typing import Optional

import click

from readmeai.cli import options
from readmeai.main import main


@click.command()
@options.align
@options.api_key
@options.badges
@options.emojis
@options.image
@options.model
@options.offline
@options.output
@options.repository
@options.temperature
@options.template
@options.language
def commands(
    align: Optional[str],
    api_key: str,
    badges: Optional[str],
    emojis: Optional[bool],
    image: Optional[str],
    model: Optional[str],
    offline: Optional[bool],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    template: Optional[int],
    language: Optional[str],
):
    """Entry point for the readme-ai CLI application."""
    main(
        align=align,
        api_key=api_key,
        badges=badges,
        emojis=emojis,
        image=image,
        model=model,
        offline=offline,
        output=output,
        repository=repository,
        temperature=temperature,
    )


if __name__ == "__main__":
    commands()
