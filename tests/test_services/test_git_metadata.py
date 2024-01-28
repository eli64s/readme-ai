"""Unit tests for fetching Git repository metadata from multiple providers."""

from dataclasses import asdict
from unittest.mock import AsyncMock, patch

import aiohttp
import pytest

from readmeai.services.git_metadata import (
    RepositoryMetadata,
    _fetch_repository_metadata,
    fetch_git_repository_metadata,
)


@pytest.fixture
def metadata():
    """Returns a RepositoryMetadata instance."""
    return RepositoryMetadata(
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
    """Tests the RepositoryMetadata dataclass types."""
    assert isinstance(metadata.name, str)
    assert isinstance(metadata.languages, list)


def test_metadata_values(metadata):
    """Tests the RepositoryMetadata dataclass values."""
    assert metadata.forks_count == 5
    assert metadata.language == "Python"


def test_metadata_asdict(metadata):
    """Tests the RepositoryMetadata asdict method."""
    dict_rep = asdict(metadata)
    assert dict_rep["name"] == "test-repo"
    assert dict_rep["topics"] == ["test", "example"]


def test_process_repo_metadata(metadata):
    """Tests the process_repo_metadata method."""
    assert isinstance(metadata, RepositoryMetadata)


@pytest.mark.asyncio
async def test_fetch_git_repository_metadata_success():
    """Tests the fetch_git_repository_metadata method."""
    repo_name = "example-repo"
    repo_owner = "example-owner"
    full_name = f"{repo_owner}/{repo_name}"
    with patch(
        "readmeai.services.git_utils.fetch_git_api_url",
        return_value="api_url",
    ), patch(
        "readmeai.services.git_metadata._fetch_repository_metadata",
        return_value={
            "name": repo_name,
            "full_name": full_name,
        },
    ):
        metadata = await fetch_git_repository_metadata(
            AsyncMock(), "https://github.com/example.com"
        )
        assert metadata.name == repo_name
        assert metadata.full_name == full_name


@pytest.mark.asyncio
async def test_fetch_git_repository_metadata_failure():
    """Tests the fetch_git_api method."""
    url = "https://api.github.com/badurl"

    with patch("aiohttp.ClientSession.get") as mock_get:
        mock_response = AsyncMock()
        mock_response.status = 404
        mock_response.headers = {"Content-Type": "application/json"}
        mock_response.json = AsyncMock(return_value={})
        mock_response.raise_for_status.side_effect = (
            aiohttp.ClientResponseError(
                request_info=mock_response.request_info,
                history=mock_response.history,
                status=mock_response.status,
                message="Not Found",
            )
        )
        mock_get.return_value.__aenter__.return_value = mock_response
        with pytest.raises(aiohttp.ClientResponseError) as exc:
            await _fetch_repository_metadata(mock_get, url)
        assert isinstance(exc.value, aiohttp.ClientResponseError)
