"""
Python dependency file parsers methods.
"""

import re
import sys

import yaml

from readmeai.core.parsers import BaseFileParser

if sys.version_info < (3, 11):
    import tomli as toml
else:
    import tomllib as toml


class RequirementsParser(BaseFileParser):
    """
    Parser for requirements.txt files.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
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

        except re.error as exc:
            return self.handle_parsing_error(f"requirements.txt: {exc!s}")


class TomlParser(BaseFileParser):
    """
    Parser for Python TOML dependency files.
    Handles build systems like Pipenv, Poetry, and Flit.
    """

    def parse(self, content: str) -> list[str]:
        """Extracts package names from a TOML file."""
        try:
            data = toml.loads(content)

            # For Pipfile
            if "packages" in data and "dev-packages" in data:
                packages = list(data.get("packages", {}).keys())
                dev_packages = list(data.get("dev-packages", {}).keys())
                return packages + dev_packages

            # For pyproject.toml (Poetry) and cargo.toml (Rust)
            if "tool" in data and "poetry" in data["tool"]:
                poetry_data = data["tool"]["poetry"]
                dependencies = list(poetry_data.get("dependencies", {}).keys())

                if "dev-dependencies" in poetry_data:
                    dependencies.extend(
                        poetry_data.get("dev-dependencies", {}).keys(),
                    )

                if "group" in poetry_data and "dev" in poetry_data["group"]:
                    poetry_data_dev = data["tool"]["poetry"]["group"]["dev"]
                    dependencies.extend(
                        poetry_data_dev.get("dependencies", {}).keys(),
                    )

                if "group" in poetry_data and "test" in poetry_data["group"]:
                    poetry_data_main = data["tool"]["poetry"]["group"]["test"]
                    dependencies.extend(
                        poetry_data_main.get("dependencies", {}).keys(),
                    )

                if "group" in poetry_data and "docs" in poetry_data["group"]:
                    poetry_data_main = data["tool"]["poetry"]["group"]["docs"]
                    dependencies.extend(
                        poetry_data_main.get("dependencies", {}).keys(),
                    )

                return dependencies

            # For pyproject.toml (Flit)
            elif "project" in data and "dependencies" in data["project"]:
                dependencies = self.extract_package_names(
                    data["project"]["dependencies"],
                )
                if (
                    "project" in data
                    and "optional-dependencies" in data["project"]
                ):
                    for group_deps in data["project"][
                        "optional-dependencies"
                    ].values():
                        dependencies.extend(
                            self.extract_package_names(group_deps),
                        )
            else:
                dependencies = []

            return dependencies

        except Exception as exc:
            return self.handle_parsing_error(f"pyproject.toml: {exc!s}")

    def extract_package_names(self, dependencies: list[str]) -> list[str]:
        """Helper method to extract package names from dependency strings."""
        package_names = []
        for dep in dependencies:
            match = re.match(r"([a-zA-Z0-9\-_]+)", dep.split(";")[0].strip())
            if match:
                package_names.append(match.group(1))
        return package_names


class YamlParser(BaseFileParser):
    """
    Parser for Python YAML based dependency files i.e. environment.yml
    """

    def parse(self, content: str) -> list[str]:
        """Extracts package names from environment.yml file."""
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and "dependencies" in data:
                dependencies = []
                for package in data["dependencies"]:
                    if isinstance(package, str):
                        dependencies.append(
                            package.split("=")[0].split(">")[0].split("<")[0],
                        )
                    elif isinstance(package, dict):
                        for pip_package in package.values():
                            if isinstance(pip_package, list):
                                for pip_dep in pip_package:
                                    dependencies.append(pip_dep.split("==")[0])
                return dependencies

        except yaml.YAMLError as exc:
            return self.handle_parsing_error(
                f"conda environment.yml: {exc!s}",
            )
