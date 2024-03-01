"""
Tests for the abstract base LLM API handler.
"""

import pytest

from readmeai._exceptions import UnsupportedServiceError
from readmeai.models.factory import model_handler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.models.vertex import VertexAIHandler


def test_model_handler_openai(openai_handler):
    """Test that the model handler returns the correct handler for OpenAI."""
    assert isinstance(openai_handler, OpenAIHandler)


def test_model_handler_vertex(vertex_handler):
    """Test model handler returns the correct handler for Vertex AI."""
    assert isinstance(vertex_handler, VertexAIHandler)


def test_model_handler_offline(offline_handler):
    """Test model handler returns the correct handler for offline mode."""
    assert isinstance(offline_handler, OfflineHandler)


def test_model_handler_unsupported_service(mock_config, mock_configs):
    """Test that model handler raises an error for an unsupported service."""
    mock_config.llm.api = "OpenAGI"
    mock_config.llm.model = "agi-turbo-3000"
    with pytest.raises(Exception) as exc:
        model_handler(mock_config, mock_configs)
        assert isinstance(exc.value, UnsupportedServiceError)
        assert str(exc.value) == "Unsupported service: OpenAGI"
