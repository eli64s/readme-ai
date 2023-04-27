"""Unit tests for the model.py module."""

import pytest

from src.model import (code_to_text, dummy_summary, fetch_summary,
                       generate_summary_text, summarize_text_spacy)


def test_code_to_text():
    """Test the code_to_text function."""

    files = {
        "file1.py": """
def foo():
    return 1
""",
        "file2.md": """
This is a markdown file.
""",
    }

    expected_results = {
        "file1.py": "This function returns 1.",
        "file2.md": "This is a markdown file.",
    }

    results = code_to_text(files)

    assert results == expected_results


def test_dummy_summary():
    """Test the dummy_summary function."""

    expected_result = "This is a dummy summary."

    result = dummy_summary("file.py", "This is a dummy summary.")

    assert result == expected_result


def test_fetch_summary():
    """Test the fetch_summary function."""

    response = """
{
    "choices": [
        {
            "id": "da567890-1234-5678-90ab-cdef01234567",
            "text": "This is a summary.",
            "score": 1.0,
        }
    ]
}
"""

    with pytest.mock.patch("requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = response

        result = fetch_summary("file.py", "This is a prompt.")

        assert result == ("file.py", "This is a summary.")


def test_generate_summary_text():
    """Test the generate_summary_text function."""

    expected_result = "This is a summary."

    result = generate_summary_text("This is a prompt.")

    assert result == expected_result


def test_summarize_text_spacy():
    """Test the summarize_text_spacy function."""

    expected_result = "This is a summary."

    result = summarize_text_spacy("This is a prompt.")

    assert result == expected_result
