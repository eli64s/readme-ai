"""
Tests for building and formatting the markdown tables.
"""

from unittest.mock import patch

import pytest

from readmeai.generators.tables import (
    construct_markdown_table,
    extract_folder_name,
    format_as_markdown_table,
    format_code_summaries,
    generate_markdown_tables,
    group_summaries_by_folder,
    is_valid_tuple_summary,
)

mock_data = [
    ("file1.py", "Summary 1"),
    ("dir/file2.py", "Summary 2"),
    ("file3.py", "Summary 3"),
]


@pytest.fixture
def mock_logger():
    with patch("readmeai.generators.tables._logger") as mock:
        yield mock


def test_construct_markdown_table_local_repo(mock_logger):
    with patch("pathlib.Path.exists", return_value=True):
        result = construct_markdown_table(
            mock_data,
            "/local/repo",
            "local_repo",
        )

    assert "| File | Summary |" in result
    assert "| [file1.py](/local/repo/file1.py) | Summary 1 |" in result
    assert "| [file2.py](/local/repo/dir/file2.py) | Summary 2 |" in result
    assert "| [file3.py](/local/repo/file3.py) | Summary 3 |" in result


def test_construct_markdown_table_remote_repo(mock_logger):
    with (
        patch("pathlib.Path.exists", return_value=False),
        patch("readmeai.generators.tables.GitURL") as mock_git_url,
    ):
        mock_git_url.create.return_value.get_file_url.side_effect = [
            "https://github.com/owner/repo/blob/main/file1.py",
            "https://github.com/owner/repo/blob/main/dir/file2.py",
            "https://github.com/owner/repo/blob/main/file3.py",
        ]
        result = construct_markdown_table(
            mock_data,
            "https://github.com/owner/repo.git",
            "owner/repo",
        )

    assert "| File | Summary |" in result
    assert (
        "| [file1.py](https://github.com/owner/repo/blob/main/file1.py) | Summary 1 |"
        in result
    )
    assert (
        "| [file2.py](https://github.com/owner/repo/blob/main/dir/file2.py) | Summary 2 |"
        in result
    )
    assert (
        "| [file3.py](https://github.com/owner/repo/blob/main/file3.py) | Summary 3 |"
        in result
    )


def test_construct_markdown_table_max_rows(mock_logger):
    result = construct_markdown_table(
        mock_data,
        "/local/repo",
        "local_repo",
        max_rows=2,
    )

    assert "| File | Summary |" in result
    assert "| [file1.py](/local/repo/file1.py) | Summary 1 |" in result
    assert "| [file2.py](/local/repo/dir/file2.py) | Summary 2 |" in result
    assert "| ... | ... |" in result
    assert "| [file3.py](/local/repo/file3.py) | Summary 3 |" not in result
    mock_logger.warning.assert_called_once()


def test_construct_markdown_table_empty_data(mock_logger):
    result = construct_markdown_table([], "/local/repo", "local_repo")

    assert result == ""
    mock_logger.warning.assert_called_once()


def test_construct_markdown_table_invalid_git_url(mock_logger):
    with (
        patch("pathlib.Path.exists", return_value=False),
        patch("readmeai.generators.tables.GitURL") as mock_git_url,
    ):
        mock_git_url.create.side_effect = ValueError("Invalid Git URL")
        result = construct_markdown_table(
            mock_data,
            "invalid_url",
            "owner/repo",
        )

    assert "| File | Summary |" in result
    mock_logger.error.assert_called_once()


def test_construct_markdown_table_git_url_file_error(mock_logger):
    with (
        patch("pathlib.Path.exists", return_value=False),
        patch("readmeai.generators.tables.GitURL") as mock_git_url,
    ):
        mock_git_url.create.return_value.get_file_url.side_effect = [
            "https://github.com/owner/repo/blob/main/file1.py",
            ValueError("Invalid file path"),
            "https://github.com/owner/repo/blob/main/file3.py",
        ]
        result = construct_markdown_table(
            mock_data,
            "https://github.com/owner/repo.git",
            "owner/repo",
        )

    assert "| File | Summary |" in result
    assert (
        "| [file1.py](https://github.com/owner/repo/blob/main/file1.py) | Summary 1 |"
        in result
    )
    assert "| file2.py | Summary 2 |" in result
    assert (
        "| [file3.py](https://github.com/owner/repo/blob/main/file3.py) | Summary 3 |"
        in result
    )
    mock_logger.error.assert_called_once()


@pytest.mark.parametrize(
    "invalid_input",
    [
        ("not a list", "/local/repo", "local_repo"),
        (
            [("file1.py", "Summary 1"), "not a tuple"],
            "/local/repo",
            "local_repo",
        ),
        (mock_data, 12345, "local_repo"),
        (mock_data, "/local/repo", 12345),
        (mock_data, "/local/repo", "local_repo", "not an int"),
    ],
)
def test_construct_markdown_table_invalid_input(invalid_input):
    with pytest.raises(AssertionError):
        construct_markdown_table(*invalid_input)


def test_extract_folder_name():
    """Test that the extract_folder_name function extracts the folder name."""
    assert extract_folder_name("folder/module.py") == "folder"
    assert extract_folder_name("module.py") == "."


def test_format_as_markdown_table():
    """Test that the format_as_markdown_table function formats the table."""
    rows = [["Header1", "Header2"], ["---", "---"], ["Data1", "Data2"]]
    table = format_as_markdown_table(rows)
    assert "Header1" in table
    assert "--" in table
    assert "Data2" in table


def test_format_code_summaries(mock_config):
    """Test that the format_code_summaries function formats the summaries."""
    placeholder = mock_config.md.placeholder
    summaries = [("module1.py", placeholder), ("invalid", placeholder)]
    formatted = format_code_summaries(placeholder, summaries)
    assert formatted == [
        ("module1.py", placeholder),
        ("invalid", placeholder),
    ]


@patch("readmeai.generators.tables.group_summaries_by_folder")
@patch("readmeai.generators.tables.construct_markdown_table")
def test_generate_markdown_tables(mock_construct, mock_group):
    """Test that the generate_markdown_tables function generates the tables."""
    mock_group.return_value = {"folder1": [("module1.py", "Summary 1")]}
    mock_construct.return_value = "Mocked Table"
    dropdown_template = "## {0}\n{1}"
    result = generate_markdown_tables(
        dropdown_template,
        [("module1.py", "Summary 1")],
        "ProjectName",
        "RepoURL",
    )
    assert result == "## folder1\nMocked Table"


def test_group_summaries_by_folder():
    """Test that the group_summaries_by_folder function groups the summaries."""
    summaries = [
        ("folder1/module1.py", "Summary 1"),
        ("folder2/module2.py", "Summary 2"),
    ]
    grouped = group_summaries_by_folder(summaries)
    assert grouped == {
        "folder1": [("folder1/module1.py", "Summary 1")],
        "folder2": [("folder2/module2.py", "Summary 2")],
    }


def test_is_valid_tuple_summary():
    """Test that the is_valid_tuple_summary function validates the summary."""
    valid_summary = ("module.py", "Summary")
    invalid_summary = "Invalid Summary"
    assert is_valid_tuple_summary(valid_summary)
    assert not is_valid_tuple_summary(invalid_summary)
