"""
Model factory that returns the appropriate LLM handler based on CLI input.
"""

from readmeai._exceptions import UnsupportedServiceError
from readmeai.cli.options import ModelOptions as llms
from readmeai.config.settings import ConfigLoader
from readmeai.core.models import BaseModelHandler
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


class ModelFactory:
    """Factory that returns the appropriate LLM handler based on CLI input."""

    _model_map = {
        llms.OFFLINE.value: OfflineHandler,
        llms.OLLAMA.value: OpenAIHandler,
        llms.OPENAI.value: OpenAIHandler,
        llms.GEMINI.value: GeminiHandler,
    }

    @staticmethod
    def model_handler(conf: ConfigLoader) -> BaseModelHandler:
        """Returns the appropriate LLM API handler based on CLI input."""
        llm_handler = ModelFactory._model_map.get(conf.config.llm.api)
        if llm_handler is None:
            raise UnsupportedServiceError(
                f"Unsupported LLM service provided: {conf.config.llm.api}"
            )
        return llm_handler(conf)
