"""Abstract factory module for all project file parsers."""

from typing import Dict, Type

from readmeai.core.parsers import BaseFileParser
from readmeai.parsers.configuration.docker import (
    DockerComposeParser,
    DockerfileParser,
)
from readmeai.parsers.configuration.properties import PropertiesParser
from readmeai.parsers.language.cpp import (
    CMakeParser,
    ConfigureAcParser,
    MakefileAmParser,
)
from readmeai.parsers.language.go import GoModParser
from readmeai.parsers.language.python import (
    RequirementsParser,
    TomlParser,
    YamlParser,
)
from readmeai.parsers.language.rust import CargoTomlParser
from readmeai.parsers.language.swift import SwiftPackageParser
from readmeai.parsers.package.gradle import (
    BuildGradleKtsParser,
    BuildGradleParser,
)
from readmeai.parsers.package.maven import MavenParser
from readmeai.parsers.package.npm import PackageJsonParser
from readmeai.parsers.package.yarn import YarnLockParser

ParserRegistryType = dict[str, Type[BaseFileParser]]

PARSER_REGISTRY = {
    # Configuration
    ".properties": PropertiesParser,
    # Language/Framework
    # Python
    "Pipfile": TomlParser(),
    "pyproject.toml": TomlParser(),
    "requirements.in": RequirementsParser(),
    "requirements.txt": RequirementsParser(),
    "requirements-dev.txt": RequirementsParser(),
    "requirements-test.txt": RequirementsParser(),
    "requirements-prod.txt": RequirementsParser(),
    "dev-requirements.txt": RequirementsParser(),
    "environment.yml": YamlParser(),
    "environment.yaml": YamlParser(),
    # "setup.py": setup_py_parser,
    # "setup.cfg": setup_cfg_parser,
    # C/C++
    "cmakeLists.txt": CMakeParser(),
    "configure.ac": ConfigureAcParser(),
    "Makefile.am": MakefileAmParser(),
    # JavaScript/Node.js
    "package.json": PackageJsonParser(),
    "yarn.lock": YarnLockParser(),
    # Kotlin and Kotlin DSL
    "build.gradle": BuildGradleParser(),
    "build.gradle.kts": BuildGradleKtsParser(),
    # Go
    "go.mod": GoModParser(),
    # Java
    "pom.xml": MavenParser(),
    # Rust
    "cargo.toml": CargoTomlParser(),
    # Swift
    "Package.swift": SwiftPackageParser(),
    "Dockerfile": DockerfileParser(),
    "docker-compose.yaml": DockerComposeParser(),
    # Package Managers
    # Monitoring and Logging
}


def parser_handler() -> Dict[str, BaseFileParser]:
    """Returns a dictionary of callable file parser methods."""
    return PARSER_REGISTRY
