"""Unit tests for the GPT LLM API handler."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import HTTPStatusError, Response
from tenacity import RetryError

from readmeai.core.model import LlmApiHandler


@pytest.fixture
def handler(config):
    """Returns an instance of readmeai.core.model.LlmApiHandler class."""
    return LlmApiHandler(config)


@pytest.mark.asyncio
async def test_prompt_processor_summaries(handler):
    file_context = {
        "summaries": [
            ("path/to/file1.py", "File 1 placeholder"),
            ("path/to/file2.py", "File 2 placeholder"),
        ]
    }
    result = await handler.prompt_processor("summaries", file_context)
    assert len(result) == 2
    assert result[0][0] == "path/to/file1.py"
    assert result[1][0] == "path/to/file2.py"


@pytest.mark.asyncio
async def test_prompt_processor_other(config, handler):
    """Test that the prompt processor returns the prompt."""
    context = {
        "name": config.git.repository,
        "tree": config.md.tree,
        "deps": ["python", "requests", "pytest"],
        "summaries": [("path/to/file1.py", "File 1 placeholder")],
    }
    result = await handler.prompt_processor("features", context)
    assert "features" in result


@pytest.mark.asyncio
async def test_generate_text_errors(config, handler):
    """Test that the generate_text method returns the prompt and error message."""
    prompt = config.prompts.slogan
    tokens = config.llm.tokens

    async def raise_error(*args, **kwargs):
        response = Response(500, request=args[1])
        raise Exception(response)

    with patch.object(
        handler.http_client, "post", new=AsyncMock(side_effect=raise_error)
    ):
        index, text = await handler.generate_text("test", prompt, tokens)
        assert index == "test"
        assert isinstance(text, str)


@pytest.mark.asyncio
async def test_generate_text_http_error(config, handler):
    """Test that HTTPStatusError is raised when the number of tokens exceeds the max."""
    prompt = config.prompts.summaries
    tokens = config.llm.tokens
    mock_response = MagicMock()

    async def raise_http_error(*args, **kwargs):
        raise HTTPStatusError(
            message="HTTP Error", request=MagicMock(), response=mock_response
        )

    with patch.object(
        handler.http_client,
        "post",
        new=AsyncMock(side_effect=raise_http_error),
    ):
        index, text = await handler.generate_text("test", prompt, tokens)
        assert index == "test"
        assert "HTTP" in text


@pytest.mark.asyncio
async def test_generate_text_retry_error(config, handler):
    """Test that RetryError is raised when the number of tokens exceeds the max."""
    prompt = config.prompts.overview
    tokens = config.llm.tokens

    async def raise_retry_error(*args, **kwargs):
        raise RetryError(last_attempt=MagicMock())

    with patch.object(
        handler.http_client,
        "post",
        new=AsyncMock(side_effect=raise_retry_error),
    ):
        index, text = await handler.generate_text("test", prompt, tokens)
        assert index == "test"
        assert "Retry" in text


@pytest.mark.asyncio
async def test_generate_text_general_exception(config, handler):
    """Test that general exceptions are raised."""
    prompt = config.prompts.overview
    tokens = config.llm.tokens

    async def raise_general_exception(*args, **kwargs):
        raise Exception("General error")

    with patch.object(
        handler.http_client,
        "post",
        new=AsyncMock(side_effect=raise_general_exception),
    ):
        index, text = await handler.generate_text("test", prompt, tokens)
        assert index == "test"
        assert "Exception: General error" in text


@pytest.mark.asyncio
async def test_close(handler):
    """Test that the HTTP client is closed."""
    with patch.object(handler.http_client, "aclose", new=AsyncMock()):
        await handler.close()
        handler.http_client.aclose.assert_called_once()
