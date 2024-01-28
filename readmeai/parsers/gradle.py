"""Parser for gradle dependency files."""

import re
from typing import List

from readmeai.core.base_parser import FileParser


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

        except re.error as exc:
            return self.handle_parsing_error(f"build.gradle: {str(exc)}")


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
            return self.handle_parsing_error(f"build.gradle.kts: {str(error)}")
