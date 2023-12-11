"""Unit tests for tokens module."""

from tiktoken import Encoding

from readmeai.core import tokens


def test_adjust_max_tokens():
    """Test adjust_max_tokens method."""
    max_tokens = 100
    prompt = "Hello, world!"
    target = "Hello!"
    adjusted_max_tokens = tokens.adjust_max_tokens(max_tokens, prompt, target)
    assert adjusted_max_tokens == 20


def test_get_token_count():
    """Test get_token_count method."""
    text = "Hello, world!"
    encoding_name = "cl100k_base"
    token_count = tokens.get_token_count(text, encoding_name)
    assert token_count == 4


def test_get_token_encoder():
    """Test get_token_encoder method."""
    token_encoder = tokens.get_token_encoder()
    assert isinstance(token_encoder, Encoding)


def test_truncate_tokens():
    """Test truncate_tokens method."""
    text = "Hello, world!"
    max_tokens = 5
    truncated_text = tokens.truncate_tokens(text, max_tokens)
    assert truncated_text == "Hello, world!"
