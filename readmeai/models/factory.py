from typing import ClassVar

from readmeai.config.settings import ConfigLoader
from readmeai.core.errors import UnsupportedServiceError
from readmeai.extractors.models import RepositoryContext
from readmeai.models.anthropic import AnthropicHandler
from readmeai.models.base import BaseModelHandler
from readmeai.models.enums import LLMProviders
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


class ModelFactory:
    """
    Factory class for creating LLM API handler instances.
    """

    _model_map: ClassVar[dict] = {
        LLMProviders.ANTHROPIC: AnthropicHandler,
        LLMProviders.GEMINI.value: GeminiHandler,
        LLMProviders.OLLAMA.value: OpenAIHandler,
        LLMProviders.OPENAI.value: OpenAIHandler,
        LLMProviders.OFFLINE.value: OfflineHandler,
    }

    @staticmethod
    def get_backend(
        config: ConfigLoader, context: RepositoryContext
    ) -> BaseModelHandler:
        """Retrieves configured LLM API handler instance."""
        llm_service = ModelFactory._model_map.get(config.config.llm.api)

        if llm_service is None:
            raise UnsupportedServiceError(
                f"Unsupported LLM provider: {config.config.llm.api}"
            )

        return llm_service(config, context)
