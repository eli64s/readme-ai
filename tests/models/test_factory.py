"""
Tests for the abstract base LLM API handler.
"""

import pytest

from readmeai._exceptions import UnsupportedServiceError
from readmeai.models.factory import ModelRegistry
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


def test_model_handler_openai(openai_handler):
    """Test that the model handler returns the correct handler for OpenAI."""
    assert isinstance(openai_handler, OpenAIHandler)


def test_model_handler_gemini(gemini_handler):
    """Test model handler returns the correct handler for Gemini."""
    assert isinstance(gemini_handler, GeminiHandler)


def test_model_handler_offline(offline_handler):
    """Test model handler returns the correct handler for offline mode."""
    assert isinstance(offline_handler, OfflineHandler)


def test_model_handler_unsupported_service(mock_config, mock_configs):
    """Test that model handler raises an error for an unsupported service."""
    mock_config.llm.api = "OpenAGI"
    mock_config.llm.model = "agi-turbo-3000"
    with pytest.raises(Exception) as exc:
        ModelRegistry.get_backend(mock_config, mock_configs)
        assert isinstance(exc.value, UnsupportedServiceError)
        assert str(exc.value) == "Unsupported service: OpenAGI"
