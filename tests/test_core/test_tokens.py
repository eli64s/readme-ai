"""Unit tests for tokenization LL API helper methods."""

import pytest

from readmeai.core.tokens import (
    _encoding_cache,
    _set_encoding_cache,
    adjust_max_tokens,
    token_counter,
    truncate_tokens,
)

ENCODING_NAME = "cl100k_base"


class MockEncoder:
    def encode(self, text):
        return text.split()


@pytest.fixture(autouse=True)
def mock_get_encoding(monkeypatch):
    def mock_encoder(encoding_name):
        return MockEncoder()

    monkeypatch.setattr("tiktoken.get_encoding", mock_encoder)


def test_adjust_max_tokens_valid_prompt():
    assert adjust_max_tokens(100, "Hello! This is a test") == 100


def test_adjust_max_tokens_invalid_prompt():
    assert adjust_max_tokens(100, "Invalid prompt") == 50


def test_adjust_max_tokens_edge_cases():
    assert adjust_max_tokens(0, "") == 0


def test_set_encoding_cache_new():
    encoder = _set_encoding_cache(ENCODING_NAME)
    assert _encoding_cache[ENCODING_NAME] == encoder


def test_set_encoding_cache_invalid():
    with pytest.raises(ValueError) as exc:
        _set_encoding_cache("invalid-encoding")
    assert isinstance(exc.value, ValueError)


def test_token_counter_valid():
    assert token_counter("Hello world", ENCODING_NAME) == 2


def test_token_counter_exception():
    with pytest.raises(ValueError) as exc:
        token_counter("", "invalid-encoding")
        assert isinstance(exc.value, ValueError)


def test_truncate_tokens_less_tokens(mock_get_encoding):
    assert (
        truncate_tokens(mock_get_encoding, "Hello world", 10) == "Hello world"
    )


def test_truncate_tokens_more_tokens(mock_get_encoding):
    assert (
        truncate_tokens(mock_get_encoding, "Hello world", 1) == "Hello world"
    )


def test_truncate_tokens_empty_string(mock_get_encoding):
    assert truncate_tokens(mock_get_encoding, "", 10) == ""


def test_truncate_tokens_exception(mock_get_encoding, caplog):
    assert (
        truncate_tokens(mock_get_encoding, "Hello world", 100) == "Hello world"
    )
    assert "Error truncating tokens" in caplog.text


def test_truncate_tokens_different_encodings(mock_get_encoding):
    assert truncate_tokens(mock_get_encoding, "Test", 1) == "Test"
