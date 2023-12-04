"""Parser for gradle dependency files."""

import re
from typing import List

from readmeai.parsers.base_parser import FileParser

GRADLE_DECODE_ERROR = "Error decoding build.gradle content: {0}"


class BuildGradleParser(FileParser):
    """Parser for build.gradle dependency files."""

    def parse(self, content: str) -> List[str]:
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

        except re.error as error:
            self.log_error(GRADLE_DECODE_ERROR.format(error))
            return []


class BuildGradleKtsParser(FileParser):
    """Parser for build.gradle.kts dependency files."""

    def parse(self, content: str) -> List[str]:
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
            self.log_error(GRADLE_DECODE_ERROR.format(error))
            return []
