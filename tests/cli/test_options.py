from readmeai.cli.options import BadgeStyleOptions, ImageOptions


def test_badge_options():
    """Test the CLI options for badge icons."""
    assert BadgeStyleOptions.FLAT == "flat"
    assert BadgeStyleOptions.FLAT_SQUARE == "flat-square"
    assert BadgeStyleOptions.FOR_THE_BADGE == "for-the-badge"
    assert BadgeStyleOptions.PLASTIC == "plastic"
    assert BadgeStyleOptions.SKILLS == "skills"
    assert BadgeStyleOptions.SKILLS_LIGHT == "skills-light"
    assert BadgeStyleOptions.SOCIAL == "social"


def test_image_options():
    """Test the CLI options for header images."""
    assert ImageOptions.CUSTOM.value == "CUSTOM"
    assert ImageOptions.LLM.value == "LLM"
    assert isinstance(ImageOptions.BLUE, str)
    assert isinstance(ImageOptions.BLACK, str)
