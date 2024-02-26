"""Tests for the OpenAI API LLM module."""

from unittest.mock import AsyncMock, MagicMock

import pytest


@pytest.mark.asyncio
async def test_openai_handler_sets_attributes(handler):
    """Test that the OpenAI handler sets the correct attributes."""
    # Assert
    assert hasattr(handler, "content")
    assert hasattr(handler, "encoding")
    assert hasattr(handler, "endpoint")
    assert hasattr(handler, "model")
    assert hasattr(handler, "tokens")
    assert hasattr(handler, "tokens_max")
    assert hasattr(handler, "temperature")
    assert hasattr(handler, "_http_client")
    assert handler.rate_limit_semaphore._value >= 5


@pytest.mark.asyncio
async def test_openai_handle_response_with_context(handler):
    """Test that the OpenAI handler handles a response with context."""
    # Arrange
    handler.http_client = MagicMock()
    context = "overview"
    mock_handle_response = AsyncMock()
    handler._handle_response = mock_handle_response

    # Act
    await handler._handle_response(
        context, handler.prompts.get(context), 100, []
    )

    # Assert
    mock_handle_response.assert_called_once()
    assert mock_handle_response.call_count == 1


@pytest.mark.asyncio
async def test_openai_handle_response_without_context(handler):
    """Test that the OpenAI handler handles a response without context."""
    # Arrange
    handler.http_client = MagicMock()
    context = "summary"
    mock_handle_response = AsyncMock()
    handler._handle_response = mock_handle_response

    # Act
    await handler._handle_response(
        context, handler.prompts.get(context), 100, []
    )

    # Assert
    mock_handle_response.assert_called_once()
    assert mock_handle_response.call_count == 1
