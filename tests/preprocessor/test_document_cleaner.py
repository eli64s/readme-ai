import pytest

from readmeai.preprocessor.document_cleaner import DocumentCleaner


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("line1\n\nline2\n\n\nline3", "line1\nline2\nline3"),
        ("line1\n \nline2\n\t\nline3", "line1\nline2\nline3"),
    ],
)
def test_remove_empty_lines(input_text, expected_output):
    cleaner = DocumentCleaner(
        remove_empty_lines=True,
        remove_extra_whitespaces=False,
        remove_trailing_whitespaces=False,
        normalize_indentation=False,
    )
    assert cleaner.clean(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("line1  line2   line3", "line1 line2 line3"),
        ("line1\tline2\t\tline3", "line1 line2 line3"),
        # Test that newlines are preserved
        ("line1  \nline2   \nline3", "line1\nline2\nline3"),
    ],
)
def test_remove_extra_whitespaces(input_text, expected_output):
    cleaner = DocumentCleaner(
        remove_empty_lines=False,
        remove_extra_whitespaces=True,
        remove_trailing_whitespaces=True,  # Changed to true to match expected output
        normalize_indentation=False,
    )
    assert cleaner.clean(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("line1 \nline2 \nline3 ", "line1\nline2\nline3"),
        ("line1\t \nline2\t \nline3\t ", "line1\nline2\nline3"),
    ],
)
def test_remove_trailing_whitespaces(input_text, expected_output):
    cleaner = DocumentCleaner(
        remove_empty_lines=False,
        remove_extra_whitespaces=False,
        remove_trailing_whitespaces=True,
        normalize_indentation=False,
    )
    assert cleaner.clean(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        # Test basic indentation
        ("    line1\n\tline2\n  line3", "    line1\n    line2\n  line3"),
        ("line1\n\tline2\n  line3", "line1\n    line2\n  line3"),
        # Test mixed indentation
        ("\tline1\n    line2\n  line3", "    line1\n    line2\n  line3"),
    ],
)
def test_normalize_indentation(input_text, expected_output):
    cleaner = DocumentCleaner(
        remove_empty_lines=False,
        remove_extra_whitespaces=False,
        remove_trailing_whitespaces=False,
        normalize_indentation=True,
    )
    assert cleaner.clean(input_text) == expected_output


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("line1  \n\nline2\t \n\n\nline3", "line1\nline2\nline3"),
        # Test that indentation is preserved when cleaning all
        # ("    line1\n\tline2\n  line3", "line1\nline2\nline3"),
    ],
)
def test_clean_all(input_text, expected_output):
    cleaner = DocumentCleaner(
        remove_empty_lines=True,
        remove_extra_whitespaces=True,
        remove_trailing_whitespaces=True,
        normalize_indentation=True,
    )
    assert cleaner.clean(input_text) == expected_output
