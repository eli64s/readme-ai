"""Pydantic models and settings for the readme-ai package."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import ClassVar, Literal, Tuple, Type

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
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

from readmeai.config.constants import (
    BadgeStyleOptions,
    EmojiThemeOptions,
    HeaderStyleOptions,
    ImageOptions,
    LLMService,
    TocStyleOptions,
)
from readmeai.config.resource_files import PackageResourceSettings
from readmeai.errors import GitValidationError
from readmeai.generators.banners import (
    convert_svg_to_html,
    generate_ascii_banner,
    generate_ascii_box_banner,
)
from readmeai.logger import get_logger
from readmeai.readers.git.providers import GitURL, parse_git_url
from readmeai.utils.file_handler import FileHandler
from readmeai.utils.module_importer import is_available
from readmeai.utils.resource_loader import build_resource_path

if is_available("typing_extensions"):
    from typing_extensions import Self
else:
    from typing import Self

_logger = get_logger(__name__)


class GitSettings(BaseModel):
    """
    Metadata and settings for the user's repository.
    """

    repository: Path | str = ""
    full_name: str | None = None
    host_domain: str | None = None
    host: str | None = None
    name: str | None = None

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
    def set_git_attributes(self):
        """Parse and set Git repository attributes."""
        self.host_domain, self.host, self.name, self.full_name = parse_git_url(
            str(self.repository)
        )
        return self


class MarkdownSettings(BaseModel):
    """
    Markdown content settings for the generated README.
    """

    align: Literal["left", "center", "right"] = Field(
        default="center", description="align for markdown content."
    )
    badge_color: Color = Field(
        default_factory=lambda: Color("blue"),
        description="Badge color (https://www.w3.org/TR/SVG11/types.html#ColorKeywords)",
    )
    badge_style: BadgeStyleOptions = Field(default=BadgeStyleOptions.DEFAULT)
    badges_tech_stack_icons: str = ""
    badges_tech_stack_text: str = ""
    contribute: str = ""
    emojis: EmojiThemeOptions = Field(default=EmojiThemeOptions.DEFAULT)
    features: str = "❯ INSERT-PROJECT-FEATURES"
    header_style: str = Field(default=HeaderStyleOptions.CLASSIC)
    image: AnyHttpUrl | FilePath | str = Field(default=ImageOptions.BLUE)
    image_width: str = "20%"
    overview: str = "❯ INSERT-PROJECT-OVERVIEW"
    placeholder: str = "<code>❯ REPLACE-ME</code>"
    project_index: str = ""
    quickstart: str = ""
    shieldsio_icons: str = ""
    skill_icons: str = ""
    tagline: str = "❯ INSERT-PROJECT-tagline"
    tables: str = "❯ INSERT-PROJECT-TABLES"
    toc_style: str = Field(default=TocStyleOptions.BULLET)
    tree: str = Field(default="❯ INSERT-PROJECT-TREE")
    tree_depth: PositiveInt = Field(default=2, ge=1, le=5)
    license: str = "- Credit `contributors`, `inspiration`, `references`, etc."
    roadmap: str = ""
    acknowledgements: str = ""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        use_enum_values=True,
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
    LLM API settings and parameters.
    """

    api: LLMService = LLMService.OFFLINE
    encoder: str = "cl100k_base"
    model: str = "gpt-3.5-turbo"
    base_url: str = "https://api.openai.com/"
    localhost: str = "http://localhost:11434/"
    resource: str = "v1/chat/completions"
    context_window: PositiveInt = Field(default=3900, le=4096)
    temperature: NonNegativeFloat = Field(default=0.1, le=2.0)
    tokens: PositiveInt = Field(default=699, le=2048)
    top_p: NonNegativeFloat = Field(default=0.9, le=1.0)
    rate_limit: PositiveInt = Field(default=10, le=30)
    system_message: str = (
        "You're a 10x Staff Software Engineering leader, with deep knowledge "
        "across most tech stacks. You'll use your expertise to write robust "
        "README markdown files for open-source projects. You're a master of "
        "the craft, and you're here to help others succeed."
    )

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        use_enum_values=True,
    )


class Settings(BaseSettings):
    """
    Nested Pydantic model storing all configuration settings.
    """

    _resource_files: ClassVar[PackageResourceSettings] = (
        PackageResourceSettings()
    )
    _toml_paths: ClassVar[list[str]] = [
        str(path)
        for key, paths in _resource_files.all_paths.items()
        for path in paths
        if key == "config_paths"
    ]

    model_config = SettingsConfigDict(
        extra="allow",
        toml_file=_toml_paths,
        validate_default=True,
    )

    git: GitSettings = Field(default_factory=GitSettings)
    llm: ModelSettings = Field(default_factory=ModelSettings)
    md: MarkdownSettings = Field(default_factory=MarkdownSettings)

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        """Custom settings source for TOML configuration files."""
        return (TomlConfigSettingsSource(settings_cls),)

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
            if header_style == HeaderStyleOptions.CLASSIC.value:
                self.md.header_style = HeaderStyleOptions.CLASSIC
                self.md.image_width = "30%"
            elif header_style == HeaderStyleOptions.COMPACT.value:
                self.md.header_style = HeaderStyleOptions.COMPACT
                self.md.image_width = "40%"
            elif header_style == HeaderStyleOptions.MODERN.value:
                self.md.header_style = HeaderStyleOptions.MODERN
                self.md.image_width = "30%"

        return self


class ConfigLoader:
    """
    Loads the base configuration file for the application.
    """

    file_handler: FileHandler = FileHandler()
    config_file: str = "config.toml"
    module: str = "readmeai.config"
    submodule: str = "settings"

    def __init__(self) -> None:
        """Initialize ConfigLoader with the base configuration file."""
        if "-V" not in sys.argv and "--version" not in sys.argv:
            self._load_config()

    def _load_config(self) -> Settings:
        """Loads the base configuration file."""
        file_path = build_resource_path(
            file_path=self.config_file,
            submodule=self.submodule,
        )
        config_dict = self.file_handler.read(file_path)
        self.config = Settings(**config_dict)
        _logger.info(f"Configuration file loaded: {file_path}")
        return self.config
