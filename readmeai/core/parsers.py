"""Abstract base class for dependency file parsers."""

from abc import ABC, abstractmethod
from typing import List

from readmeai.utils.logger import Logger


class BaseFileParser(ABC):
    """Abstract base class for dependency file parsers."""

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        self._logger = Logger(__name__)

    @abstractmethod
    def parse(self, content: str) -> List[str]:
        """Parses content of dependency file and returns list of dependencies."""
        ...

    def log_error(self, message: str):
        """Logs error message when parsing fails."""
        self._logger.error(f"Error parsing dependency file {message}")

    def handle_parsing_error(self, error: Exception) -> List[str]:
        """Standardized error handling for parsing exceptions."""
        self.log_error(str(error))
        return []
