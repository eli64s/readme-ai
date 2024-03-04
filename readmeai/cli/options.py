"""
Command-line interface options for the readme-ai package.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

import click


class BadgeOptions(str, Enum):
    """
    Enum for CLI options for README file badge icons.
    """

    DEFAULT = "default"
    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    FOR_THE_BADGE = "for-the-badge"
    PLASTIC = "plastic"
    SKILLS = "skills"
    SKILLS_LIGHT = "skills-light"
    SOCIAL = "social"


class ImageOptions(str, Enum):
    """
    Enum for CLI options for README file header images.
    """

    # Custom image options
    CUSTOM = "custom"
    LLM = "llm"

    # Default image options
    BLACK = "https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png"
    BLUE = "https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
    CLOUD = "https://cdn-icons-png.flaticon.com/512/6295/6295417.png"
    GRADIENT = "https://img.icons8.com/?size=512&id=55494&format=png"
    GREY = "https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png"
    PURPLE = "https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png"


class ModelOptions(str, Enum):
    """
    Enum for CLI options for the LLM API key.
    """

    OFFLINE = "OFFLINE"
    OLLAMA = "OLLAMA"
    OPENAI = "OPENAI"
    GEMINI = "GEMINI"


def prompt_for_image(
    context: Optional[click.Context],
    parameter: Optional[click.Parameter],
    value: Optional[str],
) -> str:
    """Prompt the user for a custom image URL."""
    if value == ImageOptions.CUSTOM.name:
        return click.prompt("Provide an image file path or URL")
    elif value == ImageOptions.LLM.name:
        return ImageOptions.LLM.value
    elif value in ImageOptions.__members__:
        return ImageOptions[value].value
    else:
        raise click.BadParameter(f"Invalid image provided: {value}")


alignment = click.option(
    "-a",
    "--alignment",
    type=click.Choice(["center", "left"], case_sensitive=False),
    default="center",
    help="Alignment for the README.md file header sections.",
)

api = click.option(
    "--api",
    type=click.Choice(
        [opt.value for opt in ModelOptions], case_sensitive=False
    ),
    default=None,
    help="""LLM service to use for generating the README.md file. The following services are currently supported:\n
    - OPENAI  # OpenAI - gpt-3.5-turbo \n
    - OLLAMA  # Ollama - llama2 \n
    - GEMINI  # Google Gemini API - gemini-pro \n
    - OFFLINE # Offline mode - no LLM service used \n
    """,
)

badge_color = click.option(
    "--badge-color",
    type=str,
    default="0080ff",
    help="Custom color for the badge icon. Provide a valid color name or hex code.",
)

badge_style = click.option(
    "--badge-style",
    type=click.Choice(
        [opt.value for opt in BadgeOptions], case_sensitive=False
    ),
    default=BadgeOptions.DEFAULT.value,
    help="""\
        Badge icon style types to select from when generating README.md badges. The following options are currently available:\n
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
    help="Base URL for the LLM API service used to generate text for the README.md file.",
)

context_window = click.option(
    "--context-window",
    default=3999,
    type=int,
    help="Maximum number of tokens to use for the model's context window.",
)

emojis = click.option(
    "-e",
    "--emojis",
    is_flag=True,
    default=False,
    help="This option adds emojis to the README.md file's header sections. For example, the default header for the 'Overview' section generates the markdown code as '## Overview'. Adding the --emojis flag generates the markdown code as '## 📍 Overview'.",
)

image = click.option(
    "-i",
    "--image",
    type=click.Choice(
        [opt.name for opt in ImageOptions], case_sensitive=False
    ),
    default=ImageOptions.BLUE.name,
    callback=prompt_for_image,
    show_choices=True,
    help="""\
        Project logo image displayed in the README file header. The following options are currently supported:\n

        Custom image options:\n
        - CUSTOM (use a custom image file path or URL) \n
        - LLM (use LLM multi-modal capabilities to generate an image) \n

        Default image options:\n
        - BLACK \n
        - BLUE \n
        - CLOUD \n
        - GRADIENT \n
        - GREY \n
        - PURPLE \n
        """,
)

language = click.option(
    "-l",
    "--language",
    default="en",
    help="Language to use for generating the README.md file. Default is English (en).",
)

model = click.option(
    "-m",
    "--model",
    default="gpt-3.5-turbo",
    help="Large language model (LLM) API used to generate text for the README.md file. Default model uses OpenAI's gpt-3.5-turbo.",
)

output = click.option(
    "-o",
    "--output",
    default="readme-ai.md",
    help="Output file name for your README file. Default name is 'readme-ai.md'.",
)

rate_limit = click.option(
    "--rate-limit",
    default=10,
    type=click.IntRange(1, 25, clamp=True),
    help="Rate limit for the number of API requests per minute.",
)

repository = click.option(
    "-r",
    "--repository",
    required=True,
    help="Provide a remote repository URL (GitHub, GitLab, BitBucket), or a local directory path to your project.",
)

temperature = click.option(
    "-t",
    "--temperature",
    default=0.9,
    type=click.FloatRange(0.0, 2.0, clamp=True),
    help="Setting the model's temperature to a higher value will yield more creative content generated, while a lower value will generate more predictable content.",
)

template = click.option(
    "--template",
    type=str,
    help="README template file to use for generating the README.md file.",
)

top_p = click.option(
    "--top-p",
    default=0.9,
    type=click.FloatRange(0.0, 1.0, clamp=True),
    help="Top-p sampling probability for the model's generation. This value can be set between 0.0 and 1.0.",
)

tree_depth = click.option(
    "--tree-depth",
    default=2,
    type=int,
    help="Maximum depth of the directory tree thats included in the README.md file.",
)
