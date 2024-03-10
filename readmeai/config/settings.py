"""
Data models and configuration settings for the readme-ai package.
"""

from __future__ import annotations

from functools import cached_property
from pathlib import Path
from typing import Optional, Union

from pydantic import BaseModel, Field, HttpUrl, validator

from readmeai.config.validators import GitValidator
from readmeai.core.logger import Logger
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.file_resources import get_resource_path


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

    repository: Union[str, Path] = Field(
        ..., description="URL or directory path to the repository."
    )
    full_name: Optional[str] = Field(
        None, description="The full name of the repository."
    )
    host_domain: Optional[str] = Field(
        None, description="Domain of the repository host."
    )
    host: Optional[str] = Field(
        None, description="The repository host i.e. 'github'."
    )
    name: Optional[str] = Field(
        None, description="Project name i.e. 'readme-ai'."
    )

    _validate_repository = validator("repository", pre=True, always=True)(
        GitValidator.validate_repository
    )
    _validate_full_name = validator("full_name", pre=True, always=True)(
        GitValidator.validate_full_name
    )
    _set_host_domain = validator("host_domain", pre=True, always=True)(
        GitValidator.set_host_domain
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
    width: str


class ModelSettings(BaseModel):
    """LLM API settings used for generating text for the README.md file."""

    api: Optional[str]
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
        sub_module: str = "settings",
    ) -> None:
        """Initialize ConfigLoader with the base configuration file."""
        self._logger = Logger(__name__)
        self.file_handler = FileHandler()
        self.config_file = config_file
        self.sub_module = sub_module
        self.config = self._base_config
        self.load_settings()

    @cached_property
    def _base_config(self) -> Settings:
        """Loads the base configuration file."""
        file_path = get_resource_path(
            file_path=self.config_file, sub_module=self.sub_module
        )
        config_dict = self.file_handler.read(file_path)
        return Settings.parse_obj(config_dict)

    def load_settings(self) -> dict[str, dict]:
        """Loads all configuration settings.

        - Loads the base configuration file from `settings/config.toml`.
        - Loads any additional configuration files specified in the base settings
          under the `files` key.

        Returns:
            A dictionary containing all loaded configuration settings, where
            the keys are the section names from `Settings` and the values
            are their respective data dictionaries.
        """
        settings = self._base_config.dict()

        for key, file_name in settings["files"].items():
            if not file_name.endswith(".toml"):
                continue
            file_path = get_resource_path(
                file_path=file_name,
            )
            data_dict = self.file_handler.read(file_path)
            settings[key] = data_dict
            setattr(self, key, data_dict)
            self._logger.info(
                f"Loaded configuration file: {self.sub_module}/{file_name}"
            )

        return settings
