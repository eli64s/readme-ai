"""Unit tests for the markdown headers generator."""

import pytest

from readmeai.markdown.headers import (
    build_readme_md,
    format_readme_md,
    remove_emojis_from_headers,
)


@pytest.mark.skip(reason="Not implemented yet")
def test_format_readme_md_local_source(config, config_helper):
    """Tests the format_readme_md method."""
    assert 1 == 1


@pytest.mark.skip(reason="Not implemented yet")
def test_format_readme_md_nonlocal_source(config, config_helper):
    """Tests the format_readme_md method."""
    assert 1 == 1


def test_remove_emojis_from_headers_with_emojis():
    """Tests the remove_emojis_from_headers method."""
    content_with_emojis = ["# Header 🚀", "## Another Header 😃"]
    expected_output = ["# Header ", "## Another Header "]
    assert remove_emojis_from_headers(content_with_emojis) == expected_output


def test_remove_emojis_from_headers_without_emojis():
    """Tests the remove_emojis_from_headers method."""
    content_without_emojis = ["# Header", "## Another Header"]
    assert (
        remove_emojis_from_headers(content_without_emojis)
        == content_without_emojis
    )
