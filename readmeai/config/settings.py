"""Data models and functions for configuring the readme-ai CLI tool."""

from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, DirectoryPath, HttpUrl, validator

from readmeai._exceptions import FileReadError
from readmeai.config.validators import GitValidator
from readmeai.core.logger import Logger
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.resource_loader import get_resource_path

_logger = Logger(__name__)


class APISettings(BaseModel):
    """
    Universal LLM API settings.
    """

    content: Optional[str]
    rate_limit: Optional[int]


class FileSettings(BaseModel):
    """File paths used by the readme-ai CLI tool."""

    blacklist: str
    commands: str
    languages: str
    markdown: str
    parsers: str
    prompts: str
    shields_icons: str
    skill_icons: str


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


class ModelSettings(BaseModel):
    """LLM API settings used for generating text for the README.md file."""

    api: str
    base_url: Optional[HttpUrl]
    context_window: Optional[int]
    encoder: Optional[str]
    model: Optional[str]
    temperature: Optional[float]
    tokens: Optional[int]
    top_p: Optional[float]


class Settings(BaseModel):
    """Nested data model to store all configuration settings."""

    api: APISettings
    files: FileSettings
    git: GitSettings
    llm: ModelSettings
    md: MarkdownSettings

    class Config:
        """Pydantic configuration settings."""

        validate_assignment = True


class ConfigLoader:
    """Loads the configuration settings for the CLI."""

    def __init__(
        self,
        config_file: Union[str, Path] = "config.toml",
    ) -> None:
        """Initialize ConfigLoader with the base configuration file."""
        self.file_handler = FileHandler()
        self.config_file = config_file
        self.config = self._load_base_config()
        self._load_all_configs()

    def _load_base_config(self) -> Settings:
        """Load the base configuration file."""
        config_dict = get_resource_path(self.file_handler, self.config_file)
        return Settings.parse_obj(config_dict)

    def _load_all_configs(self) -> None:
        """Load additional configuration files specified in the Settings."""
        for (
            key,
            file_name,
        ) in self.config.files.dict().items():
            if not file_name.endswith(".toml"):
                continue

            try:
                config_data = get_resource_path(self.file_handler, file_name)
                setattr(self, key, config_data)
                _logger.debug(f"Loaded config file: {file_name}")

            except FileReadError as exc:
                setattr(self, key, None)
                _logger.warning(f"Config file not found: {file_name} - {exc}")
