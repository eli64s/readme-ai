"""Enable offline mode when no LLM API service is specified."""

from typing import List, Tuple

from readmeai.config.settings import AppConfig
from readmeai.core.logger import Logger
from readmeai.core.model import ModelHandler

logger = Logger(__name__)


class OfflineModeHandler(ModelHandler):
    """Offline model handler."""

    def __init__(self, config: AppConfig) -> None:
        """Initialize OpenAI API LLM."""
        self.config = config
        self._llm_settings()
        super().__init__(config)

    def _llm_settings(self):
        """Set default values for offline mode."""
        self.placeholder = self.config.md.default
        self.prompts = self.config.prompts

    async def _handle_response(
        self,
        index: str = None,
        prompt: str = None,
        tokens: int = None,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Use default placeholders when offline mode is enabled."""
        file_summaries = [
            (str(file_path), self.placeholder) for file_path, _ in raw_files
        ]
        return (
            file_summaries,
            self.placeholder,
            self.placeholder,
            self.placeholder,
        )
