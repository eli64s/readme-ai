"""Python dependency file parsers methods."""

import re
import sys

import yaml

from readmeai.parsers.base import BaseFileParser

if sys.version_info < (3, 11):
    import tomli as toml
else:
    import tomllib as toml


class RequirementsParser(BaseFileParser):
    """
    Parser for requirements.txt files.
    """

    def __init__(self) -> None:
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """
        Extracts package names from requirements.txt file.
        Excludes the version specifiers and comments.
        """
        try:
            lines = content.splitlines()
            package_names = []
            for line in lines:
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                if match := re.match(r"([a-zA-Z0-9\-_]+)", line):
                    package_names.append(match[1])
            return package_names

        except re.error as exc:
            return self.handle_parsing_error(f"requirements.txt: {exc!s}")


class TomlParser(BaseFileParser):
    """
    Parser for Python TOML dependency files.

    - Handles build systems:
        - Pipenv, Poetry, Flit, Hatch, etc.
    """

    def parse(self, content: str) -> list[str]:
        """Extracts all package dependencies from a TOML file."""
        try:
            data = toml.loads(content)
            dependencies = []

            # Look for dependencies in different possible sections
            # Pipfile-style
            if "packages" in data:
                dependencies.extend(data.get("packages", {}).keys())
            if "dev-packages" in data:
                dependencies.extend(data.get("dev-packages", {}).keys())

            # pyproject.toml-style (Poetry, Hatch, Flit)
            if "project" in data:
                dependencies.extend(
                    self.extract_package_names(
                        data["project"].get("dependencies", [])
                    )
                )
                if "optional-dependencies" in data["project"]:
                    for group_deps in data["project"][
                        "optional-dependencies"
                    ].values():
                        dependencies.extend(
                            self.extract_package_names(group_deps)
                        )

            # For build-system specific tools like Poetry
            if "tool" in data:
                if "poetry" in data["tool"]:
                    poetry_data = data["tool"]["poetry"]
                    dependencies.extend(
                        poetry_data.get("dependencies", {}).keys()
                    )

                    # Add dev-dependencies and any group dependencies
                    for group in ["dev-dependencies", "group"]:
                        if group in poetry_data:
                            group_data = poetry_data[group]
                            if isinstance(group_data, dict):
                                for section in group_data.values():
                                    dependencies.extend(
                                        section.get("dependencies", {}).keys()
                                    )

                if "hatch" in data["tool"]:
                    hatch_data = data["tool"]["hatch"].get("envs", {})
                    for env, env_data in hatch_data.items():
                        dependencies.extend(env_data.get("dependencies", []))
                        if "extra-dependencies" in env_data:
                            dependencies.extend(env_data["extra-dependencies"])

            # For Cargo.toml (Rust) style
            if "dependencies" in data:
                dependencies.extend(data.get("dependencies", {}).keys())
            if "dev-dependencies" in data:
                dependencies.extend(data.get("dev-dependencies", {}).keys())

            return list(set(dependencies))

        except Exception as exc:
            return self.handle_parsing_error(exc)

    def extract_package_names(self, dependencies: list[str]) -> list[str]:
        """Helper method to extract package names from a list of dependencies."""
        package_names = []
        for dep in dependencies:
            # Handle cases where dependencies might be in the format 'package_name>=1.0.0'
            if isinstance(dep, str):
                package_name = (
                    dep.split(">=")[0].split("<=")[0].split("==")[0].strip()
                )
                package_names.append(package_name)
            elif isinstance(dep, dict):
                package_names.extend(dep.keys())
        return package_names

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
            return self.handle_parsing_error(exc)
