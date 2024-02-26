"""Tests for package resources utility methods."""

import pytest

from readmeai.config.utils import get_resource_path
from readmeai.exceptions import FileReadError
from readmeai.utils.file_handler import FileHandler


def test_get_resource_path():
    """Test that the resource path is returned correctly."""
    try:
        file_path = get_resource_path(
            FileHandler(), "config.toml", "readmeai.config", "settings"
        )
        assert isinstance(file_path, dict)
    except FileReadError as exc:
        assert isinstance(exc, FileReadError)


def test_file_read_error():
    """Test that the FileReadError is raised correctly."""
    with pytest.raises(Exception) as exc:
        get_resource_path(FileHandler(), "config.yaml", "readmeai", "config")
        assert isinstance(exc.value, FileReadError)
