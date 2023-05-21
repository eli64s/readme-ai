"""Unit tests for utils.py"""

import re
from unittest.mock import MagicMock

import spacy

from src.utils import reformat_sentence, spacy_text_processor, valid_url


def test_reformat_sentence():
    sentence = "Hello ,   world  !"
    formatted_sentence = reformat_sentence(sentence)
    assert formatted_sentence == "Hello, world!"


def test_spacy_text_processor(mocker):
    # mock the Spacy's NLP object and its return value when it's called
    mock_nlp = mocker.patch.object(spacy, "load", return_value=MagicMock())
    mock_token = MagicMock()
    mock_token.text = "test"
    mock_nlp.return_value.return_value = [mock_token]

    # call the function with a test string
    processed_text = spacy_text_processor("This is a test string")

    # verify the return value
    assert processed_text == "test"

    # verify that the mock was called with the right parameters
    mock_nlp.assert_called_once_with("en_core_web_sm")
    mock_nlp.return_value.assert_called_once_with("This is a test string")


def test_valid_url():
    assert valid_url("https://www.google.com/")
    assert valid_url("ftp://ftp.example.com/")
    assert not valid_url("www.example.com")


def test_reformat_sentence_with_non_letter_characters():
    sentence = "1234Hello,   world!"
    formatted_sentence = reformat_sentence(sentence)
    assert formatted_sentence == "Hello, world!"


def test_reformat_sentence_with_hyphens():
    sentence = "Hello -   world!"
    formatted_sentence = reformat_sentence(sentence)
    assert formatted_sentence == "Hello-world!"
