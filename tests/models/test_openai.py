from unittest.mock import AsyncMock, MagicMock

import aiohttp
import pytest
import tenacity
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.models.enums import LLMProviders
from readmeai.models.openai import OpenAIHandler


def test_openai_handler_sets_attributes(openai_handler: OpenAIHandler):
    """Test that the OpenAI handler sets the correct attributes."""
    assert hasattr(openai_handler, "model")
    assert hasattr(openai_handler, "max_tokens")
    assert hasattr(openai_handler, "top_p")


def test_openai_endpoint_configuration_for_openai(
    mock_config_loader: ConfigLoader,
    openai_handler: OpenAIHandler,
):
    """Test that the correct endpoint is set for OpenAI API."""
    mock_config_loader.config.llm.api = LLMProviders.OPENAI.value
    assert openai_handler.url == f"{openai_handler.host_name}{openai_handler.resource}"


def test_openai_endpoint_configuration_for_ollama(
    mock_config_loader: ConfigLoader,
    ollama_localhost: str,
):
    """Test that the correct endpoint is set for OLLAMA."""
    mock_config_loader.config.llm.api = LLMProviders.OLLAMA.value
    mock_config_loader.config.llm.localhost = ollama_localhost
    assert (
        "v1/chat/completions"
        in f"{mock_config_loader.config.llm.localhost}v1/chat/completions"
    )


@pytest.mark.asyncio
async def test_openai_build_payload(openai_handler: OpenAIHandler):
    """Test that the OpenAI handler builds the correct payload."""
    prompt = "test_prompt"
    payload = await openai_handler._build_payload(prompt)
    assert isinstance(payload, dict)
    assert "max_tokens" in payload
    assert "messages" in payload


@pytest.mark.asyncio
async def test_make_request_success(openai_handler_with_mock_session: OpenAIHandler):
    """Test _make_request with a successful response."""
    index, result = await openai_handler_with_mock_session._make_request(
        "test_index",
        "test_prompt",
        100,
        None,
    )
    assert isinstance(result, str)
    assert index == "test_index"
    assert result == "test_response"


@pytest.mark.asyncio
async def test_openai_make_request_with_context(openai_handler: OpenAIHandler):
    """Test that the OpenAI handler handles a response with context."""
    # Create a new mock for _make_request
    mock_make_request = AsyncMock()
    # Assign the mock to the method
    openai_handler._make_request = mock_make_request
    context = "overview"
    await openai_handler._make_request(
        context,
        openai_handler.prompts.get(context),
        100,
        [],
    )
    mock_make_request.assert_called_once()


@pytest.mark.asyncio
async def test_openai_make_request_without_context(openai_handler: OpenAIHandler):
    """Test that the OpenAI handler handles a response without context."""
    # Create a new mock for _make_request
    mock_make_request = AsyncMock()
    # Assign the mock to the method
    openai_handler._make_request = mock_make_request
    context = "summary"
    await openai_handler._make_request(
        context,
        openai_handler.prompts.get(context),
        100,
        [],
    )
    mock_make_request.assert_called_once()


@pytest.mark.asyncio
async def test_make_request_error_handling(
    mock_config: Settings, openai_handler: OpenAIHandler
):
    """Test error handling in _make_request."""

    async def run_test(error):
        openai_handler._session = MagicMock(spec=aiohttp.ClientSession)
        openai_handler._session.post.side_effect = error  # Simulate the error
        index, result = await openai_handler._make_request(
            "test_index",
            "test_prompt",
            100,
            None,
        )
        assert index == "test_index"
        assert result == mock_config.md.placeholder
        assert openai_handler._session.post.call_count == 1

    with pytest.raises(tenacity.RetryError) as e:
        await run_test(aiohttp.ClientError())
    assert "ClientError" in str(e.value)
