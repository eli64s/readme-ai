"""
Tests Pydantic models and configuration settings.
"""

import pytest

from readmeai._exceptions import FileReadError
from readmeai.config.settings import ConfigLoader


def test_load_config_file_not_found():
    """Test loading a configuration file that does not exist."""
    with pytest.raises(FileReadError) as exc:
        config_data = ConfigLoader("invalid.toml")
        assert config_data is None
        assert "File not found" in str(exc.value)
        assert isinstance(exc.value, FileReadError)
