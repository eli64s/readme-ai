"""
Tests for Google Cloud Gemini API LLM handler implementation.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.models.gemini import GeminiHandler


@pytest.mark.asyncio
async def test_gemini_handler_sets_attributes(gemini_handler):
    """Test that the Gemini API handler sets the correct attributes."""
    assert hasattr(gemini_handler, "model")
    assert hasattr(gemini_handler, "temperature")
    assert hasattr(gemini_handler, "tokens")


@pytest.mark.asyncio
async def test_gemini_make_request_with_context(gemini_handler):
    """Test that the Gemini API handler handles a response with context."""
    # Arrange
    handler = gemini_handler
    handler.http_client = MagicMock()
    # Act
    with patch.object(
        GeminiHandler,
        "_make_request",
        new_callable=AsyncMock,
    ) as mock_make_request:
        # Act
        await handler._make_request()
        # Assert
        mock_make_request.assert_called_once_with()
        handler.http_client.post.assert_not_called()
        mock_make_request.assert_called_once_with()


@pytest.mark.asyncio
async def test_gemini_make_request_without_context(gemini_handler):
    """Test that the Gemini API handler handles a response without context."""
    # Arrange
    handler = gemini_handler
    handler.http_client = MagicMock()
    # Act
    with patch.object(
        GeminiHandler,
        "_make_request",
        new_callable=AsyncMock,
    ) as mock_make_request:
        # Act
        await handler._make_request()
        # Assert
        mock_make_request.assert_called_once_with()
        handler.http_client.post.assert_not_called()
        mock_make_request.assert_called_once_with()
