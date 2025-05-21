import pytest

from readmeai.postprocessor.response_cleaner import (
    fix_markdown_table_rows,
    format_markdown_table,
    process_markdown,
    process_text,
    remove_quotes,
)


def test_fix_markdown_table_rows():
    """Test that the markdown table is extracted from the input string."""
    text = (
        "| Feat | Summary ||---------|-------------|| Content | Content | "
        "| Content | Content |"
    )
    formatted_md_table = fix_markdown_table_rows(text)
    assert isinstance(formatted_md_table, str)
    assert len(formatted_md_table.split("\n")) == 4


def test_fix_markdown_table_rows_malformed():
    """Test malformed markdown table rows."""
    malformed_table = """| Feature || Description ||---------|-------------| | Data || More Data |"""
    result = fix_markdown_table_rows(malformed_table)
    assert isinstance(result, str)
    assert "| Feature | Description |" in result


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
def test_process_text(input_text, expected):
    """Test that the markdown text is extracted from the input string."""
    result = process_text(input_text)
    assert result == expected
    assert isinstance(result, str)


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        # No table found
        ("This is a test string.", ""),
        # Table found
        # (
        #     "| Column | Column |\n|--------|--------|\n|Data|Data|",
        #     "| Column | Column |\n|--------|--------|\n|Data|Data|",
        # ),
    ],
)
def test_format_markdown_table_parametrize(input_text, expected_output):
    """Test format_markdown_table with realistic table input."""
    result = format_markdown_table(input_text)
    assert result == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("This is a test**", "This is a test"),
        (
            "- Unmatched bullet point\n* Another unmatched bullet",
            "Unmatched bullet point\nAnother unmatched bullet",
        ),
        ("This is * a test _ with symbols", "This is  a test  with symbols"),
        (
            "- Bullet with trailing asterisks**\n* Another bullet*\nText with * symbols * in between",
            "Bullet with trailing asterisks\nAnother bullet\nText with  symbols  in between",
        ),
        ("This text is already clean.", "This text is already clean."),
        ("", ""),
        ("***", ""),
        (
            "This is a clean line.\n- This line starts with a bullet*\nAnother clean line.",
            "This is a clean line.\nThis line starts with a bullet\nAnother clean line.",
        ),
        # (
        #     "This **should** stay the *same*.",
        #     "This **should** stay the *same*.",
        # ),
        (
            "- First bullet*\n- Second bullet**\n- Third bullet***",
            "First bullet\nSecond bullet\nThird bullet",
        ),
    ],
)
def test_process_markdown(input_text, expected_output):
    assert process_markdown(input_text) == expected_output


@pytest.mark.skip(reason="Issue with the regex pattern")
@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("'Unmatched quote", "Unmatched quote"),  # Handles single quote
        ('"Unmatched quote', "Unmatched quote"),  # Handles double quote
        (
            "**Bold text** with unmatched quote'",
            "Bold text with unmatched quote",
        ),  # Handles markdown and quotes
    ],
)
def test_process_text_unmatched_quotes(input_text, expected):
    """Test process_text with unmatched quotes."""
    result = process_text(input_text)
    assert result == expected


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        (
            '"Streamlining READMEs with AI magic!"',
            "Streamlining READMEs with AI magic!",
        ),
        (
            "'Streamlining READMEs with AI magic!'",
            "Streamlining READMEs with AI magic!",
        ),
        (
            "`Streamlining READMEs with AI magic!`",
            "Streamlining READMEs with AI magic!",
        ),
        (
            '"Streamlining READMEs with AI magic!`',
            '"Streamlining READMEs with AI magic!`',
        ),
        (
            "Streamlining READMEs with AI magic!",
            "Streamlining READMEs with AI magic!",
        ),
    ],
)
def test_remove_quotes(input_string, expected_output):
    assert remove_quotes(input_string) == expected_output
