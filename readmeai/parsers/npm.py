"""File for parsing json dependency files."""

import json
import re
from typing import List

from readmeai.core.logger import Logger
from readmeai.parsers.base_parser import FileParser

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

        except json.JSONDecodeError as exc_info:
            logger.error(f"Error parsing package.json: {str(exc_info)}")

        return []


class YarnLockParser(FileParser):
    """Parser for yarn.lock dependency files."""

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a yarn.lock file."""
        try:
            return re.findall(r"(\S+)(?=@)", content)
        except re.error as exc_info:
            self.log_error(f"Error parsing yarn.lock: {str(exc_info)}")
            return []
