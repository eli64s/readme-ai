"""Tests for preprocessing the repository and extracting metadata."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from readmeai.core.preprocess import FileData, RepoProcessor


@pytest.fixture
def repo_processor(config, config_helper):
    """Fixture for RepoProcessor."""
    return RepoProcessor(config, config_helper)


def test_generate_contents(repo_processor, tmp_path):
    """Test the generate_contents method."""
    (tmp_path / "file1.py").touch()
    (tmp_path / "file2.py").touch()
    (tmp_path / "file3.py").touch()
    (tmp_path / ".github" / "workflows" / "workflow.yml").mkdir(
        parents=True, exist_ok=True
    )
    (tmp_path / "ignore.md").touch()

    with patch(
        "readmeai.core.utils.should_ignore",
        side_effect=lambda x, y: y.name == "ignore.md",
    ):
        result = repo_processor.generate_contents(tmp_path)

    assert len(result) == 3
    assert any(fd.name == "file1.py" for fd in result)


def test_generate_file_info(repo_processor, tmp_path):
    """Test the generate_file_info method."""
    (tmp_path / "file1.py").touch()
    (tmp_path / "file2.py").touch()
    (tmp_path / "file3.py").touch()
    (tmp_path / "javascript.js").touch()
    (tmp_path / ".github" / "workflows" / "workflow.yml").mkdir(
        parents=True, exist_ok=True
    )
    with patch("readmeai.core.utils.should_ignore", return_value=False):
        result = list(repo_processor.generate_file_info(tmp_path))

    assert len(result) == 4
    assert any(fd.name == "file1.py" for fd in result)


def test_generate_file_info_exception_handling(repo_processor, caplog):
    """Test the generate_file_info method."""
    mock_file = MagicMock()
    mock_file.open.side_effect = UnicodeDecodeError(
        "utf-8", b"", 0, 1, "error"
    )
    mock_path = MagicMock()
    mock_path.rglob.return_value = [mock_file]
    list(repo_processor.generate_file_info(mock_path))
    assert "Error reading file" in caplog.text


def test_create_file_data(repo_processor):
    """Test the create_file_data method."""
    file_info = ("requirements.txt", Path("requirements.txt"), "Flask==1.1.4")
    file_data = repo_processor.create_file_data(file_info)
    assert file_data.name == "requirements.txt"
    assert file_data.path == Path("requirements.txt")
    assert file_data.content == "Flask==1.1.4"


def test_extract_dependencies(repo_processor):
    """Test the extract_dependencies method."""
    file_data = FileData(
        name="requirements.txt",
        path=Path("requirements.txt"),
        content="flask==1.1.4",
        extension="txt",
    )
    mock_parser = MagicMock()
    mock_parser.parse.return_value = ["flask==1.1.4"]
    with patch(
        "readmeai.parsers.factory.parser_factory", return_value=mock_parser
    ):
        result = repo_processor.extract_dependencies(file_data)
        assert "flask" in result


def test_language_mapper(repo_processor):
    """Test the language_mapper method."""
    contents = [
        FileData(
            name="main.py",
            path=Path("main.py"),
            content="import streamlit as st\nimport pandas as pd",
            extension="py",
        ),
        FileData(
            name="README.md",
            path=Path("README.md"),
            content="## This is a test README file",
            extension="md",
        ),
    ]
    updated = repo_processor.language_mapper(contents)
    assert updated[0].language == "python"
    assert updated[1].language == "markdown"


@patch("readmeai.core.tokens.get_token_count", return_value=7)
def test_tokenize_content(mock_get_token_count, repo_processor):
    """Test the tokenize_content method."""
    contents = [
        FileData(
            name="file.py",
            path=Path("file.py"),
            content="print('Hello, world!')",
            extension="py",
        )
    ]
    file_data = repo_processor.tokenize_content(contents)
    assert isinstance(file_data[0].tokens, int)
    assert file_data[0].tokens >= 0


def test_tokenize_content_offline_mode(repo_processor):
    """Test the tokenize_content method."""
    repo_processor.config.cli.offline = True
    contents = [
        FileData(
            name="file.py",
            path=Path("file.py"),
            content="print('Hello, world!')",
            extension="py",
        )
    ]
    result = repo_processor.tokenize_content(contents)
    assert result[0].tokens == 0
