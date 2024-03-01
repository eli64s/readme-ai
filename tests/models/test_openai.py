"""
Tests for the OpenAI API LLM handler implementation.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest

from readmeai.cli.options import ModelOptions as llms

_localhost = "http://localhost:11434/v1/"


@pytest.mark.asyncio
async def test_openai_handler_sets_attributes(openai_handler):
    """Test that the OpenAI handler sets the correct attributes."""
    assert hasattr(openai_handler, "model")
    assert hasattr(openai_handler, "temperature")
    assert hasattr(openai_handler, "tokens")
    assert hasattr(openai_handler, "top_p")


@pytest.mark.asyncio
async def test_openai_build_payload(openai_handler):
    """Test that the OpenAI handler builds the correct payload."""
    # Arrange
    prompt = "test_prompt"
    tokens = 100
    # Act
    payload = await openai_handler._build_payload(prompt, tokens)
    # Assert
    assert isinstance(payload, dict)
    assert "max_tokens" in payload
    assert "messages" in payload


@pytest.mark.asyncio
async def test_openai_make_request_with_context(openai_handler):
    """Test that the OpenAI handler handles a response with context."""
    # Arrange
    openai_handler.http_client = MagicMock()
    context = "overview"
    mock_make_request = AsyncMock()
    openai_handler._make_request = mock_make_request

    # Act
    await openai_handler._make_request(
        context, openai_handler.prompts.get(context), 100, []
    )

    # Assert
    mock_make_request.assert_called_once()
    assert mock_make_request.call_count == 1


@pytest.mark.asyncio
async def test_openai_make_request_without_context(openai_handler):
    """Test that the OpenAI handler handles a response without context."""
    # Arrange
    openai_handler.http_client = MagicMock()
    context = "summary"
    mock_make_request = AsyncMock()
    openai_handler._make_request = mock_make_request
    # Act
    await openai_handler._make_request(
        context, openai_handler.prompts.get(context), 100, []
    )
    # Assert
    mock_make_request.assert_called_once()
    assert mock_make_request.call_count == 1


@pytest.mark.asyncio
async def test_openai_endpoint_configuration_for_openai(
    mock_configs, openai_handler
):
    """Test that the correct endpoint is set for OpenAI API."""
    mock_configs.config.llm.api = llms.OPENAI.name
    assert openai_handler.endpoint == mock_configs.config.llm.base_url


@pytest.mark.skip
@pytest.mark.asyncio
async def test_openai_endpoint_configuration_for_ollama(
    mock_configs, openai_handler
):
    """Test that the correct endpoint is set for OLLAMA."""
    mock_configs.config.llm.api = llms.OLLAMA.name
    assert openai_handler.endpoint == f"{_localhost}chat/completions"


@pytest.mark.asyncio
@patch("readmeai.models.openai.aiohttp.ClientSession.post")
async def test_make_request_error_handling(mock_post, openai_handler):
    """Test error handling in _make_request."""
    mock_post.side_effect = aiohttp.ClientError
    openai_handler._session = MagicMock(spec=aiohttp.ClientSession)
    openai_handler._session.post = mock_post
    index, result = await openai_handler._make_request(
        "test_index", "test_prompt", 100
    )
    assert index == "test_index"
    assert result == "<code>► INSERT-TEXT-HERE</code>"
    assert mock_post.call_count == 1
