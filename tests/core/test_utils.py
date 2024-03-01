"""
Tests utility methods in the core.utils module.
"""

from unittest.mock import patch

import pytest

from readmeai._exceptions import UnsupportedServiceError
from readmeai.cli.options import ModelOptions
from readmeai.core.utils import get_environment


@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-openai-key"}, clear=True)
def test_get_environment_openai(mock_configs):
    """Test that the environment is setup correctly for OpenAI."""
    mock_configs.config.llm.api = ModelOptions.OPENAI.name
    mock_configs.config.llm.model = "gpt-3.5-turbo"
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.OPENAI.name
    assert test_model == "gpt-3.5-turbo"


@patch.dict(
    "os.environ",
    {"VERTEXAI_LOCATION": "us-central1", "VERTEXAI_PROJECT": "test-project"},
    clear=True,
)
def test_get_environment_vertex(mock_configs):
    """Test that the environment is setup correctly for Vertex AI."""
    mock_configs.config.llm.api = ModelOptions.VERTEX.name
    mock_configs.config.llm.model = "gemini-pro"
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.VERTEX.name
    assert test_model == "gemini-pro"


@patch.dict("os.environ", {}, clear=True)
def test_offline_mode_when_no_env_vars_set(mock_configs):
    """Test that offline mode is set when no environment variables are set."""
    mock_configs.config.llm.api = None
    mock_configs.config.llm.model = None
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name


@patch.dict("os.environ", {}, clear=True)
def test_set_offline_mode(mock_configs):
    """Test that the environment is setup correctly for offline mode."""
    mock_configs.config.llm.api = ModelOptions.OFFLINE.name
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name


def test_incorrect_api_service_sets_offline_mode(mock_configs):
    """Test that an incorrect API service input defaults to offline mode."""
    mock_configs.config.llm.api = "incorrect-api"
    with pytest.raises(Exception) as exc:
        get_environment(
            mock_configs.config.llm.api, mock_configs.config.llm.model
        )
        assert isinstance(exc.value, UnsupportedServiceError)


@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-openai-key"}, clear=True)
def test_no_api_specified_but_openai_settings_exist_in_env(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = None
    mock_configs.config.llm.model = None
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.OPENAI.name
    assert test_model == "gpt-3.5-turbo"


@patch.dict(
    "os.environ",
    {"VERTEXAI_LOCATION": "us-central1", "VERTEXAI_PROJECT": "test-project"},
    clear=True,
)
def test_no_api_specified_but_vertex_settings_exist_in_env(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = None
    mock_configs.config.llm.model = None
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.VERTEX.name
    assert test_model == "gemini-pro"


@patch.dict("os.environ", {}, clear=True)
def test_missing_openai_settings_so_set_offline_mode(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = ModelOptions.OPENAI.name
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name


@patch.dict("os.environ", {}, clear=True)
def test_missing_vertex_settings_so_set_offline_mode(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = ModelOptions.VERTEX.name
    test_api, test_model = get_environment(
        mock_configs.config.llm.api, mock_configs.config.llm.model
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name
