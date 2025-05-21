"""Entrypoint for the command-line interface for readme-ai."""

import click
from readmeai.cli import options
from readmeai.config.settings import ConfigLoader, GitSettings
from readmeai.core.logger import get_logger
from readmeai.core.pipeline import readme_agent

config = ConfigLoader()
logger = get_logger(__name__)


@click.command()
@click.option(
    "--version",
    "-V",
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
@options.logo
@options.logo_size
@options.model
@options.navigation_style
@options.output
@options.rate_limit
@options.repository
@options.system_message
@options.temperature
@options.top_p
@options.tree_max_depth
def main(
    align: str,
    api: str,
    badge_color: str,
    badge_style: str,
    base_url: str,
    context_window: int,
    emojis: bool,
    header_style: str,
    logo: str,
    logo_size: str,
    model: str,
    navigation_style: str,
    output: str,
    rate_limit: int,
    repository: str,
    system_message: str,
    temperature: float,
    top_p: float,
    tree_max_depth: int,
) -> None:
    """Entry point for the readme-ai CLI application."""
    config.config.git = GitSettings(repository=repository)

    config.config.llm = config.config.llm.model_copy(
        update={
            "api": api,
            "base_url": base_url,
            "context_window": context_window,
            "model": model,
            "rate_limit": rate_limit,
            "system_message": system_message,
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
            "logo": logo,
            "logo_size": logo_size,
            "navigation_style": navigation_style,
            "tree_max_depth": tree_max_depth,
        },
    )

    logger.debug(f"Pydantic settings: {config.__dict__.keys()}")
    logger.debug(f"Repository settings: {config.config.git.model_dump()}")
    logger.debug(f"LLM API settings: {config.config.llm.model_dump()}")

    readme_agent(config=config, output_file=output)


if __name__ == "__main__":
    main()
