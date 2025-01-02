from unittest.mock import AsyncMock, patch

import aiohttp
import pytest
import tenacity
from readmeai.models.gemini import GeminiHandler


def test_gemini_handler_sets_attributes(gemini_handler: GeminiHandler):
    """Test that the Gemini handler sets the correct attributes."""
    assert gemini_handler.model_name == "gemini-1.5-flash"
    assert hasattr(gemini_handler, "model")
    assert hasattr(gemini_handler, "generation_config")
    assert gemini_handler.top_p == 0.9


@pytest.mark.asyncio
async def test_gemini_build_payload(gemini_handler: GeminiHandler):
    """Test payload building for Gemini."""
    payload = await gemini_handler._build_payload("test_prompt")
    assert payload.max_output_tokens == gemini_handler.max_tokens
    assert payload.temperature == gemini_handler.temperature
    assert payload.top_p == gemini_handler.top_p


@pytest.mark.asyncio
async def test_gemini_make_request_success(gemini_handler: GeminiHandler):
    """Test a successful request to the Gemini API."""
    with patch.object(gemini_handler.model, "generate_content_async") as mock_generate:
        mock_response = AsyncMock()
        mock_response.text = "Generated content"
        mock_generate.return_value = mock_response
        index, result = await gemini_handler._make_request(
            "test_index", "test_prompt", 100, None
        )
        assert index == "test_index"
        assert result == "Generated content"
        mock_generate.assert_called_once()


@pytest.mark.asyncio
async def test_gemini_make_request_client_error(gemini_handler: GeminiHandler):
    """Test that a client error triggers retries."""
    with patch.object(gemini_handler.model, "generate_content_async") as mock_generate:
        mock_generate.side_effect = aiohttp.ClientError("Test error")
        with pytest.raises(tenacity.RetryError):
            await gemini_handler._make_request("test_index", "test_prompt", 100, None)


@pytest.mark.asyncio
async def test_gemini_make_request_unexpected_error(gemini_handler: GeminiHandler):
    """Test handling of unexpected errors."""
    with patch.object(gemini_handler.model, "generate_content_async") as mock_generate:
        mock_generate.side_effect = Exception("Unexpected error")
        index, result = await gemini_handler._make_request(
            "test_index", "test_prompt", 100, None
        )
        assert index == "test_index"
        assert result == gemini_handler.placeholder


@pytest.mark.asyncio
async def test_gemini_retry_mechanism(gemini_handler: GeminiHandler):
    """Test retry mechanism for Gemini."""
    with patch.object(gemini_handler.model, "generate_content_async") as mock_generate:
        mock_generate.side_effect = [
            aiohttp.ClientError("Error 1"),
            aiohttp.ClientError("Error 2"),
            AsyncMock(text="Success after retries"),
        ]
        index, result = await gemini_handler._make_request(
            "test_index", "test_prompt", 100, None
        )
        assert index == "test_index"
        assert result == "Success after retries"
        assert mock_generate.call_count == 3


@pytest.mark.asyncio
async def test_gemini_rate_limiting(gemini_handler: GeminiHandler):
    """Test that rate limiting works."""
    gemini_handler.rate_limit_semaphore = AsyncMock()
    with patch.object(gemini_handler.model, "generate_content_async") as mock_generate:
        mock_response = AsyncMock()
        mock_response.text = "Rate limited content"
        mock_generate.return_value = mock_response
        result = await gemini_handler._make_request(
            "test_index", "test_prompt", 100, None
        )
        gemini_handler.rate_limit_semaphore.__aenter__.assert_called_once()
        gemini_handler.rate_limit_semaphore.__aexit__.assert_called_once()
        assert result == ("test_index", "Rate limited content")


@pytest.mark.asyncio
async def test_gemini_token_handler_integration(gemini_handler: GeminiHandler):
    """Test integration with token handler."""
    with patch("readmeai.models.gemini.token_handler") as mock_token_handler:
        mock_token_handler.return_value = "Processed prompt"
        with patch.object(
            gemini_handler.model, "generate_content_async"
        ) as mock_generate:
            mock_response = AsyncMock()
            mock_response.text = "Generated from processed prompt"
            mock_generate.return_value = mock_response
            index, result = await gemini_handler._make_request(
                "test_index", "original prompt", 100, None
            )
            mock_token_handler.assert_called_once_with(
                config=gemini_handler.config,
                index="test_index",
                prompt="original prompt",
                tokens=100,
            )
            assert index == "test_index"
            assert result == "Generated from processed prompt"
