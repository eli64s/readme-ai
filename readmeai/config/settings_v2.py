"""Pydantic models and settings for the readme-ai package."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, ClassVar, Dict, Literal, Tuple, Type, Union
from urllib.parse import urlparse

from pydantic import (
    AnyHttpUrl,
    BaseModel,
    DirectoryPath,
    Field,
    FilePath,
    NewPath,
    NonNegativeFloat,
    PositiveInt,
    UrlConstraints,
    field_validator,
    model_validator,
)
from pydantic_extra_types.color import Color
from pydantic_settings import (
    BaseSettings,
    CliSettingsSource,
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
from readmeai.errors import GitValidationError
from readmeai.logger import get_logger
from readmeai.utils.resource_loader import build_resource_path

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

logger = get_logger(__name__)


GitHostUrl = Annotated[
    AnyHttpUrl,
    UrlConstraints(
        allowed_schemes=["http", "https"],
        host_required=True,
    ),
]


class GitSettings(BaseModel):
    """
    Repository settings for Git URL or local directory.
    """

    DOMAIN_MAPPINGS: ClassVar[dict[str, str]] = {
        "github.com": "github",
        "gitlab.com": "gitlab",
        "bitbucket.org": "bitbucket",
    }

    repository: Union[GitHostUrl, DirectoryPath, None] = None
    host: str = "local"
    host_domain: str = "local"
    owner: str = ""
    name: str = ""
    full_name: str = ""

    @model_validator(mode="after")
    def set_git_attributes(self) -> Self:
        """Parse Git URL or local path to set repository attributes."""
        if self.repository is None:
            raise GitValidationError("Repository URL or path is required")

        if isinstance(self.repository, Path) and self.repository.exists():
            self.host = "local"
            self.host_domain = "local"
            self.owner = "../../"
            self.name = (str(Path(self.repository.name)),)
            self.full_name = (f"{self.owner}/{self.name}",)
            return self

        try:
            parsed = urlparse(self.repository)
            logger.info(f"URL parsed: {parsed}")
            self.host_domain = parsed.netloc.lower()
            logger.info(f"Host domain: {self.host_domain}")
            self.host = self.DOMAIN_MAPPINGS.get(self.host_domain, "unknown")
            logger.info(f"Host: {self.host}")

        except ValueError as e:
            raise GitValidationError("Failed to validate repository") from e

        path_parts = parsed.path.strip("/").replace(".git", "").split("/")
        logger.info(f"Path parts: {path_parts}")

        if len(path_parts) >= 2:
            self.owner = path_parts[0]
            self.name = path_parts[1]
            self.full_name = f"{self.owner}/{self.name}"

        logger.info(f"Repository attributes: {self.model_dump()}")
        return self


class MarkdownSettings(BaseModel):
    """Markdown document settings."""

    align: Literal["left", "center", "right"] = "center"
    badge_color: Color = Field(
        default_factory=lambda: Color("blue"),
        json_schema_extra={"examples": ["blue", "#0000ff"]},
    )
    badge_style: BadgeStyleOptions = BadgeStyleOptions.DEFAULT.value
    emojis: EmojiThemeOptions = EmojiThemeOptions.DEFAULT.value
    header_style: str = HeaderStyleOptions.CLASSIC.value
    image: AnyHttpUrl | FilePath | str = ImageOptions.BLUE.value
    image_width: str = "20%"
    toc_style: str = TocStyleOptions.BULLET
    tree_depth: PositiveInt = Field(default=2, ge=1, le=5)
    header_style: str = Field(
        default=HeaderStyleOptions.CLASSIC,
        description="Header style for the project README.",
    )
    badges_tech_stack: str = "{badges_tech_stack}"
    badges_tech_stack_text: str = "<em>Tech Stack</em>"
    contribute: str = ""
    features: str = "{0}"
    overview: str = "{0}"
    placeholder: str = Field(default="<code>❯ REPLACE-ME</code>")
    project_index: str = ""
    quickstart: str = ""
    shieldsio_icons: str = ""
    skill_icons: str = ""
    tagline: str = "{0}"
    tables: str = "{0}"
    toc_style: str = Field(default=TocStyleOptions.BULLET)
    tree: str = ""
    tree_depth: PositiveInt = Field(default=2, ge=1, le=5)

    @field_validator("badge_color")
    def set_color(cls, value: str) -> str:
        try:
            return Color(value).as_hex(format="long").lstrip("#")
        except ValueError:
            return cls.model_fields["badge_color"].default


class ModelSettings(BaseModel):
    """LLM API configuration."""

    api: LLMService = LLMService.OFFLINE
    model: str = "gpt-3.5-turbo"
    encoder: str = "cl100k_base"
    base_url: str = "https://api.openai.com/"
    localhost: str = "http://localhost:11434/"
    resource: str = "v1/chat/completions"
    system_message: str = "You're a brilliant AI researcher and Tech Lead with a passion for open-source software."
    context_window: PositiveInt = Field(3900, le=4096)
    temperature: NonNegativeFloat = Field(0.1, le=2.0)
    tokens: PositiveInt = Field(699, le=2048)
    top_p: NonNegativeFloat = Field(0.9, le=1.0)
    rate_limit: PositiveInt = Field(10, le=30)


class PackageResourceSettings(BaseModel):
    """Settings for package resource file paths.

    Manages resource files in config/settings and data/svg directories.
    """

    BASE_MODULE: ClassVar[str] = "readmeai"
    CONFIG_DIR: ClassVar[str] = "config/settings"
    DATA_DIR: ClassVar[str] = "data/svg"

    config_files: Dict[str, Path] = Field(
        default_factory=lambda: {
            "emojis": Path("emojis.toml"),
            "ignore_list": Path("ignore-list.toml"),
            "languages": Path("languages.toml"),
            "parsers": Path("parsers.toml"),
            "prompts": Path("prompts.toml"),
            "quickstart": Path("quickstart.toml"),
            "templates": Path("templates.toml"),
            "tool_config": Path("tool_config.toml"),
            "tooling": Path("tooling.toml"),
        },
        description="Configuration files in config/settings",
    )
    data_files: Dict[str, Path] = Field(
        default_factory=lambda: {
            "shieldsio": Path("shieldsio.json"),
            "skillicons": Path("skillicons.json"),
        },
        description="Data files in data/svg",
    )

    @model_validator(mode="after")
    def validate_resource_paths(self) -> Self:
        """Ensure all resource paths exist and are readable."""
        from readmeai.utils.resource_loader import build_resource_path

        for name, path in self.config_files.items():
            try:
                full_path = build_resource_path(
                    str(path),
                    module=self.BASE_MODULE,
                    submodule=self.CONFIG_DIR,
                )
                if not Path(full_path).is_file():
                    raise ValueError(
                        f"Config file not found: {name} ({full_path})"
                    )
            except Exception as e:
                raise ValueError(
                    f"Failed to validate config file {name}"
                ) from e

        for name, path in self.data_files.items():
            try:
                full_path = build_resource_path(
                    str(path), module=self.BASE_MODULE, submodule=self.DATA_DIR
                )
                if not Path(full_path).is_file():
                    raise ValueError(
                        f"Data file not found: {name} ({full_path})"
                    )
            except Exception as e:
                raise ValueError(f"Failed to validate data file {name}") from e
        self.config_files = {k: v for k, v in self.config_files.items()}
        self.data_files = {k: v for k, v in self.data_files.items()}
        return self

    def get_config_path(self, resource_name: str) -> Path:
        """Get the full path for a config resource."""
        if resource_name not in self.config_files:
            raise KeyError(f"Unknown config resource: {resource_name}")
        return Path(
            build_resource_path(
                str(self.config_files[resource_name]),
                module=self.BASE_MODULE,
                submodule=self.CONFIG_DIR,
            )
        )

    def get_data_path(self, resource_name: str) -> Path:
        """Get the full path for a data resource."""
        if resource_name not in self.data_files:
            raise KeyError(f"Unknown data resource: {resource_name}")
        return Path(
            build_resource_path(
                str(self.data_files[resource_name]),
                module=self.BASE_MODULE,
                submodule=self.DATA_DIR,
            )
        )

    @property
    def config_paths(self) -> list:
        """Get a dictionary of config resource paths."""
        return [self.get_config_path(name) for name in self.config_files]

    @property
    def data_paths(self) -> list:
        """Get a dictionary of data resource paths."""
        return [self.get_data_path(name) for name in self.data_files]


class Settings(BaseSettings):
    """Root settings configuration."""

    from readmeai import __version__

    git: GitSettings = Field(default_factory=GitSettings)
    llm: ModelSettings = Field(default_factory=ModelSettings)
    md: MarkdownSettings = Field(default_factory=MarkdownSettings)
    output: NewPath = Field("readme-ai.md")
    version: str = __version__

    model_config = SettingsConfigDict(
        extra="allow",
        case_sensitive=False,
        validate_assignment=True,
        use_enum_values=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            TomlConfigSettingsSource(settings_cls),
            CliSettingsSource(settings_cls),
            env_settings,
        )

    def update_from_cli(self, **cli_args: dict) -> Self:
        """Update settings from CLI arguments, preserving defaults for unset values."""

        if "repository" in cli_args:
            self.git = GitSettings(repository=cli_args["repository"])

        llm_fields = {
            "api",
            "model",
            "temperature",
            "context_window",
            "top_p",
            "rate_limit",
        }
        llm_updates = {
            k: v
            for k, v in cli_args.items()
            if k in llm_fields and v is not None
        }
        if llm_updates:
            for key, value in llm_updates.items():
                setattr(self.llm, key, value)
            self.llm.model_validate(self.llm)

        md_fields = {
            "align",
            "badge_color",
            "badge_style",
            "emojis",
            "header_style",
            "image",
            "image_width",
            "toc_style",
            "tree_depth",
        }
        md_updates = {
            k: v
            for k, v in cli_args.items()
            if k in md_fields and v is not None
        }
        if md_updates:
            for key, value in md_updates.items():
                setattr(self.md, key, value)
            self.md.model_validate(self.md)

        return self

    @classmethod
    def get_cli_settings(cls, **cli_args) -> Settings:
        """Create settings instance and update with CLI args."""
        settings = cls()
        return settings.update_from_cli(**cli_args)

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
