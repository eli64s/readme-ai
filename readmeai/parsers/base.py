from abc import ABC, abstractmethod

from readmeai.core.logger import get_logger


class BaseFileParser(ABC):
    """
    Abstract base class for dependency file parsers.
    """

    def __init__(self) -> None:
        self._logger = get_logger(__name__)

    @abstractmethod
    def parse(self, content: str) -> list[str]:
        """Parses content of file and return list of dependencies."""
        ...

    def log_error(self, message: str):
        """Logs error message when parsing fails."""
        self._logger.error(f"Error parsing dependency file {message}")

    def handle_parsing_error(self, error: Exception) -> list[str]:
        """Standardized error handling for parsing exceptions."""
        self.log_error(repr(error))
        return []


class DefaultParser(BaseFileParser):
    """
    Default parser for unknown file types.
    """

    def __init__(self) -> None:
        """Initializes the handler with given configuration."""
        super().__init__()

    def parse(self, content: str) -> list[str]:
        """Returns an empty list for unknown file types."""
        return []
