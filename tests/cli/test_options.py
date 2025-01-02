from readmeai.cli.options import BadgeStyles, CustomLogos, DefaultLogos


def test_badge_options():
    """Test the CLI options for badge icons."""
    assert BadgeStyles.FLAT == "flat"
    assert BadgeStyles.FLAT_SQUARE == "flat-square"
    assert BadgeStyles.FOR_THE_BADGE == "for-the-badge"
    assert BadgeStyles.PLASTIC == "plastic"
    assert BadgeStyles.SKILLS == "skills"
    assert BadgeStyles.SKILLS_LIGHT == "skills-light"
    assert BadgeStyles.SOCIAL == "social"


def test_image_options():
    """Test the CLI options for header images."""
    assert CustomLogos.CUSTOM.value == "CUSTOM"
    assert CustomLogos.LLM.value == "LLM"
    assert isinstance(DefaultLogos.BLUE, str)
    assert isinstance(DefaultLogos.GREEN, str)
    assert isinstance(DefaultLogos.ORANGE, str)
    assert isinstance(DefaultLogos.PURPLE, str)
