"""Unit tests for readmeai.settings."""

from readmeai.config.settings import (
    BadgeCliOptions,
    GitApiUrl,
    GitFileUrl,
    GitHost,
)
from readmeai.utils import utils


def test_git_host():
    """Test the default hostnames of Git repositories."""
    assert GitHost.LOCAL == "local"
    assert GitHost.GITHUB == "github.com"
    assert GitHost.GITLAB == "gitlab.com"
    assert GitHost.BITBUCKET == "bitbucket.org"


def test_api_base_urls():
    """Test the base URLs of Git repository APIs."""
    assert GitApiUrl.GITHUB == "https://api.github.com"
    assert GitApiUrl.GITLAB == "https://api.gitlab.com"
    assert GitApiUrl.BITBUCKET == "https://api.bitbucket.org"


def test_git_file_urls():
    """Test the URLs pointing to files in Git repositories."""
    repo_name = "readme-ai"
    file_name = "main.py"
    local_url = f"{file_name}"
    github_url = GitFileUrl.GITHUB.value.format(
        repo_name=repo_name, file_name=file_name
    )
    gitlab_url = GitFileUrl.GITLAB.value.format(
        repo_name=repo_name, file_name=file_name
    )
    bitbucket_url = GitFileUrl.BITBUCKET.value.format(
        repo_name=repo_name, file_name=file_name
    )
    assert isinstance(local_url, str)
    assert isinstance(github_url, str)
    assert isinstance(gitlab_url, str)
    assert isinstance(bitbucket_url, str)
    assert local_url == file_name
    assert utils.is_valid_url(github_url) is True
    assert utils.is_valid_url(gitlab_url) is True
    assert utils.is_valid_url(bitbucket_url) is True


def test_badge_options():
    """Test the CLI options for badge icons."""
    assert BadgeCliOptions.APPS == "apps"
    assert BadgeCliOptions.APPS_LIGHT == "apps-light"
    assert BadgeCliOptions.FLAT == "flat"
    assert BadgeCliOptions.FLAT_SQUARE == "flat-square"
    assert BadgeCliOptions.FOR_THE_BADGE == "for-the-badge"
    assert BadgeCliOptions.PLASTIC == "plastic"
    assert BadgeCliOptions.SOCIAL == "social"
