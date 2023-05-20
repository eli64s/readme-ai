"""Utility methods for the project."""

import re

import spacy

NLP = spacy.load("en_core_web_sm")


def reformat_sentence(text: str) -> str:
    """
    Removes extra white space and non-letter characters from a string.

    Parameters
    ----------
    text : str
        The input string.

    Returns
    -------
    str
        Reformatted text string.
    """
    # Remove non-letter characters from beginning of string
    text = re.sub(r"^[^a-zA-Z]*", "", text)

    # Remove extra white space around punctuation
    reformatted_text = re.sub(r"\s*([()'.,!?;:])(?!\.\s*\w)", r"\1", text)

    # Remove extra white space around hyphens
    reformatted_text = re.sub(r"\s*-\s*", "-", reformatted_text)

    return reformatted_text


def spacy_text_processor(text: str) -> str:
    """
    Process a text string using Spacy's NLP pipeline.

    Parameters
    ----------
    text : str
        The text to process.

    Returns
    -------
    str
        The processed text.
    """
    doc = NLP(text)
    processed_text = " ".join([token.text for token in doc])
    return processed_text


def valid_url(s: str) -> bool:
    """
    Check if a given string is a valid URL.

    Parameters
    ----------
    s : str
        The string to check.

    Returns
    -------
    bool
        Returns True if the string is a valid URL, otherwise False.

    Raises
    ------
    None

    Examples
    --------
    is_url("https://www.google.com/") --> True
    is_url("ftp://ftp.example.com/") --> True
    is_url("www.example.com") --> False
    """
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https:// or ftp:// or ftps://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,63}|[A-Z]{2,63}\.[A-Z]{2,63}))"
        r"(?::\d+)?"  # optional port number
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(regex.match(s))
