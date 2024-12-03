"""The 'Offline Mode' model handler runs the CLI without LLM API connection."""

from typing import Any

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler


class OfflineHandler(BaseModelHandler):
    """
    Offline Mode handler generates a README without LLM API connection.
    """

    def __init__(
        self, settings: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(settings, context)

    async def _model_settings(self) -> None: ...

    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """Builds request body for the LLM API request."""
        return {}

    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: Any,
    ) -> Any:
        """Inserts placeholder text where LLM generated content would be."""
        success = True
        if repo_files:
            files = [
                (file_path, self.placeholder) for file_path, _ in repo_files
            ]
            return success, files
        else:
            return success, self.placeholder
