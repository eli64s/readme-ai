from typing import Literal, LiteralString

import pytest

from readmeai.config.settings import Settings
from readmeai.generators.badges import (
    build_badges_tech_stack,
    build_default_badges,
    format_badges,
    shieldsio_icons,
    skill_icons,
)


@pytest.mark.parametrize(
    "badges, expected",
    [
        ([], ""),
        (
            [
                "https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white",
            ],
            '<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">\n',
        ),
    ],
)
def testformat_badges(
    badges: list[str], expected: Literal[""] | LiteralString
):
    """Tests the format_html method."""
    assert format_badges(badges) == expected


@pytest.mark.parametrize(
    "dependencies, svg_icons, style, expected",
    [
        ([], {}, "skills", ""),
        (
            ["python"],
            {
                "python": [
                    "https://img.shields.io/badge/Python-3776AB.svg?style={0}&logo=Python&logoColor=white",
                    "3776AB",
                ],
            },
            "flat",
            '<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">\n',
        ),
    ],
)
def test_build_badges_tech_stack(
    dependencies: list[str],
    svg_icons: dict[str, list[str]],
    style: Literal["skills"] | Literal["flat"],
    expected: Literal[""] | LiteralString,
):
    """Tests the generate_html method."""
    assert build_badges_tech_stack(dependencies, svg_icons, style) == expected


def test_build_default_badges_success(config_fixture: Settings):
    """Tests build_default_badges with valid inputs."""
    mock_config = config_fixture
    mock_config.git.host_domain = "github.com"
    mock_config.md.badge_style = "flat"
    badges = build_default_badges(mock_config, "github.com", "user/repo")
    assert isinstance(badges, str)
    assert "license" in badges


def test_shieldsio_icons_success(
    config_fixture: Settings, dependencies_fixture: list[str]
):
    """Tests shieldsio_icons with valid inputs."""
    mock_config = config_fixture
    mock_config.md.badge_style = "flat"
    badges = shieldsio_icons(
        mock_config,
        dependencies_fixture,
        "github.com",
        "user/repo",
    )
    assert isinstance(badges, tuple), "Badges should be returned as a tuple."
    assert len(badges) > 0, "Badges tuple should not be empty."
    assert any(
        "style=flat" in badge for badge in badges
    ), "Expected 'style=flat' in one of the badges."


def test_skill_icons_success(
    config_fixture: Settings, dependencies_fixture: list[str]
):
    """Tests skill_icons with valid inputs."""
    mock_config = config_fixture
    mock_config.md.badge_style = "skills-light"
    badges = skill_icons(mock_config, dependencies_fixture)
    assert isinstance(badges, str)
    assert "theme=light" in badges
    assert "md" in badges
