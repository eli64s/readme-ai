"""
Model handler for running the CLI without a LLM API service.
"""

from typing import Any

from readmeai.config.settings import ConfigLoader
from readmeai.core.models import BaseModelHandler


class OfflineHandler(BaseModelHandler):
    """Offline model handler, used when no LLM API is provided."""

    def __init__(self, config_loader: ConfigLoader) -> None:
        """Initialize the OfflineHandler class."""
        super().__init__(config_loader)
        self._model_settings()

    def _model_settings(self):
        """Set default values for offline mode."""
        self.placeholder: str = self.config.md.placeholder

    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """Builds the payload for the POST request to the LLM API."""
        return {}

    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        raw_files: list[tuple[str, str]] | None,
    ) -> list[tuple[str, str]]:
        """
        Returns placeholder text where LLM API response would be.
        """
        file_summaries = [
            (str(file_path), self.placeholder) for file_path, _ in raw_files
        ]
        return (
            file_summaries,
            self.placeholder,
            self.placeholder,
            self.placeholder,
        )
