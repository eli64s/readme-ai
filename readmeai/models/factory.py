"""
Model factory that returns the appropriate LLM handler based on CLI input.
"""

from readmeai._exceptions import UnsupportedServiceError
from readmeai.cli.options import ModelOptions as llms
from readmeai.config.settings import ConfigLoader
from readmeai.core.models import BaseModelHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.models.vertex import VertexAIHandler

MODEL_REGISTRY: dict[str, BaseModelHandler] = {
    llms.OFFLINE.name: OfflineHandler,
    llms.OLLAMA.name: OpenAIHandler,
    llms.OPENAI.name: OpenAIHandler,
    llms.VERTEX.name: VertexAIHandler,
}


def model_handler(conf: ConfigLoader) -> BaseModelHandler:
    """Registry that returns the appropriate LLM handler based on CLI input."""
    llm_handler = MODEL_REGISTRY.get(conf.config.llm.api)

    if llm_handler is None:
        raise UnsupportedServiceError(
            f"Unsupported LLM service provided: {conf.config.llm.api}"
        )

    return llm_handler(conf)
