"""Unit tests for tokenization LL API helper methods."""

from unittest.mock import patch

from readmeai.core import tokens


def test_adjust_max_tokens_valid():
    """Test that the max tokens is adjusted for a valid prompt."""
    max_tokens = 100
    prompt = "Hello, world!"
    target = "Hello!"
    adjusted_max_tokens = tokens.adjust_max_tokens(max_tokens, prompt, target)
    assert adjusted_max_tokens == 50


def test_adjust_max_tokens_invalid():
    """Test that the max tokens is adjusted for an invalid prompt."""
    max_tokens = 100
    prompt = "Invalid prompt"
    result = tokens.adjust_max_tokens(max_tokens, prompt)
    assert result == max_tokens // 2


@patch("readmeai.core.tokens.get_encoding")
def test_get_token_count(mock_get_encoding):
    """Test that the token count is returned."""
    text = "Hello world"
    encoding_name = "mock_encoding"
    mock_encoding = mock_get_encoding.return_value
    mock_encoding.encode.return_value = [1, 2, 3]
    result = tokens.get_token_count(text, encoding_name)
    mock_get_encoding.assert_called_with(encoding_name)
    assert result == 3


@patch("readmeai.core.tokens.encoding_for_model")
@patch("readmeai.core.tokens.get_encoding")
def test_get_token_encoder(mock_encoding_for_model, mock_get_encoding, config):
    """Test that the token encoder is returned."""
    mock_encoding_for_model.return_value = config.llm.model
    mock_get_encoding.return_value = config.llm.encoding
    result = tokens.get_token_encoder()
    assert result == config.llm.encoding


@patch("readmeai.core.tokens.get_token_encoder")
def test_truncate_tokens(mock_get_encoder):
    """Test that the tokens are truncated."""
    text = "Hello world out there"
    max_tokens = 10
    mock_encoder = mock_get_encoder.return_value
    mock_encoder.encode.return_value = [1] * 15
    result = tokens.truncate_tokens(text, max_tokens)
    assert len(result) < len(text)
    mock_get_encoder.side_effect = Exception
    assert tokens.truncate_tokens(text, 10) == text
