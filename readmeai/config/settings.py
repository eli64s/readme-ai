"""Data models and functions for configuring the readme-ai CLI tool."""

import re
from importlib import resources
from pathlib import Path
from typing import Dict, List, Optional, Union
from urllib.parse import urlparse, urlsplit

from pydantic import BaseModel, validator

from readmeai.config.enums import GitService
from readmeai.core.factory import FileHandler
from readmeai.core.logger import Logger
from readmeai.exceptions import FileReadError

logger = Logger(__name__)


class GitSettingsValidator:
    """Validator class for GitSettings."""

    @classmethod
    def validate_repository(cls, value: Union[str, Path]) -> Union[str, Path]:
        """Validate the repository URL or path."""
        if (
            any(service.value in value for service in GitService) is False
            and Path(value).is_dir() is False
        ):
            raise ValueError("Unsupported Git service.")

        if isinstance(value, str):
            path = Path(value)
            if path.is_dir():
                return value
            try:
                parsed_url = urlparse(value)
                if parsed_url.scheme in ["http", "https"] and any(
                    service in parsed_url.netloc for service in GitService
                ):
                    return value
            except ValueError:
                pass
        elif isinstance(value, Path) and value.is_dir():
            return value
        raise ValueError(f"Invalid repository URL or path: {value}")

    @classmethod
    def validate_full_name(cls, value: Optional[str], values: dict) -> str:
        """Validator for getting the full name of the repository."""
        url_or_path = values.get("repository")

        path = (
            url_or_path if isinstance(url_or_path, Path) else Path(url_or_path)
        )
        if path.exists():
            return str(path.name)

        patterns = {
            GitService.GITHUB: r"https?://github.com/([^/]+)/([^/]+)",
            GitService.GITLAB: r"https?://gitlab.com/([^/]+)/([^/]+)",
            GitService.BITBUCKET: r"https?://bitbucket.org/([^/]+)/([^/]+)",
        }

        for _, pattern in patterns.items():
            match = re.match(pattern, url_or_path)
            if match:
                user_name, repo_name = match.groups()
                return f"{user_name}/{repo_name}"

        raise ValueError("Error: invalid repository URL or path.")

    @classmethod
    def set_host(cls, value: Optional[str], values: dict) -> str:
        """Sets the Git service host from the repository provided."""
        repo = values.get("repository")
        if isinstance(repo, Path) or (
            isinstance(repo, str) and Path(repo).is_dir()
        ):
            return GitService.LOCAL

        parsed_url = urlparse(str(repo))
        for service in GitService:
            if service in parsed_url.netloc:
                return service.split(".")[0]

        return GitService.LOCAL

    @classmethod
    def set_name(cls, value: Optional[str], values: dict) -> str:
        """Sets the repository name from the repository provided."""
        repo = values.get("repository")
        if isinstance(repo, Path):
            return repo.name
        elif isinstance(repo, str):
            parsed_url = urlsplit(repo)
            name = parsed_url.path.split("/")[-1]
            return name.removesuffix(".git")
        return "n/a"

    @classmethod
    def set_source(cls, value: Optional[str], values: dict) -> str:
        repo = values.get("repository")
        if isinstance(repo, Path) or (
            isinstance(repo, str) and Path(repo).is_dir()
        ):
            return GitService.LOCAL

        parsed_url = urlparse(str(repo))
        for service in GitService:
            if service in parsed_url.netloc:
                return service
        return GitService.LOCAL


class CliSettings(BaseModel):
    """CLI options for the readme-ai application."""

    emojis: bool
    offline: bool


class FileSettings(BaseModel):
    """File paths for the readme-ai application."""

    dependency_files: str
    identifiers: str
    ignore_files: str
    language_names: str
    language_setup: str
    output: str
    shields_icons: str
    skill_icons: str


