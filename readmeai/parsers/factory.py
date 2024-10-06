from typing import ClassVar

from .base import BaseFileParser, DefaultParser
from .cpp import CMakeParser, ConfigureAcParser, MakefileAmParser
from .docker import DockerComposeParser, DockerfileParser
from .go import GoModParser
from .gradle import BuildGradleKtsParser, BuildGradleParser
from .maven import MavenParser
from .npm import PackageJsonParser
from .properties import PropertiesParser
from .python import RequirementsParser, TomlParser, YamlParser
from .rust import CargoTomlParser
from .swift import SwiftPackageParser

ParserRegistryType = dict[str, type[BaseFileParser]]


class ParserFactory:
    """
    Factory for creating dependency file parser callable objects.
    """

    _parsers: ClassVar[dict[str, type[BaseFileParser]]] = {
        # Python
        "Pipfile": TomlParser,
        "pyproject.toml": TomlParser,
        "requirements.in": RequirementsParser,
        "requirements.txt": RequirementsParser,
        "requirements-dev.txt": RequirementsParser,
        "requirements-test.txt": RequirementsParser,
        "requirements-prod.txt": RequirementsParser,
        "dev-requirements.txt": RequirementsParser,
        "environment.yml": YamlParser,
        "environment.yaml": YamlParser,
        "poetry.lock": DefaultParser,
        "pdm.lock": DefaultParser,
        # C/C++
        "CMakeLists.txt": CMakeParser,
        "configure.ac": ConfigureAcParser,
        "Makefile.am": MakefileAmParser,
        # JavaScript/Node.js
        "package.json": PackageJsonParser,
        # Kotlin/Kotlin DSL
        "build.gradle": BuildGradleParser,
        "build.gradle.kts": BuildGradleKtsParser,
        # Go
        "go.mod": GoModParser,
        # Java
        "pom.xml": MavenParser,
        # Rust
        "Cargo.toml": CargoTomlParser,
        # Swift
        "Package.swift": SwiftPackageParser,
        # Docker
        "Dockerfile": DockerfileParser,
        "docker-compose.yaml": DockerComposeParser,
        "docker-compose.yml": DockerComposeParser,
        # Properties
        ".properties": PropertiesParser,
    }

    @classmethod
    def register_parser(
        cls, file_name: str, parser_class: type[BaseFileParser]
    ):
        """Register a parser for the given file name."""
        cls._parsers[file_name] = parser_class

    @classmethod
    def create_parser(cls, file_name: str) -> BaseFileParser:
        """Create a parser for the given file name."""
        if parser_class := cls._parsers.get(file_name):
            return parser_class()
        else:
            return DefaultParser()
