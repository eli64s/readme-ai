"""
Utility methods to configure the LLM API environments.
"""

import os
from enum import Enum

from readmeai.config.settings import ModelOptions as llms
from readmeai.core.logger import Logger

_logger = Logger(__name__)


class SecretKey(str, Enum):
    """
    Enum class to store the environment variable keys for the LLM API services.
    """

    # ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"
    GOOGLE_API_KEY = "GOOGLE_API_KEY"
    OLLAMA_HOST = "OLLAMA_HOST"
    OPENAI_API_KEY = "OPENAI_API_KEY"


def _set_offline(message: str) -> tuple:
    """Set the LLM service to offline mode."""
    _logger.warning(
        f"{message}\n\t\n... readme-ai engine switched to offline mode ...\n",
    )
    return llms.OFFLINE.name, llms.OFFLINE.name


def get_environment(llm_api: str = "", llm_model: str = "") -> tuple:
    """Set LLM environment variables based on the specified LLM service."""
    default_models = {
        # llms.ANTHROPIC.name: "claude-3-5-sonnet",
        llms.GEMINI.name: "gemini-1.5-flash",
        llms.OLLAMA.name: "mistral",
        llms.OPENAI.name: "gpt-3.5-turbo",
    }

    env_keys = {
        # llms.ANTHROPIC.name: SecretKey.ANTHROPIC_API_KEY.value,
        llms.GEMINI.name: SecretKey.GOOGLE_API_KEY.value,
        llms.OLLAMA.name: SecretKey.OLLAMA_HOST.value,
        llms.OPENAI.name: SecretKey.OPENAI_API_KEY.value,
    }

    if llm_api and llm_api not in env_keys:
        if llm_api == llms.OFFLINE.name:
            return _set_offline("\n\n\t\t\t\tOffline mode enabled by user")
        _logger.warning("Invalid LLM service provided to CLI.")
        return _set_offline(
            "\n\n\t...No LLM API settings found in environment...",
        )

    # If OPENAI_API_KEY does not exist in env when --api OPENAI is set
    if (
        llm_api == llms.OPENAI.name
        and SecretKey.OPENAI_API_KEY.value not in os.environ
    ):
        return _set_offline(
            "OPENAI_API_KEY not found in environment. Switching to offline mode.",
        )

    # If GOOGLE_API_KEY does not exist in env when --api gemini is set
    if (
        llm_api == llms.GEMINI.name
        and SecretKey.GOOGLE_API_KEY.value not in os.environ
    ):
        return _set_offline(
            "GOOGLE_API_KEY not found in environment. Switching to offline mode.",
        )

    # If no specific API is provided or the provided API is valid
    for api_name, env_key in env_keys.items():
        if llm_api == api_name or (not llm_api and env_key in os.environ):
            model = llm_model if llm_model else default_models[api_name]
            _logger.info(f"{api_name} settings FOUND in environment!")
            return api_name, model

    # If no environment variables are found or OFFLINE is explicitly set
    if llm_api == llms.OFFLINE.name:
        return _set_offline("Offline mode enabled by user via CLI.")
    return _set_offline(
        "\n\n... No LLM API settings found in environment ...",
    )
