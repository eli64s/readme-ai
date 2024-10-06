"""
Parser for go.mod dependency files.
"""

import re

from readmeai.parsers.base import BaseFileParser


class GoModParser(BaseFileParser):
    """
    Parser for go.mod files.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Parse the content of a go.mod file."""
        try:
            lines = content.split("\n")
            pattern = r"^\s*([\w\.\-_/]+)\s+v[\w\.\-_/]+"
            regex = re.compile(pattern)
            package_names = (
                regex.match(line.strip()).group(1).split("/")[-1]
                for line in lines
                if regex.match(line.strip())
            )
            return list(package_names)

        except Exception as exc:
            return self.handle_parsing_error(f"go.mod: {exc!s}")
