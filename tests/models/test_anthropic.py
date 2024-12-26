import os
from unittest.mock import AsyncMock, MagicMock, patch

import anthropic
import pytest
import tenacity

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.anthropic import AnthropicHandler

try:
    import anthropic

    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False


@pytest.fixture
def anthropic_handler(repository_context_fixture: RepositoryContext):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    config_loader = ConfigLoader()
    context = repository_context_fixture
    os.environ["ANTHROPIC_API_KEY"] = "test"
    return AnthropicHandler(config_loader, context)


@pytest.mark.skip("Anthropic extra dependency needs review.")
@pytest.mark.asyncio
async def test_model_settings(anthropic_handler: AnthropicHandler):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    anthropic_handler._model_settings()
    assert isinstance(anthropic_handler.client, anthropic.AsyncAnthropic)
    assert anthropic_handler.model == "claude-3-opus-20240229"


@pytest.mark.asyncio
async def test_build_payload(anthropic_handler: AnthropicHandler):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    prompt = "Test prompt"
    tokens = 100
    payload = await anthropic_handler._build_payload(prompt, tokens)
    assert payload["model"] == anthropic_handler.model
    assert payload["max_tokens"] == tokens
    assert payload["messages"][0]["content"] == prompt


@pytest.mark.asyncio
@patch("readmeai.models.anthropic.token_handler", new_callable=AsyncMock)
@patch("anthropic.AsyncAnthropic", new_callable=AsyncMock)
async def test_make_request_success(
    mock_create, mock_token_handler, anthropic_handler: AnthropicHandler
):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    mock_token_handler.return_value = "Processed prompt"
    mock_token_handler.side_effect = lambda *args: args[2]
    mock_create.return_value = MagicMock(
        content=[MagicMock(text="Generated text")]
    )
    anthropic_handler.client = MagicMock()
    anthropic_handler.client.messages.create = mock_create
    anthropic_handler.rate_limit_semaphore = AsyncMock()
    assert await anthropic_handler._make_request(
        "index", "prompt", 100, []
    ) == (
        "index",
        "Generated text",
    )
    assert mock_create.call_count == 1


@pytest.mark.asyncio
@patch("readmeai.models.anthropic.token_handler", new_callable=AsyncMock)
@patch("anthropic.AsyncAnthropic", new_callable=AsyncMock)
async def test_make_request_api_error(
    mock_create, mock_token_handler, anthropic_handler: AnthropicHandler
):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    mock_token_handler.return_value = "Processed prompt"
    mock_create.side_effect = anthropic.APIError(
        message="API error",
        request=AsyncMock(),
        body={"error": "error"},
    )
    anthropic_handler.client = MagicMock()
    anthropic_handler.client.messages.create = mock_create
    anthropic_handler.rate_limit_semaphore = AsyncMock()
    with pytest.raises(tenacity.RetryError):
        await anthropic_handler._make_request("index", "prompt", 100, [])

    assert mock_create.call_count >= 3


@pytest.mark.asyncio
@patch("readmeai.models.anthropic.token_handler", new_callable=AsyncMock)
@patch("anthropic.AsyncAnthropic", new_callable=AsyncMock)
async def test_make_request_unexpected_error(
    mock_create, mock_token_handler, anthropic_handler: AnthropicHandler
):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    mock_token_handler.return_value = "Processed prompt"
    mock_create.side_effect = Exception("Unexpected error")
    anthropic_handler.client = MagicMock()
    anthropic_handler.client.messages.create = mock_create
    anthropic_handler.rate_limit_semaphore = AsyncMock()
    index, data = await anthropic_handler._make_request(
        "index", "prompt", 100, []
    )
    assert index == "index"
    assert data == anthropic_handler.placeholder
