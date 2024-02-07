"""Tests for utility functions in the core module."""

import os
from pathlib import Path
from unittest.mock import patch

from readmeai.config.enums import LLMOptions, SecretKeys
from readmeai.config.settings import ConfigHelper
from readmeai.core.utils import (
    format_md_table,
    format_md_text,
    get_resource_path,
    is_file_ignored,
    scan_environment,
    setup_environment,
)


def test_format_md_table():
    """Test that the markdown table is extracted from the input string."""
    test_string = """<remove this>
    | Column 1 | Column 2 | Column 3 |
    | -------- | -------- | -------- |
    | Content  | Content  | Content  |
    | Content  | Content  | Content  |
    | Content  | Content  | Content  |
    and this
    """
    result = format_md_table(test_string)
    assert isinstance(result, str)
    assert "<remove this>" not in result
    assert "and this" not in result


def test_format_md_text():
    """Test that the markdown text is extracted from the input string."""
    text = "'hello world'"
    formatted_sentence = format_md_text(text)
    assert formatted_sentence == "hello world"


def test_is_file_ignored(mock_config_helper: ConfigHelper):
    """Test that the file is ignored."""
    file_path_ignored = Path("README.md")
    file_path_not_ignored = Path("readmeai/main.py")
    assert is_file_ignored(mock_config_helper, file_path_ignored) is True
    assert is_file_ignored(mock_config_helper, file_path_not_ignored) is False


def test_get_resource_path_from_resources(monkeypatch):
    """Test that the resource path is returned from importlib.resources."""

    def mock_resources_files(package):
        return Path("/fake/path")

    monkeypatch.setattr("importlib.resources.files", mock_resources_files)

    package = "readmeai"
    resource_name = "data.txt"
    expected = Path("/fake/path") / resource_name
    actual = get_resource_path(package, resource_name)
    assert actual == expected


def test_get_resource_path_from_pkg_resources(monkeypatch):
    """Test that the resource path is returned from pkg_resources."""

    def mock_resource_filename(package, resource_name):
        return f"/fake/path/{resource_name}"

    monkeypatch.setattr(
        "pkg_resources.resource_filename", mock_resource_filename
    )

    package = "readmeai"
    resource_name = "settings/ignore_files.toml"
    expected = Path().cwd() / "readmeai/settings/ignore_files.toml"
    actual = get_resource_path(package, resource_name)
    assert actual == expected


def test_get_resource_path_handles_importerror(monkeypatch):
    """Test that the function handles ImportError."""

    def raise_typeerror():
        raise TypeError

    monkeypatch.setattr("importlib.resources.files", raise_typeerror)

    package = "readmeai"
    resource_name = "settings/ignore_files.toml"
    expected = str(Path().cwd() / "readmeai/settings/ignore_files.toml")
    actual = get_resource_path(package, resource_name)
    assert actual == expected


def test_setup_environment_openai(mock_config, monkeypatch):
    """Test that the environment is setup correctly for OpenAI."""
    mock_config.llm.api = LLMOptions.OPENAI.name
    monkeypatch.setenv(SecretKeys.OPENAI_API_KEY.name, "sk-test-key")
    setup_environment(mock_config, mock_config.llm.api)
    assert os.getenv(SecretKeys.OPENAI_API_KEY.name) == "sk-test-key"


def test_setup_environment_vertex(mock_config, monkeypatch):
    """Test that the environment is setup correctly for Vertex."""
    mock_config.llm.api = LLMOptions.VERTEX.name
    monkeypatch.setenv(SecretKeys.VERTEXAI_LOCATION.name, "us-central1")
    monkeypatch.setenv(SecretKeys.VERTEXAI_PROJECT.name, "test-project")
    setup_environment(mock_config, mock_config.llm.api)
    assert os.getenv(SecretKeys.VERTEXAI_LOCATION.name) == "us-central1"
    assert os.getenv(SecretKeys.VERTEXAI_PROJECT.name) == "test-project"


@patch.dict("os.environ", {}, clear=True)
def test_enable_offline_model(mock_config):
    """Test that the environment is setup correctly for offline mode."""
    setup_environment(mock_config, None)
    assert mock_config.llm.api == LLMOptions.OFFLINE.name
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_no_api_specified_but_openai_settings_exist_in_env(mock_config):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.model = "gpt-3.5-turbo"
    mock_config.llm.offline = False
    os.environ[SecretKeys.OPENAI_API_KEY.value] = "sk-test-key"
    setup_environment(mock_config, None)
    assert mock_config.llm.api == LLMOptions.OPENAI.name
    assert mock_config.llm.model == "gpt-3.5-turbo"
    assert mock_config.llm.offline is False


@patch.dict("os.environ", {}, clear=True)
def test_no_api_specified_but_vertex_settings_exist_in_env(mock_config):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.model = "gpt-3.5-turbo"
    mock_config.llm.offline = False
    os.environ[SecretKeys.VERTEXAI_LOCATION.value] = "us-central1"
    os.environ[SecretKeys.VERTEXAI_PROJECT.value] = "test-project"
    setup_environment(mock_config, None)
    assert mock_config.llm.api == LLMOptions.VERTEX.name
    assert mock_config.llm.model == "gemini-pro"
    assert mock_config.llm.offline is False


@patch.dict("os.environ", {}, clear=True)
def test_scan_environment_openai(monkeypatch):
    """Test that the environment variables are scanned correctly."""
    keys = (SecretKeys.OPENAI_API_KEY.name,)
    monkeypatch.setenv(SecretKeys.OPENAI_API_KEY.name, "sk-test-key")
    assert scan_environment(keys) is True


@patch.dict("os.environ", {}, clear=True)
def test_scan_environment_vertex(monkeypatch):
    """Test that the environment variables are scanned correctly."""
    keys = (
        SecretKeys.VERTEXAI_LOCATION.name,
        SecretKeys.VERTEXAI_PROJECT.name,
    )
    monkeypatch.setenv(SecretKeys.VERTEXAI_LOCATION.name, "us-central1")
    monkeypatch.setenv(SecretKeys.VERTEXAI_PROJECT.name, "test-project")
    assert scan_environment(keys) is True


@patch.dict("os.environ", {}, clear=True)
def test_scan_environment_missing():
    """Test that the environment variables are scanned correctly."""
    keys = ("OPENAI_API",)
    assert scan_environment(keys) is False
    keys = ("VERTEX_LOCATION", "VERTEX_PROJECT")
    assert scan_environment(keys) is False


@patch.dict("os.environ", {}, clear=True)
def test_missing_openai_settings_so_enable_offline_mode(mock_config):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.offline = False
    assert mock_config.llm.offline is False
    setup_environment(mock_config, LLMOptions.OPENAI.name)
    assert mock_config.llm.offline is True


@patch.dict("os.environ", {}, clear=True)
def test_missing_vertex_settings_so_enable_offline_mode(mock_config):
    """Test that the environment variables are scanned correctly."""
    mock_config.llm.offline = False
    assert mock_config.llm.offline is False
    setup_environment(mock_config, LLMOptions.VERTEX.name)
    assert mock_config.llm.offline is True
