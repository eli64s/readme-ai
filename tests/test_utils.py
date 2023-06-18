"""Unit tests for utils.py"""

from pathlib import Path
from unittest.mock import patch

import git
import pytest

from src.utils import (
    clone_repository,
    flatten_list,
    format_sentence,
    get_token_count,
    is_valid_url,
    truncate_text_tokens,
)


@patch("src.utils.git.Repo.clone_from")
def test_clone_repository_invalid_url(mock_clone_from):
    mock_clone_from.side_effect = git.exc.GitCommandError(
        command="git clone",
        status=128,
        stderr="fatal: repository 'is_valid_url' does not exist",
    )
    with pytest.raises(ValueError) as exc:
        clone_repository("https//www.github.woah///git.git", Path("temp_file"))

    assert "Error cloning repository" in str(exc.value)


@patch("src.utils.git.Repo.clone_from")
def test_clone_repository(mock_clone_from, config, tmp_path):
    url = config["git"]["repository"]
    path = tmp_path / config["git"]["name"]
    clone_repository(url, Path(path))
    assert Path(path).exists()


def test_get_token_count(config):
    encoding_name = config["api"]["encoding"]
    assert get_token_count("", encoding_name) == 0
    assert get_token_count("Hello, world!", encoding_name) == 4
    assert get_token_count("Hello, world! Hello, world!", encoding_name) == 8


def test_truncate_text_tokens(config):
    encoding_name = config["api"]["encoding"]
    max_tokens = 10
    assert truncate_text_tokens("", encoding_name, max_tokens) == ""
    input_text = "This is a long text with more tokens than the maximum limit"
    truncated_text = truncate_text_tokens(input_text, encoding_name, max_tokens)
    assert len(truncated_text.split()) == 10


def test_is_valid_url():
    assert is_valid_url("https://www.example.com")
    assert not is_valid_url("inis_valid_url")


def test_flatten_list():
    assert flatten_list([]) == []
    nested_list = [[1, 2, 3], [4, [5, 6]], 7, [8, [9]]]
    flattened_list = flatten_list(nested_list)
    assert flattened_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_format_sentence():
    assert format_sentence("") == ""
    input_text = "   Hello,   world! This is a  test sentence...   "
    expected_output = "Hello, world! This is a test sentence..."
    assert format_sentence(input_text) == expected_output


if __name__ == "__main__":
    pytest.main()
