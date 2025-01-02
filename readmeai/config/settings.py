"""Pydantic model settings for the readme-ai package."""

from __future__ import annotations

import random
import sys
from pathlib import Path
from typing import Dict, List, Literal, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    NonNegativeFloat,
    PositiveInt,
    field_validator,
    model_validator,
)
from pydantic_extra_types.color import Color
from readmeai.core.errors import GitValidationError
from readmeai.core.logger import get_logger
from readmeai.generators.banners import ascii
from readmeai.generators.banners.svg import SVGBannerGenerator
from readmeai.generators.enums import (
    BadgeStyles,
    CustomLogos,
    DefaultLogos,
    EmojiThemes,
    HeaderStyles,
    NavigationStyles,
)
from readmeai.models.enums import (
    AnthropicModels,
    BaseURLs,
    GeminiModels,
    LLMProviders,
    OllamaModels,
    OpenAIModels,
)
from readmeai.retrievers.git.providers import GitURL, parse_git_url
from readmeai.utilities.file_handler import FileHandler
from readmeai.utilities.importer import is_available
from readmeai.utilities.resource_manager import build_resource_path

if is_available("typing_extensions"):
    from typing_extensions import Self
else:
    from typing import Self

_logger = get_logger(__name__)


class FileSettings(BaseModel):
    """
    File path resources for the readme-ai package.
    """

    banners: str = Field(description="SVG banner templates.")
    dev_setup: str = Field(description="Development tool configurations.")
    dev_tools: str = Field(description="Development tools and utilities.")
    ignore_list: str = Field(description="List of files to ignore.")
    language_map: str = Field(description="Extension to language mappings.")
    parsers: str = Field(description="Common dependency file names.")
    prompts: str = Field(description="LLM API prompt templates.")
    quickstart_guides: str = Field(description="Quickstart guide templates.")
    shieldsio: str = Field(description="Shields.io svg icon badges.")
    skillicons: str = Field(description="Skill icon badges.")
    templates: str = Field(description="Custom README templates.")


class GitSettings(BaseModel):
    """
    User repository settings for a remote or local codebase.
    """

    repository: Union[str, Path] = Field(..., description="Repository URL or path.")
    full_name: str = Field(default="", description="Full repository name")
    host_domain: str = Field(default="", description="Git host domain")
    host: str = Field(default="", description="Git host name")
    name: str = Field(default="", description="Repository name")

    model_config = ConfigDict(extra="forbid")

    @field_validator("repository")
    def validate_repository(cls, value: Union[str, Path]) -> Union[str, Path]:
        """Validates the repository path or Git URL."""
        if isinstance(value, Path) or (
            isinstance(value, str) and Path(value).is_dir() and Path(value).exists()
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
    """Markdown configuration settings for README.md file generation."""

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
        use_enum_values=True,
    )

    # Layout Settings
    align: Literal["left", "center", "right"] = Field(default="center")
    placeholder: str = Field(default="<code>❯ REPLACE-ME</code>")
    thematic_break: str = Field(default="---\n")

    # Header Settings
    logo: str = Field(default=DefaultLogos.PURPLE)
    logo_size: str = Field(default="400px")
    header_style: HeaderStyles = Field(default=HeaderStyles.CLASSIC)

    # Badge Settings
    badge_color: Color = Field(default_factory=lambda: Color("blue"))
    badge_style: BadgeStyles = Field(default=BadgeStyles.DEFAULT)
    shieldsio: str
    skillicons: str
    tech_stack_icons: str
    tech_stack_description: str

    # Navigation Settings
    navigation_style: NavigationStyles = Field(default=NavigationStyles.BULLET)
    top_anchor_markup: str = Field(default='<div id="top">')
    return_to_top_markup: str = Field(
        default="""<div align="left"><a href="#top">⬆ Return</a></div>\n"""
    )

    # Content Settings
    tagline: str = ""
    overview: str = "{0}"
    features: str = "{0}"
    roadmap: str
    contribute: str
    license: str
    acknowledgment: str
    emojis: str = Field(
        default=EmojiThemes.DEFAULT, description="Emoji theme header prefix"
    )
    directory_structure: str = Field(
        default="""```sh\n{0}\n```""", description="Directory tree code block"
    )
    tree_max_depth: PositiveInt = Field(
        default=2, ge=1, le=5, description="Directory tree depth limit"
    )

    @field_validator("badge_color")
    def set_color(cls, value: str) -> str:
        """Format badge color value to hexadecimal."""
        try:
            return Color(value).as_hex(format="long").lstrip("#")
        except ValueError as e:
            _logger.error(f"Invalid color provided: {value} - {e}")
            return cls.model_fields["badge_color"].default

    @field_validator("logo")
    def validate_logo(cls, value) -> str:
        """Validate the logo is not empty or None."""
        if not value or value in [None, "", DefaultLogos, CustomLogos]:
            return DefaultLogos.PURPLE.value
        return value

    @model_validator(mode="after")
    def validate_emojis(self):
        """Validate the emoji theme is not empty or None."""
        if self.emojis == EmojiThemes.RANDOM.value:
            self.emojis = random.choice(list(EmojiThemes))
            _logger.info(f"Random emoji theme selected: {self.emojis}")
        return self


