"""Unit tests for generating markdown badges."""

import pytest

from readmeai.markdown.badges import build_html_badges, format_html_badges


@pytest.mark.parametrize(
    "badges, expected",
    [
        ([], ""),
        (
            ["https://img.shields.io/badge/coverage-100%25-brightgreen.svg"],
            '<img src="https://img.shields.io/badge/coverage-100%25-brightgreen.svg" alt="coverage">',
        ),
    ],
)
def test_format_html_badges(badges, expected):
    """Tests the format_html method."""
    assert format_html_badges(badges) == expected


@pytest.mark.parametrize(
    "dependencies, git_host, svg_icons, expected",
    [
        ([], "local", {}, ""),
        (
            [],
            "github",
            {"python": ["https://img.shields.io/badge/python-3.6-blue.svg"]},
            "",
        ),
    ],
)
def test_build_html_badges(dependencies, git_host, svg_icons, expected):
    """Tests the generate_html method."""
    assert (
        build_html_badges(
            dependencies,
            git_host,
            svg_icons,
        )
        == expected
    )
