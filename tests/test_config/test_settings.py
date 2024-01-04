"""Unit tests for Pydantic models and configuration settings."""

import pytest

from readmeai.config.settings import BadgeOptions, GitSettings, load_config


def test_badge_options():
    """Test the CLI options for badge icons."""
    assert BadgeOptions.DEFAULT == "default"
    assert BadgeOptions.FLAT == "flat"
    assert BadgeOptions.FLAT_SQUARE == "flat-square"
    assert BadgeOptions.FOR_THE_BADGE == "for-the-badge"
    assert BadgeOptions.PLASTIC == "plastic"
    assert BadgeOptions.SKILLS == "skills"
    assert BadgeOptions.SKILLS_LIGHT == "skills-light"
    assert BadgeOptions.SOCIAL == "social"


def test_git_settings_invalid_url():
    """Test GitSettings with an invalid URL."""
    with pytest.raises(ValueError) as exc_info:
        GitSettings(repository="invalid_url")
    assert isinstance(exc_info.value, ValueError)


def test_load_config_file_not_found():
    """Test loading a configuration file that does not exist."""
    with pytest.raises(FileNotFoundError) as exc_info:
        load_config("nonexistent.toml")
    assert isinstance(exc_info.value, FileNotFoundError)
