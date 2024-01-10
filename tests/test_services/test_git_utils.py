"""Unit tests for git service helper functions."""

import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import git
import pytest

from readmeai.config.enums import GitService
from readmeai.exceptions import GitCloneError
from readmeai.services.git_utils import (
    clone_to_temporary_directory,
    fetch_git_api_url,
    fetch_git_file_url,
    find_git_executable,
    validate_file_permissions,
    validate_git_executable,
)

GIT_URL = "https://github.com/eli64s/readme-ai-streamlit"


@pytest.mark.asyncio
async def test_clone_valid_repo(tmp_path):
    """Test that a valid repository is cloned."""
    cloned_dir = await clone_to_temporary_directory(GIT_URL, tmp_path)
    assert os.path.isdir(cloned_dir)


@pytest.mark.asyncio
async def test_clone_invalid_repo(tmp_path):
    """Test that an invalid repository is not cloned."""
    git_url = "https://invalid/repo.git"
    with pytest.raises(GitCloneError) as exc:
        await clone_to_temporary_directory(git_url, tmp_path)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_local_repo(tmp_path):
    """Test that a local repository is cloned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        cloned_dir = await clone_to_temporary_directory(tmp_path, temp_dir)
        assert Path(cloned_dir).is_dir() is True
        assert Path(cloned_dir).exists() is True
        assert Path(cloned_dir).is_file() is False


@pytest.mark.asyncio
async def test_clone_nonexistent_local_path(tmp_path):
    """Test that a nonexistent local path is not cloned."""
    local_dir = "/nonexistent/path"
    with pytest.raises(GitCloneError) as exc:
        await clone_to_temporary_directory(local_dir, tmp_path)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_git_command_error(tmp_path):
    """Test clone failure due to GitCommandError."""
    with patch("git.Repo.clone_from") as mock_clone, pytest.raises(
        GitCloneError
    ) as exc:
        mock_clone.side_effect = git.GitCommandError("clone", "error")
        await clone_to_temporary_directory(GIT_URL, tmp_path)
        assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_non_git_url(tmp_path):
    """Test clone failure for non-Git URL."""
    non_git_url = "http://example.com/not-a-git-repo"
    with patch("git.Repo.clone_from") as mock_clone, pytest.raises(
        GitCloneError
    ) as exc:
        mock_clone.side_effect = git.GitCommandError("clone", "error")
        await clone_to_temporary_directory(non_git_url, tmp_path)
        assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_local_path_is_file(tmp_path):
    """Test that local path which is a file raises an error."""
    with tempfile.NamedTemporaryFile() as temp_file, pytest.raises(
        GitCloneError
    ) as exc:
        await clone_to_temporary_directory(temp_file.name, tmp_path)
    assert isinstance(exc.value, GitCloneError)


def test_fetch_git_file_url(mock_config):
    """Test method for getting the remote file URL."""
    full_name = mock_config.git.full_name
    file_path = f"{mock_config.git.name}/main.py"
    repo_url = mock_config.git.repository
    file_url = fetch_git_file_url(file_path, full_name, repo_url)
    expected_url = GitService.GITHUB.file_url_template.format(
        full_name=full_name, file_path=file_path
    )
    assert file_url == expected_url


@pytest.mark.asyncio
async def test_fetch_git_api_url(mock_config):
    """Test method for parsing the repository URL."""
    git_url = mock_config.git.repository
    full_name = mock_config.git.full_name
    expected_api_url = f"{GitService.GITHUB.api_url}{full_name}"
    with patch(
        "aiohttp.ClientSession.get", new_callable=AsyncMock
    ) as mock_response:
        api_url = await fetch_git_api_url(git_url)
        await mock_response.raise_for_status()
        assert api_url == expected_api_url


@pytest.mark.asyncio
async def test_etch_git_api_url_unsupported_service():
    """Test method for parsing the repository URL."""
    unsupported_service_url = "https://unsupported.com/username/repository"
    with pytest.raises(ValueError) as exc:
        await fetch_git_api_url(unsupported_service_url)
    assert isinstance(exc.value, ValueError)


def test_validate_git_executable_invalid_path():
    """Test validation of non-existent git executable path."""
    with pytest.raises(ValueError):
        validate_git_executable("/invalid/git/path")


def test_validate_file_permissions_read_execute():
    """Test file permission validation for lack of read/execute permissions."""
    mock_file = MagicMock()
    mock_file.stat.return_value.st_mode = (
        0o200  # Lack of read/execute permissions
    )
    with pytest.raises(SystemExit):
        validate_file_permissions(mock_file)


def test_find_git_executable():
    """Test that the git executable is found."""
    git_exec_path = find_git_executable()
    assert isinstance(git_exec_path, Path)
    assert git_exec_path.exists()


@patch("readmeai.services.git_utils.platform")
def test_validate_git_executable(mock_platform):
    """Test that the git executable is validated."""
    mock_platform.system.return_value = "Linux"
    git_exec_path = "/usr/bin/git"
    validate_git_executable(git_exec_path)
    assert isinstance(git_exec_path, str)


def test_validate_file_permissions():
    """Test that the file permissions are validated."""
    mock_file = MagicMock()
    mock_file.stat.return_value.st_mode = 0o644
    with pytest.raises(SystemExit):
        validate_file_permissions(mock_file)


def test_validate_git_executable_not_exists():
    """Test validation failure if git executable does not exist."""
    with pytest.raises(ValueError) as exc_info:
        validate_git_executable("/invalid/git/path")
    assert "Git executable not found" in str(exc_info.value)


def test_validate_file_permissions_insufficient():
    """Test file permission validation for insufficient permissions."""
    mock_file = MagicMock()
    mock_file.stat.return_value.st_mode = 0o600  # Not enough permissions
    with pytest.raises(SystemExit):
        validate_file_permissions(mock_file)
