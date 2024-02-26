"""Parser for Docker (Dockerfile, docker-compose.yaml) configuration files."""

import re
from typing import List

import yaml

from readmeai.core.parsers import BaseFileParser


class DockerfileParser(BaseFileParser):
    """Parser for Dockerfile dependency files."""

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> List[str]:
        """Extracts package names from a Dockerfile."""
        try:
            dependencies = []
            lines = content.split("\n")
            for line in lines:
                if line.startswith("FROM"):
                    match = re.search(
                        r"FROM\s+(?:--platform=[^\s]+\s+)?([^\s:]+):?([^\s]*)",
                        line,
                    )
                    if match:
                        base_image, version = match.groups()
                        if not version:
                            version = "latest"
                        dependencies.append((base_image, version))

            return dependencies

        except re.error as exc:
            return self.handle_parsing_error(f"Dockerfile: {str(exc)}")


class DockerComposeParser(BaseFileParser):
    """Parser for Docker related files."""

    def parse(self, content: str) -> List[str]:
        """Parse docker-compose.yaml file and return a list of services."""
        try:
            data = yaml.safe_load(content)
            if isinstance(data, dict) and "services" in data:
                return list(data["services"].keys())

        except yaml.YAMLError as exc:
            return self.handle_parsing_error(f"Dockerfile: {str(exc)}")
