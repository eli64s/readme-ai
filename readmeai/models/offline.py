"""Enable offline mode when no LLM API service is specified."""

from typing import List, Tuple

from readmeai.config.settings import ConfigLoader, Settings
from readmeai.core.models import BaseModelHandler


class OfflineHandler(BaseModelHandler):
    """Offline model handler."""

    def __init__(self, config: Settings, config_loader: ConfigLoader) -> None:
        """Initialize OpenAI API LLM."""
        super().__init__(config, config_loader)
        self._llm_settings()

    def _llm_settings(self):
        """Set default values for offline mode."""
        self.placeholder = self.config.md.placeholder

    async def _handle_response(
        self,
        index: str = None,
        prompt: str = None,
        tokens: int = None,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Use default placeholders when offline mode is enabled."""
        self._logger.info("Running offline mode handler module...")

        file_summaries = [
            (str(file_path), self.placeholder) for file_path, _ in raw_files
        ]
        return (
            file_summaries,
            self.placeholder,
            self.placeholder,
            self.placeholder,
            self.placeholder,
        )
