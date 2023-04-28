"""Unit tests for preprocess.py."""

import os
import tempfile
from unittest.mock import patch

import pytest

import src.preprocess as prepr


def test_add_space_between_sentences():
    text = "Hello!My name is John."
    result = prepr.add_space_between_sentences(text)
    assert result == "Hello! My name is John."


def test_get_codebase_local_directory(monkeypatch):
    test_data = {"test_file.txt": "This is a test file."}

    def mock_get_file_contents(*args, **kwargs):
        return test_data

    monkeypatch.setattr(prepr, "_get_file_contents", mock_get_file_contents)
    assert prepr.get_codebase("test_dir") == test_data


def test_get_codebase_remote_url(monkeypatch):
    test_data = {"test_file.txt": "This is a test file."}

    def mock_get_codebase_remote(*args, **kwargs):
        return test_data

    monkeypatch.setattr(prepr, "_get_codebase_remote", mock_get_codebase_remote)
    assert prepr.get_codebase(None, "https://github.com/test/repo.git") == test_data


def test_get_codebase_remote_error(monkeypatch):
    def mock_get_codebase_remote(*args, **kwargs):
        raise ValueError("Test error")

    monkeypatch.setattr(prepr, "_get_codebase_remote", mock_get_codebase_remote)
    with pytest.raises(ValueError, match="Test error"):
        prepr.get_codebase(None, "https://github.com/test/repo.git")


def test_get_file_contents():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, "test_file.txt")
        with open(file_path, "w") as file:
            file.write("This is a test file.")

        result = prepr._get_file_contents(temp_dir)
        assert result == {os.path.relpath(file_path, temp_dir): "This is a test file."}


@patch("preprocess.helper.list_files")
@patch("preprocess._clone_or_copy_repository")
@patch("preprocess._get_file_parsers")
def test_get_project_dependencies(
    mock_file_parsers, mock_clone_or_copy, mock_list_files
):
    mock_list_files.return_value = ["test_file.txt"]
    mock_file_parsers.return_value = {"test_file.txt": lambda x: ["test_package"]}
    dependencies = prepr.get_project_dependencies("test_repo", [], ["test_file.txt"])
    assert dependencies == ["test_package"]

    mock_list_files.return_value = ["file.py", "file.txt"]
    mock_file_parsers.return_value = {}
    dependencies = prepr.get_project_dependencies("test_repo", {"py": "python"}, [])
    assert "python" in dependencies


def test_get_repo_name():
    assert prepr.get_repo_name("https://github.com/test/repo.git") == "repo"
    assert prepr.get_repo_name("https://github.com/test/repo") == "repo"
    assert prepr.get_repo_name("C:/path/to/repo") == "repo"
    assert prepr.get_repo_name("C:/path/to/repo/") == "repo"
