from unittest.mock import AsyncMock

import aiohttp
import pytest
import tenacity
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.models.anthropic import ANTHROPIC_AVAILABLE, AnthropicHandler
from readmeai.models.enums import AnthropicModels, LLMProviders


@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
def test_anthropic_handler_sets_attributes(anthropic_handler: AnthropicHandler):
    assert hasattr(anthropic_handler, "model")
    assert hasattr(anthropic_handler, "max_tokens")
    assert hasattr(anthropic_handler, "top_p")


@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
def test_anthropic_endpoint_configuration_for_anthropic(
    mock_config_loader: ConfigLoader,
    anthropic_handler: AnthropicHandler,
):
    mock_config_loader.config.llm.api = LLMProviders.ANTHROPIC.value
    assert anthropic_handler.model in [model.value for model in AnthropicModels]


@pytest.mark.asyncio
@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
async def test_anthropic_build_payload(anthropic_handler: AnthropicHandler):
    prompt = "test_prompt"
    payload = await anthropic_handler._build_payload(prompt)
    assert isinstance(payload, dict)
    assert "max_tokens" in payload
    assert "messages" in payload


@pytest.mark.asyncio
@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
async def test_anthropic_make_request_success(
    anthropic_handler_with_mock_session: AnthropicHandler,
):
    # Act
    index, result = await anthropic_handler_with_mock_session._make_request(
        "test_index",
        "test_prompt",
        100,
        None,
    )
    # Assert
    assert isinstance(result, str)
    assert index == "test_index"
    assert result == "test_response"


@pytest.mark.asyncio
@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
async def test_anthropic_make_request_with_context(anthropic_handler: AnthropicHandler):
    mock_make_request = AsyncMock()
    anthropic_handler._make_request = mock_make_request
    context = "overview"
    await anthropic_handler._make_request(
        context, anthropic_handler.prompts.get(context), 100, []
    )
    mock_make_request.assert_called_once()


@pytest.mark.asyncio
@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
async def test_anthropic_make_request_without_context(
    anthropic_handler: AnthropicHandler,
):
    mock_make_request = AsyncMock()
    anthropic_handler._make_request = mock_make_request
    context = "summary"
    await anthropic_handler._make_request(
        context, anthropic_handler.prompts.get(context), 100, []
    )
    mock_make_request.assert_called_once()


@pytest.mark.asyncio
@pytest.mark.skipif(
    not ANTHROPIC_AVAILABLE, reason="Anthropic library is not available"
)
async def test_anthropic_make_request_error_handling(
    mock_config: Settings, anthropic_handler: AnthropicHandler
):
    async def run_test(error):
        # Mock to consistently raise the retryable exception
        anthropic_handler.client.messages.create = AsyncMock(side_effect=error)
        # Assert RetryError is raised after retries
        with pytest.raises(tenacity.RetryError):
            await anthropic_handler._make_request(
                "test_index",
                "test_prompt",
                100,
                None,
            )

    # Test with a retryable exception
    await run_test(aiohttp.ClientError())
