"""
Tests for preprocessing the repository and extracting metadata.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from readmeai.core.preprocess import (
    FileContext,
    RepositoryProcessor,
)


def test_generate_contents(repo_processor, tmp_path):
    """Test the generate_contents method."""
    (tmp_path / "file1.py").touch()
    (tmp_path / "file2.py").touch()
    (tmp_path / "file3.py").touch()
    (tmp_path / ".github" / "workflows" / "workflow.yml").mkdir(
        parents=True,
        exist_ok=True,
    )
    (tmp_path / "ignore.md").touch()
    with patch(
        "readmeai.core.preprocess.RepositoryProcessor._filter_file",
        return_value=False,
    ):
        result = list(repo_processor.generate_contents(tmp_path))
    assert isinstance(result, list)
    assert any(fd.file_name == "file1.py" for fd in result)


def test_generate_file_info(repo_processor, tmp_path):
    """Test the generate_file_info method."""
    (tmp_path / "file1.py").touch()
    (tmp_path / "file2.py").touch()
    (tmp_path / "file3.py").touch()
    (tmp_path / "javascript.js").touch()
    (tmp_path / ".github" / "workflows" / "workflow.yml").mkdir(
        parents=True,
        exist_ok=True,
    )
    with patch(
        "readmeai.core.preprocess.RepositoryProcessor._filter_file",
        return_value=False,
    ):
        result = list(repo_processor.generate_file_info(tmp_path))

    assert isinstance(result, list)
    assert any(fd.file_name == "file1.py" for fd in result)


def test_generate_file_info_exception_handling(repo_processor, tmp_path):
    """Test the generate_file_info method."""
    with pytest.raises(Exception) as exc:
        repo_processor.generate_file_info(None)
        assert isinstance(exc, Exception)


def test_create_file_data(repo_processor):
    """Test the create_file_data method."""
    file_info = ("requirements.txt", Path("requirements.txt"), "Flask==1.1.4")
    context = repo_processor.create_file_data(file_info)
    assert context.file_name == "requirements.txt"
    assert context.file_path == Path("requirements.txt")
    assert context.content == "Flask==1.1.4"


def test_extract_dependencies(repo_processor):
    """Test the extract_dependencies method."""
    file_data = FileContext(
        file_name="requirements.txt",
        file_path=Path("requirements.txt"),
        content="flask==1.1.4",
        file_ext="txt",
    )
    mock_parser = MagicMock()
    mock_parser.parse.return_value = ["flask==1.1.4"]
    with patch(
        "readmeai.parsers.factory.parser_handler",
        return_value=mock_parser,
    ):
        result = repo_processor.extract_dependencies(file_data)
        assert "flask" in result


def test_get_dependencies(mock_file_data, mock_configs):
    """Test the get_dependencies method."""
    processor = RepositoryProcessor(mock_configs)
    dependencies = processor.get_dependencies(mock_file_data)
    assert isinstance(dependencies, list)
    assert "py" in dependencies


def test_get_dependencies_exception_handling(mock_file_data, mock_configs):
    """Test the get_dependencies method."""
    processor = RepositoryProcessor(mock_configs)
    processor.extract_dependencies = MagicMock(
        side_effect=Exception("Test exception"),
    )
    dependencies = processor.get_dependencies(mock_file_data)
    assert isinstance(dependencies, list)


@pytest.mark.parametrize(
    "file_extension, expected",
    [
        ("py", "python"),
        ("js", "javascript"),
        ("md", "markdown"),
        ("txt", "text"),
        ("rs", "rust"),
    ],
)
def test_language_mapping(repo_processor, file_extension, expected):
    """Test method that maps file extensions to programming languages."""
    contents = [
        FileContext(
            file_path=Path(f"main.{file_extension}"),
            file_name=f"main.{file_extension}",
            file_ext=file_extension,
            content="...",
        ),
    ]
    updated = repo_processor._language_mapper(contents)
    assert updated[0].language == expected
