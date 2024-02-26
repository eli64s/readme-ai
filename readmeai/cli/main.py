"""CLI entrypoint for the readme-ai application."""

from typing import Optional

import click

from readmeai.cli import options
from readmeai.readmeai import readme_agent


@click.command()
@options.alignment
@options.api
@options.badge_color
@options.badge_style
@options.emojis
@options.image
@options.language
@options.max_tokens
@options.model
@options.output
@options.repository
@options.temperature
@options.tree_depth
@options.template
def main(
    alignment: Optional[str],
    api: str,
    badge_color: Optional[str],
    badge_style: Optional[str],
    emojis: Optional[bool],
    image: Optional[str],
    language: Optional[str],
    max_tokens: Optional[int],
    model: Optional[str],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    template: Optional[str],
    tree_depth: Optional[int],
) -> None:
    """Entry point for the readme-ai CLI application."""
    readme_agent(
        alignment=alignment,
        api=api,
        badge_color=badge_color,
        badge_style=badge_style,
        emojis=emojis,
        image=image,
        # language=language,
        max_tokens=max_tokens,
        model=model,
        output=output,
        repository=repository,
        temperature=temperature,
        # template=template,
        tree_depth=tree_depth,
    )


if __name__ == "__main__":
    main()
