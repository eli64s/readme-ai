"""
Parser for gradle dependency files.
"""

import re

from readmeai.parsers.base import BaseFileParser


class BuildGradleParser(BaseFileParser):
    """
    Parser for build.gradle dependency files.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Extracts package names from a build.gradle file."""
        try:
            pattern = r"(implementation|classpath|api|testImplementation|androidTestImplementation|kapt)\s+['\"]([^'\"]+)['\"]"
            matches = re.findall(pattern, content)
            package_names = set()
            for _, dependency in matches:
                parts = dependency.split(":")
                for part in parts:
                    part = part.split(".")
                    for p in part:
                        if p.isalpha():
                            package_names.add(p)

            return list(package_names)

        except re.error as exc:
            return self.handle_parsing_error(f"build.gradle: {exc!s}")


class BuildGradleKtsParser(BaseFileParser):
    """
    Parser for build.gradle.kts dependency files.
    """

    def parse(self, content: str) -> list[str]:
        """Extracts package names from a build.gradle.kts file."""
        try:
            pattern = r"(\bimplementation|testImplementation)\s*\((['\"])([^'\"]+)\2\)"
            matches = re.findall(pattern, content)
            package_names = set()
            for _, _, dependency in matches:
                parts = dependency.split(":")
                for part in parts:
                    part = part.split(".")
                    for p in part:
                        if p.isalpha():
                            package_names.add(p)
            return list(package_names)

        except re.error as error:
            return self.handle_parsing_error(f"build.gradle.kts: {error!s}")
