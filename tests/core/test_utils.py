"""Tests for utility functions in the core module."""

import os
from pathlib import Path
from unittest.mock import patch

from readmeai.config.enums import ModelOptions, SecretKeys
from readmeai.config.settings import ConfigLoader
from readmeai.core.utils import (
    _scan_environ,
    _set_offline,
    filter_file,
    set_model_engine,
)


def test_filter_file(mock_configs: ConfigLoader):
    """Test that the file is ignored."""
    file_path_ignored = Path("README.md")
    file_path_not_ignored = Path("readmeai/main.py")
    assert filter_file(mock_configs, file_path_ignored) is True
    assert filter_file(mock_configs, file_path_not_ignored) is False


def test_filter_file_all_conditions_false():
    """Test that the file is not ignored."""
    # Arrange
    config_loader = ConfigLoader()
    file_path = Path("example.txt")
    ignore_files = {
        "blacklist": {"files": [], "extensions": [], "directories": []}
    }
    config_loader.blacklist = ignore_files
    # Act
    assert filter_file(config_loader, file_path) is False


@patch.dict("os.environ", {}, clear=True)
def test_set_model_engine_openai(mock_config, monkeypatch):
    """Test that the environment is setup correctly for OpenAI."""
    mock_config.llm.api = ModelOptions.OPENAI.name
    monkeypatch.setenv(SecretKeys.OPENAI_API_KEY.name, "sk-test-key")
    set_model_engine(mock_config)
    assert os.getenv(SecretKeys.OPENAI_API_KEY.name) == "sk-test-key"


def test_set_model_engine_vertex(mock_config, monkeypatch):
    """Test that the environment is setup correctly for Vertex."""
    mock_config.llm.api = ModelOptions.VERTEX.name
    monkeypatch.setenv(SecretKeys.VERTEXAI_LOCATION.name, "us-central1")
    monkeypatch.setenv(SecretKeys.VERTEXAI_PROJECT.name, "test-project")
    set_model_engine(mock_config)
    assert os.getenv(SecretKeys.VERTEXAI_LOCATION.name) == "us-central1"
    assert os.getenv(SecretKeys.VERTEXAI_PROJECT.name) == "test-project"


@patch.dict("os.environ", {}, clear=True)
def test_set_offline_mode_directly(mock_config):
    """Test the _set_offline_mode function directly for setting offline mode."""
    mock_config.llm.api = ModelOptions.OFFLINE.name
    _set_offline(mock_config, "Run in offline mode...")
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_offline_mode_when_no_env_vars_set(mock_config):
    """Test that offline mode is set when no environment variables are set."""
    mock_config.llm.api = None
    set_model_engine(mock_config)
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_set_offline_mode(mock_config):
    """Test that the environment is setup correctly for offline mode."""
    mock_config.llm.api = ModelOptions.OFFLINE.name
    mock_config.llm.offline = True
    set_model_engine(mock_config)
    assert mock_config.llm.api == ModelOptions.OFFLINE.name
    assert mock_config.llm.offline is True


def test_incorrect_api_service_sets_offline_mode(mock_config):
    """Test that an incorrect API service input defaults to offline mode."""
    mock_config.llm.api = "non_existent_api"
    set_model_engine(mock_config)
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_no_api_specified_but_openai_settings_exist_in_env(
    mock_config, monkeypatch
):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.api = None
    mock_config.llm.model = "gpt-3.5-turbo"
    mock_config.llm.offline = False
    monkeypatch.setenv(SecretKeys.OPENAI_API_KEY.value, "sk-openai-key")
    set_model_engine(mock_config)
    assert mock_config.llm.api == ModelOptions.OPENAI.name
    assert mock_config.llm.model == "gpt-3.5-turbo"
    assert mock_config.llm.offline is False


@patch.dict("os.environ", {}, clear=True)
def test_no_api_specified_but_vertex_settings_exist_in_env(
    mock_config, monkeypatch
):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.api = None
    mock_config.llm.model = "gpt-3.5-turbo"
    mock_config.llm.offline = False
    monkeypatch.setenv(SecretKeys.VERTEXAI_LOCATION.name, "us-central1")
    monkeypatch.setenv(SecretKeys.VERTEXAI_PROJECT.name, "test-project")
    set_model_engine(mock_config)
    assert mock_config.llm.api == ModelOptions.VERTEX.name
    assert mock_config.llm.model == "gemini-pro"
    assert mock_config.llm.offline is False


@patch.dict("os.environ", {}, clear=True)
def test_missing_openai_settings_so_set_offline_mode(mock_config, monkeypatch):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.api = ModelOptions.OPENAI.name
    set_model_engine(mock_config)
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_missing_vertex_settings_so_set_offline_mode(mock_config):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.api = ModelOptions.VERTEX.name
    mock_config.llm.offline = False
    assert mock_config.llm.offline is False
    set_model_engine(mock_config)
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_scan_environ_openai(monkeypatch):
    """Test that the environment variables are scanned correctly."""
    keys = (SecretKeys.OPENAI_API_KEY.name,)
    monkeypatch.setenv(SecretKeys.OPENAI_API_KEY.name, "sk-test-key")
    assert _scan_environ(keys) is True


@patch.dict("os.environ", {}, clear=True)
def test_scan_environ_vertex(monkeypatch):
    """Test that the environment variables are scanned correctly."""
    keys = (
        SecretKeys.VERTEXAI_LOCATION.name,
        SecretKeys.VERTEXAI_PROJECT.name,
    )
    monkeypatch.setenv(SecretKeys.VERTEXAI_LOCATION.name, "us-central1")
    monkeypatch.setenv(SecretKeys.VERTEXAI_PROJECT.name, "test-project")
    assert _scan_environ(keys) is True


@patch.dict(
    "os.environ",
    {SecretKeys.VERTEXAI_LOCATION.name: "us-central1"},
    clear=True,
)
def test_scan_environ_vertex_partial():
    """Test that the environment variables are scanned correctly when some are missing."""
    keys = (
        SecretKeys.VERTEXAI_LOCATION.name,
        SecretKeys.VERTEXAI_PROJECT.name,
    )
    assert _scan_environ(keys) is False


@patch.dict("os.environ", {}, clear=True)
def test_scan_environ_missing():
    """Test that the environment variables are scanned correctly."""
    keys = ("OPENAI_API",)
    assert _scan_environ(keys) is False
    keys = ("VERTEX_LOCATION", "VERTEX_PROJECT")
    assert _scan_environ(keys) is False
