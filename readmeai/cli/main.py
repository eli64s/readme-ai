"""Entrypoint for the command-line interface for readme-ai."""

import click
from readmeai.auth import auth_source_label, get_openai_bearer_token, login_openai_codex as login_openai_codex_flow, print_login_success
from readmeai.cli import options
from readmeai.config.settings import ConfigLoader, GitSettings
from readmeai.core.logger import get_logger
from readmeai.core.pipeline import readme_agent
from readmeai.oauth_openai_codex import probe_openai_codex_responses

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
@options.openai_auth_mode
@options.context_window
@options.emojis
@options.header_style
@options.logo
@options.logo_size
@options.login_openai_codex
@options.check_openai_auth
@options.probe_openai_codex
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
    openai_auth_mode: str,
    context_window: int,
    emojis: bool,
    header_style: str,
    logo: str,
    logo_size: str,
    login_openai_codex: bool,
    check_openai_auth: bool,
    probe_openai_codex: bool,
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
    if login_openai_codex:
        auth_path = login_openai_codex_flow()
        print_login_success(auth_path)
        return

    if check_openai_auth:
        token = get_openai_bearer_token()
        click.echo(f"OpenAI auth source: {auth_source_label()}")
        click.echo(f"OpenAI token available: {'yes' if token else 'no'}")
        return

    if probe_openai_codex:
        token = get_openai_bearer_token()
        if not token:
            raise click.ClickException("No OpenAI token found. Set OPENAI_API_KEY or run --login-openai-codex first.")
        result = probe_openai_codex_responses(token, model=model or 'gpt-4o-mini')
        click.echo(f"Codex probe status: {result['status']}")
        click.echo(str(result['body']))
        return

    config.config.git = GitSettings(repository=repository)

    config.config.llm = config.config.llm.model_copy(
        update={
            "api": api,
            "base_url": base_url,
            "openai_auth_mode": openai_auth_mode,
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
