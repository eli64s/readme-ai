"""Data models for configuration constants."""

from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse, urlsplit

from pkg_resources import resource_filename
from pydantic import BaseModel, validator

from readmeai.core import factory, logger

logger = logger.Logger(__name__)


class GitHost(str, Enum):
    """
    Enum for default hostnames of Git repositories.
    """

    LOCAL = "local"
    GITHUB = "github.com"
    GITLAB = "gitlab.com"
    BITBUCKET = "bitbucket.org"

    @staticmethod
    def from_url(url: str):
        """Returns the Git host from the URL."""
        for host in GitHost:
            if host.value in url:
                return host
        raise ValueError(f"Unsupported Git host in URL: {url}")


class GitApiUrl(str, Enum):
    """
    Enum for base URLs of Git repository APIs.
    """

    GITHUB = "https://api.github.com/repos/"
    GITLAB = "https://api.gitlab.com/v4/projects/"
    BITBUCKET = "https://api.bitbucket.org/2.0/repositories/"


class GitFileUrl(str, Enum):
    """
    Enum for URLs pointing to files in Git repositories.
    """

    LOCAL = "{file_path}"
    GITHUB = "https://github.com/{full_name}/blob/main/{file_path}"
    GITLAB = "https://gitlab.com/{full_name}/-/blob/master/{file_path}"
    BITBUCKET = "https://bitbucket.org/{full_name}/src/master/{file_path}"


class BadgeCliOptions(str, Enum):
    """
    Enum for CLI options for README file badge icons.
    """

    APPS = "apps"
    APPS_LIGHT = "apps-light"
    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    FOR_THE_BADGE = "for-the-badge"
    PLASTIC = "plastic"
    SOCIAL = "social"


class ApiConfig(BaseModel):
    """Pydantic model for OpenAI API configuration."""

    endpoint: str
    encoding: str
    model: str
    rate_limit: int
    tokens: int
    tokens_max: int
    temperature: float


class CliConfig(BaseModel):
    """CLI options for the readme-ai application."""

    emojis: bool = True
    offline: bool = False


class GitConfig(BaseModel):
    """Command-line interface configuration."""

    repository: str
    source: Optional[str]
    name: Optional[str]

    @validator("repository", pre=True, always=True)
    def validate_repository(cls, value: str) -> str:
        path = Path(value)
        if path.is_dir():
            return value
        try:
            parsed_url = urlparse(value)
        except ValueError:
            raise ValueError(f"Invalid repository URL or path: {value}")

        if (
            parsed_url.scheme != "https"
            or parsed_url.netloc not in GitHost._value2member_map_
        ):
            raise ValueError(f"Invalid repository URL or path: {value}")

        return value

    @validator("source", pre=True, always=True)
    def set_source(cls, value: str, values: dict) -> str:
        """Set the source of the repository"""
        repo = values.get("repository")

        if Path(repo).is_dir():
            return GitHost.LOCAL.value

        parsed_url = urlparse(repo)
        return GitHost._value2member_map_.get(parsed_url.netloc)

    @validator("name", pre=True, always=True)
    def set_name(cls, value: str, values: dict) -> str:
        """Sets the project name from the repository provided."""
        repo = values.get("repository")
        parsed_url = urlsplit(repo)
        if parsed_url.hostname in GitHost._value2member_map_:
            path = parsed_url.path
            name = path.rsplit("/", 1)[-1] if "/" in path else path
            if name.endswith(".git"):
                name = name[:-4]
            return name
        else:
            return Path(repo).name


class MarkdownConfig(BaseModel):
    """Pydantic model for Markdown code block templates."""

    badges: str
    badges_alt: str
    badges_offline: str
    badge_style: str
    contribute: str
    default: str
    dropdown: str
    header: str
    intro: str
    modules: str
    setup: str
    tables: str
    toc: str
    tree: str


class PathsConfig(BaseModel):
    """Pydantic model for configuration file paths."""

    dependency_files: str
    identifiers: str
    ignore_files: str
    language_names: str
    language_setup: str
    shieldsio_icons: str
    skill_icons: str
    output: str


class PromptsConfig(BaseModel):
    """Pydantic model for OpenAI prompts."""

    features: str
    overview: str
    slogan: str
    summaries: str


class AppConfig(BaseModel):
    """Nested Pydantic model for the entire configuration."""

    api: ApiConfig
    cli: CliConfig
    git: GitConfig
    md: MarkdownConfig
    paths: PathsConfig
    prompts: PromptsConfig


class AppConfigModel(BaseModel):
    """Pydantic model for the entire configuration."""

    app: AppConfig

    class Config:
        """Pydantic model configuration."""

        validate_assignment = True


class ConfigHelper(BaseModel):
    """Helper class to load additional configuration files."""

    conf: AppConfigModel
    dependency_files: List[str] = []
    ignore_files: Dict[str, List[str]] = {}
    language_names: Dict[str, str] = {}
    language_setup: Dict[str, List[str]] = {}

    class Config:
        allow_mutation = True

    def __init__(self, conf: AppConfigModel, **data):
        super().__init__(conf=conf, **data)
        self.load_helper_files()

    def load_helper_files(self):
        """Load helper configuration files."""
        handler = factory.FileHandler()
        conf_path_list = [
            self.conf.app.paths.dependency_files,
            self.conf.app.paths.ignore_files,
            self.conf.app.paths.language_names,
            self.conf.app.paths.language_setup,
        ]

        for path in conf_path_list:
            conf_dict = _get_config_dict(handler, path)

            if "dependency_files" in conf_dict:
                self.dependency_files.extend(
                    conf_dict.get("dependency_files", [])
                )
            if "ignore_files" in conf_dict:
                self.ignore_files.update(conf_dict["ignore_files"])
            if "language_names" in conf_dict:
                self.language_names.update(conf_dict["language_names"])
            if "language_setup" in conf_dict:
                self.language_setup.update(conf_dict["language_setup"])


def _get_config_dict(handler: factory.FileHandler, file_path: str) -> dict:
    """Get configuration dictionary from TOML file."""
    path = Path(
        resource_filename("readmeai", f"settings/{file_path}")
    ).resolve()
    return handler.read(path)


def load_config(path: str = "config.toml") -> AppConfig:
    """Load configuration constants from TOML file."""
    handler = factory.FileHandler()
    conf_dict = _get_config_dict(handler, path)
    return AppConfigModel.parse_obj({"app": conf_dict}).app


def load_config_helper(conf: AppConfigModel) -> ConfigHelper:
    """Load multiple configuration helper TOML files."""
    return ConfigHelper(conf=conf)
