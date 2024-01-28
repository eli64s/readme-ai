"""Abstract factory for all dependency file parsers."""

from typing import Dict

from readmeai.core.base_parser import FileParser
from readmeai.parsers.cpp import (
    CMakeParser,
    ConfigureAcParser,
    MakefileAmParser,
)
from readmeai.parsers.docker import DockerComposeParser, DockerfileParser
from readmeai.parsers.go import GoModParser
from readmeai.parsers.gradle import BuildGradleKtsParser, BuildGradleParser
from readmeai.parsers.maven import MavenParser
from readmeai.parsers.npm import PackageJsonParser, YarnLockParser
from readmeai.parsers.python import RequirementsParser, TomlParser, YamlParser
from readmeai.parsers.rust import CargoTomlParser
from readmeai.parsers.swift import SwiftPackageParser


def parser_factory() -> Dict[str, FileParser]:
    """Returns a dictionary of callable file parser methods."""
    yaml_parser = YamlParser()
    toml_parser = TomlParser()
    requirements_parser = RequirementsParser()

    return {
        # Python
        "Pipfile": toml_parser,
        "pyproject.toml": toml_parser,
        "requirements.in": requirements_parser,
        "requirements.txt": requirements_parser,
        "requirements-dev.txt": requirements_parser,
        "requirements-test.txt": requirements_parser,
        "requirements-prod.txt": requirements_parser,
        "dev-requirements.txt": requirements_parser,
        "environment.yml": yaml_parser,
        "environment.yaml": yaml_parser,
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
    }
