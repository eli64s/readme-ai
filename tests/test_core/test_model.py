"""Tests for the LLM API handler abstract base class."""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.core.model import ModelHandler
from readmeai.llms.openai import OpenAIHandler


@pytest.mark.asyncio
async def test_openai_handler_sets_attributes(mock_config):
    """Test the setting of attributes for the OpenAIHandler."""
    # Act
    handler = OpenAIHandler(mock_config)

    # Assert
    assert hasattr(handler, "content")
    assert hasattr(handler, "encoder")
    assert hasattr(handler, "endpoint")
    assert hasattr(handler, "model")
    assert hasattr(handler, "prompts")
    assert hasattr(handler, "tokens")
    assert hasattr(handler, "tokens_max")
    assert hasattr(handler, "temperature")


def test_rate_limit_semaphore_initialization(mock_config):
    mock_config.llm.rate_limit = 10  # Example rate limit
    handler = OpenAIHandler(mock_config)
    assert handler.rate_limit_semaphore._value == 10


@pytest.mark.asyncio
async def test_openai_handle_response_with_context(mock_config):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response("test_context")

        # Assert
        mock_handle_response.assert_called_once_with("test_context")
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with("test_context")


@pytest.mark.asyncio
async def test_openai_handle_response_without_context(mock_config):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()
    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await handler._handle_response()

        # Assert
        mock_handle_response.assert_called_once_with()
        handler.http_client.post.assert_not_called()
        mock_handle_response.assert_called_once_with()


@pytest.mark.asyncio
async def test_openai_handle_response_with_context_and_prompt(mock_config):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    handler = OpenAIHandler(mock_config)
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
async def test_batch_request(mock_config, mock_dependencies, mock_summaries):
    """Test the batch request for the OpenAI API."""
    # Arrange
    handler = OpenAIHandler(mock_config)

    with patch.object(
        OpenAIHandler, "_batch_prompts", new_callable=AsyncMock
    ) as mock_batch_prompts:
        # Act
        await handler.batch_request(mock_dependencies, mock_summaries)

        # Assert
        assert mock_batch_prompts.call_count == 2


@pytest.mark.asyncio
def test_generation_of_batches(mock_config):
    """Test the generation of batches from a list of items."""
    items = ["a", "b", "c", "d", "e"]
    expected_batch1 = ["a", "b"]
    expected_batch2 = ["c", "d"]
    expected_batch3 = ["e"]

    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()

    # Act
    test_batch = list(handler._generate_batches(items, 2))

    # Assert
    assert len(test_batch) == 3
    assert isinstance(test_batch, list)
    assert test_batch[0] == expected_batch1
    assert test_batch[1] == expected_batch2
    assert test_batch[2] == expected_batch3


@pytest.mark.asyncio
async def test_batch_prompts(mock_config):
    """Test the processing of prompts in batches and the return of the generated text."""
    # Arrange
    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()

    with patch.object(
        OpenAIHandler, "_process_batch", new_callable=AsyncMock
    ) as mock_process_batch:
        # Act
        await handler._batch_prompts(["test_prompt"])

        # Assert
        mock_process_batch.assert_called_once_with("test_prompt")
        handler.http_client.post.assert_not_called()
        mock_process_batch.assert_called_once_with("test_prompt")


@pytest.mark.asyncio
async def test_process_batch(mock_config):
    """Test the processing of a prompt and the return of the generated text."""
    test_handler = OpenAIHandler(mock_config)
    test_handler.http_client = MagicMock()

    with patch.object(
        OpenAIHandler, "_handle_response_code_summary", new_callable=AsyncMock
    ) as mock_handle_response_code_summary:
        # Act
        await test_handler._process_batch(
            {"type": "summaries", "context": "test"}
        )

        # Assert
        mock_handle_response_code_summary.assert_called_once_with("test")
        test_handler.http_client.post.assert_not_called()
        mock_handle_response_code_summary.assert_called_once_with("test")


@pytest.mark.asyncio
async def test_handle_response_code_summary(mock_config, mock_file_data):
    """Test the generation of code summaries for the README.md file."""
    test_handler = OpenAIHandler(mock_config)
    test_handler.http_client = MagicMock()

    with patch.object(
        OpenAIHandler, "_handle_response", new_callable=AsyncMock
    ) as mock_handle_response:
        # Act
        await test_handler._handle_response(
            mock_file_data, mock_config.prompts.summaries
        )

        # Assert
        assert "summary" in mock_handle_response.call_args[0][1]
        test_handler.http_client.post.assert_not_called()
        assert isinstance(mock_handle_response.call_args[0][1], str)


@pytest.mark.parametrize("invalid_item", [[1, 2], {"key": "value"}])
def test_invalid_types_in_items_raises_exception(invalid_item, mock_config):
    """Test that the TypeError is raised when the items are not of the correct type."""
    items = ["a", "b", invalid_item]
    handler = OpenAIHandler(mock_config)
    handler.http_client = MagicMock()

    with pytest.raises(TypeError) as exc:
        list(ModelHandler._generate_batches(items, 2))
    assert isinstance(exc.value, TypeError)
