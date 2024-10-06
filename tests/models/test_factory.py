import pytest

from readmeai.config.settings import ConfigLoader, Settings
from readmeai.errors import UnsupportedServiceError
from readmeai.models.factory import ModelFactory
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


def test_model_handler_openai(openai_handler: OpenAIHandler):
    """Test that the model handler returns the correct handler for OpenAI."""
    assert isinstance(openai_handler, OpenAIHandler)


def test_model_handler_gemini(gemini_handler: GeminiHandler):
    """Test model handler returns the correct handler for Gemini."""
    assert isinstance(gemini_handler, GeminiHandler)


def test_model_handler_offline(offline_handler: OfflineHandler):
    """Test model handler returns the correct handler for offline mode."""
    assert isinstance(offline_handler, OfflineHandler)


def test_model_handler_unsupported_service(
    config_fixture: Settings, config_loader_fixture: ConfigLoader
):
    """Test that model handler raises an error for an unsupported service."""
    config_fixture.llm.api = "OpenAGI"
    config_fixture.llm.model = "agi-turbo-3000"
    with pytest.raises(Exception) as exc:
        ModelFactory.get_backend(config_loader_fixture, [])
        assert isinstance(exc.value, UnsupportedServiceError)
        assert str(exc.value) == "Unsupported service: OpenAGI"
