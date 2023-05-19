"""Unit tests for utils.py"""

from src.utils import reformat_sentence, valid_url


def test_reformat_sentence():
    # Test reformatting a sentence
    sentence = "Hello ,   world  !"
    formatted_sentence = reformat_sentence(sentence)
    assert formatted_sentence == "Hello, world!"


def test_valid_url():
    # Test valid URL detection
    assert valid_url("https://www.google.com/")
    assert valid_url("ftp://ftp.example.com/")
    assert not valid_url("www.example.com")
