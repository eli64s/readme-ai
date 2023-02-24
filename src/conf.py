""" src/conf.py """
from dataclasses import dataclass


@dataclass
class OpenAI:
    """OpenAI API details."""

    engine: str
    key: str


@dataclass
class GitHub:
    """GitHub repository."""

    dirs: str
    url: str


@dataclass
class Markdown:
    """Markdown template code."""

    head: str
    toc: str
    body: str
    modules: str
    tree: str
    usage: str


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
