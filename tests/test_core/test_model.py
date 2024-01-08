"""Unit tests for the GPT LLM API handler."""

from unittest.mock import AsyncMock, Mock

import pytest
from cachetools import TTLCache
from httpx import HTTPStatusError, TimeoutException

from readmeai.core.model import ModelHandler


def test_init(mock_config):
    handler = ModelHandler(mock_config)
    assert handler.tokens_max == mock_config.llm.tokens_max
    assert isinstance(handler.cache, TTLCache)


class MockResponse:
    def __init__(self, json_data=None, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise HTTPStatusError(message="HTTP Error", request=MockRequest())


class MockRequest:
    def __init__(self):
        self.url = "http://mockurl.com"


class MockHTTPStatusError(HTTPStatusError):
    def __init__(self):
        super().__init__(
            message="HTTP Error",
            request=MockRequest(),
            response=MockResponse(status_code=404),
        )


@pytest.mark.asyncio
async def test_handle_response_success(mock_config):
    handler = ModelHandler(mock_config)
    handler.http_client.post = AsyncMock(
        return_value=MockResponse(
            json_data={
                "choices": [{"message": {"content": "Expected summary"}}]
            }
        )
    )
    index, summary = await handler._handle_response("test", "Some prompt", 50)
    assert summary == "Expected summary"
    assert index == "test"


@pytest.mark.asyncio
async def test_batch_request(mock_config, mock_dependencies, mock_summaries):
    handler = ModelHandler(mock_config)
    handler._process_prompt = AsyncMock(
        side_effect=lambda p: f"Processed: {p}"
    )
    responses = await handler.batch_request(
        [Mock(), Mock()], mock_dependencies, mock_summaries
    )
    assert "Processed" in responses[0]


@pytest.mark.asyncio
async def test_handle_reponse_with_retry(mock_config):
    """Test generate_text method with retry."""
    handler = ModelHandler(mock_config)
    handler.http_client.post = AsyncMock(
        side_effect=[TimeoutException("Timeout"), MockResponse()]
    )
    index, summary = await handler._handle_response(
        "retry_test", "Some prompt", 50
    )
    assert summary is not None
    assert index == "retry_test"


@pytest.mark.asyncio
async def test_set_prompt_context(
    mock_config, mock_dependencies, mock_summaries
):
    """Test the generate_prompts function."""
    mock_config.git.repository = "https://example.com/repo"
    file_context = [Mock(), Mock(), Mock()]
    handler = ModelHandler(mock_config)
    handler.http_client.post = AsyncMock(
        side_effect=[TimeoutException("Timeout"), MockResponse()]
    )
    prompts = await handler._set_prompt_context(
        file_context,
        mock_dependencies,
        mock_summaries,
    )
    assert len(prompts) == 4
    expected_prompts = []
    for prompt, expected in zip(prompts, expected_prompts):
        assert prompt == expected
