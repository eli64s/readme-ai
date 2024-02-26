"""Tests for utility functions in the core module."""

import pytest

from readmeai.utils.formatter import (
    clean_text,
    fix_md_table_rows,
    format_md_table,
    format_response,
)


def test_fix_md_table_rows():
    """Test that the markdown table is extracted from the input string."""
    text = """| Feat | Summary ||---------|-------------|| Content | Content | | Content | Content |"""
    formatted_md_table = fix_md_table_rows(text)
    assert isinstance(formatted_md_table, str)
    assert len(formatted_md_table.split("\n")) == 4


def test_format_response():
    """Test that the markdown table is extracted from the input string."""
    test_string = """<remove this>
    | Column 1 | Column 2 | Column 3 |
    | -------- | -------- | -------- |
    | Content  | Content  | Content  |
    | Content  | Content  | Content  |
    | Content  | Content  | Content  |
    and this
    """
    result = format_response("features", test_string)
    assert isinstance(result, str)
    assert "<remove this>" not in result
    assert "and this" not in result


def test_format_response_no_table():
    """Test that the markdown table is extracted from the input string."""
    test_string = "This is a test string."
    result = format_response("features", test_string)
    assert isinstance(result, str)
    assert len(result) == 0


@pytest.mark.parametrize(
    "input_text, expected",
    [
        # (
        #    "Code Summary: `function()` provides functions to",
        #    "Provides functions to",
        # ),
        (
            "**Code Summary:** provides functions to",
            "Provides functions to",
        ),
        ("'hello world'", "Hello world"),
        ("Clear, Concise, Captivating**", "Clear, Concise, Captivating"),
        ("main.py** : hello world!", "Hello world!"),
        ("AI-Driven, Streamlined Success'", "AI-Driven, Streamlined Success"),
        (
            "**AI-Driven, Streamlined Success**",
            "AI-Driven, Streamlined Success",
        ),
        ("**AI-Driven, Streamlined Success", "AI-Driven, Streamlined Success"),
        (
            "'\AI-Driven, Streamlined Success!",
            "AI-Driven, Streamlined Success!",
        ),
    ],
)
def test_clean_text(input_text, expected):
    """Test that the markdown text is extracted from the input string."""
    result = clean_text(input_text)
    assert result == expected
    assert isinstance(result, str)


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("This is a test string.", ""),
    ],
)
def test_format_md_table_parametrize(input_text, expected_output):
    """Test that the markdown table is extracted from the input string."""
    result = format_md_table(input_text)
    assert result == expected_output
    assert isinstance(result, str)
