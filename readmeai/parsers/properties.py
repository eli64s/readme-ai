"""
Parser for .properties configuration files.
"""

import re

from readmeai.core.parsers import BaseFileParser


class PropertiesParser(BaseFileParser):
    """
    Parser for .properties files.
    """

    def parse(self, content: str) -> list[str]:
        """Parse the content of a .properties file."""
        names = []

        # Extracting jdbc connection strings
        regex = r"jdbc:(\w+)://"
        match = re.search(regex, content)
        if match:
            names.append(match.group(1))

        # Other packages
        regex = r"(?P<name>[\w.]+)[\s]*="
        for match in re.finditer(regex, content):
            names.append(match.group("name"))

        return names
