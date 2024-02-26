"""Data models and functions for configuring the readme-ai CLI tool."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, DirectoryPath, HttpUrl, validator

from readmeai.config.enums import ModelOptions
from readmeai.config.validators import GitValidator
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.logger import Logger

_base_dir = Path(__file__).resolve().parent
_github_discussions = "https://github.com/eli64s/readme-ai/discussions"
_output_file = "readme-ai.md"
_logger = Logger(__name__)


class APISettings(BaseModel):
    """LLM API settings used for generating text for the README.md file."""

    api: str
    content: Optional[str]
    endpoint: Optional[str]
    encoding: Optional[str]
    model: Optional[str]
    offline: Optional[bool]
    temperature: Optional[float]
    tokens: Optional[int]
    tokens_max: Optional[int]
    rate_limit: Optional[int]

    def __post_init__(self) -> None:
        """Set the default values for the LLM API settings."""
        if self.api != ModelOptions.OFFLINE.name:
            self.offline = False
        else:
            self.offline = True


class GitSettings(BaseModel):
    """User repository settings, sanitized and validated by Pydantic."""

    repository: Union[HttpUrl, DirectoryPath]
    full_name: Optional[str]
    host: Optional[str]
    host_domain: Optional[str]
    name: Optional[str]

    _validate_repository = validator("repository", pre=True, always=True)(
        GitValidator.validate_repository
    )
    _validate_full_name = validator("full_name", pre=True, always=True)(
        GitValidator.validate_full_name
    )
    _set_host = validator("host", pre=True, always=True)(GitValidator.set_host)
    _set_name = validator("name", pre=True, always=True)(GitValidator.set_name)


class MarkdownSettings(BaseModel):
    """Markdown template blocks for the README.md file."""

    alignment: str
    badge_color: str
    badge_style: str
    badge_icons: str
    contribute: str
    emojis: bool
    features: str
    header: str
    image: str
    modules: str
    modules_widget: str
    overview: str
    placeholder: str
    quickstart: str
    shields_icons: str
    skill_icons: str
    slogan: str
    tables: str
    toc: str
    tree: str
    tree_depth: int


class ResourceSettings(BaseModel):
    """File paths used by the readme-ai CLI tool."""

    blacklist: str
    commands: str
    languages: str
    markdown: str
    parsers: str
    prompts: str
    shields_icons: str
    skill_icons: str


class Settings(BaseModel):
    """Nested data model to store all configuration settings."""

    discussions: HttpUrl = _github_discussions
    output_file: Path = _output_file

    llm: APISettings
    git: GitSettings
    md: MarkdownSettings
    files: ResourceSettings

    class Config:
        """Pydantic configuration settings."""

        validate_assignment = True


class ConfigLoader:
    """Loads the configuration settings for the readme-ai CLI tool."""

    def __init__(
        self,
        config_file: Union[str, Path] = "config.toml",
        package: str = "readmeai/config",
        submodule: str = "settings",
    ) -> None:
        """Initialize the ConfigLoader."""
        self.package = package
        self.submodule = submodule
        self.config_path = f"{package}/{submodule}/{config_file}"
        self.config = self._load_base_config()
        self._load_all_configs()

    def _load_all_configs(self) -> None:
        """Load additional configuration files specified in the Settings."""
        for key, file_name in self.config.files.__dict__.items():
            if not file_name.endswith(".toml"):
                continue

            file_path = _base_dir / self.submodule / file_name
            log_path = f"{self.package}/{self.submodule}/{file_name}"

            if file_path.exists():
                config_data = FileHandler().read(file_path)
                setattr(self, key, config_data)
                _logger.debug(f"Loaded config file @ {log_path}")
            else:
                setattr(self, key, None)
                _logger.warning(f"Config file not found: {log_path}")

    def _load_base_config(self) -> Settings:
        """Load the main configuration file for the readme-ai package."""
        config_dict = FileHandler().read(self.config_path)
        return Settings(**config_dict)
