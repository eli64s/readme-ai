from pathlib import Path
from typing import Generator
from unittest.mock import Mock, patch

import pytest
from readmeai.generators.banners.ascii import (
    _create_letter,
    _wrap_with_pre_tag,
    generate_banner,
    generate_box_banner,
)


@pytest.fixture
def temp_svg_file(tmp_path: Path) -> Generator[Path, None, None]:
    """Provide a temporary SVG file path."""
    svg_path = tmp_path / "test_banner.svg"
    yield svg_path
    if svg_path.exists():
        svg_path.unlink()


@pytest.fixture
def mock_logger() -> Generator[Mock, None, None]:
    """Mock the logger for testing."""
    with patch("readmeai.generators.banner._logger") as mock_log:
        yield mock_log


def test_generate_banner_basic() -> None:
    """Test basic ASCII banner generation."""
    result = generate_banner("ABC")
    assert "<pre>" in result
    assert "</pre>" in result
    assert "██████" in result  # Common pattern in A, B, C
    # Verify banner structure (5 lines of content)
    content_lines = result.strip().split("\n")[1:-1]  # Remove pre tags
    assert len(content_lines) == 5


def test_generate_banner_empty() -> None:
    """Test ASCII banner generation with empty string."""
    result = generate_banner("")
    assert result == "<pre>\n\n\n\n\n\n</pre>"


def test_generate_banner_special_chars() -> None:
    """Test ASCII banner generation with special characters."""
    result = generate_banner("A-B")
    assert "<pre>" in result
    assert "██████" in result  # Pattern for horizontal line in '-'


def test_generate_box_banner_basic() -> None:
    """Test basic ASCII box banner generation."""
    result = generate_box_banner("TEST")
    assert "╔" in result  # Top left corner
    assert "╗" in result  # Top right corner
    assert "╚" in result  # Bottom left corner
    assert "╝" in result  # Bottom right corner
    assert "═" in result  # Horizontal border
    assert "║" in result  # Vertical border


def test_generate_box_banner_empty() -> None:
    """Test ASCII box banner generation with empty string."""
    result = generate_box_banner("")
    # Check for the exact pattern that should appear
    assert "╔════╗" in result
    assert "╚════╝" in result
    # Verify the empty content area
    assert "║    ║" in result


def test_generate_box_banner_with_tagline() -> None:
    """Test ASCII box banner generation with a tagline."""
    result = generate_box_banner("TEST", "A test tagline")
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
