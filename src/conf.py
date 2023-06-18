"""Data classes to store README-AI configuration constants."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlsplit

import dacite

from factory import FileHandler


@dataclass
class ApiConfig:
    """OpenAI API configuration."""

    endpoint: str
    engine: str
    encoding: str
    rate_limit: int
    tokens: int
    tokens_max: int
    temperature: float


@dataclass
class GitConfig:
    """Repository configuration."""

    name: str
    repository: str
    _hosts: List[str] = field(default_factory=lambda: ["github.com", "gitlab.com"])

    def __post_init__(self):
        self.name = self.get_repository_name(self.repository)

    def get_repository_name(self, path: Union[str, Path]) -> str:
        """Extract repository name from path."""
        parsed_url = urlsplit(str(path))
        if parsed_url.hostname in self._hosts:
            repo_path = parsed_url.path
            name = repo_path.rsplit("/", 1)[-1] if "/" in repo_path else repo_path
            if name.endswith(".git"):
                name = name[:-4]
        else:
            name = Path(path).name
        return name


@dataclass
class MarkdownConfig:
    """Markdown configuration."""

    badges: str
    default: str
    dropdown: str
    ending: str
    header: str
    intro: str
    modules: str
    setup: str
    toc: str
    tree: str


@dataclass
class PathsConfig:
    """Paths to configuration files."""

    badges: str
    dependency_files: str
    ignore_files: str
    language_names: str
    language_setup: str
    readme: str


@dataclass
class PromptsConfig:
    """LLM prompts configuration."""

    code_summary: str
    features: str
    overview: str
    slogan: str


@dataclass
class AppConfig:
    """README-AI application configuration."""

    api: ApiConfig
    git: GitConfig
    md: MarkdownConfig
    paths: PathsConfig
    prompts: PromptsConfig


@dataclass
class ConfigHelper:
    """README-AI application helper configuration."""

    conf: AppConfig
    dependency_files: List[str] = field(default_factory=list)
    ignore_files: Dict[str, List[str]] = field(default_factory=dict)
    language_names: Dict[str, str] = field(default_factory=dict)
    language_setup: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        handler = FileHandler()
        conf_path_list = [
            self.conf.paths.dependency_files,
            self.conf.paths.ignore_files,
            self.conf.paths.language_names,
            self.conf.paths.language_setup,
        ]

        for path in conf_path_list:
            path = Path("conf/").joinpath(path).resolve()
            conf_dict = handler.read(path)
            if "dependency_files" in conf_dict:
                self.dependency_files.extend(
                    conf_dict["dependency_files"].get("dependency_files", [])
                )
            if "ignore_files" in conf_dict:
                self.ignore_files.update(conf_dict["ignore_files"])
            if "language_names" in conf_dict:
                self.language_names.update(conf_dict["language_names"])
            if "language_setup" in conf_dict:
                self.language_setup.update(conf_dict["language_setup"])


def _get_config_dict(handler: FileHandler, filename: str) -> dict:
    """Get configuration dictionary from TOML file."""
    path = Path("conf/") / filename
    return handler.read(path)


def load_config(path: str = "conf.toml") -> Dict[str, str]:
    """Load configuration constants from TOML file."""
    handler = FileHandler()
    conf_dict = _get_config_dict(handler, path)
    return dacite.from_dict(AppConfig, conf_dict)


def load_config_helper(conf: AppConfig) -> ConfigHelper:
    """Load multiple configuration helper TOML files."""
    return ConfigHelper(conf=conf)
