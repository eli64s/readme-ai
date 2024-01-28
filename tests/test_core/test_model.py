"""Unit tests for the GPT LLM API handler."""

import asyncio
from unittest.mock import AsyncMock, patch

import httpx
import openai
import pytest

from readmeai.core.logger import Logger
from readmeai.core.model import ModelHandler


@pytest.fixture
async def mock_handler(mock_config):
    """Mock the ModelHandler class."""
    async with ModelHandler(mock_config) as handler:
        yield handler


class MockResponse:
    """Mock response."""

    def __init__(self, json_data=None, status_code=200):
        """Initialize the mock response."""
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        """Return the json data."""
        return self.json_data

    def raise_for_status(self):
        """Raise an error if the status code is not 200."""
        if self.status_code != 200:
            raise httpx.HTTPStatusError(
                message="HTTP Error", request=MockRequest()
            )


class MockRequest:
    """Mock request."""

    def __init__(self):
        """Initialize the mock request."""
        self.url = "http://mockurl.com"


@pytest.mark.asyncio
async def test_model_handler_initialization(mock_config):
    mock_handler = ModelHandler(mock_config)
    assert mock_handler.config == mock_config
    assert mock_handler.cache is not None
    assert mock_handler.logger is not None
    assert mock_handler.http_client is not None
    assert isinstance(mock_handler.logger, Logger)
    assert isinstance(mock_handler.http_client, httpx.AsyncClient)
    assert isinstance(mock_handler.rate_limit_semaphore, asyncio.Semaphore)
    assert isinstance(mock_handler.rate_limit, int)
    await mock_handler.close()


@pytest.mark.asyncio
async def test_model_handler_initialization_with_invalid_config():
    with pytest.raises(Exception) as exc:
        invalid_config = {}
        handler = ModelHandler(invalid_config)
        await handler.use_api(invalid_config)
    assert isinstance(exc.value, Exception)


def test_http_client_initialization(mock_config):
    mock_config.llm.rate_limit = 10
    handler = ModelHandler(mock_config)
    handler._http_client()
    assert handler.rate_limit_semaphore._value == 10


@pytest.mark.asyncio
async def test_model_handler_batch_request(mock_config):
    """Test the batch_request function."""
    handler = ModelHandler(mock_config)
    with patch.object(
        handler, "_batch_prompts", new_callable=AsyncMock
    ) as mock_batch:
        mock_batch.return_value = ...
        await handler.batch_request([1, 2, 3], [4, 5, 6], [7, 8, 9])
    await handler.close()
    assert mock_batch.called


@pytest.mark.asyncio
async def test_generate_batches_odd_number_of_elements(mock_config):
    """Test generator behavior when given an odd number of elements."""
    batch_size = 3
    items = [1, 2, 3, 4, 5, 6, 7]
    model_handler = ModelHandler(mock_config)
    batches = list(model_handler._generate_batches(items, batch_size))
    model_handler.close()
    assert isinstance(batches, list)
    assert len(batches) == 3
    assert batches[0] == [1, 2, 3]
    assert batches[1] == [4, 5, 6]
    assert batches[2] == [7]


@pytest.mark.asyncio
async def test_large_batch_size_handling(mock_config):
    handler = ModelHandler(mock_config)
    large_batch = ["prompt"] * 1000
    responses = await handler._batch_prompts(large_batch)
    assert len(responses) == len(large_batch)
    assert isinstance(responses, list)
    await handler.close()


@pytest.mark.asyncio
async def test_batch_prompts_exception_handling(mock_config):
    handler = ModelHandler(mock_config)
    mock_prompts = ["prompt1", "prompt2"]

    with patch.object(
        handler, "_process_batch", side_effect=Exception("Test Error")
    ):
        responses = await handler._batch_prompts(mock_prompts)

    assert len(responses) == len(mock_prompts)
    await handler.close()


@pytest.mark.asyncio
async def test_handle_response(mock_config):
    """Test the _handle_response function."""
    content = "Extension for Python code files?"
    handler = ModelHandler(mock_config)
    handler.http_client.post_async = AsyncMock(
        side_effect=MockResponse(
            json_data={"choices": [{"message": {"content": content}}]}
        )
    )
    index, response = await handler._handle_response("overview", content, 30)
    await handler.close()
    assert response is not None
    assert isinstance(response, str)


@pytest.mark.asyncio
async def test_handle_response_openai_error(mock_config):
    """Test the _handle_response function."""
    handler = ModelHandler(mock_config)
    handler.http_client.post_async = AsyncMock(
        side_effect=MockResponse(status_code=500)
    )
    with pytest.raises(openai.OpenAIError) as exc:
        await handler._handle_response(None, "", "")
    assert isinstance(exc.value, openai.OpenAIError)
