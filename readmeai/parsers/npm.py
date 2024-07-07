"""
Parsers for npm related dependency files.
"""

import json
import re

from readmeai.core.parsers import BaseFileParser


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
            return self.handle_parsing_error(f"package.json: {exc!s}")


class YarnLockParser(BaseFileParser):
    """
    Parser for yarn.lock dependency files.
    """

    def parse(self, content: str) -> list[str]:
        """Extracts package names from a yarn.lock file."""
        try:
            return re.findall(r"(\S+)(?=@)", content)
        except re.error as exc:
            return self.handle_parsing_error(f"yarn.lock: {exc!s}")
