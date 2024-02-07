"""Tests for the OpenAI API LLM module."""

from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from readmeai.llms.openai import OpenAIHandler


@pytest.mark.asyncio
async def test_openai_handler_sets_attributes(mock_config):
    """Test that the OpenAI handler sets the correct attributes."""
    # Act
    handler = OpenAIHandler(mock_config)

    # Assert
    assert hasattr(handler, "content")
    assert hasattr(handler, "encoder")
    assert hasattr(handler, "endpoint")
    assert hasattr(handler, "model")
    assert hasattr(handler, "prompts")
    assert hasattr(handler, "tokens")
    assert hasattr(handler, "tokens_max")
    assert hasattr(handler, "temperature")


@pytest.mark.asyncio
async def test_openai_handle_response_with_context(mock_config):
    """Test that the OpenAI handler handles a response with context."""
    # Arrange
    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response("test_context")

        # Assert
        mock_handle_response.assert_called_once_with("test_context")
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with("test_context")


@pytest.mark.asyncio
async def test_openai_handle_response_without_context(mock_config):
    """Test that the OpenAI handler handles a response without context."""
    # Arrange
    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response()

        # Assert
        mock_handle_response.assert_called_once_with()
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with()


@pytest.mark.asyncio
async def test_handle_response_success(mock_config):
    """Test that the OpenAI handler handles a successful response."""
    mock_config.llm.tokens_max = 100

    # Mocking response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "choices": [{"message": {"content": "Generated text"}}]
    }

    # Mocking HTTP client
    mock_http_client = AsyncMock(return_value=mock_response)

    # Patching external dependencies
    with patch("readmeai.llms.openai.openai.api_key", "mock_api_key"), patch(
        "readmeai.llms.openai.httpx.AsyncClient"
    ) as mock_async_client:
        mock_async_client.return_value.post = mock_http_client
        handler = OpenAIHandler(mock_config)
        response_index, response_text = await handler._handle_response(
            "test_index", "test_prompt", 100
        )

    assert response_index == "test_index"
    assert response_text == "Generated text"


@pytest.mark.asyncio
async def test_handle_response_retry(mock_config):
    """Test that the OpenAI handler retries on error."""
    mock_config.llm.tokens_max = 100

    # Mocking response
    mock_response = MagicMock()
    mock_response.json.side_effect = [
        httpx.HTTPStatusError(
            "500 Server Error", request=MagicMock(), response=MagicMock()
        ),
        {"choices": [{"message": {"content": "Generated text"}}]},
    ]

    # Mocking HTTP client
    mock_http_client = AsyncMock(
        side_effect=[
            httpx.HTTPStatusError(
                "500 Server Error", request=MagicMock(), response=MagicMock()
            ),
            mock_response,
        ]
    )

    # Patching external dependencies
    with patch("readmeai.llms.openai.openai.api_key", "mock_api_key"), patch(
        "readmeai.llms.openai.httpx.AsyncClient"
    ) as mock_async_client:
        mock_async_client.return_value.post = mock_http_client
        handler = OpenAIHandler(mock_config)
        response_index, response_text = await handler._handle_response(
            "test_index", "test_prompt", 100
        )

    assert response_index == "test_index"
    assert response_text == mock_config.md.default
