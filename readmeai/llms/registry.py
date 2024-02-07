"""Model factory to return the appropriate LLM implementation module."""

from readmeai.config.settings import AppConfig
from readmeai.exceptions import UnsupportedServiceError
from readmeai.llms.offline import OfflineModeHandler
from readmeai.llms.openai import OpenAIHandler
from readmeai.llms.vertex import VertexAIHandler

MODEL_REGISTRY = {
    "offline": OfflineModeHandler,
    "openai": OpenAIHandler,
    "vertex": VertexAIHandler,
}


def model_handler(config: AppConfig) -> MODEL_REGISTRY:
    """Returns the appropriate LLM implementation."""
    llm_service = config.llm.api.lower()
    llm_module = MODEL_REGISTRY.get(llm_service)
    if not llm_module:
        raise UnsupportedServiceError(
            llm_service, f"LLM API service settings: {config.llm.api}"
        )
    return llm_module(config)
