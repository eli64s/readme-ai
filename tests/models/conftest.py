"""Fixtures for the LLM API clients."""

from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.anthropic import ANTHROPIC_AVAILABLE, AnthropicHandler
from readmeai.models.enums import GeminiModels
from readmeai.models.gemini import GeminiHandler
from readmeai.models.openai import OpenAIHandler


@pytest.fixture
def mock_config_loader():
    """Fixture to provide a ConfigLoader instance."""
    return ConfigLoader()


@pytest.fixture
def mock_config(mock_config_loader: ConfigLoader):
    """Fixture to provide a Settings instance."""
    config = mock_config_loader.config
    config.llm.tokens = 100
    config.md.placeholder = "<code>❯ REPLACE-ME</code>"
    return config


@pytest.fixture
def mock_aiohttp_session():
    """Fixture to provide a mocked aiohttp.ClientSession."""
    mock_session = MagicMock(spec=aiohttp.ClientSession)
    mock_response_cm = AsyncMock()
    mock_response = AsyncMock(
        json=AsyncMock(
            return_value={
                "choices": [{"message": {"content": "test_response"}}],
            },
        ),
    )
    mock_response.raise_for_status = MagicMock()
    mock_response_cm.__aenter__.return_value = mock_response
    mock_session.post.return_value = mock_response_cm
    return mock_session


@pytest.fixture
def anthropic_handler(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    if not ANTHROPIC_AVAILABLE:
        pytest.skip("Anthropic library is not available")
    context = mock_repository_context
    return AnthropicHandler(
        config_loader=mock_config_loader,
        context=context,
    )


@pytest.fixture
def anthropic_handler_with_mock_session(
    anthropic_handler: AnthropicHandler, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test_api_key")
    mock_create = AsyncMock(
        return_value=MagicMock(content=[MagicMock(text="test_response")])
    )
    anthropic_handler.client.messages.create = mock_create
    return anthropic_handler


@pytest.fixture
def gemini_handler(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
):
    """Fixture to provide a GeminiHandler instance."""
    mock_config_loader.config.llm.model = GeminiModels.GEMINI_FLASH.value
    with (
        patch("google.generativeai.configure"),
        patch.dict("os.environ", {"GOOGLE_API_KEY": "test_key"}, clear=True),
    ):
        yield GeminiHandler(mock_config_loader, mock_repository_context)


@pytest.fixture
def openai_handler(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
    monkeypatch: pytest.MonkeyPatch,
):
    """Fixture to provide an OpenAIHandler instance with a mocked API key."""
    monkeypatch.setenv("OPENAI_API_KEY", "test_api_key")
    return OpenAIHandler(
        config_loader=mock_config_loader,
        context=mock_repository_context,
    )


@pytest.fixture
def openai_handler_with_mock_session(
    openai_handler: OpenAIHandler, mock_aiohttp_session: MagicMock
):
    """Fixture to provide an OpenAIHandler with a mocked session."""
    openai_handler._session = mock_aiohttp_session
    return openai_handler


@pytest.fixture
def ollama_localhost():
    """Fixture to provide a localhost URL for Ollama."""
    return "http://localhost:11434/"
