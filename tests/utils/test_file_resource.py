from pathlib import Path
from unittest.mock import patch

import pytest

from readmeai.errors import FileReadError
from readmeai.utils.resource_loader import build_resource_path


@patch("importlib.resources.files")
def test_resource_path_found_using_importlib_resources(mock_files):
    """Test that a resource path is found using importlib.resources."""
    mock_files.return_value.joinpath.return_value = Path("file.txt")

    @patch("importlib.resources.files")
    def test_resource_path_found_using_importlib_resources(mock_files):
        """Test that a resource path is found using importlib.resources."""
        mock_files.return_value.joinpath.return_value = Path("file.txt")
        assert build_resource_path(
            "file.txt",
            "readmeai.config",
            "settings",
        ) == Path("file.txt")
        mock_files.return_value.joinpath.assert_called_once_with(
            "settings",
            "file.txt",
        )
        mock_files.assert_called_once_with("readmeai.config")


@patch("importlib.resources.files")
def test_resource_path_not_found_using_importlib_resources(mock_files):
    """Test FileReadError is raised when a resource path is not found using importlib.resources."""
    mock_files.return_value.joinpath.side_effect = FileNotFoundError

    @patch("importlib.resources.files")
    def test_resource_path_not_found_using_importlib_resources(mock_files):
        """Test FileReadError is raised when a resource path is not found using importlib.resources."""
        mock_files.return_value.joinpath.side_effect = FileNotFoundError
        with pytest.raises(FileReadError):
            build_resource_path(
                "file.txt",
                "readmeai.config",
                "settings",
            )
        mock_files.return_value.joinpath.assert_called_once_with(
            "settings",
            "file.txt",
        )
        mock_files.assert_called_once_with("readmeai.config")


@patch("importlib.resources.files", side_effect=TypeError)
def test_resource_path_found_using_pkg_resources(mock_files):
    """Test that a resource path is found using pkg_resources."""
    mock_files.return_value.joinpath.side_effect = TypeError

    @patch("importlib.resources.files", side_effect=TypeError)
    def test_resource_path_found_using_pkg_resources(mock_files):
        """Test that a resource path is found using pkg_resources."""
        mock_files.return_value.joinpath.side_effect = TypeError
        with patch(
            "pkg_resources.resource_filename",
        ) as mock_resource_filename:
            mock_resource_filename.return_value = "file.txt"
            assert build_resource_path(
                "file.txt",
                "readmeai.config",
                "settings",
            ) == Path("file.txt")
            mock_resource_filename.assert_called_once_with(
                "readmeai",
                "settings/file.txt",
            )
            mock_files.assert_called_once_with("readmeai.config")
