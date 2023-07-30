"""Unit tests for utils.py"""

from pathlib import Path
from unittest.mock import patch

import pytest
from git import GitCommandError, Repo

from readmeai.utils import (
    adjust_max_tokens,
    clone_repository,
    flatten_list,
    format_sentence,
    get_github_file_link,
    get_token_count,
    get_user_repository_name,
    is_valid_url,
    truncate_text_tokens,
)


def test_clone_repository_success():
    with patch.object(Repo, "clone_from") as mock_clone:
        clone_repository("http://my-repo-url.com", Path("/tmp/my-repo"))
        mock_clone.assert_called_once_with(
            "http://my-repo-url.com", Path("/tmp/my-repo"), depth=1
        )


def test_clone_repository_failure():
    with patch.object(Repo, "clone_from") as mock_clone:
        mock_clone.side_effect = GitCommandError("git clone", "Some error")
        with pytest.raises(ValueError, match="Error cloning repository:"):
            clone_repository("http://my-repo-url.com", Path("/tmp/my-repo"))
        mock_clone.assert_called_once()


def test_get_github_file_link():
    url = get_github_file_link("path/to/my_file.py", "username/repo")
    assert url == "https://github.com/username/repo/blob/main/path/to/my_file.py"
    url = get_github_file_link("readme.md", "myorg/myrepo")
    assert url == "https://github.com/myorg/myrepo/blob/main/readme.md"
    url = get_github_file_link("dir/subdir/my_file.py", "anotheruser/anotherrepo")
    assert (
        url
        == "https://github.com/anotheruser/anotherrepo/blob/main/dir/subdir/my_file.py"
    )


def test_get_user_repository_name_valid_url():
    assert get_user_repository_name("https://github.com/user/repo") == "user/repo"
    assert get_user_repository_name("http://github.com/user/repo") == "user/repo"


def test_get_user_repository_name_invalid_url():
    assert (
        get_user_repository_name("https://notgithub.com/user/repo")
        == "Invalid remote git URL."
    )
    assert (
        get_user_repository_name("https://github.com/user") == "Invalid remote git URL."
    )
    assert get_user_repository_name("http://github") == "Invalid remote git URL."
    assert get_user_repository_name("invalid_url") == "Invalid remote git URL."


def test_adjust_max_tokens_with_valid_prompt():
    max_tokens = 150
    prompt = "Hello! How are you today?"
    result = adjust_max_tokens(max_tokens, prompt)
    assert result == 150, "Expected max tokens to remain the same for valid prompts"


def test_adjust_max_tokens_with_invalid_prompt():
    max_tokens = 150
    prompt = "How are you today?"
    result = adjust_max_tokens(max_tokens, prompt)
    assert (
        result == 50
    ), "Expected max tokens to be reduced to a third for invalid prompts"


def test_adjust_max_tokens_with_target_string():
    max_tokens = 120
    prompt = "Good morning! Have a nice day."
    target = "Good morning!"
    result = adjust_max_tokens(max_tokens, prompt, target)
    assert (
        result == 120
    ), "Expected max tokens to remain the same for prompts starting with target string"


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
