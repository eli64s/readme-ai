"""Unit tests for generating markdown badges."""

import pytest

from readmeai.markdown.badges import (
    build_html_badge_block,
    format_html_badge_block,
)


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
def test_format_html_badge_block(badges, expected):
    """Tests the format_html method."""
    assert format_html_badge_block(badges) == expected


@pytest.mark.parametrize(
    "svg_icons, dependencies, expected",
    [
        ({}, [], ""),
        (
            {"python": ["https://img.shields.io/badge/python-3.6-blue.svg"]},
            [],
            "",
        ),
    ],
)
def test_build_html_badge_block(svg_icons, dependencies, expected):
    """Tests the generate_html method."""
    assert build_html_badge_block(svg_icons, dependencies) == expected
