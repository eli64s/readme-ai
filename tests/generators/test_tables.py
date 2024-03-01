"""
Tests for building and formatting the markdown tables.
"""

from unittest.mock import patch

from readmeai.generators.tables import (
    construct_markdown_table,
    extract_folder_name,
    format_as_markdown_table,
    format_code_summaries,
    generate_markdown_tables,
    group_summaries_by_folder,
    is_valid_tuple_summary,
)
from readmeai.services.git import fetch_git_file_url


def test_construct_markdown_table(mock_config):
    """Test that the construct_markdown_table function constructs the table."""
    data = [("module1.py", "Summary 1")]
    repo_url = str(mock_config.git.repository)
    full_name = mock_config.git.full_name
    expected_link = fetch_git_file_url(repo_url, full_name, "module1.py")
    table = construct_markdown_table(data, repo_url, full_name)
    assert expected_link in f"[module1.py]({expected_link})"
    assert "module1.py" in table
    assert "Summary 1" in table


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
