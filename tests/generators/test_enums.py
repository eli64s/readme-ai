from readmeai.generators.enums import (
    BadgeStyles,
    CustomLogos,
)


def test_badge_options():
    assert BadgeStyles.DEFAULT == "default"
    assert BadgeStyles.FLAT == "flat"
    assert BadgeStyles.FLAT_SQUARE == "flat-square"
    assert BadgeStyles.FOR_THE_BADGE == "for-the-badge"
    assert BadgeStyles.PLASTIC == "plastic"
    assert BadgeStyles.SKILLS == "skills"
    assert BadgeStyles.SKILLS_LIGHT == "skills-light"
    assert BadgeStyles.SOCIAL == "social"


def test_image_options():
    assert CustomLogos.CUSTOM.name == "CUSTOM"
    assert CustomLogos.LLM.name == "LLM"
