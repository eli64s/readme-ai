import pytest

from readmeai.models.tokens import (
    _encoding_cache,
    _set_encoding_cache,
    count_tokens,
    truncate_tokens,
    update_max_tokens,
)

ENCODING_NAME = "cl100k_base"


class MockEncoder:
    def encode(self, text):
        """Mock the encode method."""
        return text.split()


@pytest.fixture(autouse=True)
def mock_get_encoding(monkeypatch: pytest.MonkeyPatch):
    """Mock the get_encoding function."""

    def mock_encoder(encoding_name):
        """Mock the get_encoding function."""
        return MockEncoder()

    monkeypatch.setattr("tiktoken.get_encoding", mock_encoder)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("This is a [SEP] test.", 8),
        ("Hello world!<|endoftext|>", 9),
        ("Hello world", 2),
        ("<|endoftext|>", 7),  # Original issue
        ("<|endoftext|>", 7),  # Repeated start token
        ("<| endoftext |>", 6),  # Spaces inserted
        ("hello <|endoftext|> world", 8),  # Token embedded in text
        ("Hello, 世界", 6),
        ("👍👍👍", 9),
        # New test cases designed to challenge the encoder
        (",", 1),  # Single comma, might be related to the mentioned issue
        ("[UNK]", 3),  # Testing a common unknown token representation
        ("[CLS] [SEP]", 6),  # Testing with special tokens used in some models
        ("\n", 1),  # Newline character, to see if it's counted as a token
        (
            "This is a test with a newline\ncharacter",
            9,
        ),  # Including newline within text
        (
            "This is a test with a carriage return\rcharacter",
            10,
        ),  # Carriage return
        (
            "\"'!@#$%^&*()_+-=[]{}|;':,./<>?",
            19,
        ),  # Special characters, might be tokenized differently
        (
            "This is a `test` case.",
            8,
        ),  # Backticks, which might be problematic or special
        (
            "This \t has \t tabs",
            5,
        ),  # Tab characters, to see if they're counted or ignored
        ("   ", 1),  # Multiple spaces, to check if they're ignored
        (
            "ThisIsAStringWithoutSpacesButWithCamelCase",
            11,
        ),  # CamelCase, to see if it's split
        (
            "This_is_a_string_with_underscores",
            8,
        ),  # Underscores, might be treated as delimiters
        ("Emoji sequence 👩‍👩‍👧‍👦 is tricky", 21),  # Complex emoji sequence
        (
            "Surrogate pairs 😇 are encoded differently",
            8,
        ),  # Surrogate pairs in Unicode
        (
            "Here is a zero-width space​character",
            8,
        ),  # Zero-width space, might not be visible
        (
            "Text with\u200bzero-width space",
            6,
        ),  # Explicit zero-width space, Unicode escape
        (
            "VeryLongStringWithoutSpacesOrPunctuation",
            8,
        ),  # Long string without delimiters
        ("", 0),  # Empty string, edge case
        (" ", 1),  # Single space, edge case
        ("[PAD]", 3),  # Testing with padding token
        ("This\nincludes\nmultiple\nlines", 7),  # Multiple newline characters
    ],
)
def test_count_tokens_edge_cases(text, expected, ENCODING_NAME="cl100k_base"):
    """
    Test count_tokens function with various edge cases. See below for details:
    https://github.com/run-llama/llama_index/issues/1206
    """
    assert count_tokens(text, ENCODING_NAME) == expected


def test_count_tokens_exception():
    with pytest.raises(TypeError) as exc:
        count_tokens([1, 2, 4, 5], ENCODING_NAME)
    assert isinstance(exc.value, TypeError)


def test_update_max_tokens_valid_prompt():
    assert update_max_tokens(100, "Hello! This is a test") == 100


def test_update_max_tokens_invalid_prompt():
    assert update_max_tokens(100, "Invalid prompt") == 50


def test_update_max_tokens_edge_cases():
    assert update_max_tokens(0, "") == 0


def test_set_encoding_cache_new():
    encoder = _set_encoding_cache(ENCODING_NAME)
    assert _encoding_cache[ENCODING_NAME] == encoder


def test_set_encoding_cache_invalid():
    with pytest.raises(ValueError) as exc:
        _set_encoding_cache("invalid-encoding")
    assert isinstance(exc.value, ValueError)


def test_truncate_tokens_less_tokens(mock_get_encoding: None):
    assert (
        truncate_tokens(mock_get_encoding, "Hello world", 10) == "Hello world"
    )


def test_truncate_tokens_more_tokens(mock_get_encoding: None):
    assert (
        truncate_tokens(mock_get_encoding, "Hello world", 1) == "Hello world"
    )


def test_truncate_tokens_empty_string(mock_get_encoding: None):
    assert truncate_tokens(mock_get_encoding, "", 10) == ""


def test_truncate_tokens_exception(
    mock_get_encoding: None, caplog: pytest.LogCaptureFixture
):
    with pytest.raises(Exception) as e:
        truncate_tokens(mock_get_encoding, None, 10)
        assert isinstance(e, Exception)


def test_truncate_tokens_different_encodings(mock_get_encoding: None):
    assert truncate_tokens(mock_get_encoding, "Test", 1) == "Test"


def test_truncate_tokens_truncation_required():
    """Test where the number of tokens exceeds the maximum allowed."""
    max_tokens = 3
    long_text = "This is a longer text that needs to be truncated"
    truncated_text = truncate_tokens(ENCODING_NAME, long_text, max_tokens)
    assert len(truncated_text) < len(long_text)
    assert "This is a" in truncated_text
