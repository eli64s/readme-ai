"""Unit tests for the factory file I/O read and write methods."""

import json
from unittest.mock import mock_open, patch

import pytest

from readmeai.core.factory import (
    FileHandler,
    ReadFileException,
    WriteFileException,
)


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
        mocked_file.side_effect = Exception("Error")
        with pytest.raises(ReadFileException):
            file_handler.read(mock_file_path)


def test_write_success(file_handler, mock_json_data, mock_file_path):
    """Test write method."""
    with patch("builtins.open", mock_open()) as mocked_file:
        file_handler.write(mock_file_path, mock_json_data)
        mocked_file.assert_called_with(mock_file_path, "w", encoding="utf-8")


def test_write_failure(file_handler, mock_json_data, mock_file_path):
    """Test write method failure."""
    with patch("builtins.open", mock_open()) as mocked_file:
        mocked_file.side_effect = Exception("Error")
        with pytest.raises(WriteFileException):
            file_handler.write(mock_file_path, mock_json_data)


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
    assert issubclass(ReadFileException, Exception)
    assert issubclass(WriteFileException, Exception)
