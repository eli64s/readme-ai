"""
Parser for yarn.lock dependency files.
"""

import re

from readmeai.core.parsers import BaseFileParser


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
