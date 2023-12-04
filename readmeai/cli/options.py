"""Command line options for readmeai CLI."""

from __future__ import annotations

import os

import click

from readmeai.config.settings import BadgeCliOptions

badge_options = [badge.value for badge in BadgeCliOptions]

api_key = click.option(
    "-k",
    "--api-key",
    default=os.environ.get("OPENAI_API_KEY", None),
    help="Large language model API secret key.",
)
badges = click.option(
    "-b",
    "--badges",
    type=click.Choice(badge_options, case_sensitive=False),
    default="flat-square",
    help="""\
        Badge icon type to use in README.md header. \
        Options: flat, flat-square, for-the-badge, plastic, social, apps, apps-light""",
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
    default="gpt-4",
    help="Large language model engine to use.",
)

offline = click.option(
    "-f",
    "--offline",
    default=False,
    help="When offline is true, a README.md is generated without the LLM API.",
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
