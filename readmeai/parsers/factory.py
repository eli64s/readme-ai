"""Abstract factory for all dependency file parsers."""

from typing import Dict

from readmeai.parsers.base_parser import FileParser
from readmeai.parsers.cmake import (
    CMakeParser,
    ConfigureAcParser,
    MakefileAmParser,
)
from readmeai.parsers.go import GoModParser
from readmeai.parsers.gradle import BuildGradleKtsParser, BuildGradleParser
from readmeai.parsers.maven import MavenParser
from readmeai.parsers.npm import PackageJsonParser, YarnLockParser
from readmeai.parsers.python import RequirementsParser, TomlParser, YamlParser
from readmeai.parsers.rust import CargoTomlParser


def parser_factory() -> Dict[str, FileParser]:
    """Returns a dictionary of callable file parser methods."""
    yaml_parser = YamlParser()
    toml_parser = TomlParser()
    requirements_parser = RequirementsParser()

    return {
        "build.gradle": BuildGradleParser(),
        "build.gradle.kts": BuildGradleKtsParser(),
        "cargo.toml": CargoTomlParser(),
        "go.mod": GoModParser(),
        "environment.yml": yaml_parser,
        "environment.yaml": yaml_parser,
        "Pipfile": toml_parser,
        "pyproject.toml": toml_parser,
        "pom.xml": MavenParser(),
        "requirements.in": requirements_parser,
        "requirements.txt": requirements_parser,
        "requirements-dev.txt": requirements_parser,
        "requirements-test.txt": requirements_parser,
        "requirements-prod.txt": requirements_parser,
        "dev-requirements.txt": requirements_parser,
        "cmakeLists.txt": CMakeParser(),
        "configure.ac": ConfigureAcParser(),
        "Makefile.am": MakefileAmParser(),
        "package.json": PackageJsonParser(),
        "yarn.lock": YarnLockParser(),
    }
