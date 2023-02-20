""" src/conf.py """
from dataclasses import dataclass


@dataclass
class OpenAI:
    """_summary_"""

    engine: str
    key: str


@dataclass
class GitHub:
    """_summary_"""

    url: str


@dataclass
class Html:
    """_summary_"""

    head: str
    body: str
    setup: str
    tree: str


@dataclass
class Paths:
    """_summary_"""

    badges: str = "conf/badges.json"
    docs: str = "docs/gpt/raw_data.csv"
    html: str = "docs/html/readme.html"
    md: str = "docs/md/_readme.md"


@dataclass
class AppConfig:
    """_summary_"""

    api: OpenAI
    github: GitHub
    html: Html
    paths: Paths
