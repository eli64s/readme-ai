"""Tests for validator methods used on command-line arguments."""

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from readmeai.config.validators import GitValidator, ModelValidator
from readmeai.exceptions import GitValidationError


def test_set_environment_with_key(monkeypatch, caplog):
    """Test setting the environment with a provided API key."""
    monkeypatch.setattr(os, "environ", {})
    api_key = "test_api_key"
    ModelValidator.set_environment(api_key, {})
    assert os.environ["OPENAI_API_KEY"] == api_key
    assert "Provided API key exported to environment." in caplog.text


def test_set_environment_with_existing_key(monkeypatch, caplog):
    """Test using existing API key in the environment."""
    monkeypatch.setenv("OPENAI_API_KEY", "existing_key")
    result = ModelValidator.set_environment(None, {})
    assert result == "existing_key"


def test_set_environment_no_key(monkeypatch, caplog):
    """Test setting environment in offline mode when no API key is provided."""
    monkeypatch.setattr(os, "environ", {})
    values = {}
    ModelValidator.set_environment(None, values)
    assert values["offline"] is True
    assert "No API key found. Running in offline mode." in caplog.text


@pytest.mark.parametrize(
    "url",
    [
        "https://github.com/user/repo",
        "https://gitlab.com/user/repo",
        "https://bitbucket.org/user/repo",
    ],
)
def test_validate_repository_with_valid_git_url(url):
    """Test validating a valid git URL."""
    assert GitValidator.validate_repository(url) == url


def test_validate_repository_with_valid_directory(tmp_path: Path):
    """Test validating a valid directory."""
    assert isinstance(GitValidator.validate_repository(tmp_path), Path)


def test_validate_repository_with_invalid_url():
    """Test validating an invalid git URL."""
    with pytest.raises(GitValidationError):
        GitValidator.validate_repository("https://invalidurl.com/user/repo")


def test_validate_repository_with_invalid_string():
    """Test validating an invalid string."""
    with pytest.raises(GitValidationError):
        GitValidator.validate_repository("not_a_url_or_directory")


def test_validate_repository_with_non_directory_path(tmp_path: Path):
    """Test validating a non-directory path."""
    non_dir_path = tmp_path / "file.txt"
    non_dir_path.touch()
    with pytest.raises(GitValidationError):
        GitValidator.validate_repository(non_dir_path)


def test_validate_repository_with_exception_during_parsing():
    """Test validating a URL that raises an exception during parsing."""
    with patch("readmeai.config.validators.urlparse") as mock_urlparse:
        mock_urlparse.side_effect = Exception("Parsing error")
        with pytest.raises(GitValidationError):
            GitValidator.validate_repository("https://github.com/user/repo")


@pytest.mark.parametrize(
    "url,expected_full_name",
    [
        ("https://github.com/user/repo", "user/repo"),
        ("https://gitlab.com/user/repo", "user/repo"),
        ("https://bitbucket.org/user/repo", "user/repo"),
    ],
)
def test_validate_full_name_with_valid_git_url(url, expected_full_name):
    """Test validating a valid git URL."""
    values = {"repository": url}
    assert (
        GitValidator.validate_full_name(None, values)
        == expected_full_name.lower()
    )


def test_validate_full_name_with_valid_directory(tmp_path: Path):
    """Test validating a valid directory."""
    repo_path = tmp_path / "repo"
    repo_path.mkdir()
    values = {"repository": repo_path}
    assert GitValidator.validate_full_name(None, values) == "repo"


def test_validate_full_name_with_invalid_url():
    """Test validating an invalid git URL."""
    values = {"repository": "https://invalidurl.com/user/repo"}
    with pytest.raises(GitValidationError):
        GitValidator.validate_full_name(None, values)


def test_validate_full_name_with_non_existing_path():
    """Test validating a non-existing path."""
    values = {"repository": "/non/existing/path"}
    with pytest.raises(GitValidationError):
        GitValidator.validate_full_name(None, values)


@pytest.mark.parametrize(
    "url,expected_service",
    [
        ("https://github.com/user/repo", "GITHUB"),
        ("https://gitlab.com/user/repo", "GITLAB"),
        ("https://bitbucket.org/user/repo", "BITBUCKET"),
    ],
)
def test_set_host_with_valid_git_url(url, expected_service):
    """Test setting the host with a valid git URL."""
    values = {"repository": url}
    assert GitValidator.set_host(None, values) == expected_service.lower()


def test_set_host_with_local_directory(tmp_path: Path):
    """Test setting the host with a local directory."""
    values = {"repository": tmp_path}
    assert GitValidator.set_host(None, values).value == "local"


def test_set_host_with_invalid_url():
    """Test setting the host with an invalid git URL."""
    values = {"repository": "https://invalidurl.com/user/repo"}
    assert GitValidator.set_host(None, values).value == "local"
