import html
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Generator
from unittest.mock import Mock, patch

import pytest

from readmeai.generators.banners import (
    _create_letter,
    _wrap_with_pre_tag,
    convert_svg_to_html,
    generate_ascii_banner,
    generate_ascii_box_banner,
)


@pytest.fixture
def temp_svg_file(tmp_path: Path) -> Generator[Path, None, None]:
    """Provide a temporary SVG file path."""
    svg_path = tmp_path / "test_banner.svg"
    yield svg_path
    # Cleanup
    if svg_path.exists():
        svg_path.unlink()


@pytest.fixture
def mock_logger() -> Generator[Mock, None, None]:
    """Mock the logger for testing."""
    with patch("readmeai.generators.banners._logger") as mock_log:
        yield mock_log


def test_convert_svg_to_html_creates_valid_svg(
    temp_svg_file: Path, mock_logger: Mock
) -> None:
    """Test if convert_svg_to_html creates a valid SVG file with correct content."""
    title = "Test Project"
    result = convert_svg_to_html(title, str(temp_svg_file))

    # Check if file was created
    assert temp_svg_file.exists()

    # Parse and validate SVG content
    tree = ET.parse(temp_svg_file)
    root = tree.getroot()

    # Check SVG attributes
    assert root.tag == "{http://www.w3.org/2000/svg}svg"
    assert root.attrib["viewBox"] == "0 0 800 200"

    # Check if title is in the SVG
    text_elements = root.findall(".//{http://www.w3.org/2000/svg}text")
    assert any(
        title.upper() in elem.text for elem in text_elements if elem.text
    )

    # Verify logger was called
    mock_logger.info.assert_called_once()
    assert isinstance(result, str)


@pytest.mark.skip("Bug in test")
def test_convert_svg_to_html_special_characters(
    temp_svg_file: Path, mock_logger: Mock
) -> None:
    """Test handling of special characters in the title."""
    title = "Test & Project <>"
    # Escape special characters before creating SVG
    escaped_title = html.escape(title).upper()

    result = convert_svg_to_html(escaped_title, str(temp_svg_file))

    assert temp_svg_file.exists()
    content = temp_svg_file.read_text()

    # Check if special characters are properly escaped in the SVG
    assert "&amp;" in content or "&AMP;" in content
    assert "&lt;" in content or "&LT;" in content
    assert "&gt;" in content or "&GT;" in content


def test_generate_ascii_banner_basic() -> None:
    """Test basic ASCII banner generation."""
    result = generate_ascii_banner("ABC")
    assert "<pre>" in result
    assert "</pre>" in result
    assert "██████" in result  # Common pattern in A, B, C

    # Verify banner structure (5 lines of content)
    content_lines = result.strip().split("\n")[1:-1]  # Remove pre tags
    assert len(content_lines) == 5


def test_generate_ascii_banner_empty() -> None:
    """Test ASCII banner generation with empty string."""
    result = generate_ascii_banner("")
    assert result == "<pre>\n\n\n\n\n\n</pre>"


def test_generate_ascii_banner_special_chars() -> None:
    """Test ASCII banner generation with special characters."""
    result = generate_ascii_banner("A-B")
    assert "<pre>" in result
    assert "██████" in result  # Pattern for horizontal line in '-'


def test_generate_ascii_box_banner_basic() -> None:
    """Test basic ASCII box banner generation."""
    result = generate_ascii_box_banner("TEST")
    assert "╔" in result  # Top left corner
    assert "╗" in result  # Top right corner
    assert "╚" in result  # Bottom left corner
    assert "╝" in result  # Bottom right corner
    assert "═" in result  # Horizontal border
    assert "║" in result  # Vertical border


def test_generate_ascii_box_banner_empty() -> None:
    """Test ASCII box banner generation with empty string."""
    result = generate_ascii_box_banner("")
    # Check for the exact pattern that should appear
    assert "╔════╗" in result
    assert "╚════╝" in result
    # Verify the empty content area
    assert "║    ║" in result


def test_generate_ascii_box_banner_with_tagline() -> None:
    """Test ASCII box banner generation with a tagline."""
    result = generate_ascii_box_banner("TEST", "A test tagline")
    assert "║" in result
    # Verify box contains both title and tagline space
    lines = result.split("\n")
    assert len(lines) > 7  # Header + spacing + 5 lines of text + footer


@pytest.mark.parametrize(
    "char,expected_lines",
    [
        ("A", ["  ██  ", " ████ ", "██  ██", "██████", "██  ██"]),
        (" ", ["    ", "    ", "    ", "    ", "    "]),
        ("?", ["?????"] * 5),  # Unknown character
        ("-", ["      ", "      ", "██████", "      ", "      "]),
    ],
)
def test_create_letter(char: str, expected_lines: list[str]) -> None:
    """Test letter creation with various inputs."""
    result = _create_letter(char)
    assert result == expected_lines


def test_wrap_with_pre_tag() -> None:
    """Test pre tag wrapping."""
    text = "test content"
    result = _wrap_with_pre_tag(text)
    assert result == f"<pre>\n{text}\n</pre>"


def test_wrap_with_pre_tag_empty() -> None:
    """Test pre tag wrapping with empty content."""
    result = _wrap_with_pre_tag("")
    assert result == "<pre>\n\n</pre>"


def test_wrap_with_pre_tag_multiline() -> None:
    """Test pre tag wrapping with multiline content."""
    text = "line1\nline2"
    result = _wrap_with_pre_tag(text)
    assert result == f"<pre>\n{text}\n</pre>"
