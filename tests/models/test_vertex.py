"""Tests for the Vertex AI LLM API module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.models.vertex import VertexAIHandler


@pytest.mark.asyncio
async def test_vertex_handler_sets_attributes(mock_config, mock_configs):
    """Test that the Vertex AI handler sets the correct attributes."""
    # Arrange
    app_config = mock_config
    app_config.llm.rate_limit = 5
    app_config.llm.api = "VERTEX"

    # Act
    handler = VertexAIHandler(app_config, mock_configs)

    # Assert
    assert handler.model == "gemini-pro"


@pytest.mark.asyncio
async def test_vertex_handle_response_with_context(mock_config, mock_configs):
    """Test that the Vertex AI handler handles a response with context."""
    # Arrange
    app_config = mock_config
    app_config.llm.rate_limit = 5
    app_config.llm.api = "VERTEX"
    handler = VertexAIHandler(mock_config, mock_configs)
    handler.http_client = MagicMock()

    # Act
    with patch.object(
        VertexAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response()

        # Assert
        mock_handle_response.assert_called_once_with()
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with()


@pytest.mark.asyncio
async def test_handle_response_success(mock_config, mock_configs):
    """Test that the Vertex AI handler handles a successful response."""
    mock_config.llm.tokens_max = 100
    mock_response = MagicMock()
    mock_response.text = "Generated text"
    mock_model = MagicMock()
    mock_model.generate_content_async = AsyncMock(return_value=mock_response)

    with patch("readmeai.models.vertex.vertexai.init"), patch(
        "readmeai.models.vertex.GenerativeModel", return_value=mock_model
    ):
        handler = VertexAIHandler(mock_config, mock_configs)
        response_index, response_text = await handler._handle_response(
            "test_index", "test_prompt", 100
        )

    assert response_index == "test_index"
    assert response_text == "Generated text"
