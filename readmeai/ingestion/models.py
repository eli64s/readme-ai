from typing import Annotated, Any

from pydantic import BaseModel, Field, StringConstraints


class QuickStart(BaseModel):
    """
    Instructions for installation, usage, and testing a repository.
    """

    primary_language: str | None = None
    language_counts: dict[str, int] = Field(default_factory=dict)
    package_managers: dict[str, str] = Field(default_factory=dict)
    containers: dict[str, str] = Field(default_factory=dict)
    install_commands: str = ""
    usage_commands: str = ""
    test_commands: str = ""


class FileContext(BaseModel):
    """
    FileContext model for storing file information.
    """

    path: str
    name: str
    ext: str
    content: str
    language: Annotated[str, StringConstraints(to_lower=True)]
    dependencies: Annotated[list[str], Field(default_factory=list)]


class RepositoryContext(BaseModel):
    """
    RepositoryContext model for storing repository information
    """

    files: list[FileContext]
    dependencies: list[str]
    languages: list[str]
    language_counts: dict[str, int]
    metadata: dict[str, Any] = Field(default_factory=dict)
    quickstart: QuickStart = Field(default_factory=QuickStart)
