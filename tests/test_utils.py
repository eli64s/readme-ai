"""Unit tests for utils.py"""

import pytest

from src.utils import format_sentence, valid_url


def test_format_sentence():
    assert format_sentence("   !hello,world!   ") == "hello,world!"
    assert format_sentence("   hello,    world!   ") == "hello, world!"
    assert format_sentence("hello  -  world") == "hello-world"
    assert format_sentence(" hello     world ") == "hello world"
    assert format_sentence(" hello (  world ) ") == "hello (world)"
    assert format_sentence("hello...  world") == "hello... world"
    assert format_sentence("hello  .  world") == "hello. world"
    assert format_sentence("hello  .world") == "hello.world"
    assert format_sentence("   123hello,    world!   ") == "hello, world!"
    assert format_sentence("   hello, 123   world!   ") == "hello, 123 world!"
    assert format_sentence("") == ""
    assert format_sentence("hello(world)") == "hello(world)"
    assert format_sentence("hello!?world") == "hello!?world"
    assert format_sentence("!! hello world !!") == "hello world!!"
    assert format_sentence("   -hello world-   ") == "hello world-"

    with pytest.raises(TypeError):
        format_sentence(None)
    with pytest.raises(TypeError):
        format_sentence(123)


def test_valid_url():
    assert valid_url("https://www.google.com") is True
    assert valid_url("http://www.google.com") is True
    assert valid_url("ftp://www.google.com") is True
    assert valid_url("ftps://www.google.com") is True
    assert valid_url("www.google.com") is False
    assert valid_url("https://google") is False
    assert valid_url("https://www.google") is True
    assert valid_url("https://www.google.c") is False
    assert valid_url("https://www.google.com/path") is True
    assert valid_url("https://www.google.com/path/subpath") is True
    assert valid_url("https://www.google.com?query=string") is True
    assert valid_url("http://user:pass@www.google.com") is False
    assert valid_url("http://www.google.com:8080") is True
    assert valid_url("telnet://www.google.com") is False
    assert valid_url("ssh://www.google.com") is False
    assert (
        valid_url("http://www.google.com?query=string_with_%20special%20chars")
        is True
    )
    assert valid_url("") is False

    with pytest.raises(TypeError):
        valid_url(None)
    with pytest.raises(TypeError):
        valid_url(123)
