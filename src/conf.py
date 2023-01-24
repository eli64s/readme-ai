"""
src/conf.py
"""
from pydantic import AnyUrl
from pydantic.dataclasses import dataclass


@dataclass
class OpenAPI:
    engine: str
    sk_key: str


@dataclass
class GitHub:
    url: str


@dataclass
class Html:
    head: str
    setup: str
    body: str
    close: str


@dataclass
class Paths:
    docs: str = "docs/raw_docs.csv"
    html: str = "docs/html_docs.html"
    mrkd: str = "docs/output.md"
    pkgs: str = "conf/data/icons.json"
