"""Unit tests for the markdown headers generator."""

from readmeai.markdown import headers


def test_remove_emojis_from_headers():
    """Tests the remove_emojis_from_headers method."""
    content = ["# Header 😊", "Some content", "# Another Header 🚀"]
    expected = ["# Header ", "Some content", "# Another Header "]
    result = headers.remove_emojis_from_headers(content)
    assert result == expected
