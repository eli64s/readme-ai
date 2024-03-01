"""Utility methods for the readme-ai CLI application."""

from __future__ import annotations

import os
from enum import Enum

from readmeai.cli.options import ModelOptions as llms
from readmeai.core.logger import Logger

_logger = Logger(__name__)


class SecretKey(str, Enum):
    """
    Enum class to store the environment variable keys for the LLM API services.
    """

    OLLAMA_HOST = "OLLAMA_HOST"
    OPENAI_API_KEY = "OPENAI_API_KEY"
    VERTEXAI_LOCATION = "VERTEXAI_LOCATION"
    VERTEXAI_PROJECT = "VERTEXAI_PROJECT"


def _set_offline(message: str) -> tuple:
    """Set the LLM service to offline mode."""
    _logger.warning(f"{message}\n\t\t...Generating README without LLM API...")
    return llms.OFFLINE.name, llms.OFFLINE.name


def get_environment(llm_api: str, llm_model: str) -> tuple:
    """Set LLM environment variables based on the specified LLM service."""
    _log_message = "\n\t\t...{} settings NOT FOUND in environment..."

    if llm_api:
        _log_message = "{} settings FOUND in environment!"
        if llm_api == llms.OPENAI.name:
            if SecretKey.OPENAI_API_KEY.value in os.environ:
                _logger.info(_log_message.format("OpenAI"))
                return (
                    llms.OPENAI.name,
                    llm_model if llm_model is not None else "gpt-3.5-turbo",
                )
            else:
                return _set_offline(_log_message.format("OpenAI"))

        elif llm_api == llms.OLLAMA.name:
            if SecretKey.OLLAMA_HOST.value in os.environ:
                _logger.info(_log_message.format("Ollama"))
                return (
                    llms.OLLAMA.name,
                    llm_model if llm_model is not None else "mistral",
                )
            else:
                return _set_offline(_log_message.format("Ollama"))

        elif llm_api == llms.VERTEX.name:
            if (
                SecretKey.VERTEXAI_LOCATION.value in os.environ
                and SecretKey.VERTEXAI_PROJECT.value in os.environ
            ):
                _logger.info(_log_message.format("Goolge Cloud Vertex AI"))
                return (
                    llms.VERTEX.name,
                    llm_model if llm_model is not None else "gemini-1.0-pro",
                )

            else:
                return _set_offline(_log_message.format("Vertex AI"))

        elif llm_api == llms.OFFLINE.name:
            return _set_offline("\n\t\t...Offline mode enabled by user...")

    else:
        _log_message = "Running CLI with {} API llm engine..."
        _logger.warning(
            "NO LLM service provided to CLI. Checking environment."
        )

        if SecretKey.OPENAI_API_KEY.value in os.environ:
            _logger.info(_log_message.format("OpenAI"))
            return (
                llms.OPENAI.name,
                llm_model if llm_model is not None else "gpt-3.5-turbo",
            )

        elif SecretKey.OLLAMA_HOST.value in os.environ:
            _logger.info(_log_message.format("Ollama"))
            return (
                llms.OLLAMA.name,
                llm_model if llm_model is not None else "mistral",
            )
        elif (
            SecretKey.VERTEXAI_LOCATION.value in os.environ
            and SecretKey.VERTEXAI_PROJECT.value in os.environ
        ):
            _logger.info(_log_message.format("Vertex AI"))
            return (
                llms.VERTEX.name,
                llm_model if llm_model is not None else "gemini-1.0-pro",
            )

        else:
            if llm_api == llms.OFFLINE.name:
                message = "Offline mode enabled by user via CLI."
            else:
                message = (
                    "\n\n\t\t...No LLM API settings found in environment..."
                )
                return _set_offline(message)
