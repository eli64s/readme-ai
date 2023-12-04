"""Parser utilities for Java-based dependency files."""

import re
from typing import List

from readmeai.parsers.base_parser import FileParser

XML_DECODE_ERROR = "Error decoding XML content: {0}"


class MavenParser(FileParser):
    """
    Parser for Maven dependency files in pom.xml format.
    """

    def parse(self, content: str) -> List[str]:
        """Extract packages names from Maven pom.xml files."""
        try:
            regex = re.compile(
                r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>"
            )
            matches = regex.findall(content)
            dependencies = [
                artifact_id for group_id, artifact_id, version in matches
            ]
            if any("spring" in dependency for dependency in dependencies):
                dependencies.append("spring")
            return set(dependencies)

        except Exception as error:
            self.log_error(XML_DECODE_ERROR.format(error))
            return []
