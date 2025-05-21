"""
Parser utilities for Java-based dependency files.
"""

import re

from readmeai.parsers.base import BaseFileParser


class MavenParser(BaseFileParser):
    """
    Parser for Maven dependency files in pom.xml format.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Extract packages names from Maven pom.xml files."""
        try:
            regex = re.compile(
                r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>",
            )
            matches = regex.findall(content)
            dependencies = [
                artifact_id for group_id, artifact_id, version in matches
            ]
            if any("spring" in dependency for dependency in dependencies):
                dependencies.append("spring")
            return set(dependencies)

        except re.error as exc:
            return self.handle_parsing_error(f"pom.xml: {exc!s}")
