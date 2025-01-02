"""Command-line interface options for the readme-ai package."""

from __future__ import annotations

import click
from readmeai import __version__
from readmeai.generators.enums import (
    BadgeStyles,
    CustomLogos,
    DefaultLogos,
    EmojiThemes,
    HeaderStyles,
    NavigationStyles,
)
from readmeai.models.enums import LLMProviders, OpenAIModels


def prompt_for_logo(
    ctx: click.Context | None = None,
    param: click.Parameter | None = None,
    value: str | None = None,
) -> str:
    """Manage user project logo selection."""
    if value is None:
        return DefaultLogos.BLUE.value
    if value == CustomLogos.CUSTOM.value:
        return click.prompt("Provide an logo file path or URL")
    elif value == CustomLogos.LLM.value:
        return CustomLogos.LLM.value
    elif value in DefaultLogos.__members__:
        return DefaultLogos[value].value
    else:
        raise click.BadParameter(f"Invalid logo provided: {value}")


def version_callback(
    ctx: click.Context | None = None,
    param: click.Parameter | None = None,
    value: str | None = None,
) -> None:
    """Prints the version of readme-ai."""
    if not value or (ctx and ctx.resilient_parsing):
        return
    click.echo(f"readmeai version {__version__}")
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
        [opt.value for opt in LLMProviders],
        case_sensitive=False,
    ),
    default=LLMProviders.OFFLINE.value,
    help="LLM API service provider to power the README file generation.",
)

badge_color = click.option(
    "-bc",
    "--badge-color",
    type=str,
    default="0080ff",
    help="Primary color (hex code or name) to use for the badge icons.",
)

badge_style = click.option(
    "-bs",
    "--badge-style",
    type=click.Choice(
        [opt.value for opt in BadgeStyles],
        case_sensitive=False,
    ),
    default=BadgeStyles.DEFAULT.value,
    help="Visual style of the badge icons used in the README file.",
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
    type=click.Choice(
        [opt.value for opt in EmojiThemes],
        case_sensitive=False,
    ),
    default=EmojiThemes.DEFAULT.value,
    help="Emoji theme 'packs' for customizing header section titles.",
)

header_style = click.option(
    "-hs",
    "--header-style",
    type=click.Choice(
        [opt.name for opt in HeaderStyles],
        case_sensitive=False,
    ),
    default=HeaderStyles.CLASSIC.value,
    help="README header style template options.",
)

logo = click.option(
    "-l",
    "--logo",
    type=click.Choice(
        [opt.name for opt in DefaultLogos] + [opt.value for opt in CustomLogos],
        case_sensitive=False,
    ),
    default=DefaultLogos.PURPLE.name,
    callback=prompt_for_logo,
    show_choices=True,
    help="Project logo for the README file.",
)

logo_size = click.option(
    "-ls",
    "--logo-size",
    type=str,
    default="30%",
    help="Project logo size.",
)

model = click.option(
    "-m",
    "--model",
    default=OpenAIModels.GPT35_TURBO.value,
    help="LLM API model to power the README file generation.",
)

navigation_style = click.option(
    "-ns",
    "--navigation-style",
    type=click.Choice(
        [opt.name for opt in NavigationStyles],
        case_sensitive=False,
    ),
    default=NavigationStyles.BULLET.value,
    help="Navigation menu styles for the README table of contents.",
)

output = click.option(
    "-o",
    "--output",
    default="readme-ai.md",
    help="Output file path for the generated README file.",
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
    help="Provide a repository URL (GitHub, GitLab, BitBucket) or local path.",
)

system_message = click.option(
    "-sm",
    "--system-message",
    default="You're a 10x Staff Software Engineering leader, with deep knowledge across most tech stacks. You'll use your expertise to write robust README markdown files for open-source projects. You're a master of the craft, and you're here to help others succeed.",
    help="System message to display in the README file.",
)

temperature = click.option(
    "-t",
    "--temperature",
    default=0.1,
    type=click.FloatRange(min_open=0.0, max=2.0, clamp=True),
    help="Increasing temperature yields more randomness in text generation.",
)

top_p = click.option(
    "-tp",
    "--top-p",
    default=0.9,
    type=click.FloatRange(0.0, 1.0, clamp=True),
    help="Top-p sampling probability for the model's generation.",
)

tree_max_depth = click.option(
    "-td",
    "--tree-max-depth",
    default=2,
    type=int,
    help="Maximum depth of the directory tree generated for the README file.",
)
