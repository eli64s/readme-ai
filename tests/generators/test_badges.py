"""Unit tests for generating the badges for the README file."""

import pytest

from readmeai.generators.badges import (
    _format_badges,
    build_default_badges,
    build_project_badges,
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
def test_format_badges(badges, expected):
    """Tests the format_html method."""
    assert _format_badges(badges) == expected


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
def test_build_project_badges(dependencies, svg_icons, style, expected):
    """Tests the generate_html method."""
    assert build_project_badges(dependencies, svg_icons, style) == expected


def test_build_default_badges_success(mock_config):
    """Tests build_default_badges with valid inputs."""
    mock_config.git.host_domain = "github.com"
    mock_config.md.badge_style = "flat"
    badges = build_default_badges(mock_config, "github.com", "user/repo")
    assert isinstance(badges, str)
    assert "license" in badges


def test_shieldsio_icons_success(mock_config, mock_dependencies):
    """Tests shieldsio_icons with valid inputs."""
    mock_config.md.badge_style = "flat"
    badges = shieldsio_icons(
        mock_config,
        mock_dependencies,
        "github.com",
        "user/repo",
    )
    assert isinstance(badges, tuple)
    assert any("style=flat" in badge for badge in badges)
    assert any("Python" in badge for badge in badges)


def test_skill_icons_success(mock_config, mock_dependencies):
    """Tests skill_icons with valid inputs."""
    mock_config.md.badge_style = "skills-light"
    badges = skill_icons(mock_config, mock_dependencies)
    assert isinstance(badges, str)
    assert "theme=light" in badges
    assert "md" in badges
