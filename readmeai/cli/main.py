"""Command-line interface entrypoint for the readme-ai package."""

import click

from readmeai.__main__ import readme_agent
from readmeai.cli import options
from readmeai.config.settings import ConfigLoader, GitSettings
from readmeai.logger import get_logger

config = ConfigLoader()
logger = get_logger(__name__)


@click.command()
@click.option(
    "-V",
    "--version",
    is_flag=True,
    callback=options.version_callback,
    expose_value=False,
    is_eager=True,
    help="Show the version and exit.",
)
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
    config.config.git = GitSettings(repository=repository)
    config.config.llm = config.config.llm.model_copy(
        update={
            "api": api,
            "base_url": base_url,
            "context_window": context_window,
            "model": model,
            "temperature": temperature,
            "top_p": top_p,
        },
    )
    config.config.md = config.config.md.model_copy(
        update={
            "align": align,
            "badge_color": badge_color,
            "badge_style": badge_style,
            "emojis": emojis,
            "header_style": header_style,
            "image": image,
            "toc_style": toc_style,
            "tree_depth": tree_depth,
        },
    )
    config.config.api.rate_limit = rate_limit

    logger.info(f"Pydantic settings: {config.__dict__.keys()}")
    logger.info(f"Repository settings: {config.config.git}")
    logger.info(f"LLM API settings: {config.config.llm}")

    readme_agent(config=config, output_file=output)


if __name__ == "__main__":
    main()
