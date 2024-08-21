"""
CLI entrypoint for the readme-ai package.
"""

import click

from readmeai.__main__ import readme_agent
from readmeai.cli import options


@click.command()
@options.align
@options.api
@options.badge_color
@options.badge_style
@options.base_url
@options.context_window
@options.emojis
@options.header_style
@options.image
@options.model
@options.output
@options.rate_limit
@options.repository
@options.temperature
@options.toc_style
@options.top_p
@options.tree_depth
def main(
    align: str,
    api: str,
    badge_color: str,
    badge_style: str,
    base_url: str,
    context_window: int,
    emojis: bool,
    header_style: str,
    image: str,
    model: str,
    output: str,
    rate_limit: int,
    repository: str,
    temperature: float,
    toc_style: str,
    top_p: float,
    tree_depth: int,
) -> None:
    """Entry point for the readme-ai CLI application."""
    readme_agent(
        align=align,
        api=api,
        badge_color=badge_color,
        badge_style=badge_style,
        base_url=base_url,
        context_window=context_window,
        emojis=emojis,
        header_style=header_style,
        image=image,
        model=model,
        output=output,
        rate_limit=rate_limit,
        repository=repository,
        temperature=temperature,
        toc_style=toc_style,
        top_p=top_p,
        tree_depth=tree_depth,
    )


if __name__ == "__main__":
    main()