class ModelSettings(BaseModel):
    """
    LLM API service configuration and parameters.
    """

    model_config = ConfigDict(
        use_enum_values=True,
        validate_assignment=True,
    )

    api: LLMProviders = LLMProviders.OFFLINE
    encoder: str = "cl100k_base"
    base_url: str = Field(
        default=BaseURLs.OPENAI,
        description="Base URL for the selected API service",
    )
    context_window: PositiveInt = Field(default=3900, le=4096)
    localhost: str = "http://localhost:11434/"
    temperature: NonNegativeFloat = Field(default=0.1, le=2.0)
    tokens: PositiveInt = Field(default=699, le=2048)
    top_p: NonNegativeFloat = Field(default=0.9, le=1.0)
    rate_limit: PositiveInt = Field(default=10, le=30)
    resource: str = "v1/chat/completions"
    system_message: str = (
        "You're a 10x Staff Software Engineering leader, with deep knowledge "
        "across most tech stacks. You'll use your expertise to write robust "
        "README markdown files for open-source projects. You're a master of "
        "the craft, and you're here to help others succeed."
    )
    supported_models: Dict[str, List[str]] = Field(
        default_factory=lambda: {
            "ollama": [model.value for model in OllamaModels],
            "openai": [model.value for model in OpenAIModels],
            "anthropic": [model.value for model in AnthropicModels],
            "gemini": [model.value for model in GeminiModels],
        }
    )
    model: Union[OllamaModels, OpenAIModels, AnthropicModels, GeminiModels] = Field(
        default=OpenAIModels.GPT35_TURBO,
        description="Model for text generation",
    )

    def get_supported_models(self) -> List[str]:
        """Get a list of supported models for a given LLM API."""
        return self.supported_models.get(self.api, [])

    def validate_model(self, model: str) -> bool:
        """Validate if a LLM API supports a given model."""
        return model in self.get_supported_models()


class Settings(BaseModel):
    """
    Nested Pydantic model storing all configuration settings.
    """

    files: FileSettings
    git: GitSettings
    llm: ModelSettings
    md: MarkdownSettings

    model_config = ConfigDict(
        extra="allow",
        validate_assignment=True,
    )

    @model_validator(mode="after")
    def generate_banner(self) -> Self:
        """Generates a banner based on the selected header style."""
        header_style = self.md.header_style.lower()

        if header_style == HeaderStyles.CONSOLE.value:
            self.md.logo = ascii.generate_console_banner(self.git.name)
            self.md.header_style = HeaderStyles.CONSOLE
            return self

        if header_style == HeaderStyles.ASCII.value:
            self.md.logo = ascii.generate_banner(self.git.name)
            self.md.header_style = HeaderStyles.ASCII

        elif header_style == HeaderStyles.ASCII_BOX.value:
            self.md.logo = ascii.generate_box_banner(self.git.name)
            self.md.header_style = HeaderStyles.ASCII

        elif header_style == HeaderStyles.BANNER.value:
            self.md.logo = SVGBannerGenerator(
                f"config/settings/{self.files.banners}"
            ).generate_svg(
                title=self.git.name,
                # subtitle=self.md.placeholder,
            )
            self.md.header_style = HeaderStyles.BANNER
        elif (
            header_style
            in [
                HeaderStyles.CLASSIC.value,
                HeaderStyles.COMPACT.value,
                HeaderStyles.MODERN.value,
            ]
            or self.md.logo == CustomLogos.LLM.value
        ):
            self._set_header_style(header_style)

        return self

    def _set_header_style(self, header_style: str) -> None:
        """Helper method to set the header style."""
        style_map = {
            HeaderStyles.CLASSIC.value: HeaderStyles.CLASSIC,
            HeaderStyles.CLEAN.value: HeaderStyles.CLEAN,
            HeaderStyles.COMPACT.value: HeaderStyles.COMPACT,
            HeaderStyles.MODERN.value: HeaderStyles.MODERN,
        }
        if header_style in style_map:
            self.md.header_style = style_map[header_style]


class ConfigLoader:
    """
    Load all resources and settings for the readme-ai package.
    """

    file_handler: FileHandler = FileHandler()
    config_file: str = "config.toml"
    module: str = "readmeai.config"
    submodule: str = "settings"

    def __init__(self) -> None:
        if "-V" not in sys.argv and "--version" not in sys.argv:
            self._load_config()
            self._load_settings()

    def _load_config(self) -> Settings:
        """Loads the base configuration file."""
        file_path = build_resource_path(
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
                file_path = build_resource_path(file_path=file_path)
                config_dict = self.file_handler.read(file_path)
                settings[key] = config_dict
                setattr(self, key, config_dict)
                _logger.info(f"Succesfully loaded cofing: {file_path.name}")

        themes_path = build_resource_path(
            file_path="emojis.yaml", submodule=f"{self.submodule}/themes"
        )
        themes_data = self.file_handler.read(themes_path)
        self.themes = themes_data.get("themes", {})
        _logger.info(f"Emoji themes loaded: {list(self.themes.keys())}")

        return settings
