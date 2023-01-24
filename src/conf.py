""" src/conf.py """
from enum import Enum

from pydantic import AnyUrl
from pydantic import validator
from pydantic.dataclasses import dataclass


@dataclass
class OpenAI:
    """_summary_"""

    engine: str
    sk_key: str


@dataclass
class GitHub:
    """_summary_"""

    url: str


@dataclass
class HtmlObjs:
    """_summary_"""

    head: str
    body: str
    close: str


@dataclass
class Paths:
    """_summary_"""

    docs: str = "docs/raw_docs.csv"
    html: str = "docs/html_docs.html"
    mrkd: str = "docs/output.md"
    pkgs: str = "conf/data/icons.json"


@dataclass
class AppConfig:
    api: OpenAI
    html: HtmlObjs
    paths: Paths
    store: GitHub
