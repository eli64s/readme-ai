"""File for parsing json dependency files."""

import json
import re
from typing import List

from readmeai.core.base_parser import FileParser
from readmeai.core.logger import Logger

logger = Logger(__name__)


class PackageJsonParser(FileParser):
    def parse(self, content: str) -> List[str]:
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
            return self.handle_parsing_error(f"package.json: {str(exc)}")


class YarnLockParser(FileParser):
    """Parser for yarn.lock dependency files."""

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a yarn.lock file."""
        try:
            return re.findall(r"(\S+)(?=@)", content)
        except re.error as exc:
            return self.handle_parsing_error(f"yarn.lock: {str(exc)}")
