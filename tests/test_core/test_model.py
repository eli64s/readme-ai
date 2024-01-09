"""Unit tests for the GPT LLM API handler."""

from unittest.mock import AsyncMock, Mock, patch

import aiohttp
import pytest

from readmeai.core.model import ModelHandler


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
            raise aiohttp.ClientResponseError(
                message="HTTP Error", request=MockRequest()
            )


class MockRequest:
    """Mock request."""

    def __init__(self):
        """Initialize the mock request."""
        self.url = "http://mockurl.com"


class MockHTTPStatusError(aiohttp.ClientResponseError):
    """Mock HTTP status error."""

    def __init__(self):
        """Initialize the mock HTTP status error."""
        super().__init__(
            message="HTTP Error",
            request=MockRequest(),
            response=MockResponse(status_code=404),
        )


@pytest.mark.asyncio
async def test_batch_request(mock_config, mock_dependencies, mock_summaries):
    handler = ModelHandler(mock_config)
    handler._process_prompt = AsyncMock(side_effect=lambda p: f"Processed: {p}")
    responses = await handler.batch_request(
        [Mock(), Mock()], mock_dependencies, mock_summaries
    )
    assert "Processed" in responses[0]


@pytest.mark.asyncio
async def test_set_prompt_context(mock_config, mock_dependencies, mock_summaries):
    """Test the generate_prompts function."""
    file_context = [Mock(), Mock(), Mock()]
    handler = ModelHandler(mock_config)
    handler.http_client.post = AsyncMock(
        side_effect=[
            MockResponse(
                json_data={"choices": [{"message": {"content": "Expected summary"}}]}
            ),
            MockResponse(
                json_data={"choices": [{"message": {"content": "Expected summary"}}]}
            ),
            MockResponse(
                json_data={"choices": [{"message": {"content": "Expected summary"}}]}
            ),
        ],
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


@pytest.mark.asyncio
async def test_process_prompt_summaries(mock_config):
    """Test the _process_prompt function."""
    handler = ModelHandler(mock_config)
    handler._handle_code_summary_response = AsyncMock(return_value="Processed summary")
    mock_prompt = {"type": "summaries", "context": "Some context"}
    result = await handler._process_prompt(mock_prompt)
    assert result == "Processed summary"


@pytest.mark.asyncio
async def test_process_prompt_other_types(mock_config):
    """Test the _process_prompt function."""
    handler = ModelHandler(mock_config)
    handler._inject_prompt_context = Mock(return_value="Injected prompt")
    handler._handle_response = AsyncMock(
        return_value=("type", "Processed other prompt")
    )
    mock_prompt = {"type": "overview", "context": "Some context"}
    result = await handler._process_prompt(mock_prompt)
    assert result == "Processed other prompt"


@pytest.mark.asyncio
async def test_handle_response(mock_config):
    """Test the _handle_response function."""
    handler = ModelHandler(mock_config)
    handler.http_client.post_async = AsyncMock(
        side_effect=[
            MockResponse(
                json_data={
                    "choices": [
                        {
                            "message": {
                                "content": "Python is a programming language for .py files."
                            }
                        }
                    ]
                }
            ),
        ],
    )
    index, response = await handler._handle_response(
        "overview", "what programming language is .py?", 50
    )
    await handler.close()
    assert index == "overview"
    assert "python" in response.lower()


@pytest.mark.asyncio
async def test_handle_response_client_connection_error(mock_config):
    with patch("aiohttp.ClientSession.post") as mock_post:
        mock_post.side_effect = aiohttp.ClientConnectionError()
        handler = ModelHandler(mock_config)
        index, response = await handler._handle_response("overview", "test prompt", 50)
        await handler.close()
        assert "aiohttp.client_exceptions.ClientConnectionError" in response


@pytest.mark.asyncio
async def test_handle_response_server_timeout_error(mock_config):
    with patch("aiohttp.ClientSession.post") as mock_post:
        mock_post.side_effect = aiohttp.ServerTimeoutError()
        handler = ModelHandler(mock_config)
        index, response = await handler._handle_response("overview", "test prompt", 50)
        await handler.close()
        assert "aiohttp.client_exceptions.ServerTimeoutError" in response


@pytest.mark.asyncio
async def test_handle_response_cache(mock_config):
    handler = ModelHandler(mock_config)
    handler.cache[("cached_index", "cached_prompt", 50)] = (
        "cached_index",
        "Cached response",
    )
    index, response = await handler._handle_response(
        "cached_index", "cached_prompt", 50
    )
    assert index == "cached_index"
    assert response == "Cached response"
