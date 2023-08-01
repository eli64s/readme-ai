"""Pydantic models for configuration constants."""

import os
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse, urlsplit

import openai
from pkg_resources import resource_filename
from pydantic import BaseModel, Field, SecretStr, validator

from . import factory, logger

LOGGER = logger.Logger(__name__)


class ApiConfig(BaseModel):
    """OpenAI API configuration."""

    endpoint: str
    engine: str
    encoding: str
    rate_limit: int
    tokens: int
    tokens_max: int
    temperature: float
    api_key: SecretStr = Field(
        default_factory=lambda: os.environ.get("OPENAI_API_KEY", "")
    )

    @validator("api_key")
    def validate_api_key(cls, api_key) -> None:
        """Validate the OpenAI API key."""
        if not api_key:
            api_key = os.environ.get("OPENAI_API_KEY", "")
        if not api_key:
            raise ValueError("Exception: invalid OpenAI API key.")

        os.environ["OPENAI_API_KEY"] = api_key

        try:
            cls._set_openai_api_key()
            openai.Model.list()

        except (
            openai.error.AuthenticationError,
            openai.error.InvalidRequestError,
        ) as excinfo:
            cls._handle_openai_error(excinfo)

        finally:
            cls.api_key = os.environ["OPENAI_API_KEY"]
            LOGGER.info("Successfully validated OpenAI API key.")

    @classmethod
    def _set_openai_api_key(cls) -> None:
        """Set the OpenAI API key."""
        openai.api_key = os.environ["OPENAI_API_KEY"]

    @staticmethod
    def _handle_openai_error(excinfo) -> None:
        """Handle OpenAI API errors."""
        LOGGER.error(f"OpenAI API Exception:\n{excinfo}")
        raise ValueError(f"{traceback.format_exc()}")


@dataclass
class GitConfig:
    """Repository configuration."""

    repository: str
    name: Optional[str] = None

    def __post_init__(self) -> None:
        """Post-initialization hook."""
        if not self.validate_repository(self.repository):
            raise ValueError(f"Ivalid repository URL or path: {self.repository}")

        self.name = self.get_repository_name(self.repository)

    @staticmethod
    def get_default_hosts() -> List[str]:
        """Get the default valid hosts."""
        return ["github.com", "gitlab.com"]

    @staticmethod
    def get_repository_name(repository_path: str) -> str:
        """Extract the repository name from the URL or path."""
        parsed_url = urlsplit(str(repository_path))
        if parsed_url.hostname in GitConfig.get_default_hosts():
            path = parsed_url.path
            name = path.rsplit("/", 1)[-1] if "/" in path else path
            if name.endswith(".git"):
                name = name[:-4]
        else:
            name = Path(repository_path).name
        return name

    @staticmethod
    def validate_repository(repository: str) -> bool:
        """Check if the repository URL or local directory is valid."""
        path = Path(repository)
        if path.is_dir():
            return True

        parsed_url = urlparse(repository)
        if parsed_url.scheme != "https":
            return False

        if parsed_url.netloc not in GitConfig.get_default_hosts():
            return False

        path_segments = parsed_url.path.strip("/").split("/")
        if len(path_segments) != 2:
            return False

        return True


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


class AppConfigModel(BaseModel):
    """Application configuration model."""

    app: AppConfig

    class Config:
        """Configuration for the Pydantic model."""

        validate_assignment = True


@dataclass
class ConfigHelper:
    """README-AI application helper configuration."""

    conf: AppConfigModel
    dependency_files: List[str] = field(default_factory=list)
    ignore_files: Dict[str, List[str]] = field(default_factory=dict)
    language_names: Dict[str, str] = field(default_factory=dict)
    language_setup: Dict[str, List[str]] = field(default_factory=dict)

    def __post_init__(self):
        """Post-initialization hook to load helper configuration files."""
        handler = factory.FileHandler()
        conf_path_list = [
            self.conf.app.paths.dependency_files,
            self.conf.app.paths.ignore_files,
            self.conf.app.paths.language_names,
            self.conf.app.paths.language_setup,
        ]

        for path in conf_path_list:
            path = Path(resource_filename("readmeai", f"conf/{path}")).resolve()
            conf_dict = handler.read(path)

            if "dependency_files" in conf_dict:
                self.dependency_files.extend(conf_dict.get("dependency_files", []))
            if "ignore_files" in conf_dict:
                self.ignore_files.update(conf_dict["ignore_files"])
            if "language_names" in conf_dict:
                self.language_names.update(conf_dict["language_names"])
            if "language_setup" in conf_dict:
                self.language_setup.update(conf_dict["language_setup"])


def _get_config_dict(handler: factory.FileHandler, filename: str) -> dict:
    """Get configuration dictionary from TOML file."""
    path = resource_filename("readmeai", f"conf/{filename}")
    return handler.read(path)


def load_config(path: str = "conf.toml") -> AppConfig:
    """Load configuration constants from TOML file."""
    handler = factory.FileHandler()
    conf_dict = _get_config_dict(handler, path)
    return AppConfigModel.parse_obj({"app": conf_dict}).app


def load_config_helper(conf: AppConfigModel) -> ConfigHelper:
    """Load multiple configuration helper TOML files."""
    return ConfigHelper(conf=conf)
