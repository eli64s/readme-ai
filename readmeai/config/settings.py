"""Pydantic models and settings for the readme-ai package."""

from __future__ import annotations

from pathlib import Path
from typing import Literal, Self

from pydantic import (
    AnyHttpUrl,
    BaseModel,
    ConfigDict,
    Field,
    FilePath,
    NonNegativeFloat,
    PositiveInt,
    field_validator,
    model_validator,
)
from pydantic_extra_types.color import Color

from readmeai.config.constants import (
    BadgeStyleOptions,
    HeaderStyleOptions,
    ImageOptions,
    TocStyleOptions,
)
from readmeai.errors import GitValidationError
from readmeai.generators.banner import (
    convert_svg_to_html,
    generate_ascii_banner,
    generate_ascii_box_banner,
)
from readmeai.logger import get_logger
from readmeai.readers.git.providers import GitURL, parse_git_url
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.file_resource import get_resource_path

_logger = get_logger(__name__)


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

    ignore_list: str = Field(description="List of files to ignore.")
    languages: str = Field(description="Extension to language mappings.")
    parsers: str = Field(description="Common dependency file names.")
    prompts: str = Field(description="LLM API prompt templates.")
    tool_config: str = Field(description="Development tool configurations.")
    tooling: str = Field(description="Development tools and utilities.")
    shieldsio_icons: str = Field(description="Shields.io svg icon badges.")
    skill_icons: str = Field(description="Skill icon badges.")


class GitSettings(BaseModel):
    """
    User repository settings for a remote or local codebase.
    """

    repository: Path | str
    full_name: str | None = None
    host_domain: str | None = None
    host: str | None = None
    name: str = ""

    model_config = ConfigDict(extra="forbid")

    @field_validator("repository")
    def validate_repository(cls, value: Path | str) -> Path | str:
        """Validates the repository path or Git URL."""
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

    @model_validator(mode="after")
    def set_git_attributes(self) -> Self:
        """Parse and set Git repository attributes."""
        self.host_domain, self.host, self.name, self.full_name = parse_git_url(
            str(self.repository)
        )
        return self


class MarkdownSettings(BaseModel):
    """
    Markdown code template blocks for building the README.md file.
    """

    align: Literal["left", "center", "right"] = Field(
        default="center", description="align for markdown content."
    )
    badge_color: Color = Field(
        default_factory=lambda: Color("blue"),
        description="Badge color (https://www.w3.org/TR/SVG11/types.html#ColorKeywords)",
    )
    badge_style: BadgeStyleOptions = Field(
        default=BadgeStyleOptions.DEFAULT, description="Badge icon style type."
    )
    badges_tech_stack: str
    badges_tech_stack_text: str
    contribute: str
    emojis: bool = Field(
        default=False, description="Enable emoji prefixes for headers."
    )
    features: str = Field(
        default="❯ INSERT-PROJECT-FEATURES",
        description="Project feature markdown table content.",
    )
    header_style: str = Field(
        default=HeaderStyleOptions.CLASSIC,
        description="Header style for the project README.",
    )
    image: AnyHttpUrl | FilePath | str = Field(
        default=ImageOptions.BLUE,
        description="Project image URL or file path.",
    )
    image_width: str = Field(default="20%")
    overview: str = Field(default="❯ INSERT-PROJECT-OVERVIEW")
    placeholder: str = Field(default="<code>❯ REPLACE-ME</code>")
    project_index: str
    quickstart: str
    shieldsio_icons: str
    skill_icons: str
    slogan: str = Field(default="❯ INSERT-PROJECT-SLOGAN")
    tables: str = Field(default="❯ INSERT-PROJECT-TABLES")
    toc_style: str = Field(default=TocStyleOptions.BULLET)
    tree: str
    tree_depth: PositiveInt = Field(default=2, ge=1, le=5)

    model_config = ConfigDict(
        use_enum_values=True,
        arbitrary_types_allowed=True,
    )

    @field_validator("badge_color")
    def set_color(cls, value: str) -> str:
        """Field validator to set the badge color."""
        try:
            return Color(value).as_hex(format="long").lstrip("#")
        except ValueError:
            _logger.error(f"Invalid color provided: {value}", exc_info=True)
            return cls.model_fields["badge_color"].default


class ModelSettings(BaseModel):
    """
    LLM API model settings and parameters.
    """

    api: str
    base_url: str
    context_window: PositiveInt
    encoder: str
    host_name: AnyHttpUrl
    localhost: AnyHttpUrl
    model: str
    path: str
    temperature: NonNegativeFloat
    tokens: PositiveInt
    top_p: NonNegativeFloat


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

    @model_validator(mode="after")
    def generate_banner(self) -> Self:
        """Generates the project banner based on the settings."""
        header_style = self.md.header_style.lower()
        if header_style == HeaderStyleOptions.ASCII.value:
            self.md.image = generate_ascii_banner(self.git.name)
            self.md.header_style = HeaderStyleOptions.ASCII
        elif header_style == HeaderStyleOptions.ASCII_BOX.value:
            self.md.image = generate_ascii_box_banner(self.git.name)
            self.md.header_style = HeaderStyleOptions.ASCII
        elif header_style == HeaderStyleOptions.SVG.value:
            self.md.image = convert_svg_to_html(
                self.git.name, f"{self.git.name}-banner.svg"
            )
            self.md.header_style = HeaderStyleOptions.SVG
        elif (
            header_style
            in [
                HeaderStyleOptions.CLASSIC.value,
                HeaderStyleOptions.COMPACT.value,
                HeaderStyleOptions.MODERN.value,
            ]
            or self.md.image == ImageOptions.LLM.value
        ):
            self.md.image_width = "30%"
            if header_style == HeaderStyleOptions.CLASSIC.value:
                self.md.header_style = HeaderStyleOptions.CLASSIC
            elif header_style == HeaderStyleOptions.COMPACT.value:
                self.md.header_style = HeaderStyleOptions.COMPACT
            elif header_style == HeaderStyleOptions.MODERN.value:
                self.md.header_style = HeaderStyleOptions.MODERN

        return self


class ConfigLoader:
    """
    Loads the configuration settings for the readme-ai package.
    """

    file_handler: FileHandler = FileHandler()
    config_file: str = "config.toml"
    module: str = "readmeai.config"
    submodule: str = "settings"

    def __init__(self) -> None:
        """Initialize ConfigLoader with the base configuration file."""
        self._load_config()
        self._load_settings()

    def _load_config(self) -> Settings:
        """Loads the base configuration file."""
        file_path = get_resource_path(
            file_path=self.config_file,
            submodule=self.submodule,
        )
        config_dict = self.file_handler.read(file_path)
        self.config = Settings.model_validate(config_dict)
        return self.config

    def _load_settings(self) -> dict[str, dict]:
        """Loads all TOML config files from ./config/settings/*.toml."""
        settings = self.config.model_dump()

        for key, file_path in settings["files"].items():
            if file_path.endswith(".toml"):
                file_path = get_resource_path(file_path=file_path)
                config_dict = self.file_handler.read(file_path)
                settings[key] = config_dict
                setattr(self, key, config_dict)
                _logger.info(f"Configuration file loaded: {file_path}")

        return settings
