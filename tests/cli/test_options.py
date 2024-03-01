"""Tests for the readme-ai CLI options module."""

from readmeai.cli.options import BadgeOptions, ImageOptions


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


def test_image_options():
    """Test the CLI options for header images."""
    assert ImageOptions.CUSTOM.value == "custom"
    assert ImageOptions.LLM.value == "llm"
    assert isinstance(ImageOptions.BLUE, str)
    assert isinstance(ImageOptions.BLACK, str)
