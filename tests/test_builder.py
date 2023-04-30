"""Unit tests for the builder.py module."""

import os
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src import builder


def test_get_badges():
    data = {
        "icons": [
            {"name": "Python", "src": "https://path.to/python.svg"},
            {"name": "Django", "src": "https://path.to/django.svg"},
        ]
    }
    dependencies = ["Python", "Django"]
    expected_result = (
        '<img src="https://path.to/python.svg" alt="Python" />\n\n'
        '<img src="https://path.to/django.svg" alt="Django" />'
    )
    assert builder.get_badges(data, dependencies) == expected_result


def test_format_badges():
    badges = [
        "https://path.to/python.svg",
        "https://path.to/django.svg",
        "https://path.to/flask.svg",
    ]
    dependencies = ["Python", "Django", "Flask"]
    expected_result = (
        '<img src="https://path.to/python.svg" alt="Python" />\n'
        '<img src="https://path.to/django.svg" alt="Django" />\n'
        '<img src="https://path.to/flask.svg" alt="Flask" />'
    )
    assert builder.format_badges(badges, dependencies) == expected_result


@patch("git.Repo.clone_from")
@patch("subprocess.check_output")
def test_create_directory_tree(mock_check_output, mock_clone_from):
    mock_check_output.return_value = b"repo\n|-- file.py\n`-- dir\n    `-- file2.py"
    url = "https://github.com/test/repo.git"
    expected_result = "```bash\nrepo\n|-- file.py\n`-- dir\n    `-- file2.py```"
    assert builder.create_directory_tree(url) == expected_result


@patch("git.Repo.clone_from")
@patch("subprocess.check_output")
def test_create_directory_tree_error(mock_check_output, mock_clone_from):
    mock_check_output.side_effect = Exception("Test error")
    url = "https://github.com/test/repo.git"
    assert builder.create_directory_tree(url) == ""


def test_create_tables():
    data = {
        "Module": ["src/file.py", "file2.py"],
        "Summary": ["Summary 1", "Summary 2"],
    }
    df = pd.DataFrame(data)
    dropdown = "<details>\n<summary>{0}</summary>\n\n{1}\n</details>\n\n"
    expected_result = (
        "<details>\n<summary>Root</summary>\n\n|    File |   Summary |\n"
        "|---------|-----------|\n| file2.py | Summary 2 |\n</details>\n\n"
        "<details>\n<summary>Src</summary>\n\n|    File |   Summary |\n"
        "|---------|-----------|\n| file.py | Summary 1 |\n</details>\n\n"
    )
    assert builder.create_tables(df, dropdown) == expected_result


def test_parse_pandas_cols():
    data = {
        "Module": ["src/file.py", "file2.py"],
        "Summary": ["Summary 1", "Summary 2"],
    }
    df = pd.DataFrame(data)
    expected_data = {
        "Module": ["src/file.py", "file2.py"],
        "Summary": ["Summary 1", "Summary 2"],
        "Directory": ["src", "."],
        "File": ["file.py", "file2.py"],
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(builder.parse_pandas_cols(df), expected_df)
