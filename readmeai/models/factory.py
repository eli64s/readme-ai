"""
Factory class that selects appropriate LLM API service based on CLI input.
"""

from typing import ClassVar

from readmeai._exceptions import UnsupportedServiceError
from readmeai.config.settings import ConfigLoader, ModelOptions
from readmeai.core.models import BaseModelHandler
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


class ModelRegistry:
    """
    Returns the appropriate LLM API handler based on CLI input.
    """

    _model_map: ClassVar[dict] = {
        # ModelOptions.ANTHROPIC.value: AnthropicHandler,
        ModelOptions.GEMINI.value: GeminiHandler,
        ModelOptions.OFFLINE.value: OfflineHandler,
        ModelOptions.OLLAMA.value: OpenAIHandler,
        ModelOptions.OPENAI.value: OpenAIHandler,
    }

    @staticmethod
    def get_backend(conf: ConfigLoader) -> BaseModelHandler:
        """
        Returns the appropriate LLM API handler based on CLI input.
        """
        backend_service = ModelRegistry._model_map.get(conf.config.llm.api)
        if backend_service is None:
            raise UnsupportedServiceError(
                f"Unsupported LLM service provided: {conf.config.llm.api}",
            )
        return backend_service(conf)
