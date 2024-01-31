"""CLI entrypoint for the readme-ai application."""

from typing import Optional, Tuple

import click

from readmeai.app import readme_agent
from readmeai.cli import options


@click.command()
@options.align
@options.api_key
@options.badges
@options.badge_color
@options.emojis
@options.image
@options.language
@options.max_tokens
@options.model
@options.offline
@options.output
@options.repository
@options.temperature
@options.tree_depth
@options.template
@options.vertex_ai
def main(
    align: Optional[str],
    api_key: Optional[str],
    badges: Optional[str],
    badge_color: Optional[str],
    emojis: Optional[bool],
    image: Optional[str],
    language: Optional[str],
    max_tokens: Optional[int],
    model: Optional[str],
    offline: Optional[bool],
    output: Optional[str],
    repository: str,
    temperature: Optional[float],
    template: Optional[str],
    tree_depth: Optional[int],
    vertex_ai: Optional[Tuple[str, str]],
) -> None:
    """Entry point for the readme-ai CLI application."""
    readme_agent(
        align=align,
        api_key=api_key,
        badges=badges,
        badge_color=badge_color,
        emojis=emojis,
        image=image,
        # language=language,
        max_tokens=max_tokens,
        model=model,
        offline=offline,
        output=output,
        repository=repository,
        temperature=temperature,
        # template=template,
        tree_depth=tree_depth,
        vertex_ai=vertex_ai,
    )


if __name__ == "__main__":
    main()
