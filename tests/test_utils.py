"""Unit tests for utility functions."""

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from readmeai import utils


@pytest.fixture
def temp_dir(tmp_path):
    return tmp_path / "repo"


def test_find_git_executable_windows():
    with patch("platform.system") as mock_system:
        mock_system.return_value = "Windows"
        with patch("pathlib.Path.exists") as mock_exists:
            mock_exists.return_value = True
            git_exec_path = utils.find_git_executable()
            assert git_exec_path == Path(
                "C:\\Program Files\\Git\\cmd\\git.EXE"
            )


def test_find_git_executable_linux():
    with patch("platform.system") as mock_system:
        mock_system.return_value = "Linux"
        with patch("os.environ.get") as mock_get:
            mock_get.return_value = None
            with patch("os.environ.__getitem__") as mock_getitem:
                mock_getitem.return_value = "/usr/bin:/usr/local/bin"
                with patch("pathlib.Path.exists") as mock_exists:
                    mock_exists.return_value = True
                    git_exec_path = utils.find_git_executable()
                    assert git_exec_path == Path("/usr/bin/git")


def test_validate_git_executable():
    with pytest.raises(ValueError):
        utils.validate_git_executable(None)
    with pytest.raises(ValueError):
        utils.validate_git_executable("invalid/path/to/git")
    with patch("pathlib.Path.exists") as mock_exists:
        mock_exists.return_value = True
        utils.validate_git_executable("/usr/bin/git")


def test_validate_file_permissions_windows(temp_dir):
    with patch("platform.system") as mock_system:
        mock_system.return_value = "Windows"
        utils.validate_file_permissions(temp_dir)


def test_validate_file_permissions_linux(temp_dir):
    with patch("platform.system") as mock_system:
        mock_system.return_value = "Linux"
        with patch("pathlib.Path.stat") as mock_stat:
            mock_stat.return_value.st_mode = 0o700
            utils.validate_file_permissions(temp_dir)


def test_get_github_file_link():
    file = "README.md"
    user_repo_name = "user/repo"
    link = utils.get_github_file_link(file, user_repo_name)
    assert link == f"https://github.com/{user_repo_name}/blob/main/{file}"


def test_get_user_repository_name_local_path(temp_dir):
    os.makedirs(temp_dir)
    user_repo_name = utils.get_user_repository_name(temp_dir)
    assert user_repo_name == temp_dir.name


def test_get_user_repository_name_github_url():
    url = "https://github.com/user/repo.git"
    user_repo_name = utils.get_user_repository_name(url)
    assert user_repo_name == "user/repo.git"
