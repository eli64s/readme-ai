"""Unit tests for the markdown headers generator."""

import pytest

from readmeai.markdown import headers


def test_build_readme_md():
    """Tests the build_readme_md method."""
    pass


def test_format_markdown_content():
    """Tests the format_markdown_content method."""
    pass


def test_remove_emojis_from_headers():
    """Tests the remove_emojis_from_headers method."""
    # Prepare the test data
    content = ["# Header 😊", "Some content", "# Another Header 🚀"]
    expected = ["# Header ", "Some content", "# Another Header "]

    # Call the method under test
    result = headers.remove_emojis_from_headers(content)

    # Verify the result
    assert result == expected
