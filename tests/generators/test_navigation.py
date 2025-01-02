import pytest
from readmeai.generators.enums import NavigationStyles
from readmeai.generators.headers import HeaderRegistry
from readmeai.generators.navigation import NavigationTemplate


@pytest.fixture
def mock_header_registry():
    """Create a mock HeaderRegistry for testing."""

    class MockHeaderRegistry:
        def get_themed_title(self, title):
            return title

        def _strip_emoji(self, title):
            return title

        emoji_theme = "default"

    return MockHeaderRegistry()


def test_navigation_template_initialization(mock_header_registry: HeaderRegistry):
    """Test initialization of NavigationTemplate with different styles."""
    # Test default bullet style
    nav_template = NavigationTemplate("bullet", mock_header_registry)
    assert nav_template.style == NavigationStyles.BULLET
    assert nav_template.using_emojis == "default"

    # Test other valid styles
    styles = ["number", "roman", "accordion"]
    for style in styles:
        nav_template = NavigationTemplate(style, mock_header_registry)
        assert nav_template.style == NavigationStyles[style.upper()]

    # Test invalid style (should default to bullet)
    nav_template = NavigationTemplate("invalid_style", mock_header_registry)
    assert nav_template.style == NavigationStyles.BULLET


def test_generate_anchor():
    """Test GitHub-compatible anchor link generation."""
    header_registry = HeaderRegistry(emoji_theme="default", theme_data={"mapping": {}})
    nav_template = NavigationTemplate("bullet", header_registry)

    # Test various title transformations
    test_cases = [
        ("Hello World", "hello-world"),
        ("Hello   World", "hello-world"),
        ("Hello-World!", "hello-world"),
        ("🚀 Deployment Guide", "deployment-guide"),
        ("Advanced Setup & Configuration", "advanced-setup-configuration"),
        ("Multiple---Hyphens", "multiple-hyphens"),
    ]

    for input_title, expected_anchor in test_cases:
        assert nav_template._generate_anchor(input_title) == expected_anchor


def test_to_roman(mock_header_registry: HeaderRegistry):
    """Test Roman numeral conversion."""
    nav_template = NavigationTemplate("roman", mock_header_registry)
    test_cases = [
        (1, "I"),
        (4, "IV"),
        (9, "IX"),
        (14, "XIV"),
        (49, "XLIX"),
        (99, "XCIX"),
        (500, "D"),
        (999, "CMXCIX"),
    ]

    for num, expected in test_cases:
        assert nav_template._to_roman(num) == expected


def test_format_link(mock_header_registry: HeaderRegistry):
    """Test link formatting for different navigation styles."""
    # Bullet style
    bullet_nav = NavigationTemplate("bullet", mock_header_registry)
    assert (
        bullet_nav._format_link("Hello World", index=1)
        == "- [Hello World](#hello-world)\n"
    )
    assert (
        bullet_nav._format_link("Nested Section", level=1, index=1, sub_index=2)
        == "    - [Nested Section](#nested-section)\n"
    )

    # Numbered style
    number_nav = NavigationTemplate("number", mock_header_registry)
    assert (
        number_nav._format_link("Hello World", index=1)
        == "1. [Hello World](#hello-world)\n"
    )
    assert (
        number_nav._format_link("Nested Section", level=1, index=1, sub_index=2)
        == "    1.2. [Nested Section](#nested-section)\n"
    )

    # Roman style
    roman_nav = NavigationTemplate("roman", mock_header_registry)
    assert (
        roman_nav._format_link("Hello World", index=1)
        == "I. [Hello World](#hello-world)<br>\n"
    )
    assert (
        roman_nav._format_link("Nested Section", index=1, sub_index=2)
        == "&nbsp;&nbsp;&nbsp;&nbsp;I.b. [Nested Section](#nested-section)<br>\n"
    )


def test_render_navigation(mock_header_registry: HeaderRegistry):
    """Test rendering of navigation with different styles."""
    # Prepare test data
    test_data = {
        "sections": [
            {
                "title": "Introduction",
                "subsections": [
                    {"title": "Getting Started"},
                    {"title": "Installation"},
                ],
            },
            {"title": "Advanced Usage"},
        ]
    }

    # Test bullet style
    bullet_nav = NavigationTemplate("bullet", mock_header_registry)
    bullet_result = bullet_nav.render(test_data)
    assert "- [Introduction](#introduction)\n" in bullet_result
    assert "    - [Getting Started](#getting-started)\n" in bullet_result

    # Test accordion style
    accordion_nav = NavigationTemplate("accordion", mock_header_registry)
    accordion_result = accordion_nav.render(test_data)
    assert accordion_result.startswith("<details>\n")
    assert "<summary>Table of Contents</summary>" in accordion_result
    assert "</details>" in accordion_result

    # Test roman style
    roman_nav = NavigationTemplate("roman", mock_header_registry)
    roman_result = roman_nav.render(test_data)
    assert "I. [Introduction](#introduction)<br>\n" in roman_result
    assert (
        "&nbsp;&nbsp;&nbsp;&nbsp;I.a. [Getting Started](#getting-started)<br>\n"
        in roman_result
    )
