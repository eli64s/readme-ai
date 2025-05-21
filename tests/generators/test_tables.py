from pathlib import Path

import pytest
from readmeai.generators.tables import (
    _generate_nested_module_content,
    _generate_table_rows,
    _get_file_hyperlink,
    build_submodule_disclosure_widget,
    format_summary,
    generate_nested_module_tables,
    group_summaries_by_nested_module,
)


@pytest.fixture
def sample_summaries() -> list[tuple[str, str]]:
    return [
        ("Makefile", "Facilitates project maintenance and development tasks."),
        ("pyproject.toml", "Contains project metadata and dependencies."),
        ("scripts/clean.sh", "Script to clean build artifacts."),
        ("src/cli.py", "Defines the command-line interface."),
        ("src/app.py", "Main application logic."),
        ("src/utils/helpers.py", "Utility functions for the app."),
    ]


@pytest.fixture
def project_path() -> Path:
    return Path("/path/to/readme-ai-streamlit")


@pytest.fixture
def repository_url() -> str:
    return "https://github.com/eli64s/readme-ai-streamlit"


def test_format_summary():
    input_summary = "This is a test. It has multiple sentences."
    expected_output = "- This is a test<br>- It has multiple sentences."
    assert format_summary(input_summary) == expected_output

    input_summary = "Single sentence summary"
    expected_output = "Single sentence summary"
    assert format_summary(input_summary) == expected_output


def test_group_summaries_by_nested_module(sample_summaries):
    grouped = group_summaries_by_nested_module(sample_summaries)
    expected = {
        "__root__": [
            (
                "Makefile",
                "Facilitates project maintenance and development tasks.",
            ),
            ("pyproject.toml", "Contains project metadata and dependencies."),
        ],
        "scripts": {
            "": [
                ("scripts/clean.sh", "Script to clean build artifacts."),
            ]
        },
        "src": {
            "": [],
            "utils": {
                "": [
                    ("src/utils/helpers.py", "Utility functions for the app."),
                ]
            },
            "cli.py": {},
            "app.py": {},
        },
    }
    assert grouped["__root__"] == expected["__root__"]
    assert grouped["scripts"] == expected["scripts"]
    assert grouped["src"]["utils"] == expected["src"]["utils"]


def test_generate_nested_module_tables(sample_summaries, project_path, repository_url):
    output = generate_nested_module_tables(
        sample_summaries, project_path, repository_url
    )
    assert "<details open>" in output
    assert (
        "<details open>\n\t<summary><b><code>README-AI-STREAMLIT/"
        "</code></b></summary>\n\t<details>" in output
    )
    assert "Makefile" in output
    assert "cli.py" in output
    assert "helpers.py" in output


@pytest.mark.parametrize(
    "file_path_str, is_local, expected_link",
    [
        (
            "src/app.py",
            False,
            "https://github.com/eli64s/readme-ai-streamlit/blob/master/src/app.py",
        ),
        (
            "Makefile",
            False,
            "https://github.com/eli64s/readme-ai-streamlit/blob/master/Makefile",
        ),
        (
            "src/utils/helpers.py",
            True,
            "/path/to/readme-ai-streamlit/src/utils/helpers.py",
        ),
    ],
)
def test_get_file_hyperlink(
    file_path_str, is_local, expected_link, project_path, repository_url
):
    link = _get_file_hyperlink(file_path_str, project_path, is_local, repository_url)
    assert link == expected_link


def test_invalid_summary_handling():
    invalid_summaries = [
        (None, "Valid summary"),
        ("src/app.py", None),
        (123, "Summary with non-string module"),
    ]
    grouped = group_summaries_by_nested_module(invalid_summaries)
    assert grouped == {"__root__": []}


def test_empty_summaries():
    """Test generating tables with empty summaries"""
    empty_summaries = []
    output = generate_nested_module_tables(empty_summaries, "/path", "https://repo.url")
    # Updated to match actual empty table structure with styling
    expected_structure = """<div class='directory-path' style='padding: 8px 0; color: #666;'>
\t\t\t\t<code><b>⦿ __root__</b></code>
\t\t\t<table style='width: 100%; border-collapse: collapse;'>"""
    assert expected_structure in output


def test_generate_nested_module_tables(sample_summaries, project_path, repository_url):
    """Test generating nested module tables"""
    output = generate_nested_module_tables(
        sample_summaries, project_path, repository_url
    )
    # Updated to include directory structure and styling
    expected_header = """<details open>
\t<summary><b><code>README-AI-STREAMLIT/</code></b></summary>
\t<!-- __root__ Submodule -->
\t<details>"""
    assert expected_header in output
    assert "Makefile" in output
    assert "cli.py" in output
    assert "helpers.py" in output


def test_generate_table_rows():
    """Test generating table rows with styling"""
    files = [
        ("src/app.py", "Main application logic."),
        ("src/cli.py", "Defines the command-line interface."),
    ]
    repo_path = "/path/to/readme-ai-streamlit"
    repo_url = "https://github.com/eli64s/readme-ai-streamlit"
    is_local_repo = False
    rows = _generate_table_rows(files, repo_path, is_local_repo, repo_url, indent="")
    expected_row = """<tr style='border-bottom: 1px solid #eee;'>
\t<td style='padding: 8px;'><b><a href='"""
    assert expected_row in rows[0]
    assert len(rows) == 2


def test_generate_nested_module_content():
    """Test generating nested module content"""
    src_module = {
        "": [
            ("src/cli.py", "Defines the command-line interface."),
            ("src/app.py", "Main application logic."),
        ]
    }
    content = _generate_nested_module_content(
        src_module, "/path/to/readme-ai-streamlit", True, ""
    )
    expected_row = """<tr style='border-bottom: 1px solid #eee;'>
\t<td style='padding: 8px;'><b><a href='/path/to/readme-ai-streamlit/src/cli.py'>"""
    assert expected_row in "".join(content)


def test_build_submodule_disclosure_widget(
    sample_summaries, project_path, repository_url
):
    """Test building the submodule disclosure widget"""
    grouped = group_summaries_by_nested_module(sample_summaries)
    output = build_submodule_disclosure_widget(grouped, project_path, repository_url)

    # Check basic structure
    assert "<details open>" in output
    assert "<summary><b><code>README-AI-STREAMLIT/</code></b></summary>" in output

    # Check table styling and structure
    assert "<table style='width: 100%; border-collapse: collapse;'>" in output
    assert "<div class='directory-path' style='padding: 8px 0; color: #666;'>" in output

    # Check table headers
    assert (
        "<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>"
        in output
    )
    assert "<th style='text-align: left; padding: 8px;'>Summary</th>" in output

    # Check table rows
    assert "<tr style='border-bottom: 1px solid #eee;'>" in output
    assert "<td style='padding: 8px;'>" in output

    # Check content
    assert "Makefile" in output
    assert "pyproject.toml" in output
    assert "clean.sh" in output
    assert "helpers.py" in output
