"""Unit tests for the factory file I/O read and write methods."""

import json
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from readmeai.core.factory import FileHandler
from readmeai.exceptions import FileReadError, FileWriteError


@pytest.fixture
def mock_file_path():
    """Return mocked file path."""
    return "test_data.json"


@pytest.fixture
def mock_json_data():
    """Return test JSON data."""
    return """{"a": 1, "b": 2, "c": 3}"""


@pytest.fixture
def file_handler():
    """Return FileHandler instance."""
    return FileHandler()


def test_read_success(file_handler, mock_json_data, mock_file_path):
    """Test read method."""
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        content = file_handler.read(mock_file_path)
        assert content == json.loads(mock_json_data)


def test_caching(file_handler, mock_json_data, mock_file_path):
    """Test caching of read method."""
    with patch(
        "builtins.open", mock_open(read_data=mock_json_data)
    ) as mocked_file:
        content1 = file_handler.read(mock_file_path)
        content2 = file_handler.read(mock_file_path)
        assert content1 == content2
        mocked_file.assert_called_once_with(
            mock_file_path, "r", encoding="utf-8"
        )


def test_read_failure(file_handler, mock_file_path):
    """Test read method failure."""
    with patch("builtins.open", mock_open()) as mocked_file:
        mocked_file.side_effect = Exception(FileReadError)
        with pytest.raises(Exception) as exc:
            file_handler.read(mock_file_path)
            FileReadError(exc, mock_file_path)


def test_write_success(file_handler, mock_json_data, mock_file_path):
    """Test write method."""
    with patch("builtins.open", mock_open()) as mocked_file:
        file_handler.write(mock_file_path, mock_json_data)
        mocked_file.assert_called_with(mock_file_path, "w", encoding="utf-8")


def test_write_failure(file_handler, mock_json_data, mock_file_path):
    """Test write method failure."""
    with patch("builtins.open", mock_open()) as mocked_file:
        mocked_file.side_effect = FileWriteError(
            "Error writing file", mock_file_path
        )
        with pytest.raises(FileWriteError):
            file_handler.write(mock_file_path, mock_json_data)
            FileWriteError("Error writing file", mock_file_path)

    assert mocked_file.call_count == 1
    assert issubclass(FileReadError, Exception)
    assert issubclass(FileWriteError, Exception)


def test_read_json_success(file_handler, mock_json_data, mock_file_path):
    """Test read_json method."""
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        content = file_handler.read(mock_file_path)
        assert content == json.loads(mock_json_data)


def test_caching_json(file_handler, mock_json_data, mock_file_path):
    """Test caching of read_json method."""
    with patch("builtins.open", mock_open(read_data=mock_json_data)):
        content1 = file_handler.read(mock_file_path)
        content2 = file_handler.read(mock_file_path)
        assert content1 == content2


def test_read_json_failure(file_handler, mock_file_path):
    """Test read_json method failure."""
    with patch("builtins.open", mock_open()) as mocked_file:
        mocked_file.side_effect = json.JSONDecodeError("Error", "doc", 0)
        with pytest.raises(json.JSONDecodeError):
            file_handler.read_json(mock_file_path)


def test_get_action_valid(file_handler):
    """Test get_action method."""
    action = file_handler.get_action("json", "read")
    assert callable(action)


def test_get_action_invalid_extension(file_handler):
    """Test get_action method with invalid extension."""
    with pytest.raises(ValueError):
        file_handler.get_action("invalid", "read")


def test_get_action_invalid_action_type(file_handler):
    """Test get_action method with invalid action type."""
    with pytest.raises(ValueError):
        file_handler.get_action("json", "invalid")


def test_custom_exceptions():
    """Test custom exceptions."""
    assert issubclass(FileReadError, Exception)
    assert issubclass(FileWriteError, Exception)


def test_read_caches_file_content():
    """Test read method caches file content."""
    file_path = "test.json"
    handler = FileHandler()
    with pytest.raises(FileReadError) as exc:
        handler.read(file_path)
    assert "No such file or directory" in str(exc.value)


def test_get_action_raises_value_error_for_unsupported_file_type():
    """Test get_action method raises ValueError for unsupported file type."""
    handler = FileHandler()
    with pytest.raises(ValueError) as exc:
        handler.get_action("unsupported", "read")
    assert str(exc.value) == "Unsupported file type: unsupported"


def test_write_raises_write_file_exception_for_permission_error():
    """Test write method raises FileWriteError for PermissionError."""
    file_path = "test.txt"
    handler = FileHandler()
    with patch(
        "builtins.open",
        side_effect=FileWriteError("Permission denied", file_path),
    ):
        with pytest.raises(FileWriteError) as exc:
            handler.write(file_path, "test")
            assert str(exc.value) == "Expected file to be writable: test.txt"


def test_read_json_file():
    file_path = "test_data/config.json"
    expected_content = {"key": "value"}
    with pytest.raises(FileReadError) as exc:
        content = FileHandler().read(file_path)
        assert content == expected_content
        assert (
            str(exc.value)
            == "Configuration file not found: test_data/config.json"
        )


def test_write_markdown_file():
    file_path = "test_output/test.md"
    content = "# Test Markdown Content"
    with pytest.raises(FileWriteError) as exc:
        FileHandler().write(file_path, content)
        assert (
            str(exc.value)
            == "Directory not found for file: test_output/test.md"
        )


def test_unsupported_file_type():
    file_path = "test_data/invalid.xyz"
    with pytest.raises(FileReadError) as exc:
        FileHandler().read(file_path)
    assert isinstance(exc.value, FileReadError)


def test_unsupported_action_type():
    """Test get_action method raises ValueError for unsupported action type."""
    with pytest.raises(ValueError) as exc:
        FileHandler().get_action("json", "invalid_action")
    assert isinstance(exc.value, ValueError)


def test_cache_functionality(mock_config):
    """Test caching of read method."""
    file_path = Path("readmeai/settings") / mock_config.files.dependency_files
    content1 = FileHandler().read(file_path)
    content2 = FileHandler().read(file_path)
    assert content1 == content2
