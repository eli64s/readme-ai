from abc import ABC, abstractmethod
from typing import Any


class BaseTemplate(ABC):
    """
    Base class for all templates.
    """

    @abstractmethod
    def render(self, data: dict[str, Any]) -> str:
        """
        Render the template with the given data.

        Args:
            data (Dict[str, Any]): The data to use for rendering the template.

        Returns:
            str: The rendered template as a string.
        """
        ...

    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """
        Sanitize input string to prevent XSS attacks.

        Args:
            input_str (str): The input string to sanitize.

        Returns:
            str: The sanitized string.
        """
        return input_str.replace("<", "&lt;").replace(">", "&gt;")
