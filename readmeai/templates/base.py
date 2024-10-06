from abc import ABC, abstractmethod
from typing import Any


class BaseTemplate(ABC):
    """
    Abstract base class for all Markdown templates.
    """

    @abstractmethod
    def render(self, data: dict[str, Any]) -> str: ...
