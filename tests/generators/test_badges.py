from typing import Literal, LiteralString

import pytest
from readmeai.config.settings import Settings
from readmeai.generators.badges import (
    build_code_metrics,
    build_tech_stack,
    format_badges,
    shieldsio,
    skillicons,
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
def testformat_badges(badges: list[str], expected: Literal[""] | LiteralString):
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
def test_build_tech_stack(
    dependencies: list[str],
    svg_icons: dict[str, list[str]],
    style: Literal["skills"] | Literal["flat"],
    expected: Literal[""] | LiteralString,
):
    """Tests the generate_html method."""
    assert build_tech_stack(dependencies, svg_icons, style) == expected


def test_build_code_metrics_success(mock_config: Settings):
    """Tests build_code_metrics with valid inputs."""
    mock_config = mock_config
    mock_config.git.host_domain = "github.com"
    mock_config.md.badge_style = "flat"
    badges = build_code_metrics(mock_config, "github.com", "user/repo")
    assert isinstance(badges, str)
    assert "license" in badges


def test_shieldsio_success(mock_config: Settings, dependencies_fixture: list[str]):
    """Tests shieldsio with valid inputs."""
    mock_config = mock_config
    mock_config.md.badge_style = "flat"
    badges = shieldsio(
        mock_config,
        dependencies_fixture,
        "github.com",
        "user/repo",
    )
    assert isinstance(badges, tuple), "Badges should be returned as a tuple."
    assert len(badges) > 0, "Badges tuple should not be empty."
    assert any("style=flat" in badge for badge in badges), (
        "Expected 'style=flat' in one of the badges."
    )


def test_skillicons_success(mock_config: Settings, dependencies_fixture: list[str]):
    """Tests skillicons with valid inputs."""
    mock_config = mock_config
    mock_config.md.badge_style = "skills-light"
    badges = skillicons(mock_config, dependencies_fixture)
    assert isinstance(badges, str)
    assert "theme=light" in badges
    assert "md" in badges
