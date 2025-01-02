"""Parser for Docker (Dockerfile, docker-compose.yaml) configuration files."""

import re
from typing import Any

import yaml
from readmeai.parsers.base import BaseFileParser


class DockerfileParser(BaseFileParser):
    """
    Parser for Dockerfile dependency files.
    """

    def __init__(self) -> None:
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Extracts package names from a Dockerfile."""
        try:
            dependencies = []
            lines = content.split("\n")
            for line in lines:
                if match := re.search(
                    r"^FROM\s+(?:--platform=[^\s]+\s+)?([^\s:]+):?([^\s]*)",
                    line,
                ):
                    base_image, version = match.groups()
                    if not version:
                        version = "latest"
                    dependencies.append((base_image, version))

            return [f"{dep[0]}: {dep[1]}" for dep in dependencies]

        except re.error as e:
            return self.handle_parsing_error(e)


class DockerComposeParser(BaseFileParser):
    """
    Parser for docker-compose.yaml files.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()
        self.compose_data: dict[str, Any] = {}

    def parse(self, content: str) -> list[str]:
        """Parses docker-compose YAML content and returns dependency list."""
        try:
            self.compose_data = yaml.safe_load(content)
            return self.get_services()
        except yaml.YAMLError as e:
            return self.handle_parsing_error(e)

    def get_services(self) -> list[str]:
        """Get a list of all service names from the docker-compose.yaml file."""
        if self.compose_data is None:
            return []
        return list(self.compose_data.get("services", {}).keys())

    def get_service_info(self, service_name: str) -> dict[str, Any]:
        """Get detailed information for a specific service."""
        return self.compose_data.get("services", {}).get(service_name, {})

    def get_service_environment(self, service_name: str) -> list[str]:
        """Get the environment variables for a specific service."""
        service_info = self.get_service_info(service_name)
        return service_info.get("environment", [])

    def get_service_ports(self, service_name: str) -> list[str]:
        """Get the ports for a specific service."""
        service_info = self.get_service_info(service_name)
        return service_info.get("ports", [])

    def get_service_command(self, service_name: str) -> str:
        """Get the command for a specific service."""
        service_info = self.get_service_info(service_name)
        return service_info.get("command", "")

    def get_service_networks(self, service_name: str) -> list[str]:
        """Get the networks for a specific service."""
        service_info = self.get_service_info(service_name)
        return service_info.get("networks", [])

    def get_service_image(self, service_name: str) -> str:
        """Get the image used by a specific service."""
        service_info = self.get_service_info(service_name)
        return service_info.get("image", "")

    def get_all_service_details(self) -> list[dict[str, dict[str, Any]]]:
        """Get all metadata for all services."""
        return [
            {
                service_name: {
                    "image": self.get_service_image(service_name),
                    "environment": self.get_service_environment(service_name),
                    "ports": self.get_service_ports(service_name),
                    "command": self.get_service_command(service_name),
                    "networks": self.get_service_networks(service_name),
                    "details": self.get_service_info(service_name),
                }
                for service_name in self.get_services()
            }
        ]
