from unittest.mock import AsyncMock, patch

import aiohttp
import google.generativeai as genai
import pytest
import tenacity

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.gemini import GeminiHandler


@pytest.fixture
async def gemini_handler(
    config_loader_fixture: ConfigLoader,
    repository_context_fixture: RepositoryContext,
):
    mock_config_loader = config_loader_fixture
    mock_config_loader.config.llm.model = "gemini-1.5-flash"
    with (
        patch.dict("os.environ", {"GOOGLE_API_KEY": "test_key"}),
        patch("google.generativeai.configure"),
    ):
        yield GeminiHandler(mock_config_loader, repository_context_fixture)


@pytest.mark.asyncio
async def test_model_settings(gemini_handler: GeminiHandler):
    assert gemini_handler.model_name == "gemini-1.5-flash"
    assert isinstance(gemini_handler.model, genai.GenerativeModel)
    assert gemini_handler.top_p == 0.9


@pytest.mark.asyncio
async def test_build_payload(gemini_handler: GeminiHandler):
    payload = await gemini_handler._build_payload("test prompt", 100)
    assert isinstance(payload, genai.types.GenerationConfig)
    assert payload.max_output_tokens == 699
    assert payload.temperature == 0.1
    assert payload.top_p == 0.9


@pytest.mark.asyncio
async def test_make_request_success(gemini_handler: GeminiHandler):
    with patch.object(
        gemini_handler.model, "generate_content_async"
    ) as mock_generate:
        mock_response = AsyncMock()
        mock_response.text = "Generated content"
        mock_generate.return_value = mock_response

        result = await gemini_handler._make_request(
            "test_index", "test prompt", 100, None
        )

        assert result == ("test_index", "Generated content")
        mock_generate.assert_called_once()


@pytest.mark.asyncio
async def test_make_request_client_error(gemini_handler: GeminiHandler):
    with patch.object(
        gemini_handler.model, "generate_content_async"
    ) as mock_generate:
        mock_generate.side_effect = aiohttp.ClientError("Test error")

        with pytest.raises(tenacity.RetryError):
            await gemini_handler._make_request(
                "test_index", "test prompt", 100, None
            )
            assert mock_generate.call_count == 3


@pytest.mark.asyncio
async def test_make_request_unexpected_error(gemini_handler: GeminiHandler):
    with patch.object(
        gemini_handler.model, "generate_content_async"
    ) as mock_generate:
        mock_generate.side_effect = Exception("Unexpected error")

        result = await gemini_handler._make_request(
            "test_index", "test prompt", 100, None
        )

        assert result == ("test_index", gemini_handler.placeholder)


@pytest.mark.asyncio
async def test_retry_mechanism(gemini_handler: GeminiHandler):
    with patch.object(
        gemini_handler.model, "generate_content_async"
    ) as mock_generate:
        mock_generate.side_effect = [
            aiohttp.ClientError("Error 1"),
            aiohttp.ClientError("Error 2"),
            AsyncMock(text="Success after retries"),
        ]

        result = await gemini_handler._make_request(
            "test_index", "test prompt", 100, None
        )

        assert result == ("test_index", "Success after retries")
        assert mock_generate.call_count == 3


@pytest.mark.asyncio
async def test_rate_limiting(gemini_handler: GeminiHandler):
    gemini_handler.rate_limit_semaphore = AsyncMock()

    with patch.object(
        gemini_handler.model, "generate_content_async"
    ) as mock_generate:
        mock_response = AsyncMock()
        mock_response.text = "Rate limited content"
        mock_generate.return_value = mock_response

        await gemini_handler._make_request(
            "test_index", "test prompt", 100, None
        )

        gemini_handler.rate_limit_semaphore.__aenter__.assert_called_once()
        gemini_handler.rate_limit_semaphore.__aexit__.assert_called_once()


@pytest.mark.asyncio
async def test_token_handler_integration(gemini_handler: GeminiHandler):
    with patch("readmeai.models.gemini.token_handler") as mock_token_handler:
        mock_token_handler.return_value = "Processed prompt"
        with patch.object(
            gemini_handler.model, "generate_content_async"
        ) as mock_generate:
            mock_response = AsyncMock()
            mock_response.text = "Generated from processed prompt"
            mock_generate.return_value = mock_response

            await gemini_handler._make_request(
                "test_index", "original prompt", 100, None
            )

            mock_token_handler.assert_called_once_with(
                gemini_handler.config, "test_index", "original prompt", 100
            )
            mock_generate.assert_called_once_with(
                "Processed prompt",
                generation_config=mock_generate.call_args[1][
                    "generation_config"
                ],
            )
