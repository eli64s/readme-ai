"""CLI entrypoint for the readme-ai application."""

from typing import Optional

import click

from readmeai.app import readme_agent
from readmeai.cli import options


@click.command()
@options.align
@options.api
@options.badges
@options.badge_color
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
    align: Optional[str],
    api: str,
    badges: Optional[str],
    badge_color: Optional[str],
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
        align=align,
        api=api,
        badges=badges,
        badge_color=badge_color,
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
