import json
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest
from readmeai.core.errors import FileReadError, FileWriteError
from readmeai.utilities.file_handler import FileHandler


def test_read_json(file_handler: FileHandler, tmp_path: Path):
    """Test that a JSON file is read."""
    test_data = {"key": "value"}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(test_data))
    data = file_handler.read(file)
    assert data == test_data


def test_read_json_cache(file_handler: FileHandler, tmp_path: Path):
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


def test_write_json(file_handler: FileHandler, tmp_path: Path):
    """Test that a JSON file is written."""
    test_data = {"key": "value"}
    file = tmp_path / "out.json"
    file_handler.write(file, test_data)
    data = json.loads(file.read_text())
    assert data == test_data


def test_read_exception(file_handler: FileHandler, json_file_path_fixture: Path):
    """Test that a read exception raises a FileReadError."""
    with (
        patch(
            "readmeai.utilities.file_handler.FileHandler.get_action",
            side_effect=Exception("Read error"),
        ),
        pytest.raises(FileReadError) as exc,
    ):
        file_handler.read(json_file_path_fixture)
        assert isinstance(exc.value, FileReadError)


def test_write_exception(
    file_handler: FileHandler,
    json_file_path_fixture: Path,
    json_data_fixture: str,
):
    """Test that a write exception raises a FileWriteError."""
    with (
        patch(
            "readmeai.utilities.file_handler.FileHandler.get_action",
            side_effect=Exception("Write error"),
        ),
        pytest.raises(FileWriteError) as exc,
    ):
        file_handler.write(json_file_path_fixture, json_data_fixture)
        assert isinstance(exc.value, FileWriteError)


def test_caching(
    file_handler: FileHandler,
    json_data_fixture: str,
    json_file_path_fixture: Path,
):
    """Test that file reads are cached."""
    with patch("builtins.open", mock_open(read_data=json_data_fixture), create=True):
        file_handler.read(json_file_path_fixture)

    with patch.object(FileHandler, "read_json") as read_json_mock:
        file_handler.read(json_file_path_fixture)
        read_json_mock.assert_not_called()
        assert isinstance(file_handler.cache, dict)


def test_unsupported_file_type_read(file_handler: FileHandler):
    """Test that an unsupported file type raises a FileReadError."""
    with pytest.raises(FileReadError) as exc:
        file_handler.read("unsupported_file.xyz")
    assert isinstance(exc.value, FileReadError)


def test_unsupported_file_type_write(file_handler: FileHandler, json_data_fixture: str):
    """Test that an unsupported file type raises a FileWriteError."""
    with pytest.raises(FileWriteError) as exc:
        file_handler.write("unsupported_file.xyz", json_data_fixture)
    assert isinstance(exc.value, FileWriteError)


def test_unsupported_action_type(file_handler: FileHandler):
    """Test that an unsupported action type raises a ValueError."""
    with pytest.raises(ValueError):
        file_handler.get_action("json", "unsupported_action")


def test_read_write_json(file_handler: FileHandler, json_file_path_fixture: Path):
    """Test that a JSON file is read and written."""
    test_data = {"key": "value"}
    with patch(
        "builtins.open",
        mock_open(read_data=json.dumps(test_data)),
        create=True,
    ):
        file_handler.write_json(json_file_path_fixture, test_data)
        content = file_handler.read_json(json_file_path_fixture)
        assert content == test_data


def test_read_write_markdown(file_handler: FileHandler, json_file_path_fixture: Path):
    """Test that a Markdown file is read and written."""
    test_content = "# Markdown Content"
    with patch("builtins.open", mock_open(read_data=test_content), create=True):
        file_handler.write_markdown(json_file_path_fixture, test_content)
        content = file_handler.read_markdown(json_file_path_fixture)
        assert content == test_content


def test_read_write_yaml(file_handler: FileHandler, json_file_path_fixture: Path):
    """Test that a YAML file is read and written."""
    test_data = {"key": "value"}
    with patch(
        "builtins.open",
        mock_open(read_data=json.dumps(test_data)),
        create=True,
    ):
        file_handler.write_yaml(json_file_path_fixture, test_data)
        content = file_handler.read_yaml(json_file_path_fixture)
        assert content == test_data
