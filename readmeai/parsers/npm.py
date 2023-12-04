"""File for parsing json dependency files."""

import json
from typing import List

from readmeai.core import logger
from readmeai.parsers.base_parser import FileParser


class JsonParser(FileParser):
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

        except json.JSONDecodeError as excinfo:
            logger.error(f"Error parsing package.json: {str(excinfo)}")

        return []
