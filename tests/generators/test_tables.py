from pathlib import Path

import pytest

from readmeai.generators.tables import (
    _generate_nested_module_content,
    _generate_table_rows,
    _get_file_hyperlink,
    build_submodule_disclosure_widget,
    format_code_summaries,
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


def test_generate_nested_module_tables(
    sample_summaries, project_path, repository_url
):
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
    link = _get_file_hyperlink(
        file_path_str, project_path, is_local, repository_url
    )
    assert link == expected_link


def test_build_submodule_disclosure_widget(
    sample_summaries, project_path, repository_url
):
    grouped = group_summaries_by_nested_module(sample_summaries)
    output = build_submodule_disclosure_widget(
        grouped, project_path, repository_url
    )
    assert "<details open>" in output
    assert "<table>" in output
    assert "Facilitates project maintenance and development tasks." in output


def test_generate_table_rows():
    files = [
        ("src/app.py", "Main application logic."),
        ("src/cli.py", "Defines the command-line interface."),
    ]
    repo_path = "/path/to/readme-ai-streamlit"
    repo_url = "https://github.com/eli64s/readme-ai-streamlit"
    is_local_repo = False
    rows = _generate_table_rows(
        files, repo_path, is_local_repo, repo_url, indent=""
    )
    assert "<tr>" in rows[0]
    assert "app.py" in rows[0]
    assert "<tr>\n\t<td><b><a href=" in rows[1]
    assert len(rows) == 2


def test_generate_nested_module_content(
    sample_summaries, project_path, repository_url
):
    grouped = group_summaries_by_nested_module(sample_summaries)
    src_module = grouped["src"]
    content = _generate_nested_module_content(
        src_module, project_path, True, repository_url
    )
    assert "<table>" in content[0]
    assert (
        "<tr>\n\t<td><b><a href='/path/to/readme-ai-streamlit/src/cli.py'>"
        "cli.py</a></b></td>\n\t<td>"
    ) in content[1]
    assert "helpers.py" in "".join(content)


def test_invalid_summary_handling():
    invalid_summaries = [
        (None, "Valid summary"),
        ("src/app.py", None),
        (123, "Summary with non-string module"),
    ]
    grouped = group_summaries_by_nested_module(invalid_summaries)
    assert grouped == {"__root__": []}


def test_empty_summaries():
    empty_summaries = []
    output = generate_nested_module_tables(
        empty_summaries, "/path", "https://repo.url"
    )
    assert (
        "<blockquote>\n\t\t\t<table>\n\t\t\t</table>\n\t\t</blockquote>"
        in output
    )


def test_format_code_summaries():
    code_summaries = [("module.py", "Summary of module.")]
    placeholder = "No summary available."
    formatted = format_code_summaries(placeholder, code_summaries)
    assert formatted == [("module.py", "Summary of module.")]

    code_summaries = ["module.py"]
    formatted = format_code_summaries(placeholder, code_summaries)
    assert formatted == [("module.py", "No summary available.")]