class GitSettings(BaseModel):
    """Codebase repository settings and validations."""

    repository: Union[str, Path]
    full_name: Optional[str]
    host: Optional[str]
    name: Optional[str]
    source: Optional[str]

    _validate_repository = validator("repository", pre=True, always=True)(
        GitSettingsValidator.validate_repository
    )
    _validate_full_name = validator("full_name", pre=True, always=True)(
        GitSettingsValidator.validate_full_name
    )
    _set_host = validator("host", pre=True, always=True)(
        GitSettingsValidator.set_host
    )
    _set_name = validator("name", pre=True, always=True)(
        GitSettingsValidator.set_name
    )
    _set_source = validator("source", pre=True, always=True)(
        GitSettingsValidator.set_source
    )


class LlmApiSettings(BaseModel):
    """Pydantic model for OpenAI LLM API details."""

    content: str
    endpoint: str
    encoding: str
    model: str
    rate_limit: int
    temperature: float
    tokens: int
    tokens_max: int


class MarkdownSettings(BaseModel):
    """Pydantic model for Markdown code block templates."""

    align: str
    default: str
    badge_color: str
    badge_style: str
    badges_software: str
    badges_shields: str
    badges_skills: str
    contribute: str
    features: str
    header: str
    image: str
    modules: str
    modules_widget: str
    overview: str
    quickstart: str
    slogan: str
    tables: str
    toc: str
    tree: str


class PromptSettings(BaseModel):
    """Pydantic model for OpenAI prompts."""

    features: str
    overview: str
    slogan: str
    summaries: str


class AppConfig(BaseModel):
    """Nested Pydantic model for the entire configuration."""

    cli: CliSettings
    files: FileSettings
    git: GitSettings
    llm: LlmApiSettings
    md: MarkdownSettings
    prompts: PromptSettings


class AppConfigModel(BaseModel):
    """Pydantic model for the entire configuration."""

    app: AppConfig

    class Config:
        """Pydantic model configuration."""

        validate_assignment = True


class ConfigHelper(BaseModel):
    """Helper class to load additional configuration files."""

    conf: AppConfigModel
    dependency_files: Dict[str, str] = {}
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
        handler = FileHandler()
        conf_path_list = [
            self.conf.app.files.dependency_files,
            self.conf.app.files.ignore_files,
            self.conf.app.files.language_names,
            self.conf.app.files.language_setup,
        ]

        for path in conf_path_list:
            conf_dict = _get_config_dict(handler, path)

            if "dependency_files" in conf_dict:
                self.dependency_files.update(conf_dict["dependency_files"])
            if "ignore_files" in conf_dict:
                self.ignore_files.update(conf_dict["ignore_files"])
            if "language_names" in conf_dict:
                self.language_names.update(conf_dict["language_names"])
            if "language_setup" in conf_dict:
                self.language_setup.update(conf_dict["language_setup"])


def _get_config_dict(handler: FileHandler, file_path: str) -> dict:
    """Get configuration dictionary from TOML file."""
    try:
        resource_path = resources.files("readmeai.settings") / file_path
        logger.info(f"Using importlib.resources to load: {resource_path}")

    except TypeError as exc_info:
        logger.debug(f"Error using importlib.resources: {exc_info}")

        try:
            import pkg_resources

            resource_path = Path(
                pkg_resources.resource_filename(
                    "readmeai", f"settings/{file_path}"
                )
            ).resolve()
            logger.info(
                f"Using pkg_resources.resource_filename: {resource_path}"
            )

        except Exception as exc:
            raise FileReadError("Failed to load file", file_path) from exc

    if resource_path.exists() is False:
        raise FileReadError("File not found", resource_path) from None

    return handler.read(resource_path)


def load_config(path: str = "config.toml") -> AppConfig:
    """Load configuration constants from TOML file."""
    handler = FileHandler()
    conf_dict = _get_config_dict(handler, path)
    return AppConfigModel.parse_obj({"app": conf_dict}).app


def load_config_helper(conf: AppConfigModel) -> ConfigHelper:
    """Load multiple configuration helper TOML files."""
    return ConfigHelper(conf=conf)
