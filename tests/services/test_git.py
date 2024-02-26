"""Unit tests for git service helper functions."""

import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import git
import pytest

from readmeai.exceptions import GitCloneError
from readmeai.services.git import (
    clone_repository,
    fetch_git_api_url,
    fetch_git_file_url,
    find_git_executable,
    remove_hidden_contents,
    validate_file_permissions,
    validate_git_executable,
)

GIT_URL = "https://github.com/eli64s/readme-ai-streamlit"


@pytest.mark.asyncio
async def test_clone_valid_repo(tmp_path):
    """Test that a valid repository is cloned."""
    cloned_dir = await clone_repository(GIT_URL, tmp_path)
    assert os.path.isdir(cloned_dir)


@pytest.mark.asyncio
async def test_clone_invalid_repo(tmp_path):
    """Test that an invalid repository is not cloned."""
    git_url = "https://invalid/repo.git"
    with pytest.raises(GitCloneError) as exc:
        await clone_repository(git_url, tmp_path)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_nonexistent_local_path(tmp_path):
    """Test that a nonexistent local path is not cloned."""
    local_dir = "/nonexistent/path"
    with pytest.raises(GitCloneError) as exc:
        await clone_repository(local_dir, tmp_path)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_local_repo(tmp_path):
    """Test that a local repository is cloned."""
    with tempfile.TemporaryDirectory() as temp_dir:
        repo_path = Path(temp_dir)
        repo = git.Repo.init(repo_path)
        readme = repo_path / "README.md"
        readme.write_text("# Test Repository")
        relative_readme_path = readme.relative_to(repo_path)
        repo.index.add([str(relative_readme_path)])
        repo.index.commit("Initial commit")
        cloned_dir = await clone_repository(temp_dir, tmp_path)
        assert Path(cloned_dir).exists()


@pytest.mark.asyncio
async def test_clone_non_git_url(tmp_path):
    """Test clone failure for non-Git URL."""
    non_git_url = "http://example.com/not-a-git-repo"
    with patch("git.Repo.clone_from") as mock_clone, pytest.raises(
        GitCloneError
    ) as exc:
        mock_clone.side_effect = git.GitCommandError("clone", "error")
        await clone_repository(non_git_url, tmp_path)
        assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_clone_local_path_is_file(tmp_path):
    """Test that local path which is a file raises an error."""
    with tempfile.NamedTemporaryFile() as temp_file, pytest.raises(
        GitCloneError
    ) as exc:
        await clone_repository(temp_file.name, tmp_path)
    assert isinstance(exc.value, GitCloneError)


@pytest.mark.asyncio
async def test_remove_hidden_contents(tmp_path):
    """Test that hidden files and directories are removed."""
    with tmp_path:
        (tmp_path / "visible_file.txt").touch()
        (tmp_path / ".hidden_file.txt").touch()
        (tmp_path / "visible_dir").mkdir()
        (tmp_path / ".hidden_dir").mkdir()
        (tmp_path / ".github").mkdir()

        await remove_hidden_contents(tmp_path)

        # Assert hidden files and directories are removed
        assert not (tmp_path / ".hidden_file.txt").exists()
        assert not (tmp_path / ".hidden_dir").exists()

        # Assert visible files and directories and '.github' remain
        assert (tmp_path / "visible_file.txt").exists()
        assert (tmp_path / "visible_dir").exists()
        assert (tmp_path / ".github").exists()


@pytest.mark.asyncio
async def test_fetch_git_api_url(mock_config):
    git_url = "https://github.com/eli64s/readme-ai"
    expected_api_url = "https://api.github.com/repos/eli64s/readme-ai"
    api_url = await fetch_git_api_url(git_url)
    assert api_url == expected_api_url


@pytest.mark.asyncio
async def test_fetch_git_api_url_unsupported_service():
    """Test method for parsing the repository URL."""
    unsupported_service_url = "https://unsupported.com/username/repository"
    with pytest.raises(ValueError) as exc:
        await fetch_git_api_url(unsupported_service_url)
    assert isinstance(exc.value, ValueError)


def test_fetch_git_file_url(mock_config):
    full_name = "eli64s/readme-ai"
    file_path = "main.py"
    repo_url = "https://github.com/eli64s/readme-ai"
    expected_url = "https://github.com/eli64s/readme-ai/blob/master/main.py"
    file_url = fetch_git_file_url(file_path, full_name, repo_url)
    assert file_url == expected_url


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


@patch("readmeai.services.git.platform")
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
    with pytest.raises(SystemExit) as exc:
        validate_file_permissions(mock_file)
    assert isinstance(exc.value, SystemExit)


def test_validate_git_executable_not_exists():
    """Test validation failure if git executable does not exist."""
    with pytest.raises(ValueError) as exc:
        validate_git_executable("/invalid/git/path")
    assert isinstance(exc.value, ValueError)


def test_validate_file_permissions_insufficient():
    """Test file permission validation for insufficient permissions."""
    mock_file = MagicMock()
    mock_file.stat.return_value.st_mode = 0o600  # Not enough permissions
    with pytest.raises(SystemExit) as exc:
        validate_file_permissions(mock_file)
    assert isinstance(exc.value, SystemExit)
