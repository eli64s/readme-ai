from unittest.mock import patch

import pytest
from readmeai.config.settings import ConfigLoader
from readmeai.core.errors import UnsupportedServiceError
from readmeai.extractors.models import RepositoryContext
from readmeai.models.enums import LLMProviders
from readmeai.models.factory import ModelFactory


def test_get_backend_openai(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
    monkeypatch: pytest.MonkeyPatch,
):
    """Test getting OpenAI backend with proper environment setup."""
    mock_config_loader.config.llm.api = LLMProviders.OPENAI.value
    monkeypatch.setenv("OPENAI_API_KEY", "test_key")
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert handler is not None
    assert handler.__class__.__name__ == "OpenAIHandler"


def test_get_backend_anthropic(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
    monkeypatch: pytest.MonkeyPatch,
):
    """Test getting Anthropic backend."""
    mock_config_loader.config.llm.api = LLMProviders.ANTHROPIC.value
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert handler is not None
    assert handler.__class__.__name__ == "AnthropicHandler"


def test_get_backend_gemini(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
):
    """Test getting Gemini backend."""
    mock_config_loader.config.llm.api = LLMProviders.GEMINI.value
    with patch.dict("os.environ", {"GOOGLE_API_KEY": "test_key"}, clear=True):
        handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
        assert handler is not None
        assert handler.__class__.__name__ == "GeminiHandler"


def test_get_backend_offline(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
):
    """Test getting Offline backend."""
    mock_config_loader.config.llm.api = LLMProviders.OFFLINE.value
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert handler is not None
    assert handler.__class__.__name__ == "OfflineHandler"


def test_get_backend_unsupported_service(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    """Test getting a backend with an unsupported service."""

    class UnsupportedConfig(ConfigLoader):
        """
        Mock config loader that returns a config object with an unsupported service.
        """

        def __init__(self) -> None:
            self.config = type(
                "MockConfig",
                (),
                {"llm": type("MockLLMConfig", (), {"api": "unsupported"})()},
            )()

    unsupported_config = UnsupportedConfig()

    with pytest.raises(UnsupportedServiceError) as e:
        ModelFactory.get_backend(unsupported_config, mock_repository_context)

    assert isinstance(e.value, UnsupportedServiceError)
