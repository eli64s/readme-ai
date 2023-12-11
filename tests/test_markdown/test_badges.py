"""Unit tests for generating markdown badges."""

import pytest

from readmeai.markdown.badges import format_html, generate_html


@pytest.mark.parametrize(
    "badges, expected",
    [
        ([], ""),
        (
            ["https://img.shields.io/badge/coverage-100%25-brightgreen.svg"],
            '<img src="https://img.shields.io/badge/coverage-100%25-brightgreen.svg" alt="coverage" />',
        ),
    ],
)
def test_format_html(badges, expected):
    """Tests the format_html method."""
    assert format_html(badges) == expected


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
def test_generate_html(svg_icons, dependencies, expected):
    """Tests the generate_html method."""
    assert generate_html(svg_icons, dependencies) == expected
