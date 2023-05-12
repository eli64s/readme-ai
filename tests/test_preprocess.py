"""Unit tests for preprocess.py."""

from pathlib import Path
from unittest.mock import patch

import pytest

import src.preprocess as preprocess

"""Tests for the _clone_or_copy_repository function."""


# Test valid github repository url
def test_clone_valid_github(temp_dir):
    repo = "https://github.com/pytest-dev/pytest"
    preprocess._clone_or_copy_repository(repo, temp_dir)
    assert (temp_dir / "pytest").is_dir()


# Test valid local directory
def test_copy_valid_local_dir(temp_dir):
    local_dir = "/path/to/local/dir"
    Path(local_dir).mkdir(parents=True, exist_ok=True)
    preprocess._clone_or_copy_repository(local_dir, temp_dir)
    assert (temp_dir / "dir").is_dir()


# Test invalid repository link
def test_clone_invalid_link(temp_dir):
    repo = "invalidlink"
    with pytest.raises(ValueError):
        preprocess._clone_or_copy_repository(repo, temp_dir)


# Test function raises ValueError for invalid github repository url
def test_clone_invalid_github(temp_dir):
    repo = "https://github.com/invalid/repo"
    with pytest.raises(ValueError):
        preprocess._clone_or_copy_repository(repo, temp_dir)


# Test function raises ValueError for invalid local directory
def test_copy_invalid_local_dir(temp_dir):
    local_dir = "/path/to/invalid/dir"
    with pytest.raises(ValueError):
        preprocess._clone_or_copy_repository(local_dir, temp_dir)


# Test that git.Repo.clone_from is called with the correct arguments for a github url
@patch("git.Repo.clone_from")
def test_clone_from_called_for_github_url(mock_clone_from, temp_dir):
    repo = "https://github.com/pytest-dev/pytest"
    preprocess._clone_or_copy_repository(repo, temp_dir)
    mock_clone_from.assert_called_once_with(repo, temp_dir)


# Test that shutil.copytree is called with the correct arguments for a local directory
@patch("shutil.copytree")
def test_copytree_called_for_local_dir(mock_copytree, temp_dir):
    local_dir = "/path/to/local/dir"
    Path(local_dir).mkdir(parents=True, exist_ok=True)
    preprocess._clone_or_copy_repository(local_dir, temp_dir)
    mock_copytree.assert_called_once_with(local_dir, temp_dir / "dir")


# Test that a ValueError is raised when the provided repository link is not valid
def test_raise_value_error_for_invalid_repository_link(temp_dir):
    with pytest.raises(ValueError):
        preprocess._clone_or_copy_repository("invalidlink", temp_dir)


"""Tests for the _get_codebase_remote function."""


@pytest.fixture
def remote_repo_url():
    return "https://github.com/pytest-dev/pytest"


# Test that the function returns a dictionary
def test_returns_dict(remote_repo_url):
    result = preprocess._get_codebase_remote(remote_repo_url)
    assert isinstance(result, dict)


# Test that the function returns a non-empty dictionary
def test_returns_non_empty_dict(remote_repo_url):
    result = preprocess._get_codebase_remote(remote_repo_url)
    assert len(result) > 0


# Test that the function returns an empty dictionary for an invalid URL
def test_returns_empty_dict_for_invalid_url():
    invalid_url = "https://github.com/invalid/repo"
    result = preprocess._get_codebase_remote(invalid_url)
    assert len(result) == 0


# Test that the function returns an empty dictionary for a non-existent URL
def test_returns_empty_dict_for_non_existent_url():
    non_existent_url = "https://github.com/non-existent/repo"
    result = preprocess._get_codebase_remote(non_existent_url)
    assert len(result) == 0


# Test that the function returns an empty dictionary for a non-Git URL
def test_returns_empty_dict_for_non_git_url():
    non_git_url = "https://www.google.com"
    result = preprocess._get_codebase_remote(non_git_url)
    assert len(result) == 0


"""Tests for the _get_file_contents function."""


@pytest.fixture
def test_dir(tmp_path):
    test_file_1 = tmp_path / "test_file_1.txt"
    test_file_2 = tmp_path / "test_file_2.bin"
    test_file_1.write_text("Test file 1\n")
    test_file_2.write_bytes(b"\x00\x01\x02")
    return tmp_path


# Test that the function returns a dictionary
def test_returns_dict(test_dir):
    result = preprocess._get_file_contents(test_dir)
    assert isinstance(result, dict)


# Test that the function returns a non-empty dictionary
def test_returns_non_empty_dict(test_dir):
    result = preprocess._get_file_contents(test_dir)
    assert len(result) > 0


# Test that the function returns an empty dictionary for an empty directory
def test_returns_empty_dict_for_empty_directory(tmp_path):
    result = preprocess._get_file_contents(tmp_path)
    assert len(result) == 0


# Test that the function returns an empty dictionary for a non-existent directory
def test_returns_empty_dict_for_non_existent_directory():
    result = preprocess._get_file_contents("non-existent-directory")
    assert len(result) == 0


# Test that the function returns file contents as expected
def test_returns_file_contents(test_dir):
    result = preprocess._get_file_contents(test_dir)
    assert "Test file 1\n" in result.values()


# Test that the function handles non-text or non-UTF-8 files gracefully
def test_handles_non_text_or_non_utf8_files(test_dir):
    result = preprocess._get_file_contents(test_dir)
    assert "Could not decode content: non-text or non-UTF-8 file." in result.values()
