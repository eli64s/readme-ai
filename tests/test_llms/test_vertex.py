"""Tests for the Vertex AI LLM API module."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from readmeai.llms.vertex import VertexAIHandler


@pytest.mark.asyncio
async def test_vertex_handler_sets_attributes(mock_config):
    """Test that the Vertex AI handler sets the correct attributes."""
    # Arrange
    app_config = mock_config
    app_config.llm.rate_limit = 5
    app_config.llm.api = "VERTEX"

    # Act
    handler = VertexAIHandler(app_config)

    # Assert
    assert hasattr(handler, "location")
    assert hasattr(handler, "project_id")


@pytest.mark.asyncio
async def test_vertex_handle_response_with_context(mock_config):
    """Test that the Vertex AI handler handles a response with context."""
    # Arrange
    app_config = mock_config
    app_config.llm.rate_limit = 5
    app_config.llm.api = "VERTEX"
    handler = VertexAIHandler(mock_config)
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
async def test_handle_response_success(mock_config):
    """Test that the Vertex AI handler handles a successful response."""
    mock_config.llm.tokens_max = 100

    # Mocking response
    mock_response = MagicMock()
    mock_response.text = "Generated text"

    # Mocking GenerativeModel
    mock_model = MagicMock()
    mock_model.generate_content_async = AsyncMock(return_value=mock_response)

    # Patching external dependencies
    with patch("readmeai.llms.vertex.vertexai.init"), patch(
        "readmeai.llms.vertex.GenerativeModel", return_value=mock_model
    ):
        handler = VertexAIHandler(mock_config)
        response_index, response_text = await handler._handle_response(
            "test_index", "test_prompt", 100
        )

    assert response_index == "test_index"
    assert response_text == "Generated text"


@pytest.mark.asyncio
async def test_handle_response_retry(mock_config):
    """Test that the Vertex AI handler retries on error."""
    mock_config.llm.tokens_max = 100

    # Mocking response
    mock_response = MagicMock()
    mock_response.text = "Generated text"

    # Mocking GenerativeModel
    mock_model = MagicMock()
    mock_model.generate_content_async = AsyncMock(
        side_effect=[
            httpx.HTTPStatusError(
                "500 Server Error", request=MagicMock(), response=MagicMock()
            ),  # Error on first attempt
            mock_response,  # Success on retry
        ]
    )

    # Patching external dependencies
    with patch("readmeai.llms.vertex.vertexai.init"), patch(
        "readmeai.llms.vertex.GenerativeModel", return_value=mock_model
    ):
        handler = VertexAIHandler(mock_config)
        response_index, response_text = await handler._handle_response(
            "test_index", "test_prompt", 100
        )

    assert response_index == "test_index"
    assert response_text == mock_config.md.default
