"""
Pydantic models and settings for the readme-ai package.
"""

from __future__ import annotations

from enum import Enum
from functools import cached_property
from pathlib import Path
from typing import Literal

from pydantic import (
    AnyHttpUrl,
    BaseModel,
    ConfigDict,
    Field,
    FilePath,
    PositiveFloat,
    PositiveInt,
    field_validator,
    model_validator,
)
from pydantic_extra_types.color import Color

from readmeai.core.logger import Logger
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.file_resources import get_resource_path
from readmeai.vcs.errors import GitValidationError
from readmeai.vcs.url_builder import GitURL, parse_git_url

_logger = Logger(__name__)


class BadgeOptions(str, Enum):
    DEFAULT = "default"
    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    FOR_THE_BADGE = "for-the-badge"
    PLASTIC = "plastic"
    SKILLS = "skills"
    SKILLS_LIGHT = "skills-light"
    SOCIAL = "social"


class ImageOptions(str, Enum):
    CUSTOM = "CUSTOM"
    LLM = "LLM"
    BLACK = "https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png"
    BLUE = "https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
    CLOUD = "https://cdn-icons-png.flaticon.com/512/6295/6295417.png"
    GRADIENT = "https://img.icons8.com/?size=512&id=55494&format=png"
    GREY = "https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png"
    PURPLE = "https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png"


class ModelOptions(str, Enum):
    # ANTHROPIC = "ANTHROPIC"
    GEMINI = "GEMINI"
    OFFLINE = "OFFLINE"
    OLLAMA = "OLLAMA"
    OPENAI = "OPENAI"


class APISettings(BaseModel):
    """
    LLM API settings and parameters.
    """

    rate_limit: PositiveInt = Field(gt=0, le=25, description="API rate limit.")
    system_message: str = Field(description="LLM system prompt content field.")


class FileSettings(BaseModel):
    """
    File path resources for the readme-ai package.
    """

    commands: str = Field(description="'Quickstart' setup commands.")
    ignore_list: str = Field(description="List of files to ignore.")
    languages: str = Field(description="Extension to language mappings.")
    markdown: str = Field(description="Markdown code template blocks.")
    parsers: str = Field(description="Common dependency file names.")
    prompts: str = Field(description="LLM API prompt templates.")
    shieldsio_icons: str = Field(description="Shields.io svg icon badges.")
    skill_icons: str = Field(description="Skill icon badges.")


class GitSettings(BaseModel):
    """
    User repository settings for a remote or local codebase.
    """

    repository: Path | str
    git_url: GitURL | None = None
    full_name: str | None = None
    host_domain: str | None = None
    host: str | None = None
    name: str | None = None

    model_config = ConfigDict(extra="forbid")

    @field_validator("repository")
    def validate_repository(cls, value: Path | str) -> Path | str:
        """
        Validates the repository path or Git URL.
        """
        if isinstance(value, Path) or (
            isinstance(value, str)
            and Path(value).is_dir()
            and Path(value).exists()
        ):
            return value
        try:
            return str(GitURL.create(value).url)
        except ValueError as exc:
            raise GitValidationError(
                f"Invalid Git repository URL or path: {value}",
            ) from exc

    @field_validator("git_url")
    def set_git_url(cls, value: GitURL | None, values) -> GitURL | None:
        """
        Set Git URL from the repository path if not provided.
        """
        if value is None and "repository" in values:
            return GitURL.create(str(values["repository"]))
        return value

    @model_validator(mode="after")
    def set_git_attributes(self) -> GitSettings:
        """
        Parse and set Git repository attributes.
        """
        if self.git_url:
            self.host_domain = self.git_url.host_domain
            self.host = self.git_url.host.name if self.git_url.host else None
            self.name = self.git_url.name
            self.full_name = self.git_url.full_name
        else:
            self.host_domain, self.host, self.name, self.full_name = (
                parse_git_url(str(self.repository))
            )
        return self

    def get_file_url(self, file_path: str) -> str:
        """
        Generates a URL for a file in the repository.
        """
        if self.git_url:
            return self.git_url.get_file_url(file_path)
        elif isinstance(self.repository, Path) or (
            isinstance(self.repository, str) and Path(self.repository).is_dir()
        ):
            return str(Path(self.repository) / file_path)
        else:
            raise GitValidationError("Failed to generate git file URL")


