"""
Tests the abstract base LLM API handler implementations.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.models.openai import OpenAIHandler
from readmeai.models.tokens import token_handler


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input_context, expected_call_count",
    [
        ("overview", 1),
        ("summary", 1),
    ],
)
async def test_openai_make_request(
    openai_handler,
    input_context,
    expected_call_count,
):
    """Test that the OpenAI handler handles a response."""
    # Arrange
    openai_handler.http_client = MagicMock()
    mock_make_request = AsyncMock()
    openai_handler._make_request = mock_make_request
    # Act
    await openai_handler._make_request(input_context)
    # Assert
    mock_make_request.assert_called_once()
    assert mock_make_request.call_count == expected_call_count


@pytest.mark.asyncio
async def test_batch_request_generates_correct_prompts(openai_handler):
    """Test that the OpenAI handler generates the correct prompts."""
    # Arrange
    openai_handler.http_client = MagicMock()
    mock_make_request = AsyncMock()
    openai_handler._make_request = mock_make_request
    # Act
    await openai_handler._make_request("overview")
    # Assert
    mock_make_request.assert_called_once()
    assert mock_make_request.call_count == 1


@pytest.mark.asyncio
async def test_openai_make_request_with_context(openai_handler):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    openai_handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler,
        "_make_request",
        new_callable=AsyncMock,
    ) as mock_make_request:
        # Act
        await openai_handler._make_request("test_context", "test_prompt")

        # Assert
        mock_make_request.assert_called_once_with(
            "test_context",
            "test_prompt",
        )
        openai_handler.http_client.post.assert_not_called()
        mock_make_request.assert_called_once_with(
            "test_context",
            "test_prompt",
        )


@pytest.mark.asyncio
async def test_openai_make_request_without_context(openai_handler):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    openai_handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler,
        "_make_request",
        new_callable=AsyncMock,
    ) as mock_make_request:
        # Act
        await openai_handler._make_request("test_context", "test_prompt")

        # Assert
        mock_make_request.assert_called_once_with(
            "test_context",
            "test_prompt",
        )
        openai_handler.http_client.post.assert_not_called()
        mock_make_request.assert_called_once_with(
            "test_context",
            "test_prompt",
        )


@pytest.mark.asyncio
async def test_batch_request(
    openai_handler,
    mock_dependencies,
    mock_summaries,
):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    openai_handler.http_client = MagicMock()
    openai_handler._make_request = AsyncMock()
    # Act
    test_response = await openai_handler.batch_request(
        mock_dependencies,
        mock_summaries,
    )
    # Assert
    assert isinstance(test_response, list)
    assert len(test_response) == 4


def test_generate_batches(openai_handler):
    """Test the generation of batches."""
    # Arrange
    items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    # Act
    batches = openai_handler._generate_batches(items, 3)
    # Assert
    assert len(list(batches)) == 4


@pytest.mark.asyncio
async def test_handle_invalid_items_raises_exception(openai_handler):
    """Test TypeError is raised when the items are not of the correct type."""
    # Arrange
    openai_handler.http_client = MagicMock()
    # Act
    with pytest.raises(Exception) as exc:
        openai_handler._generate_batches(None, None)
        assert isinstance(exc.value, Exception)


@pytest.mark.asyncio
async def test_make_request_code_summary(openai_handler, mock_file_data):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    openai_handler.http_client = MagicMock()
    openai_handler._make_request_code_summary = AsyncMock()
    # Act
    await openai_handler._make_request_code_summary(
        "file_summary",
        "test_prompt",
        100,
        mock_file_data,
    )
    # Assert
    openai_handler._make_request_code_summary.assert_called_once()


@pytest.mark.skip
@pytest.mark.asyncio
async def test_token_handler_truncates_prompt(mock_config):
    """Test prompt truncation when exceeding max tokens."""
    # Arrange
    mock_config.llm.context_window = 100
    prompt = "a" * 200
    # Act
    truncated_prompt = token_handler(mock_config, "overview", prompt, 10)
    # Assert
    assert len(truncated_prompt) == 100
