"""Unit tests for utils.py"""

from pathlib import Path
from unittest.mock import patch

import git
import nbformat
import pytest

from src.utils import (
    clone_repository,
    convert_ipynb_to_py,
    flatten_list,
    format_sentence,
    get_token_count,
    truncate_text_tokens,
    valid_url,
)


@patch("src.utils.git.Repo.clone_from")
def test_clone_repository_invalid_url(mock_clone_from):
    mock_clone_from.side_effect = git.exc.GitCommandError(
        command="git clone",
        status=128,
        stderr="fatal: repository 'valid_url' does not exist",
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


def test_convert_ipynb_to_py(tmp_path):
    nb_path = tmp_path / "notebook.ipynb"
    notebook_content = nbformat.v4.new_notebook()
    notebook_content.cells.append(
        nbformat.v4.new_code_cell("# coding: utf-8\nprint('Hello, world!')")
    )
    nbformat.write(notebook_content, str(nb_path))
    python_code = convert_ipynb_to_py(nb_path)
    assert python_code.startswith("# coding: utf-8")
    assert "print('Hello, world!')" in python_code


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


def test_valid_url():
    assert valid_url("https://www.example.com")
    assert not valid_url("invalid_url")


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
