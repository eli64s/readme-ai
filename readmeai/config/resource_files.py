from pathlib import Path
from typing import ClassVar, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class SharedMetadata(BaseModel):
    """
    Immutable shared metadata model for PyPI package resources.
    """

    module: str = "readmeai"
    submodule: str = "config/settings"
    format: str = "toml"

    model_config = ConfigDict(
        frozen=True,
    )


class ResourceFile(BaseModel):
    """
    Resource model with shared metadata.
    """

    _shared_metadata: ClassVar[SharedMetadata] = SharedMetadata()

    path: Path
    description: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        use_enum_values=True,
    )

    @computed_field
    def module(self) -> str:
        """Gets module name (package) from shared metadata when needed."""
        return self._shared_metadata.module

    @computed_field
    def submodule(self) -> str:
        """Gets submodule name (directory) from shared metadata when needed."""
        return self._shared_metadata.submodule

    @computed_field
    def format(self) -> str:
        """Gets file format (extension) from shared metadata when needed."""
        return self._shared_metadata.format

    @computed_field
    def full_path(self) -> Path:
        """Computes full path of the package resource file."""
        from readmeai.utils.resource_loader import build_resource_path

        return Path(
            build_resource_path(
                str(self.path), module=self.module, submodule=self.submodule
            )
        )


class ConfigFile(ResourceFile):
    """
    Configuration file resources. Inherits _shared_metadata reference.
    """

    _shared_metadata: ClassVar[SharedMetadata] = SharedMetadata(
        submodule="config/settings", format="toml"
    )


class DataFile(ResourceFile):
    """
    Data file resources. Inherits _shared_metadata reference.
    """

    _shared_metadata: ClassVar[SharedMetadata] = SharedMetadata(
        submodule="data/svg", format="json"
    )


class ConfigFilesSettings(BaseSettings):
    """
    Configuration file resources with memory optimization.
    """

    dev_setup: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("analyzer/dev-setup.toml")
        )
    )
    dev_tools: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("analyzer/dev-tools.toml")
        )
    )
    ignore_list: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("analyzer/ignore-list.toml")
        )
    )
    language_map: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("analyzer/language-map.toml")
        )
    )
    project_manifest: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("analyzer/project-manifest.toml")
        )
    )
    document_template: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("templates/document.toml")
        )
    )
    quickstart_template: ConfigFile = Field(
        default_factory=lambda: ConfigFile(
            path=Path("templates/quickstart.toml")
        )
    )
    prompts: ConfigFile = Field(
        default_factory=lambda: ConfigFile(path=Path("prompts/prompts.toml"))
    )
    emoji_themes: ConfigFile = Field(
        default_factory=lambda: ConfigFile(path=Path("themes/emojis.toml"))
    )

    model_config = SettingsConfigDict(
        extra="forbid",
        validate_default=True,
        validate_assignment=True,
    )

    @computed_field
    def paths(self) -> List[Path]:
        """Get all config paths efficiently."""
        return [
            getattr(self, name).full_path
            for name in self.model_fields
            if isinstance(getattr(self, name), ResourceFile)
        ]


class DataFilesSettings(BaseSettings):
    """
    Data file resources with memory optimization.
    """

    shieldsio: DataFile = Field(
        default_factory=lambda: DataFile(path=Path("shieldsio.json"))
    )
    skillicons: DataFile = Field(
        default_factory=lambda: DataFile(path=Path("skillicons.json"))
    )

    model_config = SettingsConfigDict(
        extra="forbid",
        validate_default=True,
        validate_assignment=True,
    )

    @computed_field
    def paths(self) -> list[Path]:
        """Get all data paths efficiently."""
        return [
            getattr(self, name).full_path
            for name in self.model_fields
            if isinstance(getattr(self, name), ResourceFile)
        ]


class PackageResourceSettings(BaseSettings):
    """
    Top-level settings with memory optimization.
    """

    config: ConfigFilesSettings = Field(default_factory=ConfigFilesSettings)
    data: DataFilesSettings = Field(default_factory=DataFilesSettings)

    model_config = SettingsConfigDict(
        extra="forbid",
        validate_default=True,
        validate_assignment=True,
    )

    @computed_field
    def all_paths(self) -> Dict[str, List[Path]]:
        """Get all resource paths efficiently."""
        return {
            "config_paths": self.config.paths,
            "data_paths": self.data.paths,
        }


# def demonstrate_settings():
#     """Demonstrate the settings and resource management."""
#     settings = PackageResourceSettings()
#     all_paths = settings.all_paths
#     # Access config files (lazy computation of paths)
#     emojis_path = settings.config.emojis.model_dump()
#     prompts_path = settings.config.prompts.full_path
#     print(f"Emojis path: {emojis_path}\n")
#     print(f"{settings.config.emojis}\n")

#     # Access data files
#     shields_path = settings.data.shieldsio.full_path

#     # Verify shared metadata
#     print(id(settings.config.emojis._shared_metadata))
#     print(id(settings.config.prompts._shared_metadata))
#     assert (
#         settings.config.emojis._shared_metadata
#         is settings.config.prompts._shared_metadata
#     )

#     # Get all paths
#     all_paths = settings.all_paths

#     return {
#         "emojis_path": emojis_path,
#         "prompts_path": prompts_path,
#         "shields_path": shields_path,
#         "all_paths": all_paths,
#     }


# if __name__ == "__main__":
#     paths = demonstrate_settings()
#     for key, value in paths.items():
#         print(f"{key}: {value}\n")
