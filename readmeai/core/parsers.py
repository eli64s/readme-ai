"""
Abstract base class for dependency file parsers.
"""

from abc import ABC, abstractmethod

from readmeai.core.logger import Logger


class BaseFileParser(ABC):
    """
    Abstract base class for dependency file parsers.
    """

    def __init__(self) -> None:
        self._logger = Logger(__name__)

    @abstractmethod
    def parse(self, content: str) -> list[str]:
        """Parses content of file and return list of dependencies."""
        ...

    def log_error(self, message: str):
        """Logs error message when parsing fails."""
        self._logger.error(f"Error parsing dependency file {message}")

    def handle_parsing_error(self, error: Exception) -> list[str]:
        """Standardized error handling for parsing exceptions."""
        self.log_error(str(error))
        return []
