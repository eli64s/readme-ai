"""Unit tests for fetching Git repository metadata from multiple providers."""

from unittest.mock import patch

import pytest
import requests

from readmeai.config.settings import GitApiUrl, GitHost
from readmeai.services import git_metadata


def test_github_repo_metadata():
    """Tests fetching GitHub repository metadata."""
    repo_url = "https://github.com/user/repo"
    with patch(
        "readmeai.services.git_metadata.repo_metadata"
    ) as mock_repo_metadata:
        git_metadata.github_repo_metadata(repo_url)
        mock_repo_metadata.assert_called_with(
            repo_url, git_metadata.GitHost.GITHUB
        )


def test_gitlab_repo_metadata():
    """Tests fetching GitLab repository metadata."""
    repo_url = "https://gitlab.com/user/repo"
    with patch(
        "readmeai.services.git_metadata.repo_metadata"
    ) as mock_repo_metadata:
        git_metadata.gitlab_repo_metadata(repo_url)
        mock_repo_metadata.assert_called_with(
            repo_url, git_metadata.GitHost.GITLAB
        )


@patch("readmeai.services.git_metadata.fetch_api_data")
def test_fetch_api_data_success(mock_requests):
    """Tests successful API request in fetch_api_data()."""
    url = "https://api.github.com/repos/user/repo"
    mock_requests.return_value = {"name": "repo"}
    data = git_metadata.fetch_api_data(url)
    assert data == {"name": "repo"}


@patch("requests.get")
def test_fetch_api_data_error(mock_get):
    """Tests handling errors in fetch_api_data()."""
    mock_get.side_effect = requests.exceptions.RequestException
    with pytest.raises(ValueError) as exc_info:
        git_metadata.fetch_api_data("url")
    assert "API request failed" in str(exc_info.value)


@patch("readmeai.services.git_metadata.fetch_api_data")
def test_repo_metadata(mock_fetch):
    """Tests fetching repository metadata."""
    url = "https://github.com/user/repo"
    git_metadata.repo_metadata(url)
    api_url = f"{git_metadata.GitApiUrl.GITHUB.value}user/repo"
    mock_fetch.assert_called_with(api_url)


def test_parse_repo_url_github():
    """Tests parsing a GitHub repository URL."""
    url = "https://github.com/user/repo"
    expected = f"{GitApiUrl.GITHUB.value}user/repo"
    assert git_metadata.parse_repo_url(url, GitHost.GITHUB.value) == expected


def test_parse_repo_url_gitlab():
    """Tests parsing a GitLab repository URL."""
    url = "https://gitlab.com/user/repo"
    expected = f"{GitApiUrl.GITLAB.value}user%2Frepo"
    assert git_metadata.parse_repo_url(url, GitHost.GITLAB.value) == expected


def test_parse_repo_url_invalid():
    """Tests parsing an invalid repository URL."""
    with pytest.raises(ValueError) as exc_info:
        git_metadata.parse_repo_url("url", "invalid")
    assert "Invalid repository URL" in str(exc_info.value)


def test_git_host_detection():
    """Tests detecting the Git host from a URL."""
    assert (
        git_metadata.GitHost.from_url(GitApiUrl.GITHUB.value) == "github.com"
    )
    assert (
        git_metadata.GitHost.from_url(GitApiUrl.GITLAB.value) == "gitlab.com"
    )
    assert (
        git_metadata.GitHost.from_url(GitApiUrl.BITBUCKET.value)
        == "bitbucket.org"
    )


@patch("readmeai.services.git_metadata.parse_repo_url")
def test_repo_metadata_handles_errors(mock_parse):
    """Tests handling errors in repo_metadata()."""
    mock_parse.return_value = None
    with pytest.raises(ValueError) as exc_info:
        git_metadata.repo_metadata("url")
    assert "Unsupported Git host" in str(exc_info.value)
