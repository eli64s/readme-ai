"""Factory class to handle file I/O operations."""

import json
from pathlib import Path
from typing import Any, Callable, Dict, Union

import toml
import yaml


class ReadFileException(Exception):
    """Exception raised when a file cannot be read."""


class WriteFileException(Exception):
    """Exception raised when a file cannot be written."""


class FileHandler:
    """Factory class to handle file I/O operations."""

    def __init__(self):
        """Initialize the file handler."""
        self.file_actions: Dict[str, Dict[str, Callable[[str], Any]]] = {
            "json": {"read": self.read_json, "write": self.write_json},
            "md": {"read": self.read_markdown, "write": self.write_markdown},
            "toml": {"read": self.read_toml, "write": self.write_toml},
            "txt": {"read": self.read_text, "write": self.write_text},
            "yaml": {"read": self.read_yaml, "write": self.write_yaml},
        }
        self.cache = {}

    def read(self, file_path: Union[str, Path]) -> Any:
        """Read the content of a file."""
        if file_path in self.cache:
            return self.cache[file_path]

        try:
            file_extension = str(file_path).rsplit(".", maxsplit=1)[-1]
            reader = self.get_action(file_extension, "read")
            content = reader(file_path)
            self.cache[file_path] = content
            return content
        except Exception as excinfo:
            raise ReadFileException(
                f"Exception: failed to read file {file_path}: {excinfo}"
            )

    def write(self, file_path: Union[str, Path], content: Any) -> None:
        """Write the content to a file."""
        try:
            file_extension = str(file_path).rsplit(".", maxsplit=1)[-1]
            writer = self.get_action(file_extension, "write")
            writer(file_path, content)
        except Exception as excinfo:
            raise WriteFileException(
                f"Exception: failed to write file {file_path}: {excinfo}"
            )

    def get_action(
        self, file_extension: str, action_type: str
    ) -> Callable[[str], Any]:
        """Get method for the passed file extension and I/O operation."""
        file_actions = self.file_actions.get(file_extension)
        if not file_actions:
            raise ValueError(f"Unsupported file type: {file_extension}")

        action = file_actions.get(action_type)
        if not action:
            raise ValueError(f"Unsupported action type: {action_type}")

        return action

    @staticmethod
    def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:
        """Read the content of a JSON file."""
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def read_markdown(file_path: Union[str, Path]) -> str:
        """Read the content of a Markdown file."""
        with open(file_path, encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def read_toml(file_path: Union[str, Path]) -> Dict[str, Any]:
        """Read the content of a TOML file."""
        with open(file_path, encoding="utf-8") as file:
            data = toml.load(file)
        data_cleaned = {key.lower(): value for key, value in data.items()}
        return data_cleaned

    @staticmethod
    def read_text(file_path: Union[str, Path]) -> str:
        """Read the content of a TXT file."""
        with open(file_path, encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def read_yaml(file_path: Union[str, Path]) -> Dict[str, Any]:
        """Read the content of a YAML file."""
        with open(file_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    @staticmethod
    def write_json(
        file_path: Union[str, Path], content: Dict[str, Any]
    ) -> None:
        """Write the content to a JSON file."""
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(content, file, indent=4)

    @staticmethod
    def write_markdown(file_path: Union[str, Path], content: str) -> None:
        """Write the content to a Markdown file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def write_toml(
        file_path: Union[str, Path], content: Dict[str, Any]
    ) -> None:
        """Write the content to a TOML file."""
        with open(file_path, "w", encoding="utf-8") as file:
            toml.dump(content, file)

    @staticmethod
    def write_text(file_path: Union[str, Path], content: str) -> None:
        """Write the content to a TXT file."""
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def write_yaml(
        file_path: Union[str, Path], content: Dict[str, Any]
    ) -> None:
        """Write the content to a YAML file."""
        with open(file_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(content, file)
