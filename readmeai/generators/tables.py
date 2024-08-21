"""
Creates Markdown tables to store LLM text responses in the README file.
"""

from pathlib import Path

from readmeai.core.logger import Logger
from readmeai.vcs.url_builder import GitURL

_logger = Logger(__name__)


def construct_markdown_table(
    data: list[tuple[str, str]],
    repo_path: str | Path,
    full_name: str,
    max_rows: int = 100,
) -> str:
    """
    Builds a Markdown table to store LLM text responses in README file.
    """
    assert isinstance(data, list), "Data must be a list"
    assert all(
        isinstance(item, tuple) and len(item) == 2 for item in data
    ), "Each data item must be a tuple of (str, str)"
    assert isinstance(
        repo_path,
        str | Path,
    ), "repo_path must be a string or Path"
    assert isinstance(full_name, str), "full_name must be a string"
    assert (
        isinstance(max_rows, int) and max_rows > 0
    ), "max_rows must be a positive integer"

    if not data:
        _logger.warning("Empty data provided for Markdown table")
        return ""

    is_local_repo = Path(repo_path).exists()

    if not is_local_repo:
        try:
            git_url = GitURL.create(str(repo_path))
        except ValueError:
            _logger.error(f"Invalid Git repository URL: {repo_path}")
            is_local_repo = True  # Fallback to treating it as a local path

    headers = ["File", "Summary"]
    table_rows = [headers, ["---", "---"]]

    for module, summary in data[:max_rows]:
        file_name = Path(module).name
        if is_local_repo:
            file_path = Path(repo_path) / module
            md_format_file_url = f"[{file_name}]({file_path})"
        else:
            try:
                file_url = git_url.get_file_url(module)
                md_format_file_url = f"[{file_name}]({file_url})"
            except ValueError as e:
                _logger.error(f"Error generating file URL for {module}: {e}")
                md_format_file_url = file_name

        table_rows.append([md_format_file_url, summary])

    if len(data) > max_rows:
        _logger.warning(
            f"Table truncated. Showing {max_rows} out of {len(data)} rows.",
        )
        table_rows.append(["...", "..."])

    return _format_as_markdown_table(table_rows)


def _format_as_markdown_table(rows: list[list[str]]) -> str:
    """
    Formats the given rows as a Markdown table.
    """
    assert len(rows) >= 3, "Table must have at least headers and separator"
    assert all(
        len(row) == len(rows[0]) for row in rows
    ), "All rows must have the same number of columns"

    return "\n".join(f"| {' | '.join(row)} |" for row in rows)


def extract_folder_name(module: str) -> str:
    """
    Extracts the folder name from a module path.
    """
    path_parts = Path(module).parts
    return ".".join(path_parts[:-1]) if len(path_parts) > 1 else "."


def format_as_markdown_table(rows: list[list[str]]) -> str:
    """
    Formats rows of data as a Markdown table.
    """
    max_column_widths = [
        max(len(str(row[col])) for row in rows) for col in range(len(rows[0]))
    ]

    formatted_lines = [
        "| "
        + " | ".join(
            str(item).ljust(width)
            for item, width in zip(row, max_column_widths, strict=False)
        )
        + " |"
        for row in rows
    ]

    return "\n".join(formatted_lines)


def format_code_summaries(
    placeholder: str,
    code_summaries: list[tuple[str, str]],
) -> list[tuple[str, str]]:
    """
    Converts the given code summaries into a formatted list.
    """
    formatted_summaries = []

    for summary in code_summaries:
        if is_valid_tuple_summary(summary):
            module, summary_text = summary
        else:
            module, summary_text = summary, placeholder

        formatted_summaries.append((module, summary_text))

    return formatted_summaries


def generate_markdown_tables(
    table_widget: str,
    summaries: list[tuple[str, str]],
    project_name: str,
    repository_url: str,
) -> str:
    """
    Produces Markdown tables for each project sub-directory.
    """
    summaries_by_folder = group_summaries_by_folder(summaries)

    markdown_tables = []
    for folder, entries in summaries_by_folder.items():
        table_in_markdown = construct_markdown_table(
            entries,
            repository_url,
            project_name,
        )
        table_wrapper = table_widget.format(folder, table_in_markdown)
        markdown_tables.append(table_wrapper)

    return "\n".join(markdown_tables)


def group_summaries_by_folder(summaries: list[tuple[str, str]]) -> dict:
    """
    Groups code summaries by their sub-directory.
    """
    folder_map: dict[str, list[tuple[str, str]]] = {}
    for module, summary in summaries:
        folder_name = extract_folder_name(module)
        folder_map.setdefault(folder_name, []).append((module, summary))
    return folder_map


def is_valid_tuple_summary(summary: tuple[str, str]) -> bool:
    """
    Checks if a summary is a valid tuple format.
    """
    return isinstance(summary, tuple) and len(summary) == 2
