"""Unit tests that test the markdown table creator methods."""

from unittest.mock import patch

from readmeai.markdown.tables import (
    construct_markdown_table,
    create_hyperlink,
    extract_folder_name,
    format_as_markdown_table,
    format_code_summaries,
    generate_markdown_tables,
    group_summaries_by_folder,
    is_valid_tuple_summary,
)
from readmeai.services import git_utils


def test_construct_markdown_table(mock_config):
    """Test that the construct_markdown_table function constructs the table."""
    data = [("module1.py", "Summary 1")]
    repository = mock_config.git.repository
    full_name = "eli64s/readme-ai"
    table = construct_markdown_table(data, repository, full_name)
    assert "Summary" in table
    assert "| ---" in table
    assert f"[module1.py]({repository}" in table


def test_create_hyperlink(mock_config):
    """Test that the create_hyperlink function creates the hyperlink."""
    file_name = "main.py"
    module = f"readmeai/{file_name}"
    full_name = mock_config.git.full_name
    repo_url = mock_config.git.repository
    repo_file_url = git_utils.fetch_git_file_url(module, full_name, repo_url)
    hyperlink = create_hyperlink(
        file_name,
        full_name,
        module,
        repo_url,
    )
    assert f"[{file_name}]({repo_file_url}" in hyperlink


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
    placeholder = mock_config.md.default
    summaries = [("module1.py", placeholder), ("invalid", placeholder)]
    formatted = format_code_summaries(placeholder, summaries)
    assert formatted == [
        ("module1.py", placeholder),
        ("invalid", placeholder),
    ]


@patch("readmeai.markdown.tables.group_summaries_by_folder")
@patch("readmeai.markdown.tables.construct_markdown_table")
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
