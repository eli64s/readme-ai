"""Unit tests for fetching Git repository metadata from multiple providers."""

from unittest.mock import MagicMock, patch

import pytest
import requests

from readmeai.config.settings import GitService
from readmeai.services import git_metadata


@patch("requests.get")
def test_fetch_git_api_success(mock_get):
    """Tests successful API request in fetch_api_data()."""
    repo_url = "https://gitlab.com/user/repo"
    mock_response = MagicMock()
    mock_response.json.return_value = {"name": "repo"}
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    data = git_metadata.fetch_git_api(repo_url)
    assert data == {"name": "repo"}


@patch("requests.get")
def test_fetch_git_api_error(mock_get):
    """Tests handling errors in fetch_api_data()."""
    mock_get.side_effect = requests.exceptions.RequestException
    with pytest.raises(ValueError) as exc_info:
        git_metadata.fetch_git_api("url")
    assert isinstance(exc_info.value, ValueError)


@patch("readmeai.services.git_metadata.fetch_git_api")
def test_repo_metadata(mock_fetch):
    """Tests fetching repository metadata."""
    github_url = "https://github.com/user/repo"
    git_metadata.repo_metadata(github_url)
    mock_fetch.assert_called_with(GitService.GITHUB.api_url + "user/repo")


def test_parse_repo_url_github():
    """Tests parsing a GitHub repository URL."""
    repo_url = "https://github.com/user/repo"
    expected = f"{GitService.GITHUB.api_url}user/repo"
    assert git_metadata.parse_repo_url(repo_url) == expected


def test_parse_repo_url_gitlab():
    """Tests parsing a GitLab repository URL."""
    repo_url = "https://gitlab.com/user/repo"
    expected = f"{GitService.GITLAB.api_url}user%2Frepo"
    assert git_metadata.parse_repo_url(repo_url) == expected.replace(
        "%2F", "/"
    )


def test_parse_repo_url_invalid():
    """Tests parsing an invalid repository URL."""
    with pytest.raises(ValueError) as exc_info:
        git_metadata.parse_repo_url("url")
    assert "Invalid repository URL" in str(exc_info.value)


@patch("requests.get")
def test_repo_metadata_handles_errors(mock_parse):
    """Tests handling errors in repo_metadata()."""
    mock_parse.return_value = None
    with pytest.raises(ValueError) as exc_info:
        git_metadata.repo_metadata("url")
    assert isinstance(exc_info.value, ValueError)
