"""Unit tests for the GPT LLM API handler."""

from unittest.mock import AsyncMock
import pytest
from cachetools import TTLCache
from httpx import HTTPStatusError, TimeoutException

from readmeai.core.model import ModelHandler


@pytest.fixture
def mock_settings(config):
    mock_config = config
    return mock_config


def test_init(mock_settings):
    handler = ModelHandler(mock_settings)
    assert handler.tokens_max == mock_settings.llm.tokens_max
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
async def test_generate_text_success(mock_settings):
    handler = ModelHandler(mock_settings)
    handler.http_client.post = AsyncMock(
        return_value=MockResponse(
            json_data={
                "choices": [{"message": {"content": "Expected summary"}}]
            }
        )
    )

    index, summary = await handler.generate_text("test", "Some prompt", 50)
    assert summary == "Expected summary"
    assert index == "test"


@pytest.mark.asyncio
async def test_batch_text_generator(mock_settings):
    handler = ModelHandler(mock_settings)
    handler._process_prompt = AsyncMock(
        side_effect=lambda p: f"Processed: {p}"
    )

    prompts = ["prompt1", "prompt2", "prompt3"]
    responses = await handler.batch_text_generator(prompts)
    assert responses == [f"Processed: {p}" for p in prompts]


@pytest.mark.asyncio
async def test_generate_text_failure(mock_settings):
    pass


@pytest.mark.asyncio
async def test_generate_text_with_retry(mock_settings):
    handler = ModelHandler(mock_settings)
    handler.http_client.post = AsyncMock(
        side_effect=[TimeoutException("Timeout"), MockResponse()]
    )

    index, summary = await handler.generate_text(
        "retry_test", "Some prompt", 50
    )
    assert summary is not None
    assert index == "retry_test"
