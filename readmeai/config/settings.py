"""Data models and functions for configuring the readme-ai CLI tool."""

from importlib import resources
from pathlib import Path
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field, validator

from readmeai.config.validators import GitValidator
from readmeai.core.file_io import FileHandler
from readmeai.core.logger import Logger
from readmeai.exceptions import FileReadError

logger = Logger(__name__)


class FileSettings(BaseModel):
    """File paths used by the readme-ai CLI tool."""

    dependency_files: str = Field(
        description="Top programming language dependency file name."
    )
    ignore_files: str = Field(
        description="File, directory, and extension names to ignore."
    )
    language_names: str = Field(
        description="Programming language names mapped to extension names."
    )
    language_setup: str = Field(
        description="Programming language install, run, and test commands."
    )
    shields_icons: str = Field(
        description="List of shields.io icons used to build markdown badges."
    )
    skill_icons: str = Field(
        description="List of skill icons used to build markdown badges."
    )


class GitSettings(BaseModel):
    """User repository settings, sanitized and validated by Pydantic."""

    discussions: str = "https://github.com/eli64s/readme-ai/discussions"
    repository: Union[str, Path]
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
    _set_host_domain = validator("host_domain", pre=True, always=True)(
        GitValidator.set_host_domain
    )
    _set_name = validator("name", pre=True, always=True)(GitValidator.set_name)


class ModelSettings(BaseModel):
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


class MarkdownSettings(BaseModel):
    """Markdown template blocks for the README.md file."""

    align: str
    default: str
    badge_color: str
    badge_style: str
    badges_dependencies: str
    badge_logo: str
    badges_shields: str
    badges_skills: str
    contribute: str
    emojis: bool
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
    tree_depth: int


class PromptSettings(BaseModel):
    """Prompt templates to generate text for the README.md file."""

    avatar: str = Field(
        description="Prompt to generate a project logo .png file."
    )
    features: str = Field(
        description="Prompt to generate a list of project features."
    )
    overview: str = Field(description="Prompt to generate a project overview.")
    slogan: str = Field(
        description="Prompt to generate a short project slogan or tagline."
    )
    summaries: str = Field(
        description="Prompt to generate a summary of a code file."
    )


class AppConfig(BaseModel):
    """Nested data model to store all configuration settings."""

    files: FileSettings
    git: GitSettings
    llm: ModelSettings
    md: MarkdownSettings
    prompts: PromptSettings


class AppConfigModel(BaseModel):
    """Pydantic model to store all configuration settings."""

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
    except TypeError as exc:
        logger.debug(f"Error using importlib.resources: {exc}")

        try:
            import pkg_resources

            resource_path = Path(
                pkg_resources.resource_filename(
                    "readmeai", f"settings/{file_path}"
                )
            ).resolve()
        except Exception as exc:
            raise FileReadError(
                "Error loading file via pkg_resources", file_path
            ) from exc

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
