"""Dependency parser for Docker files."""

from typing import List

import yaml

from readmeai.parsers.base_parser import FileParser

YML_DECODE_ERROR = "Error decoding YAML content: {0}"


class DockerParser(FileParser):
    """Parser for Docker related files."""

    def parse(self, content: str) -> List[str]:
        """Parse docker-compose.yaml file and return a list of services."""
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and "services" in data:
                return list(data["services"].keys())

        except yaml.YAMLError as error:
            self.logger.error(YML_DECODE_ERROR.format(error))

        return []
