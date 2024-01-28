"""Tests for preprocessing the repository and extracting metadata."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from readmeai.core.preprocess import FileContext, RepoProcessor


@pytest.fixture
def mock_file_data():
    file1 = FileContext(
        file_path="path/to/file1.py",
        file_name="file1.py",
        content="",
        file_ext="py",
        dependencies=["dependency1"],
    )
    file2 = FileContext(
        file_path="path/to/file2.js",
        file_name="file2.js",
        content="",
        file_ext="js",
        dependencies=["dependency2"],
    )
    file3 = FileContext(
        file_path="path/to/file3.txt",
        file_name="file3.txt",
        content="",
        file_ext="txt",
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
        "readmeai.core.utils.is_file_ignored",
        side_effect=lambda x, y: y.file_name == "ignore.md",
    ):
        context = repo_processor.generate_contents(tmp_path)
    assert len(context) == 3
    assert any(f.file_name == "file1.py" for f in context)


def test_generate_file_info(repo_processor, tmp_path):
    """Test the generate_file_info method."""
    (tmp_path / "file1.py").touch()
    (tmp_path / "file2.py").touch()
    (tmp_path / "file3.py").touch()
    (tmp_path / "javascript.js").touch()
    (tmp_path / ".github" / "workflows" / "workflow.yml").mkdir(
        parents=True, exist_ok=True
    )
    with patch("readmeai.core.utils.is_file_ignored", return_value=False):
        result = list(repo_processor.generate_file_info(tmp_path))

    assert len(result) == 4
    assert any(fd.file_name == "file1.py" for fd in result)


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
        "readmeai.parsers.registry.parser_factory", return_value=mock_parser
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
        FileContext(
            file_path=Path(f"main.{file_extension}"),
            file_name=f"main.{file_extension}",
            file_ext=file_extension,
            content="...",
        ),
    ]
    updated = repo_processor.language_mapper(contents)
    assert updated[0].language == expected


@patch("readmeai.llms.tokenize.count_tokens", return_value=7)
def test_tokenize_content(mock_count_tokens, repo_processor):
    """Test the tokenize_content method."""
    contents = [
        FileContext(
            file_name="file.py",
            file_path=Path("file.py"),
            file_ext="py",
            content="print('Hello, world!')",
        )
    ]
    file_data = repo_processor.tokenize_content(contents)
    assert isinstance(file_data[0].tokens, int)
    assert file_data[0].tokens >= 0


def test_tokenize_content_offline_mode(repo_processor):
    """Test the tokenize_content method."""
    repo_processor.config.llm.offline = True
    contents = [
        FileContext(
            file_name="file.py",
            file_path=Path("file.py"),
            content="print('Hello, world!')",
            file_ext="py",
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
