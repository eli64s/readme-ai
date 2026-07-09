from unittest.mock import AsyncMock, MagicMock, patch

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
    openai_handler: OpenAIHandler,
):
    """Test that the correct endpoint is set for OpenAI API."""
    assert openai_handler.url == "https://api.openai.com/v1/chat/completions"


def test_openai_endpoint_configuration_for_ollama(
    mock_config_loader: ConfigLoader,
    mock_repository_context,
):
    """Test that the default endpoint is set for Ollama."""
    mock_config_loader.config.llm.api = LLMProviders.OLLAMA.value
    handler = OpenAIHandler(mock_config_loader, mock_repository_context)
    assert handler.url == "http://localhost:11434/v1/chat/completions"


def test_openai_endpoint_configuration_for_openrouter(
    mock_config_loader: ConfigLoader,
    mock_repository_context,
    monkeypatch: pytest.MonkeyPatch,
):
    """Test that OpenAI-compatible remote base URLs are honored."""
    monkeypatch.setenv("OPENAI_API_KEY", "test_api_key")
    mock_config_loader.config.llm.api = LLMProviders.OPENAI.value
    mock_config_loader.config.llm.base_url = "https://openrouter.ai/api/v1"
    handler = OpenAIHandler(mock_config_loader, mock_repository_context)
    assert handler.url == "https://openrouter.ai/api/v1/chat/completions"


def test_openai_endpoint_configuration_for_lm_studio(
    mock_config_loader: ConfigLoader,
    mock_repository_context,
    monkeypatch: pytest.MonkeyPatch,
):
    """Test that local OpenAI-compatible endpoints are honored."""
    monkeypatch.setenv("OPENAI_API_KEY", "test_api_key")
    mock_config_loader.config.llm.api = LLMProviders.OPENAI.value
    mock_config_loader.config.llm.base_url = "http://localhost:1234/v1"
    handler = OpenAIHandler(mock_config_loader, mock_repository_context)
    assert handler.url == "http://localhost:1234/v1/chat/completions"


def test_ollama_endpoint_configuration_for_custom_host(
    mock_config_loader: ConfigLoader,
    mock_repository_context,
):
    """Test that explicit Ollama-compatible hosts are honored."""
    mock_config_loader.config.llm.api = LLMProviders.OLLAMA.value
    mock_config_loader.config.llm.base_url = "http://192.168.1.10:11434/v1"
    handler = OpenAIHandler(mock_config_loader, mock_repository_context)
    assert handler.url == "http://192.168.1.10:11434/v1/chat/completions"


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
    with patch("readmeai.models.openai.token_handler") as mock_token_handler:
        mock_token_handler.return_value = "processed_prompt"
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
        with patch("readmeai.models.openai.token_handler") as mock_token_handler:
            mock_token_handler.return_value = "processed_prompt"
            await openai_handler._make_request(
                "test_index",
                "test_prompt",
                100,
                None,
            )
        assert openai_handler._session.post.call_count == 3

    with pytest.raises(tenacity.RetryError) as e:
        await run_test(aiohttp.ClientError())
    assert "ClientError" in str(e.value)
