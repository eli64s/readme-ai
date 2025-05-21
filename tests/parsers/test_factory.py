from typing import Literal
from unittest.mock import MagicMock

import pytest

from readmeai.parsers.factory import (
    BaseFileParser,
    DefaultParser,
    ParserFactory,
)


@pytest.fixture
def mock_parser():
    return MagicMock(spec=BaseFileParser)


def test_default_parser():
    parser = ParserFactory.create_parser("unknown.extension")
    assert isinstance(parser, DefaultParser)


@pytest.mark.parametrize(
    "file_name, parser_name",
    [
        ("Pipfile", "TomlParser"),
        ("requirements.txt", "RequirementsParser"),
        ("CMakeLists.txt", "CMakeParser"),
        ("package.json", "PackageJsonParser"),
        ("build.gradle", "BuildGradleParser"),
        ("go.mod", "GoModParser"),
        ("pom.xml", "MavenParser"),
        ("Cargo.toml", "CargoTomlParser"),
        ("Package.swift", "SwiftPackageParser"),
        ("Dockerfile", "DockerfileParser"),
        ("docker-compose.yaml", "DockerComposeParser"),
        (".properties", "PropertiesParser"),
    ],
)
def test_registered_parsers(
    file_name: Literal["Pipfile"]
    | Literal["requirements.txt"]
    | Literal["CMakeLists.txt"]
    | Literal["package.json"]
    | Literal["build.gradle"]
    | Literal["go.mod"]
    | Literal["pom.xml"]
    | Literal["Cargo.toml"]
    | Literal["Package.swift"]
    | Literal["Dockerfile"]
    | Literal["docker-compose.yaml"]
    | Literal[".properties"],
    parser_name: Literal["TomlParser"]
    | Literal["RequirementsParser"]
    | Literal["CMakeParser"]
    | Literal["PackageJsonParser"]
    | Literal["BuildGradleParser"]
    | Literal["GoModParser"]
    | Literal["MavenParser"]
    | Literal["CargoTomlParser"]
    | Literal["SwiftPackageParser"]
    | Literal["DockerfileParser"]
    | Literal["DockerComposeParser"]
    | Literal["PropertiesParser"],
):
    parser = ParserFactory.create_parser(file_name)
    assert parser.__class__.__name__ == parser_name


def test_register_parser(mock_parser: MagicMock):
    ParserFactory.register_parser("newext", mock_parser)
    parser = ParserFactory.create_parser("file.newext")
    assert isinstance(parser, DefaultParser)
