"""Unit tests for Git operation utility methods."""

import shutil
import tempfile
from pathlib import Path
from unittest import mock

import pytest

from readmeai.services.git_operations import (
    clone_repo_to_temp_dir,
    find_git_executable,
    validate_file_permissions,
    validate_git_executable,
)


@pytest.fixture
def temp_dir():
    """Returns a temporary directory."""
    dir = tempfile.mkdtemp()
    yield Path(dir)
    shutil.rmtree(dir)


def test_clone_repo_to_temp_dir(temp_dir):
    """Test that the repo is cloned to a temporary directory."""
    repo = "https://github.com/eli64s/readme-ai-streamlit"
    cloned_dir = clone_repo_to_temp_dir(repo)
    assert isinstance(cloned_dir, Path)
    assert cloned_dir.exists()


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
