"""Creates markdown tables to store LLM text responses in the README file."""

from pathlib import Path
from typing import List, Tuple

from readmeai.core.logger import Logger
from readmeai.services.git_utils import fetch_git_file_url

logger = Logger(__name__)


def construct_markdown_table(
    data: List[Tuple[str, str]], repo_url: str, full_name: str
) -> str:
    """Builds a Markdown table from the provided data."""
    headers = ["File", "Summary"]
    table_rows = [headers, ["---", "---"]]
    for module, summary in data:
        file_name = str(Path(module).name)
        hyperlink = create_hyperlink(file_name, full_name, module, repo_url)
        table_rows.append([hyperlink, summary])
    return format_as_markdown_table(table_rows)


def create_hyperlink(
    file_name: str, full_name: str, module: str, repo_url: str
) -> str:
    """
    Creates a hyperlink for a file, using its Git URL if possible.
    """
    if "invalid" in full_name.lower():
        return file_name
    git_file_link = fetch_git_file_url(module, full_name, repo_url)
    return f"[{file_name}]({git_file_link})"


def extract_folder_name(module: str) -> str:
    """Extracts the folder name from a module path."""
    path_parts = Path(module).parts
    return ".".join(path_parts[:-1]) if len(path_parts) > 1 else "."


def format_as_markdown_table(rows: List[List[str]]) -> str:
    """Formats rows of data as a Markdown table."""
    max_column_widths = [
        max(len(str(row[col])) for row in rows) for col in range(len(rows[0]))
    ]

    formatted_lines = [
        "| "
        + " | ".join(
            str(item).ljust(width)
            for item, width in zip(row, max_column_widths)
        )
        + " |"
        for row in rows
    ]

    return "\n".join(formatted_lines)


def format_code_summaries(
    placeholder: str, code_summaries: Tuple[str, str]
) -> List[Tuple[str, str]]:
    """Converts the given code summaries into a formatted list."""
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
    summaries: List[Tuple[str, str]],
    project_name: str,
    repository_url: str,
) -> str:
    """Produces Markdown tables for each project sub-directory."""
    summaries_by_folder = group_summaries_by_folder(summaries)

    markdown_tables = []
    for folder, entries in summaries_by_folder.items():
        table_in_markdown = construct_markdown_table(
            entries, repository_url, project_name
        )
        table_wrapper = table_widget.format(folder, table_in_markdown)
        markdown_tables.append(table_wrapper)

    return "\n".join(markdown_tables)


def group_summaries_by_folder(summaries: List[Tuple[str, str]]) -> dict:
    """Groups code summaries by their sub-directory."""
    folder_map = {}
    for module, summary in summaries:
        folder_name = extract_folder_name(module)
        folder_map.setdefault(folder_name, []).append((module, summary))
    return folder_map


def is_valid_tuple_summary(summary: Tuple[str, str]) -> bool:
    """Checks if a summary is a valid tuple format."""
    return isinstance(summary, tuple) and len(summary) == 2
