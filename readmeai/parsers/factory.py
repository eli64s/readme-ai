"""Abstract factory for all dependency file parsers."""

from typing import Dict

from readmeai.parsers.base_parser import FileParser
from readmeai.parsers.gomod import GoModParser
from readmeai.parsers.gradle import BuildGradleKtsParser, BuildGradleParser
from readmeai.parsers.maven import MavenParser
from readmeai.parsers.npm import JsonParser
from readmeai.parsers.python import RequirementsParser, TomlParser, YamlParser
from readmeai.parsers.rust import CargoTomlParser


def parser_factory() -> Dict[str, FileParser]:
    """Returns a dictionary of callable file parser methods."""
    return {
        "build.gradle": BuildGradleParser(),
        "build.gradle.kts": BuildGradleKtsParser(),
        "cargo.toml": CargoTomlParser(),
        "go.mod": GoModParser(),
        "package.json": JsonParser(),
        "environment.yml": YamlParser(),
        "environment.yaml": YamlParser(),
        "Pipfile": TomlParser(),
        "pyproject.toml": TomlParser(),
        "requirements.txt": RequirementsParser(),
        "requirements-dev.txt": RequirementsParser(),
        "pom.xml": MavenParser(),
    }
    """
    "yarn.lock": parse_yarn_lock,
    "CMakeLists.txt": parse_cmake,
    "Makefile.am": parse_makefile_am,
    "configure.ac": parse_configure_ac,

    def parse_yarn_lock(content: str) -> List[str]:
        try:
            return re.findall(r"(\S+)(?=@)", content)
        except re.error as excinfo:
            logger.error(f"Error parsing yarn.lock: {str(excinfo)}")
        return []


    def parse_cmake(content: str) -> List[str]:
        regex = re.compile(r"add_executable\([^)]+\s+([^)]+)\)")
        package_names = regex.findall(content)
        return package_names


    def parse_configure_ac(content: str) -> List[str]:
        regex = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
        package_names = regex.findall(content)
        return package_names


    def parse_makefile_am(content: str) -> List[str]:
        regex = re.compile(r"bin_PROGRAMS\s*=\s*(.+)")
        package_names = []
        matches = regex.findall(content)
        for match in matches:
            deps = filter(None, match.split())
            package_names.extend(deps)
        return package_names
    """
