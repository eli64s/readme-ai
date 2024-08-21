"""
Tests read and write operations for file handling.
"""

import json
from unittest.mock import mock_open, patch

import pytest

from readmeai._exceptions import FileReadError, FileWriteError
from readmeai.utils.file_handler import FileHandler


def test_read_json(file_handler, tmp_path):
    """Test that a JSON file is read."""
    test_data = {"key": "value"}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(test_data))
    data = file_handler.read(file)
    assert data == test_data


def test_read_json_cache(file_handler, tmp_path):
    """Test that a file read is cached."""
    test_data = {"key": "value"}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(test_data))
    data = file_handler.read(file)

    if isinstance(data, dict):
        assert file_handler.cache.get(file) == data

    with patch.object(FileHandler, "read_json") as read_json_mock:
        file_handler.read(file)
        read_json_mock.assert_not_called()


def test_write_json(file_handler, tmp_path):
    """Test that a JSON file is written."""
    test_data = {"key": "value"}
    file = tmp_path / "out.json"
    file_handler.write(file, test_data)
    data = json.loads(file.read_text())
    assert data == test_data


def test_read_exception(file_handler, mock_json_file_path):
    """Test that a read exception raises a FileReadError."""
    with (
        patch(
            "readmeai.utils.file_handler.FileHandler.get_action",
            side_effect=Exception("Read error"),
        ),
        pytest.raises(FileReadError) as exc,
    ):
        file_handler.read(mock_json_file_path)
        assert isinstance(exc.value, FileReadError)


def test_write_exception(file_handler, mock_json_file_path, mock_json_data):
    """Test that a write exception raises a FileWriteError."""
    with (
        patch(
            "readmeai.utils.file_handler.FileHandler.get_action",
            side_effect=Exception("Write error"),
        ),
        pytest.raises(FileWriteError) as exc,
    ):
        file_handler.write(mock_json_file_path, mock_json_data)
        assert isinstance(exc.value, FileWriteError)


def test_caching(file_handler, mock_json_data, mock_json_file_path):
    """Test that file reads are cached."""
    with patch(
        "builtins.open", mock_open(read_data=mock_json_data), create=True
    ):
        file_handler.read(mock_json_file_path)

    with patch.object(FileHandler, "read_json") as read_json_mock:
        file_handler.read(mock_json_file_path)
        read_json_mock.assert_not_called()
        assert isinstance(file_handler.cache, dict)


def test_unsupported_file_type_read(file_handler):
    """Test that an unsupported file type raises a FileReadError."""
    with pytest.raises(FileReadError) as exc:
        file_handler.read("unsupported_file.xyz")
    assert isinstance(exc.value, FileReadError)


def test_unsupported_file_type_write(file_handler, mock_json_data):
    """Test that an unsupported file type raises a FileWriteError."""
    with pytest.raises(FileWriteError) as exc:
        file_handler.write("unsupported_file.xyz", mock_json_data)
    assert isinstance(exc.value, FileWriteError)


def test_unsupported_action_type(file_handler):
    """Test that an unsupported action type raises a ValueError."""
    with pytest.raises(ValueError):
        file_handler.get_action("json", "unsupported_action")


def test_read_write_json(file_handler, mock_json_file_path):
    """Test that a JSON file is read and written."""
    test_data = {"key": "value"}
    with patch(
        "builtins.open",
        mock_open(read_data=json.dumps(test_data)),
        create=True,
    ):
        file_handler.write_json(mock_json_file_path, test_data)
        content = file_handler.read_json(mock_json_file_path)
        assert content == test_data


def test_read_write_markdown(file_handler, mock_json_file_path):
    """Test that a Markdown file is read and written."""
    test_content = "# Markdown Content"
    with patch(
        "builtins.open", mock_open(read_data=test_content), create=True
    ):
        file_handler.write_markdown(mock_json_file_path, test_content)
        content = file_handler.read_markdown(mock_json_file_path)
        assert content == test_content


def test_read_write_yaml(file_handler, mock_json_file_path):
    """Test that a YAML file is read and written."""
    test_data = {"key": "value"}
    with patch(
        "builtins.open",
        mock_open(read_data=json.dumps(test_data)),
        create=True,
    ):
        file_handler.write_yaml(mock_json_file_path, test_data)
        content = file_handler.read_yaml(mock_json_file_path)
        assert content == test_data
