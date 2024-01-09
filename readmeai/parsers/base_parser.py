"""Abstract base class for all dependency file parsers."""

from abc import ABC, abstractmethod
from typing import List

from readmeai.core.logger import Logger

logger = Logger(__name__)


class FileParser(ABC):
    """Base class for all dependency file parsers."""

    @abstractmethod
    def parse(self, content: str) -> List[str]:
        """Extracts package names from dependency files."""
        pass

    def log_error(self, message):
        """Logs error message when parsing fails."""
        logger.error(f"Exception occurred while parsing file: {message}")
