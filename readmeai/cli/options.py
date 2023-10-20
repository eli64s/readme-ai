"""Options for the command line interface."""

from __future__ import annotations

import os

import click

BADGE_CHOICES = ("default", "shields", "square")


api_key = click.option(
    "-k",
    "--api-key",
    default=os.environ.get("OPENAI_API_KEY", None),
    help="Large language model API secret key.",
)
badges = click.option(
    "-b",
    "--badges",
    type=click.Choice(BADGE_CHOICES, case_sensitive=False),
    default="default",
    help="""Badge icon type to use in README.md header. \
        - 'shields' refers to badges from shields.io \
        - 'square' refers to app-like square badges.""",
)
emojis = click.option(
    "-e",
    "--emojis",
    default=True,
    help="Emojis prefixed to all README heading sections.",
)
model = click.option(
    "-m",
    "--model",
    default="gpt-3.5-turbo",
    help="Large language model engine to use.",
)

offline_mode = click.option(
    "-f",
    "--offline-mode",
    default=False,
    help="Run the tool in offline mode without calling the API.",
)

output = click.option(
    "-o",
    "--output",
    default="readme-ai.md",
    help="README.md output file path.",
)

repository = click.option(
    "-r",
    "--repository",
    required=True,
    help="Repository URL or directory path.",
)

temperature = click.option(
    "-t",
    "--temperature",
    default=1.0,
    type=float,
    help="Large language model sampling temperature.",
)

language = click.option(
    "-l",
    "--language",
    help="Language to write README.md file in.",
)

style = click.option(
    "-s",
    "--style",
    help="Template to use for README.md file.",
)
