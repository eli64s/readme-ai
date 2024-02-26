"""Parser for yarn.lock dependency files."""

import re
from typing import List

from readmeai.core.parsers import BaseFileParser


class YarnLockParser(BaseFileParser):
    """Parser for yarn.lock dependency files."""

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a yarn.lock file."""
        try:
            return re.findall(r"(\S+)(?=@)", content)
        except re.error as exc:
            return self.handle_parsing_error(f"yarn.lock: {str(exc)}")
