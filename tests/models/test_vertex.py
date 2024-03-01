"""
Tests for Google Cloud Vertex AI LLM API handler implementation.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.models.vertex import VertexAIHandler


@pytest.mark.asyncio
async def test_vertex_handler_sets_attributes(vertex_handler):
    """Test that the Vertex AI handler sets the correct attributes."""
    # Arrange
    assert hasattr(vertex_handler, "temperature")
    assert hasattr(vertex_handler, "model")


@pytest.mark.asyncio
async def test_vertex_make_request_with_context(
    vertex_handler, mock_config, mock_configs
):
    """Test that the Vertex AI handler handles a response with context."""
    # Arrange
    handler = vertex_handler
    handler.http_client = MagicMock()
    # Act
    with patch.object(
        VertexAIHandler, "_make_request", new_callable=AsyncMock
    ) as mock_make_request:
        # Act
        await handler._make_request()
        # Assert
        mock_make_request.assert_called_once_with()
        handler.http_client.post.assert_not_called()
        mock_make_request.assert_called_once_with()


@pytest.mark.asyncio
async def test_make_request_success(mock_config, mock_configs):
    """Test that the Vertex AI handler handles a successful response."""
    mock_config.llm.context_window = 100
    mock_response = MagicMock()
    mock_response.text = "Generated text"
    mock_model = MagicMock()
    mock_model.generate_content_async = AsyncMock(return_value=mock_response)

    with patch(
        "readmeai.models.vertex.GenerativeModel", return_value=mock_model
    ):
        handler = VertexAIHandler(mock_configs)
        response_index, response_text = await handler._make_request(
            "test_index", "test_prompt", 100
        )

    assert response_index == "test_index"
    assert response_text == "Generated text"
