"""
Tests for loading package resources using importlib and pkg_resources.
"""

import json
from unittest.mock import patch

import pytest
import toml

from readmeai._exceptions import FileReadError
from readmeai.utils.resource_loader import get_resource_path


def test_get_resource_json(file_handler, tmp_path):
    """Test that a JSON file is read."""
    test_data = {"key": "value"}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(test_data))
    data = get_resource_path(file_handler, file)
    assert data == test_data


def test_get_resource_tom(file_handler, tmp_path):
    """Test that a TOML file is read."""
    test_data = {"key": "value"}
    file = tmp_path / "data.toml"
    file.write_text(toml.dumps(test_data))
    data = get_resource_path(file_handler, file)
    assert data == test_data


def test_read_json(file_handler, tmp_path):
    """Test that a JSON file is read."""
    test_data = {"key": "value"}
    file = tmp_path / "data.json"
    file.write_text(json.dumps(test_data))
    data = get_resource_path(file_handler, file)
    assert data == test_data


def test_get_resource_path_raises_error(file_handler, tmp_path):
    """Test that an error is raised when the file is not found."""
    file = tmp_path / "data.json"
    with pytest.raises(FileReadError) as exc:
        get_resource_path(file_handler, file)
        assert "File not found" in str(exc.value)
        assert isinstance(exc.value, FileReadError)


def test_get_resource_path_raises_error_invalid_format(file_handler, tmp_path):
    """Test that an error is raised when the file format is not supported."""
    file = tmp_path / "data.txt"
    with pytest.raises(FileReadError) as exc:
        get_resource_path(file_handler, file)
        assert "Unsupported file format" in str(exc.value)
        assert isinstance(exc.value, FileReadError)


def test_get_resource_path_importlib_error(file_handler, tmp_path):
    """Test that an error is raised when importlib.resources fails."""
    file = tmp_path / "data.json"
    with patch("importlib.resources.files") as mock_files:
        mock_files.side_effect = TypeError
        with pytest.raises(FileReadError) as exc:
            get_resource_path(file_handler, file)
            assert "Error loading file via pkg_resources" in str(exc.value)
            assert isinstance(exc.value, FileReadError)


def test_get_resource_path_pkg_resources_error(file_handler, tmp_path):
    """Test that an error is raised when pkg_resources fails."""
    file = tmp_path / "data.json"
    with patch("importlib.resources.files") as mock_files:
        mock_files.side_effect = TypeError
        with patch("pkg_resources.resource_filename") as mock_filename:
            mock_filename.side_effect = Exception
            with pytest.raises(FileReadError) as exc:
                get_resource_path(file_handler, file)
                assert "Error loading file via pkg_resources" in str(exc.value)
                assert isinstance(exc.value, FileReadError)


def test_get_resource_path_importlib_error_no_pkg_resources(
    file_handler, tmp_path
):
    """Test error is raised when both importlib and pkg_resources fail."""
    file = tmp_path / "data.json"
    with patch("importlib.resources.files") as mock_files:
        mock_files.side_effect = TypeError
        with patch("pkg_resources.resource_filename") as mock_filename:
            mock_filename.side_effect = Exception
            with pytest.raises(FileReadError) as exc:
                get_resource_path(file_handler, file)
                assert "Error loading file via pkg_resources" in str(exc.value)
                assert isinstance(exc.value, FileReadError)
