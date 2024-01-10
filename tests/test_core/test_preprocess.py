"""Tests for preprocessing the repository and extracting metadata."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from readmeai.core.preprocess import FileData, RepoProcessor


@pytest.fixture
def mock_file_data():
    file1 = FileData(
        path="path/to/file1.py",
        name="file1.py",
        content="",
        extension="py",
        dependencies=["dependency1"],
    )
    file2 = FileData(
        path="path/to/file2.js",
        name="file2.js",
        content="",
        extension="js",
        dependencies=["dependency2"],
    )
    file3 = FileData(
        path="path/to/file3.txt",
        name="file3.txt",
        content="",
        extension="txt",
        dependencies=[],
    )
    return [file1, file2, file3]


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
        FileData(
            name=f"main.{file_extension}",
            path=Path(f"main.{file_extension}"),
            content="...",
            extension=file_extension,
        ),
    ]
    updated = repo_processor.language_mapper(contents)
    assert updated[0].language == expected


@patch("readmeai.core.tokens.token_counter", return_value=7)
def test_tokenize_content(mock_token_counter, repo_processor):
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


def test_get_dependencies_normal_behavior(
    mock_file_data, mock_config, mock_config_helper
):
    """Test the get_dependencies method."""
    processor = RepoProcessor(mock_config, mock_config_helper)
    dependencies = processor.get_dependencies(mock_file_data)
    assert len(dependencies) == 5
    assert "dependency1" in dependencies
    assert "dependency2" in dependencies
    assert "py" in dependencies
    assert "js" in dependencies


def test_get_dependencies_exception_handling(
    mock_file_data, mock_config, mock_config_helper
):
    """Test the get_dependencies method."""
    processor = RepoProcessor(mock_config, mock_config_helper)
    processor.extract_dependencies = MagicMock(
        side_effect=Exception("Test exception")
    )
    dependencies = processor.get_dependencies(mock_file_data)
    assert isinstance(dependencies, list)
