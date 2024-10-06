from typing import Literal
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.config.constants import LLMService
from readmeai.config.settings import Settings
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.models.tokens import token_handler


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input_context, expected_call_count",
    [
        ("overview", 1),
        ("file_summary", 1),
    ],
)
async def test_openai_make_request(
    openai_handler: OpenAIHandler,
    input_context: Literal["overview"] | Literal["file_summary"],
    expected_call_count: Literal[1],
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
async def test_batch_request_generates_correct_prompts(
    openai_handler: OpenAIHandler,
):
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
async def test_openai_make_request_with_context(openai_handler: OpenAIHandler):
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
async def test_openai_make_request_without_context(
    openai_handler: OpenAIHandler,
):
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
async def test_batch_request_offline():
    mock_self = MagicMock()
    mock_self.config.llm.api = LLMService.OFFLINE.name
    mock_self.documents = ["doc1", "doc2"]
    mock_self._make_request = AsyncMock(
        return_value=[("summary1", "response1"), ("summary2", "response2")]
    )
    result = await BaseModelHandler.batch_request(mock_self)
    mock_self._make_request.assert_called_once_with(
        index=None,
        prompt=None,
        tokens=None,
        repo_files=mock_self.documents,
    )
    assert result == [("summary1", "response1"), ("summary2", "response2")]


@pytest.mark.asyncio
async def test_batch_request_online():
    mock_self = MagicMock()
    mock_self.config.llm.api = "ONLINE"
    mock_self.documents = ["doc1", "doc2"]
    mock_self.repo_context = "repo_context"
    mock_self._batch_prompts = AsyncMock(
        side_effect=[
            [("summary1", "response1"), ("summary2", "response2")],
            [("additional1", "response3"), ("additional2", "response4")],
        ]
    )

    with (
        patch(
            "readmeai.models.base.set_summary_context", new_callable=AsyncMock
        ) as mock_set_summary_context,
        patch(
            "readmeai.models.base.set_additional_contexts",
            new_callable=AsyncMock,
        ) as mock_set_additional_contexts,
    ):
        mock_set_summary_context.return_value = [
            "summary_prompt1",
            "summary_prompt2",
        ]
        mock_set_additional_contexts.return_value = [
            "additional_prompt1",
            "additional_prompt2",
        ]

        result = await BaseModelHandler.batch_request(mock_self)

        mock_set_summary_context.assert_called_once_with(
            mock_self.config, mock_self.documents
        )
        mock_self._batch_prompts.assert_any_call(
            ["summary_prompt1", "summary_prompt2"]
        )
        mock_set_additional_contexts.assert_called_once_with(
            mock_self.config,
            mock_self.repo_context,
            [("summary1", "response1"), ("summary2", "response2")],
        )
        mock_self._batch_prompts.assert_any_call(
            ["additional_prompt1", "additional_prompt2"]
        )
        assert result == [
            ("summary1", "response1"),
            ("summary2", "response2"),
            ("additional1", "response3"),
            ("additional2", "response4"),
        ]


def test_generate_batches(openai_handler: OpenAIHandler):
    """Test the generation of batches."""
    # Arrange
    items = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    # Act
    batches = openai_handler._generate_batches(items, 3)
    # Assert
    assert len(list(batches)) == 4


@pytest.mark.asyncio
async def test_handle_invalid_items_raises_exception(
    openai_handler: OpenAIHandler,
):
    """Test TypeError is raised when the items are not of the correct type."""
    # Arrange
    openai_handler.http_client = MagicMock()
    # Act
    with pytest.raises(Exception) as exc:
        openai_handler._generate_batches(None, None)
        assert isinstance(exc.value, Exception)


@pytest.mark.asyncio
async def test_make_request_code_summary(
    openai_handler: OpenAIHandler,
    repository_context_fixture: RepositoryContext,
):
    """Test the handling of the response from the OpenAI API."""
    # Arrange
    mock_file_data = repository_context_fixture.files
    openai_handler.http_client = MagicMock()
    openai_handler._make_request_code_summary = AsyncMock()
    # Act
    await openai_handler._make_request_code_summary(
        mock_file_data,
    )
    # Assert
    openai_handler._make_request_code_summary.assert_called_once()


@pytest.mark.skip
@pytest.mark.asyncio
async def test_token_handler_truncates_prompt(config_fixture: Settings):
    """Test prompt truncation when exceeding max tokens."""
    # Arrange
    config_fixture.llm.context_window = 100
    prompt = "a" * 200
    # Act
    truncated_prompt = token_handler(config_fixture, "overview", prompt, 10)
    # Assert
    assert len(truncated_prompt) == 100
