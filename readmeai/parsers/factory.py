"""
Abstract factory module for all project file parsers.
"""

from readmeai.core.parsers import BaseFileParser
from readmeai.parsers.cpp import (
    CMakeParser,
    ConfigureAcParser,
    MakefileAmParser,
)
from readmeai.parsers.docker import (
    DockerComposeParser,
    DockerfileParser,
)
from readmeai.parsers.go import GoModParser
from readmeai.parsers.gradle import (
    BuildGradleKtsParser,
    BuildGradleParser,
)
from readmeai.parsers.maven import MavenParser
from readmeai.parsers.npm import PackageJsonParser
from readmeai.parsers.properties import PropertiesParser
from readmeai.parsers.python import (
    RequirementsParser,
    TomlParser,
    YamlParser,
)
from readmeai.parsers.rust import CargoTomlParser
from readmeai.parsers.swift import SwiftPackageParser
from readmeai.parsers.yarn import YarnLockParser

ParserRegistryType = dict[str, BaseFileParser]


def parser_handler() -> ParserRegistryType:
    """
    Returns a dictionary of callable file parser methods.
    """
    return {
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
        # Kotlin/Kotlin DSL
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
        # Docker
        "Dockerfile": DockerfileParser(),
        "docker-compose.yaml": DockerComposeParser(),
        ".properties": PropertiesParser(),
    }
