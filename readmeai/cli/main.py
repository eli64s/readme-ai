"""
CLI entrypoint for the readme-ai package.
"""

from typing import Optional

import click

from readmeai._agent import readme_agent
from readmeai.cli import options


@click.command()
@options.alignment
@options.api
@options.badge_color
@options.badge_style
@options.base_url
@options.context_window
@options.emojis
@options.image
@options.language
@options.model
@options.output
@options.rate_limit
@options.repository
@options.temperature
@options.tree_depth
@options.template
@options.top_p
def main(
    alignment: Optional[str],
    api: Optional[str],
    badge_color: Optional[str],
    badge_style: Optional[str],
    base_url: Optional[str],
    context_window: Optional[int],
    emojis: Optional[bool],
    image: Optional[str],
    language: Optional[str],
    model: Optional[str],
    output: Optional[str],
    rate_limit: Optional[int],
    repository: str,
    temperature: Optional[float],
    template: Optional[str],
    top_p: Optional[float],
    tree_depth: Optional[int],
) -> None:
    """Entry point for the readme-ai CLI application."""
    readme_agent(
        alignment=alignment,
        api=api,
        badge_color=badge_color,
        badge_style=badge_style,
        base_url=base_url,
        context_window=context_window,
        emojis=emojis,
        image=image,
        # language=language,
        model=model,
        output_file=output,
        rate_limit=rate_limit,
        repository=repository,
        temperature=temperature,
        # template=template,
        top_p=top_p,
        tree_depth=tree_depth,
    )


if __name__ == "__main__":
    main()
