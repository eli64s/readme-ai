"""The 'Offline Mode' model handler runs the CLI without LLM API connection."""

from typing import Any

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler


class OfflineHandler(BaseModelHandler):
    """
    OfflineMode model handler implementation.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)

    async def _model_settings(self) -> None: ...

    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """Builds the payload for the POST request to the LLM API."""
        return {}

    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: Any,
    ) -> Any:
        """Inserts placeholder text where the LLM API response would be."""
        files = [(file_path, self.placeholder) for file_path, _ in repo_files]
        return (files, self.placeholder, self.placeholder, self.placeholder)
