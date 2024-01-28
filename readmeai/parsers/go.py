"""Parse package dependencies from go.mod files."""

import re
from typing import List

from readmeai.core.base_parser import FileParser


class GoModParser(FileParser):
    """Parser for go.mod files."""

    def parse(self, content: str) -> List[str]:
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
            return self.handle_parsing_error(f"go.mod: {str(exc)}")
