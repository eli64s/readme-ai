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
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.OPENAI.name
    assert test_model == "gpt-3.5-turbo"


@pytest.mark.skip
@patch.dict(
    "os.environ",
    {"GOOGLE_API_KEY": "sk-google-key"},
    clear=True,
)
def test_get_environment_gemini(mock_configs):
    """Test that the environment is setup correctly for Gemini API."""
    mock_configs.config.llm.api = ModelOptions.GEMINI.name
    mock_configs.config.llm.model = "gemini-pro"
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.GEMINI.name
    assert test_model == "gemini-pro"


@patch.dict("os.environ", {}, clear=True)
def test_offline_mode_when_no_env_vars_set(mock_configs):
    """Test that offline mode is set when no environment variables are set."""
    mock_configs.config.llm.api = None
    mock_configs.config.llm.model = None
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name


@patch.dict("os.environ", {}, clear=True)
def test_set_offline_mode(mock_configs):
    """Test that the environment is setup correctly for offline mode."""
    mock_configs.config.llm.api = ModelOptions.OFFLINE.name
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name


def test_incorrect_api_service_sets_offline_mode(mock_configs):
    """Test that an incorrect API service input defaults to offline mode."""
    mock_configs.config.llm.api = "incorrect-api"
    with pytest.raises(Exception) as exc:
        get_environment(
            mock_configs.config.llm.api,
            mock_configs.config.llm.model,
        )
        assert isinstance(exc.value, UnsupportedServiceError)


@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-openai-key"}, clear=True)
def test_no_api_specified_but_openai_settings_exist_in_env(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = None
    mock_configs.config.llm.model = None
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.OPENAI.name
    assert test_model == "gpt-3.5-turbo"


@pytest.mark.skip
@patch.dict(
    "os.environ",
    {"GOOGLE_API_KEY": "sk-google-key"},
    clear=True,
)
def test_no_api_specified_but_gemini_settings_exist_in_env(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = None
    mock_configs.config.llm.model = None
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.GEMINI.name
    assert test_model == "gemini-pro"


@patch.dict("os.environ", {}, clear=True)
def test_missing_openai_settings_so_set_offline_mode(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = ModelOptions.OPENAI.name
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name


@pytest.mark.skip
@patch.dict("os.environ", {}, clear=True)
def test_missing_gemini_settings_so_set_offline_mode(mock_configs):
    """Test that the environment variables are scanned correctly."""
    mock_configs.config.llm.api = ModelOptions.GEMINI.name
    test_api, test_model = get_environment(
        mock_configs.config.llm.api,
        mock_configs.config.llm.model,
    )
    assert test_api == ModelOptions.OFFLINE.name
    assert test_model == ModelOptions.OFFLINE.name
