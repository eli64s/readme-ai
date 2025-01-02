import pytest
from readmeai.config.settings import ConfigLoader
from readmeai.core.errors import UnsupportedServiceError
from readmeai.extractors.models import RepositoryContext
from readmeai.models.anthropic import AnthropicHandler
from readmeai.models.enums import LLMProviders
from readmeai.models.factory import ModelFactory
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler


def test_get_backend_anthropic(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    mock_config_loader.config.llm.api = LLMProviders.ANTHROPIC.value
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert isinstance(handler, AnthropicHandler)


def test_get_backend_gemini(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    mock_config_loader.config.llm.api = LLMProviders.GEMINI.value
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert isinstance(handler, GeminiHandler)


def test_get_backend_openai(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    mock_config_loader.config.llm.api = LLMProviders.OPENAI.value
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert isinstance(handler, OpenAIHandler)


def test_get_backend_offline(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    mock_config_loader.config.llm.api = LLMProviders.OFFLINE.value
    handler = ModelFactory.get_backend(mock_config_loader, mock_repository_context)
    assert isinstance(handler, OfflineHandler)


def test_get_backend_unsupported_service(
    mock_config_loader: ConfigLoader, mock_repository_context: RepositoryContext
):
    """
    Work around test for unsupported service error. Create mock object that has similar
    structure to the original config but isn't constrained by the same validation rules.

    This allows us to:
    - Not trigger Pydantic validation errors
    - Still test the error handling for unsupported services
    - Maintain the original intent of the test case
    """

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
