"""Tests for utility functions used in the markdown module."""

import pytest

from readmeai.markdown.utils import (
    remove_emojis,
    split_markdown_headings,
    update_heading_names,
)


def test_remove_emojis_from_headers_with_emojis():
    """Tests the remove_emojis static method with emojis."""
    content_with_emojis = ["# Header 🚀", "## Another Header 😃"]
    expected_output = ["# Header ", "## Another Header "]
    result = remove_emojis(content_with_emojis)
    assert result == expected_output


def test_remove_emojis_from_headers_without_emojis():
    """Tests the remove_emojis static method without emojis."""
    content_without_emojis = ["# Header", "## Another Header"]
    result = remove_emojis(content_without_emojis)
    assert result == content_without_emojis


@pytest.mark.skip
def test_splitting_by_level_two_headings():
    """Tests the split_markdown_headings static method."""
    input_markdown = """\
    # Level One Heading

    Some text before second level heading.

    ## Level Two Heading 1
    Text under first level two heading.

    ### Level Three Heading
    Text under third level heading.

    ## Level Two Heading 2
    Text under second level heading 2.
    """
    expected_output = {
        "level_one_heading.md": "# Level One Heading\n\nSome text before second level heading.\n\n",
        "level_two_heading_1.md": "\n## Level Two Heading 1\nText under first level two heading.\n\n### Level Three Heading\nText under third level heading.\n\n",
        "level_two_heading_2.md": "\n## Level Two Heading 2\nText under second level heading 2.",
    }
    assert split_markdown_headings(input_markdown) == expected_output


@pytest.mark.skip
def test_removing_leading_emoji_underscore_and_space():
    """Tests the update_heading_names static method."""
    input_dict = {"🤖 _Header_.md": "Content under header."}
    expected_output = {"header.md": "Content under header."}
    assert update_heading_names(input_dict) == expected_output


@pytest.mark.skip
def test_replacing_html_entities_with_header_dot_md():
    """Tests the update_heading_names static method."""
    input_dict = {
        "<h1> Header 1 .md >": "Content under header 1.",
        "<h2> Header 2 .md >": "Content under header 2.",
    }
    expected_output = {
        "header_1__md": "Content under header 1.",
        "header_2__md": "Content under header 2.",
    }
    assert update_heading_names(input_dict) == expected_output


def test_split_markdown_headings():
    """Tests the split_markdown_headings static method."""
    raw_input = """## :butterfly: Section 1\nSome Content...
    ### Subsection 1\nMore nested content...
    \n---\n
    ## Section 2\nSome other content...
    """

    result = split_markdown_headings(raw_input)
    assert ":butterfly:_section_1.md" in result
    # assert "section_2.md" in result.keys()


def test_update_heading_names():
    """Tests the update_heading_names static method."""
    raw_inputs = {
        "<h1> Header 1 .md >": "Content under header 1.",
        "__leading_underscores_.md": "Content...",
        "## multiple words": "Content...",
    }

    result = update_heading_names(raw_inputs)

    assert "leading_underscores_.md" in result
    assert "multiple words" in result
