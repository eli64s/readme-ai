"""Tests for the base large language model handler module."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.models.openai import OpenAIHandler
from readmeai.models.tokens import count_tokens


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_openai_handler_sets_attributes(handler):
    """Test that the OpenAI handler sets the correct attributes."""
    # Assert
    assert hasattr(handler, "content")
    assert hasattr(handler, "encoding")
    assert hasattr(handler, "endpoint")
    assert hasattr(handler, "model")
    assert hasattr(handler, "tokens")
    assert hasattr(handler, "tokens_max")
    assert hasattr(handler, "temperature")
    assert hasattr(handler, "_http_client")
    assert handler.rate_limit_semaphore._value >= 5


@pytest.mark.parametrize(
    "input_context, expected_call_count",
    [
        ("overview", 1),
        ("summary", 1),
    ],
)
@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_openai_handle_response(
    handler, input_context, expected_call_count
):
    """Test that the OpenAI handler handles a response."""
    # Arrange
    handler.http_client = MagicMock()
    mock_handle_response = AsyncMock()
    handler._handle_response = mock_handle_response
    # Act
    await handler._handle_response(input_context)
    # Assert
    mock_handle_response.assert_called_once()
    assert mock_handle_response.call_count == expected_call_count


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_batch_request_generates_correct_prompts(handler):
    """Test that the OpenAI handler generates the correct prompts."""
    # Arrange
    handler.http_client = MagicMock()
    mock_handle_response = AsyncMock()
    handler._handle_response = mock_handle_response
    # Act
    await handler._handle_response("overview")
    # Assert
    mock_handle_response.assert_called_once()
    assert mock_handle_response.call_count == 1


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_openai_handle_response_with_context(handler):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response("test_context", "test_prompt")

        # Assert
        mock_handle_response.assert_called_once_with(
            "test_context", "test_prompt"
        )
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with(
            "test_context", "test_prompt"
        )


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_openai_handle_response_without_context(handler):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response("test_context", "test_prompt")

        # Assert
        mock_handle_response.assert_called_once_with(
            "test_context", "test_prompt"
        )
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with(
            "test_context", "test_prompt"
        )


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_batch_request(handler, mock_dependencies, mock_summaries):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler.http_client = MagicMock()
    # Act
    test_response = await handler.batch_request(
        mock_dependencies, mock_summaries
    )
    # Assert
    assert isinstance(test_response, list)
    assert len(test_response) == 5


def test_generate_batches(handler):
    """Test the generation of batches."""
    # Arrange
    items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    # Act
    batches = handler._generate_batches(items, 3)
    # Assert
    assert len(list(batches)) == 4


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_handle_invalid_items_raises_exception(handler):
    """Test TypeError is raised when the items are not of the correct type."""
    # Arrange
    handler.http_client = MagicMock()
    # Act
    with pytest.raises(Exception) as exc:
        handler._generate_batches(None, None)
        assert isinstance(exc.value, Exception)


@pytest.mark.asyncio
async def test_handle_response_code_summary(handler, mock_file_data):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler.http_client = MagicMock()
    handler._handle_response_code_summary = AsyncMock()
    # Act
    await handler._handle_response_code_summary(
        "file_summary", "test_prompt", 100, mock_file_data
    )
    # Assert
    handler._handle_response_code_summary.assert_called_once()


@pytest.mark.asyncio
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_token_handler_truncates_prompt(handler, mock_config):
    """Test prompt truncation when exceeding max tokens."""
    handler._logger = MagicMock()
    handler.tokens_max = mock_config.llm.tokens_max**2
    encoder = mock_config.llm.encoding
    tokens = 100
    index = "file_summary"
    prompt = "A" * 9999
    handler.tokens_max = 1
    result = await handler._token_handler(index, prompt, tokens)
    assert count_tokens(result, encoder) < count_tokens(prompt, encoder)
    assert len(result) < len(prompt)
