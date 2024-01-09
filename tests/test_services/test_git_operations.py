"""Unit tests for Git operation utility methods."""

import os
import tempfile
from pathlib import Path
from unittest import mock

import git
import pytest

from readmeai.exceptions import GitCloneError
from readmeai.services.git_operations import (
    clone_repo_to_temp_dir,
    find_git_executable,
    validate_file_permissions,
    validate_git_executable,
)

TEST_REPO_URL = "https://github.com/eli64s/readme-ai-streamlit"


@pytest.mark.asyncio
async def test_clone_valid_repo():
    """Test that a valid repository is cloned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        cloned_dir = await clone_repo_to_temp_dir(TEST_REPO_URL, temp_dir)
        assert os.path.isdir(cloned_dir)


@pytest.mark.asyncio
async def test_clone_invalid_repo():
    """Test that an invalid repository is not cloned."""
    with tempfile.TemporaryDirectory() as temp_dir, pytest.raises(
        GitCloneError
    ) as exc:
        await clone_repo_to_temp_dir("https://invalid/repo.git", temp_dir)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_local_repo(tmp_path):
    """Test that a local repository is cloned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        cloned_dir = await clone_repo_to_temp_dir(tmp_path, temp_dir)
        assert Path(cloned_dir).is_dir() is True
        assert Path(cloned_dir).exists() is True
        assert Path(cloned_dir).is_file() is False


@pytest.mark.asyncio
async def test_clone_nonexistent_local_path():
    """Test that a nonexistent local path is not cloned."""
    with tempfile.TemporaryDirectory() as temp_dir, pytest.raises(
        GitCloneError
    ) as exc:
        await clone_repo_to_temp_dir("/nonexistent/path", temp_dir)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_git_command_error(tmp_path):
    """Test clone failure due to GitCommandError."""
    with mock.patch("git.Repo.clone_from") as mock_clone, pytest.raises(
        GitCloneError
    ) as exc:
        mock_clone.side_effect = git.GitCommandError("clone", "error")
        await clone_repo_to_temp_dir(TEST_REPO_URL, tmp_path)
        assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_non_git_url(tmp_path):
    """Test clone failure for non-Git URL."""
    with mock.patch("git.Repo.clone_from") as mock_clone, pytest.raises(
        GitCloneError
    ) as exc:
        mock_clone.side_effect = git.GitCommandError("clone", "error")
        await clone_repo_to_temp_dir(
            "http://example.com/not-a-git-repo", tmp_path
        )
        assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_local_path_is_file():
    """Test that local path which is a file raises an error."""
    with tempfile.NamedTemporaryFile() as temp_file, pytest.raises(
        GitCloneError
    ) as exc:
        await clone_repo_to_temp_dir(temp_file.name, "/some/temp/dir")
    assert isinstance(exc.value, GitCloneError)


def test_validate_git_executable_invalid_path():
    """Test validation of non-existent git executable path."""
    with pytest.raises(ValueError):
        validate_git_executable("/invalid/git/path")


def test_validate_file_permissions_read_execute():
    """Test file permission validation for lack of read/execute permissions."""
    mock_file = mock.MagicMock()
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


@mock.patch("readmeai.services.git_operations.platform")
def test_validate_git_executable(mock_platform):
    """Test that the git executable is validated."""
    mock_platform.system.return_value = "Linux"
    git_exec_path = "/usr/bin/git"
    validate_git_executable(git_exec_path)
    assert isinstance(git_exec_path, str)


def test_validate_file_permissions():
    """Test that the file permissions are validated."""
    mock_file = mock.MagicMock()
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
    mock_file = mock.MagicMock()
    mock_file.stat.return_value.st_mode = 0o600  # Not enough permissions
    with pytest.raises(SystemExit):
        validate_file_permissions(mock_file)
