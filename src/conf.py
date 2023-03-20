""" src/conf.py """
from dataclasses import dataclass


@dataclass
class OpenAI:
    """OpenAI API details."""

    api_key: str
    engine: str
    prompt_features: str


@dataclass
class GitHub:
    """GitHub repository."""

    url: str


@dataclass
class Markdown:
    """Markdown template code."""

    body: str
    head: str
    instructions: str
    dropdown: str
    modules: str
    toc: str
    tree: str


@dataclass
class Paths:
    """Project file paths."""

    badges: str
    docs: str
    md: str


@dataclass
class AppConfig:
    """Configuration constants object."""

    api: OpenAI
    github: GitHub
    md: Markdown
    paths: Paths