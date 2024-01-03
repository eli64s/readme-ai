"""Unit tests for fetching Git repository metadata from multiple providers."""

from dataclasses import asdict
from unittest.mock import AsyncMock, patch

import pytest

from readmeai.services.git_metadata import (
    GitHubRepoMetadata,
    fetch_git_api,
    repo_metadata,
)


@pytest.fixture
def metadata():
    """Returns a GitHubRepoMetadata instance."""
    return GitHubRepoMetadata(
        name="test-repo",
        full_name="owner/test-repo",
        owner="repo-owner",
        owner_url="http://example.com/owner",
        description="Test repository",
        stars_count=10,
        forks_count=5,
        watchers_count=8,
        open_issues_count=3,
        default_branch="main",
        created_at="2020-01-01T00:00:00Z",
        updated_at="2020-02-01T00:00:00Z",
        pushed_at="2020-02-15T00:00:00Z",
        size_kb=2048,
        clone_url_http="http://example.com/clone",
        clone_url_ssh="git@example.com:clone.git",
        contributors_url="http://example.com/contributors",
        languages_url="http://example.com/languages",
        issues_url="http://example.com/issues",
        language="Python",
        languages=["Python", "HTML"],
        topics=["test", "example"],
        has_wiki=True,
        has_issues=True,
        has_projects=False,
        is_private=False,
        homepage_url="http://example.com",
        license_name="MIT",
        license_url="http://example.com/license",
    )


def test_metadata_types(metadata):
    """Tests the GitHubRepoMetadata dataclass types."""
    assert isinstance(metadata.name, str)
    assert isinstance(metadata.languages, list)


def test_metadata_values(metadata):
    """Tests the GitHubRepoMetadata dataclass values."""
    assert metadata.forks_count == 5
    assert metadata.language == "Python"


def test_metadata_asdict(metadata):
    """Tests the GitHubRepoMetadata asdict method."""
    dict_rep = asdict(metadata)

    assert dict_rep["name"] == "test-repo"
    assert dict_rep["topics"] == ["test", "example"]


@pytest.mark.asyncio
async def test_fetch_git_api_success():
    """Tests the fetch_git_api method."""
    url = "https://api.github.com/repos/user/repo"
    data = {"name": "repo"}

    with patch("aiohttp.ClientSession.get") as mock_get:
        mock_response = mock_get.return_value.__aenter__.return_value
        mock_response.status = 200
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json = AsyncMock(return_value=data)

        response = await fetch_git_api(url)
        assert response == data


@pytest.mark.asyncio
async def test_fetch_git_api_failure():
    """Tests the fetch_git_api method."""
    url = "https://api.github.com/badurl"

    with pytest.raises(ValueError):
        await fetch_git_api(url)


@pytest.mark.asyncio
async def test_repo_metadata_success():
    """Tests the repo_metadata method."""
    with patch(
        "readmeai.services.git_utilities.parse_repo_url",
        return_value="api_url",
    ), patch(
        "readmeai.services.git_metadata.fetch_git_api",
        return_value={"name": "example-repo"},
    ):
        metadata = await repo_metadata("https://github.com/example/repo")
        assert metadata.name == "example-repo"


def test_process_repo_metadata(metadata):
    """Tests the process_repo_metadata method."""
    assert isinstance(metadata, GitHubRepoMetadata)
