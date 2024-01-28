"""Unit tests for Pydantic models and configuration settings."""

import pytest

from readmeai.config.settings import load_config
from readmeai.exceptions import FileReadError


def test_load_config_file_not_found():
    """Test loading a configuration file that does not exist."""
    with pytest.raises(FileReadError) as exc:
        load_config("nonexistent.toml")
    assert isinstance(exc.value, FileReadError)
