"""Configuration constants for the application."""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import dacite

from factory import FileHandler
from logger import Logger

LOGGER = Logger("readmeai_logger")


@dataclass
class OpenAIConfig:
    """OpenAI API configuration."""

    api_key: str
    engine: str
    tokens: int


@dataclass
class GitConfig:
    """Git configuration."""

    name: str
    repository: str


@dataclass
class MarkdownConfig:
    """Markdown configuration."""

    close: str
    head: str
    intro: str
    dropdown: str
    modules: str
    setup: str
    slogan: str
    toc: str
    tree: str


@dataclass
class PathsConfig:
    """Paths to configuration files."""

    dependency_files: str
    ignore_files: str
    language_names: str
    language_setup: str
    badges: str
    md: str


@dataclass
class PromptsConfig:
    """LLM prompts configuration."""

    code_to_text: str
    features: str
    intro: str
    slogan: str


@dataclass
class AppConfig:
    """README-AI application configuration."""

    api: OpenAIConfig
    git: GitConfig
    md: MarkdownConfig
    paths: PathsConfig
    prompts: PromptsConfig


@dataclass
class ConfigHelper:
    """README-AI application helper configuration."""

    dependency_files: List[str]
    ignore_files: List[str]
    language_names: Dict[str, str]
    language_setup: Dict[str, str]


def load_config(path: Path) -> Dict[str, str]:
    """Load configuration constants from TOML file."""
    handler = FileHandler()
    conf_dict = handler.read(path)
    return dacite.from_dict(AppConfig, conf_dict)


def load_config_helper(conf: AppConfig) -> ConfigHelper:
    handler = FileHandler()
    (
        dependency_files,
        ignore_files,
        language_names,
        language_setup,
    ) = read_config_helper(handler, conf)

    return ConfigHelper(
        dependency_files=dependency_files,
        ignore_files=ignore_files,
        language_names=language_names,
        language_setup=language_setup,
    )


def read_config_helper(handler: FileHandler, conf: AppConfig):
    conf_path_list = [
        conf.paths.dependency_files,
        conf.paths.ignore_files,
        conf.paths.language_names,
        conf.paths.language_setup,
    ]

    dependency_files = []
    ignore_files = []
    language_names = {}
    language_setup = {}

    for path in conf_path_list:
        path = Path("conf/").joinpath(path).resolve()
        conf_dict = handler.read(path)
        update_config_helper(
            dependency_files,
            ignore_files,
            language_names,
            language_setup,
            conf_dict,
        )

    return dependency_files, ignore_files, language_names, language_setup


def update_config_helper(
    dependency_files, ignore_files, language_names, language_setup, conf_dict
):
    if "dependency_files" in conf_dict:
        dependency_files.extend(
            conf_dict["dependency_files"].get("dependency_files", [])
        )

    if "ignore_files" in conf_dict:
        ignore_files.extend(conf_dict["ignore_files"].get("ignore_files", []))

    if "language_names" in conf_dict:
        language_names.update(conf_dict["language_names"])

    if "language_setup" in conf_dict:
        language_setup.update(conf_dict["language_setup"])
