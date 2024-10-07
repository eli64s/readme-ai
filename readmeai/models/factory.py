from typing import ClassVar

from readmeai.config.constants import LLMService
from readmeai.config.settings import ConfigLoader
from readmeai.errors import UnsupportedServiceError
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.anthropic import AnthropicHandler
from readmeai.models.base import BaseModelHandler
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


class ModelFactory:
    """
    Factory class for creating LLM API handler instances.
    """

    _model_map: ClassVar[dict] = {
        LLMService.ANTHROPIC: AnthropicHandler,
        LLMService.GEMINI.value: GeminiHandler,
        LLMService.OLLAMA.value: OpenAIHandler,
        LLMService.OPENAI.value: OpenAIHandler,
        LLMService.OFFLINE.value: OfflineHandler,
    }

    @staticmethod
    def get_backend(
        config: ConfigLoader, context: RepositoryContext
    ) -> BaseModelHandler:
        """
        Returns the appropriate LLM API handler based on CLI input.
        """
        llm_service = ModelFactory._model_map.get(config.config.llm.api)

        if llm_service is None:
            raise UnsupportedServiceError(
                f"Unsupported LLM service provided: {config.config.llm.api}",
            )

        return llm_service(config, context)
