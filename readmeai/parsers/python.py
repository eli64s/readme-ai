"""Python dependency file parsers methods."""

import re
from typing import List

import toml
import yaml

from readmeai.parsers.base_parser import FileParser

TOM_DECODE_ERROR = "Error decoding TOML content: {0}"
TXT_DECODE_ERROR = "Error decoding TXT content: {0}"
YML_DECODE_ERROR = "Error decoding YAML content: {0}"


class RequirementsParser(FileParser):
    """Parser for requirements.txt files."""

    def parse(self, content: str) -> List[str]:
        """
        Extracts package names from a requirements.txt file.
        Excludes the version specifiers.
        """
        try:
            lines = content.splitlines()
            package_names = []
            for line in lines:
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                match = re.match(r"([a-zA-Z0-9\-_]+)", line)
                if match:
                    package_names.append(match.group(1))
            return package_names

        except re.error as error:
            self.log_error(TXT_DECODE_ERROR.format(error))

        return []


class TomlParser(FileParser):
    """
    Parser for Python TOML dependency files.
    Handles build systems like Pipenv, Poetry, and Flit.
    """

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a TOML file."""
        try:
            data = toml.loads(content)

            # For Pipfile
            if "packages" in data and "dev-packages" in data:
                packages = list(data.get("packages", {}).keys())
                dev_packages = list(data.get("dev-packages", {}).keys())
                return packages + dev_packages

            # For pyproject.toml (Poetry) and cargo.toml (Rust)
            elif "tool" in data and "poetry" in data["tool"]:
                poetry_data = data["tool"]["poetry"]
                dependencies = list(poetry_data.get("dependencies", {}).keys())
                if "dev-dependencies" in poetry_data:
                    dependencies.extend(
                        poetry_data.get("dev-dependencies", {}).keys()
                    )
                if "group" in poetry_data and "dev" in poetry_data["group"]:
                    poetry_data_dev = data["tool"]["poetry"]["group"]["dev"]
                    dependencies.extend(
                        poetry_data_dev.get("dependencies", {}).keys()
                    )
                return dependencies

            # For pyproject.toml (Flit)
            elif "project" in data and "dependencies" in data["project"]:
                dependencies = self.extract_package_names(
                    data["project"]["dependencies"]
                )
                if (
                    "project" in data
                    and "optional-dependencies" in data["project"]
                ):
                    for group_deps in data["project"][
                        "optional-dependencies"
                    ].values():
                        dependencies.extend(
                            self.extract_package_names(group_deps)
                        )
                return dependencies

        except toml.TomlDecodeError as error:
            self.log_error(TOM_DECODE_ERROR.format(error))
            return []

    def extract_package_names(self, dependencies: List[str]) -> List[str]:
        """Helper method to extract package names from dependency strings."""
        package_names = []
        for dep in dependencies:
            match = re.match(r"([a-zA-Z0-9\-_]+)", dep.split(";")[0].strip())
            if match:
                package_names.append(match.group(1))
        return package_names


class YamlParser(FileParser):
    """
    Parser for Python YAML based dependency files i.e. environment.yml
    """

    def parse(self, content: str) -> List[str]:
        """Extracts package names from environment.yml file."""
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and "dependencies" in data:
                dependencies = []
                for package in data["dependencies"]:
                    if isinstance(package, str):
                        dependencies.append(
                            package.split("=")[0].split(">")[0].split("<")[0]
                        )
                    elif isinstance(package, dict):
                        for pip_package in package.values():
                            if isinstance(pip_package, list):
                                for pip_dep in pip_package:
                                    dependencies.append(pip_dep.split("==")[0])
                return dependencies

        except yaml.YAMLError as error:
            self.log_error(YML_DECODE_ERROR.format(error))

        return []
