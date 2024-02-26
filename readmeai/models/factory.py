"""LLM registry to instantiate appropriate handler based on CLI input."""

from typing import Type

from readmeai.config.settings import ConfigLoader, Settings
from readmeai.core.models import BaseModelHandler
from readmeai.exceptions import UnsupportedServiceError
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.models.vertex import VertexAIHandler

MODEL_REGISTRY: dict[str, Type[BaseModelHandler]] = {
    "offline": OfflineHandler,
    "ollama": OpenAIHandler,
    "openai": OpenAIHandler,
    "vertex": VertexAIHandler,
}


def model_handler(
    config: Settings, config_loader: ConfigLoader
) -> BaseModelHandler:
    """Returns the instantiated LLM handler based on the CLI settings."""
    llm_service = config.llm.api.lower()
    llm_handler = MODEL_REGISTRY.get(llm_service)
    if llm_handler is None:
        raise UnsupportedServiceError(
            f"Unsupported LLM service provided: {llm_service}"
        )
    return llm_handler(config, config_loader)
