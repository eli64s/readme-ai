"""Unit tests for main module."""

from unittest.mock import MagicMock, patch

import pytest

from readmeai.app import main


@pytest.mark.asyncio
async def test_main():
    repository = "https://github.com/user/repo.git"
    with patch("readmeai.model.OpenAIHandler") as mock_openai_handler:
        mock_openai_handler_instance = MagicMock()
        mock_openai_handler.return_value = mock_openai_handler_instance
        await main(repository)
        mock_openai_handler.assert_called_once_with(main.config)
        mock_openai_handler_instance.code_to_text.assert_called_once()
        mock_openai_handler_instance.chat_to_text.assert_called_once()
