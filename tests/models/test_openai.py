from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest
import tenacity

from readmeai.cli.options import LLMService
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.models.openai import OpenAIHandler


@pytest.mark.asyncio
async def test_openai_handler_sets_attributes(openai_handler: OpenAIHandler):
    """Test that the OpenAI handler sets the correct attributes."""
    assert hasattr(openai_handler, "model")
    assert hasattr(openai_handler, "temperature")
    assert hasattr(openai_handler, "tokens")
    assert hasattr(openai_handler, "top_p")


@pytest.mark.asyncio
async def test_openai_endpoint_configuration_for_openai(
    config_loader_fixture: ConfigLoader,
    openai_handler: OpenAIHandler,
):
    """Test that the correct endpoint is set for OpenAI API."""
    config_loader_fixture.config.llm.api = LLMService.OPENAI.name
    assert (
        openai_handler.url
        == f"{config_loader_fixture.config.llm.host_name}{config_loader_fixture.config.llm.path}"
    )


@pytest.mark.asyncio
async def test_openai_endpoint_configuration_for_ollama(
    config_loader_fixture: ConfigLoader,
    ollama_localhost: str,
):
    """Test that the correct endpoint is set for OLLAMA."""
    config_loader_fixture.config.llm.api = LLMService.OLLAMA.name
    config_loader_fixture.config.llm.localhost = ollama_localhost
    assert (
        "v1/chat/completions"
        in f"{config_loader_fixture.config.llm.localhost}{config_loader_fixture.config.llm.path}"
    )


@pytest.mark.asyncio
async def test_openai_build_payload(openai_handler: OpenAIHandler):
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
@patch("readmeai.models.openai.aiohttp.ClientSession.post")
async def test_make_request_success(mock_post, openai_handler: OpenAIHandler):
    """Test _make_request with a successful response."""
    mock_response_cm = AsyncMock()
    mock_response = AsyncMock(
        json=AsyncMock(
            return_value={
                "choices": [{"message": {"content": "test_response"}}],
            },
        ),
    )
    mock_response_cm.__aenter__.return_value = mock_response
    mock_post.return_value = mock_response_cm
    openai_handler._session = MagicMock(spec=aiohttp.ClientSession)
    openai_handler._session.post = mock_post
    index, result = await openai_handler._make_request(
        "test_index",
        "test_prompt",
        100,
        None,
    )
    assert mock_post.call_count == 1
    assert mock_response_cm.__aenter__.call_count == 1
    assert mock_response.json.call_count == 1
    assert isinstance(result, str)
    assert index == "test_index"
    assert result == "test_response"
    assert (
        mock_response.json.return_value["choices"][0]["message"]["content"]
        == "test_response"
    )


@pytest.mark.asyncio
async def test_openai_make_request_with_context(openai_handler: OpenAIHandler):
    """Test that the OpenAI handler handles a response with context."""
    # Arrange
    openai_handler.http_client = MagicMock()
    context = "overview"
    mock_make_request = AsyncMock()
    openai_handler._make_request = mock_make_request
    # Act
    await openai_handler._make_request(
        context,
        openai_handler.prompts.get(context),
        100,
        [],
    )
    # Assert
    mock_make_request.assert_called_once()
    assert mock_make_request.call_count == 1


@pytest.mark.asyncio
async def test_openai_make_request_without_context(
    openai_handler: OpenAIHandler,
):
    """Test that the OpenAI handler handles a response without context."""
    # Arrange
    openai_handler.http_client = MagicMock()
    context = "summary"
    mock_make_request = AsyncMock()
    openai_handler._make_request = mock_make_request
    # Act
    await openai_handler._make_request(
        context,
        openai_handler.prompts.get(context),
        100,
        [],
    )
    # Assert
    mock_make_request.assert_called_once()
    assert mock_make_request.call_count == 1


@pytest.mark.asyncio
async def test_make_request_error_handling(
    config_fixture: Settings, openai_handler: OpenAIHandler
):
    """Test error handling in _make_request."""

    @patch("readmeai.models.openai.aiohttp.ClientSession.post")
    async def run_test(error, mock_post):
        mock_post.side_effect = error
        openai_handler._session = MagicMock(spec=aiohttp.ClientSession)
        openai_handler._session.post = mock_post

        index, result = await openai_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )

        assert index == "test_index"
        assert result == config_fixture.md.placeholder
        assert mock_post.call_count == 1

    with pytest.raises(tenacity.RetryError) as e:
        await run_test(aiohttp.ClientError())
    assert "ClientError" in str(e.value)
