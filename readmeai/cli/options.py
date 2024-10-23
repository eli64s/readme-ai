"""Command-line interface options for the readme-ai package."""

from __future__ import annotations

import click

from readmeai import __version__
from readmeai.config.constants import (
    BadgeStyleOptions,
    HeaderStyleOptions,
    ImageOptions,
    LLMService,
)


def prompt_for_image(
    ctx: click.Context | None = None,
    param: click.Parameter | None = None,
    value: str | None = None,
) -> str:
    """Prompt the user for a custom image URL."""
    if value is None:
        return ImageOptions.BLUE.value
    if value == ImageOptions.CUSTOM.name:
        return click.prompt("Provide an image file path or URL")
    elif value == ImageOptions.LLM.name:
        return ImageOptions.LLM.value
    elif value in ImageOptions.__members__:
        return ImageOptions[value].value
    else:
        raise click.BadParameter(f"Invalid image provided: {value}")


def version_callback(
    ctx: click.Context | None = None,
    param: click.Parameter | None = None,
    value: str | None = None,
) -> None:
    """Prints the version of readme-ai."""
    if not value or (ctx and ctx.resilient_parsing):
        return
    click.echo(f"readme-ai version {__version__}")
    if ctx is not None:
        ctx.exit()


align = click.option(
    "-a",
    "--align",
    type=click.Choice(["center", "left", "right"], case_sensitive=False),
    default="center",
    help="align for the README.md file header sections.",
)

api = click.option(
    "--api",
    type=click.Choice(
        [opt.value for opt in LLMService],
        case_sensitive=False,
    ),
    default=LLMService.OFFLINE,
    help="""LLM API service to use for README.md file generation. Current support for:\n
    - ANTHROPIC    # Anthropic: claude-3-5-sonnet \n
    - GEMINI       # Google Gemini: gemini-pro \n
    - OFFLINE      # Offline Mode: run without a LLM API \n
    - OLLAMA       # Ollama: llama3, mistral, etc. \n
    - OPENAI       # OpenAI: gpt-3.5-turbo \n
    """,
)

badge_color = click.option(
    "-bc",
    "--badge-color",
    type=str,
    default="0080ff",
    help="Change color of shields.io badges. Provide color name or hex code.",
)

badge_style = click.option(
    "-bs",
    "--badge-style",
    type=click.Choice(
        [opt.value for opt in BadgeStyleOptions],
        case_sensitive=False,
    ),
    default=BadgeStyleOptions.DEFAULT.value,
    help="""\
        Style for shields.io badges. Current support for:\n
        - default \n
        - flat \n
        - flat-square \n
        - for-the-badge \n
        - plastic \n
        - skills \n
        - skills-light \n
        - social \n
        """,
)

base_url = click.option(
    "--base-url",
    type=str,
    default="https://api.openai.com/v1/chat/completions",
    help="Base URL for the LLM API service.",
)

context_window = click.option(
    "-cw",
    "--context-window",
    default=3900,
    type=int,
    help="Maximum number of tokens to use for the model's context window.",
)

emojis = click.option(
    "-e",
    "--emojis",
    is_flag=True,
    default=False,
    help="Adds an emoji prefix to each header of the README.md file. For example, the header ## 'Overview' would change to '## 📍 Overview'.",
)

header_style = click.option(
    "-hs",
    "--header-style",
    type=click.Choice(
        [opt.name for opt in HeaderStyleOptions],
        case_sensitive=False,
    ),
    default="classic",
    help="Header template styles.",
)

toc_style = click.option(
    "-ts",
    "--toc-style",
    type=click.Choice(
        ["bullet", "fold", "links", "number", "roman"],
        case_sensitive=False,
    ),
    default="bullet",
    help="Table of Contents template styles.",
)

image = click.option(
    "-i",
    "--image",
    type=click.Choice(
        [opt.name for opt in ImageOptions],
        case_sensitive=False,
    ),
    default=ImageOptions.BLUE.name,
    callback=prompt_for_image,
    show_choices=True,
    help="""\
        Project logo image displayed in the README file header. The following options are currently supported:\n
        - CUSTOM (provide local image path or URL) \n
        - LLM (generate project logo using LLM API) \n
        - BLACK \n
        - BLUE \n
        - CLOUD \n
        - GRADIENT \n
        - GREY \n
        - PURPLE \n
        """,
)

model = click.option(
    "-m",
    "--model",
    default="gpt-3.5-turbo",
    help="LLM API service to use for README file text generation.",
)

output = click.option(
    "-o",
    "--output",
    default="readme-ai.md",
    help="Output file name for your README file.",
)

rate_limit = click.option(
    "-rl",
    "--rate-limit",
    default=10,
    type=click.IntRange(1, 25, clamp=True),
    help="Number of requests per minute for the LLM API service.",
)

repository = click.option(
    "-r",
    "--repository",
    required=True,
    help="Provide a remote repository URL (GitHub, GitLab, BitBucket), or local path to your project.",
)

temperature = click.option(
    "-t",
    "--temperature",
    default=0.1,
    type=click.FloatRange(min_open=0.0, max=2.0, clamp=True),
    help="Increasing temperature yields more randomness in text generation.",
)

top_p = click.option(
    "--top-p",
    default=0.9,
    type=click.FloatRange(0.0, 1.0, clamp=True),
    help="Top-p sampling probability for the model's generation.",
)

tree_depth = click.option(
    "-td",
    "--tree-depth",
    default=2,
    type=int,
    help="Maximum depth of the directory tree generated for the README file.",
)
