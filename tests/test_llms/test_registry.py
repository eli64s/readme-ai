"""Tests for the LLM API handler abstract base class."""

import pytest

from readmeai.exceptions import UnsupportedServiceError
from readmeai.llms.openai import OpenAIHandler
from readmeai.llms.registry import model_handler
from readmeai.llms.vertex import VertexAIHandler


def test_model_handler_openai(mock_config):
    """Test that the model handler returns the correct handler for OpenAI."""
    # Arrange
    mock_config.llm.api = "openai"

    # Act
    handler = model_handler(mock_config)

    # Assert
    assert isinstance(handler, OpenAIHandler)


def test_model_handler_vertex(mock_config):
    """Test that the model handler returns the correct handler for Vertex AI."""
    # Arrange
    mock_config.llm.api = "vertex"

    # Act
    handler = model_handler(mock_config)

    # Assert
    assert isinstance(handler, VertexAIHandler)


def test_model_handler_unsupported_service(mock_config):
    """Test that the model handler raises an error for an unsupported service."""
    # Arrange
    mock_config.llm.api = "openai_board_replaced_sam_altman"

    # Act
    with pytest.raises(UnsupportedServiceError) as exc:
        model_handler(mock_config)

    # Assert
    assert "openai_board_replaced_sam_altman" in str(exc.value)
    assert isinstance(exc.value, UnsupportedServiceError)
