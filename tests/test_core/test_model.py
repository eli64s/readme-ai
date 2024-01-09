"""Unit tests for the GPT LLM API handler."""

from unittest.mock import AsyncMock, Mock, call, patch

import httpx
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
            raise httpx.HTTPStatusError(message="HTTP Error", request=MockRequest())


class MockRequest:
    """Mock request."""

    def __init__(self):
        """Initialize the mock request."""
        self.url = "http://mockurl.com"


class MockHTTPStatusError(httpx.HTTPStatusError):
    """Mock HTTP status error."""

    def __init__(self):
        """Initialize the mock HTTP status error."""
        super().__init__(
            message="HTTP Error",
            request=MockRequest(),
            response=MockResponse(status_code=404),
        )


@pytest.mark.asyncio
async def test_batch_request(
    mock_config, mock_file_data, mock_dependencies, mock_summaries
):
    """Test the batch_request function."""
    model_handler = ModelHandler(mock_config)
    patch.object(model_handler, "_set_prompt_context", return_value=...)
    patch.object(model_handler, "_batch_prompts", return_value=...)
    responses = await model_handler.batch_request(
        mock_file_data, mock_dependencies, mock_summaries
    )
    model_handler.close()
    assert isinstance(responses, list)


def test_generate_batches(mock_config):
    """Test the _generate_batches function."""
    batch_size = 3
    items = [1, 2, 3, 4, 5, 6, 7, 8]
    model_handler = ModelHandler(mock_config)
    batches = list(model_handler._generate_batches(items, batch_size))
    model_handler.close()
    assert isinstance(batches, list)
    assert len(batches) == 3
    assert batches[0] == [1, 2, 3]
    assert batches[1] == [4, 5, 6]
    assert batches[2] == [7, 8]


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
    handler.close()
    assert len(prompts) == 4
    expected_prompts = []
    for prompt, expected in zip(prompts, expected_prompts):
        assert prompt == expected


@pytest.mark.asyncio
async def test_process_batch_summaries(mock_config):
    """Test the _process_prompt function."""
    handler = ModelHandler(mock_config)
    handler._handle_code_summary_response = AsyncMock(return_value="Processed summary")
    mock_prompt = {"type": "summaries", "context": "Some context"}
    result = await handler._process_batch(mock_prompt)
    handler.close()
    assert result == "Processed summary"


@pytest.mark.asyncio
async def test_process_batch_other_types(mock_config):
    """Test the _process_prompt function."""
    handler = ModelHandler(mock_config)
    handler._get_prompt_context = Mock(return_value="Injected prompt")
    handler._handle_response = AsyncMock(
        return_value=("type", "Processed other prompt")
    )
    mock_prompt = {"type": "overview", "context": "Some context"}
    result = await handler._process_batch(mock_prompt)
    handler.close()
    assert result == "Processed other prompt"


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
async def test_handle_response_http_status_error(mock_config):
    with patch(
        "httpx.AsyncClient.post",
        side_effect=httpx.HTTPStatusError(
            response=MockResponse(status_code=404),
            request=MockRequest(),
            message="HttpStatusError",
        ),
    ):
        handler = ModelHandler(mock_config)
        index, response = await handler._handle_response("overview", "test prompt", 50)
        await handler.close()
        assert "HttpStatusError" in response


@pytest.mark.asyncio
async def test_handle_response_network_error(mock_config):
    with patch(
        "httpx.AsyncClient.post",
        side_effect=httpx.NetworkError(
            request=MockRequest(),
            message="NetworkError",
        ),
    ):
        handler = ModelHandler(mock_config)
        index, response = await handler._handle_response("overview", "test prompt", 50)
        await handler.close()
        assert "NetworkError" in response


@pytest.mark.asyncio
async def test_handle_response_timeout_error(mock_config):
    with patch(
        "httpx.AsyncClient.post",
        side_effect=httpx.TimeoutException(
            request=MockRequest(),
            message="TimeoutException",
        ),
    ):
        handler = ModelHandler(mock_config)
        index, response = await handler._handle_response("overview", "test prompt", 50)
        await handler.close()
        assert "TimeoutException" in response


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