class MarkdownSettings(BaseModel):
    """
    Markdown code template blocks for building the README.md file.
    """

    align: Literal["left", "center", "right"] = Field(
        default="center",
        description="align for markdown content.",
    )
    badge_color: Color = Field(
        default_factory=lambda: Color("blue"),
        description="Badge color (https://www.w3.org/TR/SVG11/types.html#ColorKeywords)",
    )
    badge_style: BadgeOptions = Field(
        default=BadgeOptions.FLAT,
        description="Badge icon style type.",
    )
    badge_icons: str
    contribute: str
    emojis: bool = Field(
        default=False,
        description="Enable emoji prefixes for headers.",
    )
    features: str = Field(
        default="❯ INSERT-PROJECT-FEATURES",
        description="Project feature content.",
    )
    header_style: str = Field(
        default="classic",
        description="Header style for the README file.",
    )
    image: AnyHttpUrl | FilePath | str = Field(
        default=ImageOptions.BLUE,
        description="Image URL or path for the project logo.",
    )
    image_width: str = Field(
        default="20%",
        description="Project logo width",
    )
    modules: str
    modules_widget: str
    overview: str = Field(
        default="❯ INSERT-PROJECT-OVERVIEW",
        description="Project overview content.",
    )
    placeholder: str = Field(
        default="<code>❯ REPLACE-ME</code>",
        description="Placeholder image for missing content.",
    )
    quickstart: str
    requirements: str = Field(
        default="",
        description="Project system prerequisites.",
    )
    shieldsio_icons: str
    skill_icons: str
    slogan: str = Field(
        default="❯ INSERT-PROJECT-SLOGAN",
        description="Project tagline or slogan.",
    )
    tables: str = Field(default="", description="Markdown table options.")
    toc_style: str = Field(
        default="bullet",
        description="Table of contents content.",
    )
    tree: str
    tree_depth: PositiveInt = Field(
        default=2,
        ge=1,
        le=5,
        description="Depth of directory tree.",
    )

    @field_validator("badge_color")
    def set_color(cls, value: str) -> str:
        """
        Validates badge color value and returns the hex code.
        """
        try:
            return Color(value).as_hex().strip("#")
        except ValueError as exc:
            _logger.error(f"Invalid color value '{value}': {exc}")
            return cls.model_fields["badge_color"].default

    @model_validator(mode="after")
    def set_width(self) -> MarkdownSettings:
        """
        Validates and sets the width for the project logo image.
        """
        if str(self.image).lower() == ImageOptions.LLM.name.lower():
            self.image_width = "60%"
        return self


class ModelSettings(BaseModel):
    """
    LLM API model settings and parameters.
    """

    api: str | None = Field(
        default=ModelOptions.OFFLINE,
        description="API key for the LLM model.",
    )
    base_url: str
    context_window: PositiveInt
    encoder: str
    host_name: AnyHttpUrl
    localhost: AnyHttpUrl
    model: str
    path: str
    temperature: float
    tokens: PositiveInt
    top_p: PositiveFloat


class Settings(BaseModel):
    """
    Pydantic settings model for the readme-ai package.
    """

    api: APISettings
    files: FileSettings
    git: GitSettings
    llm: ModelSettings
    md: MarkdownSettings

    model_config = ConfigDict(
        validate_assignment=True,
    )


class ConfigLoader:
    """
    Loads the configuration settings for the readme-ai package.
    """

    def __init__(
        self,
        config_file: str = "config.toml",
        submodule: str = "settings",
    ) -> None:
        """Initialize ConfigLoader with the base configuration file."""
        self.file_handler = FileHandler()
        self.config_file = config_file
        self.submodule = submodule
        self.config = self._load_config
        self.load_settings()

    @cached_property
    def _load_config(self) -> Settings:
        """Loads the base configuration file."""
        file_path = get_resource_path(
            file_path=self.config_file,
            submodule=self.submodule,
        )
        config_dict = self.file_handler.read(str(file_path))
        return Settings.model_validate(config_dict)

    def load_settings(self) -> dict[str, dict]:
        """
        Loads all configuration settings.
        1. Loads the base configuration file from 'settings/config.toml'.
        2. Loads all additional TOML files defined in 'FileSettings.'
        """
        settings = self._load_config.model_dump()

        for key, file_path in settings["files"].items():
            if not file_path.endswith(".toml"):
                continue

            file_path = get_resource_path(file_path=file_path)
            data_config = self.file_handler.read(file_path)
            settings[key] = data_config
            setattr(self, key, data_config)

            _logger.info(f"Config loaded: {self.submodule}/{file_path}")

        return settings
