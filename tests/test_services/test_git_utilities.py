"""Unit tests for git utility methods."""

import pytest

from readmeai.config.enums import GitService
from readmeai.services.git_utilities import get_remote_file_url, parse_repo_url


def test_get_remote_file_url():
    """Test method for getting the remote file URL."""
    file_path = "readmeai/main.py"
    full_name = "eli64s/readme-ai"
    repo_url = "https://github.com/eli64s/readme-ai"
    file_url = get_remote_file_url(file_path, full_name, repo_url)
    expected_url = (
        "https://github.com/eli64s/readme-ai/blob/master/readmeai/main.py"
    )
    assert file_url == expected_url


@pytest.mark.asyncio
async def test_parse_repo_url_success():
    """Test method for parsing the repository URL."""
    git_service_url = "https://github.com/username/repository"
    expected_api_url = f"{GitService.GITHUB.api_url}username/repository"
    assert await parse_repo_url(git_service_url) == expected_api_url


@pytest.mark.asyncio
async def test_parse_repo_url_unsupported_service():
    """Test method for parsing the repository URL."""
    unsupported_service_url = "https://unsupported.com/username/repository"
    with pytest.raises(ValueError) as exc:
        await parse_repo_url(unsupported_service_url)
    assert isinstance(exc.value, ValueError)
