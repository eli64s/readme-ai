"""Parsers for npm related dependency files i.e. package.json"""

import json

from readmeai.parsers.base import BaseFileParser


class PackageJsonParser(BaseFileParser):
    """
    Parser for package.json dependency files.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Returns a list of dependencies parsed from a json file."""
        try:
            data = json.loads(content)
            package_names = []
            for section in [
                "dependencies",
                "devDependencies",
                "peerDependencies",
            ]:
                if section in data:
                    package_names.extend(data[section].keys())
            return package_names

        except json.JSONDecodeError as exc:
            return self.handle_parsing_error(exc)
