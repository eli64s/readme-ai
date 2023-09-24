"""Pydantic models for the readme-ai application."""

from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import urlparse, urlsplit

from pkg_resources import resource_filename
from pydantic import BaseModel, validator

from . import factory, logger

logger = logger.Logger(__name__)


class DefaultHosts(str, Enum):
    """Enum for default Git repository hosts."""

    GITHUB = "github.com"
    GITLAB = "gitlab.com"


class ApiConfig(BaseModel):
    """Pydantic model for OpenAI API configuration."""

    endpoint: str
    engine: str
    encoding: str
    rate_limit: int
    tokens: int
    tokens_max: int
    temperature: float
    offline_mode: bool


class GitConfig(BaseModel):
    """Pydantic model for Git repository configuration."""

    repository: str
    name: Optional[str] = None

    @validator("repository", pre=True, always=True)
    def validate_repository(cls, value: str) -> str:
        """Validates if the repository is a valid URL or path."""
        path = Path(value)
        if path.is_dir():
            logger.info(f"Validated user repository (local path): {value}")
            return value

        try:
            parsed_url = urlparse(value)
        except ValueError:
            raise ValueError(f"Invalid repository URL or path: {value}")

        if (
            parsed_url.scheme != "https"
            or parsed_url.netloc not in DefaultHosts.__members__.values()
            or len(parsed_url.path.strip("/").split("/")) != 2
        ):
            raise ValueError(f"Invalid repository URL or path: {value}")

        logger.info(f"Validated user repository (remote): {value}")

        return value

    @validator("name", pre=True, always=True)
    def get_repository_name(cls, value: str, values: dict) -> str:
        """Extract the repository name from the URL or path."""
        repository_path = values.get("repository")
        if repository_path:
            parsed_url = urlsplit(str(repository_path))
            if parsed_url.hostname in DefaultHosts.__members__.values():
                path = parsed_url.path
                name = path.rsplit("/", 1)[-1] if "/" in path else path
                if name.endswith(".git"):
                    name = name[:-4]
                return name
            else:
                return Path(repository_path).name
        return value


class MarkdownConfig(BaseModel):
    """Pydantic model for Markdown code block templates."""

    badges: str
    default: str
    dropdown: str
    ending: str
    header: str
    intro: str
    modules: str
    setup: str
    tables: str
    toc: str
    tree: str


class PathsConfig(BaseModel):
    """Pydantic model for configuration file paths."""

    badges: str
    dependency_files: str
    ignore_files: str
    language_names: str
    language_setup: str
    readme: str


class PromptsConfig(BaseModel):
    """Pydantic model for OpenAI prompts."""

    code_summary: str
    features: str
    overview: str
    slogan: str


class AppConfig(BaseModel):
    """Nested Pydantic model for the entire configuration."""

    api: ApiConfig
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
        # Configure the model to call the custom __init__ method
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
                self.dependency_files.extend(conf_dict.get("dependency_files", []))
            if "ignore_files" in conf_dict:
                self.ignore_files.update(conf_dict["ignore_files"])
            if "language_names" in conf_dict:
                self.language_names.update(conf_dict["language_names"])
            if "language_setup" in conf_dict:
                self.language_setup.update(conf_dict["language_setup"])


def _get_config_dict(handler: factory.FileHandler, file_path: str) -> dict:
    """Get configuration dictionary from TOML file."""
    path = Path(resource_filename("readmeai", f"conf/{file_path}")).resolve()
    return handler.read(path)


def load_config(path: str = "conf.toml") -> AppConfig:
    """Load configuration constants from TOML file."""
    handler = factory.FileHandler()
    conf_dict = _get_config_dict(handler, path)
    return AppConfigModel.parse_obj({"app": conf_dict}).app


def load_config_helper(conf: AppConfigModel) -> ConfigHelper:
    """Load multiple configuration helper TOML files."""
    return ConfigHelper(conf=conf)
