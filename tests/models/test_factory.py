"""Tests for the abstract base LLM API handler."""

from unittest.mock import patch

import pytest

from readmeai.config.enums import ModelOptions
from readmeai.exceptions import UnsupportedServiceError
from readmeai.models.factory import model_handler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.models.vertex import VertexAIHandler


@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
def test_model_handler_openai(mock_config, mock_configs):
    """Test that the model handler returns the correct handler for OpenAI."""
    # Arrange
    mock_config.llm.api = ModelOptions.OPENAI.name
    mock_config.llm.offline = False
    # Act
    handler = model_handler(mock_config, mock_configs)
    # Assert
    assert isinstance(handler, OpenAIHandler)
    assert mock_config.llm.api == ModelOptions.OPENAI.name
    assert mock_config.llm.offline is False


@patch.dict(
    "os.environ",
    {"VERTEXAI_LOCATION": "us-central1", "VERTEXAI_PROJECT": "test-project"},
    clear=True,
)
def test_model_handler_vertex(mock_config, mock_configs):
    """Test that the model handler returns the correct handler for Vertex AI."""
    # Arrange
    mock_config.llm.api = ModelOptions.VERTEX.name
    mock_config.llm.offline = False
    # Act
    handler = model_handler(mock_config, mock_configs)
    # Assert
    assert isinstance(handler, VertexAIHandler)
    assert mock_config.llm.api == ModelOptions.VERTEX.name
    assert mock_config.llm.offline is False


@pytest.mark.skip
@patch.dict("os.environ", {}, clear=True)
def test_model_handler_ollama(mock_config, mock_configs):
    """Test that model handler returns the correct handler for Ollama."""
    # Arrange
    mock_config.llm.api = ModelOptions.OLLAMA.name
    mock_config.llm.offline = False
    # Act
    handler = model_handler(mock_config, mock_configs)
    # Assert
    assert isinstance(handler, OpenAIHandler)
    assert mock_config.llm.api == ModelOptions.OLLAMA.name
    assert mock_config.llm.offline is False


@patch.dict("os.environ", {}, clear=True)
def test_model_handler_offline(mock_config, mock_configs):
    """Test that model handler returns the correct handler for offline mode."""
    # Arrange
    mock_config.llm.api = ModelOptions.OFFLINE.name
    mock_config.llm.offline = True
    # Act
    handler = model_handler(mock_config, mock_configs)
    # Assert
    assert isinstance(handler, OfflineHandler)
    assert mock_config.llm.api == ModelOptions.OFFLINE.name
    assert mock_config.llm.offline is True


def test_model_handler_unsupported_service(mock_config, mock_configs):
    """Test that model handler raises an error for an unsupported service."""
    # Arrange
    mock_config.llm.api = "OpenAGI-Turbo-3000"
    mock_config.llm.offline = False
    # Act
    with pytest.raises(Exception) as exc:
        model_handler(mock_config, mock_configs)
        assert isinstance(exc.value, UnsupportedServiceError)
