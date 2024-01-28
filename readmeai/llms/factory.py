"""Model handler factory for selecting the appropriate LLM implementation."""

from readmeai.config.settings import AppConfig
from readmeai.llms.openai import OpenAIHandler
from readmeai.llms.vertex import VertexAIHandler

LLM_HANDLER_FACTORY = {
    "openai": OpenAIHandler,
    "vertex": VertexAIHandler,
}


def llm_handler(config: AppConfig) -> LLM_HANDLER_FACTORY:
    """Returns the appropriate LLM implementation."""
    service = config.llm.service
    handler_class = LLM_HANDLER_FACTORY.get(service)

    if not handler_class:
        raise ValueError(f"Unsupported LLM service provided: {service}")

    return handler_class(config)
