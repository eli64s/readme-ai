"""Generates Markdown tables for LLM-produced code summaries."""

from pathlib import Path
from typing import List, Tuple

from readmeai.core import logger
from readmeai.services import git_utilities as vcs

logger = logger.Logger(__name__)


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


def is_valid_tuple_summary(summary: Tuple[str, str]) -> bool:
    """Checks if a summary is a valid tuple format."""
    return isinstance(summary, tuple) and len(summary) == 2


def generate_markdown_tables(
    dropdown_template: str,
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
        table_wrapper = dropdown_template.format(folder, table_in_markdown)
        markdown_tables.append(table_wrapper)

    return "\n".join(markdown_tables)


def group_summaries_by_folder(summaries: List[Tuple[str, str]]) -> dict:
    """Groups code summaries by their sub-directory."""
    folder_map = {}
    for module, summary in summaries:
        folder_name = extract_folder_name(module)
        folder_map.setdefault(folder_name, []).append((module, summary))
    return folder_map


def extract_folder_name(module: str) -> str:
    """Extracts the folder name from a module path."""
    return (
        str(module).split("/")[-2].capitalize()
        if "/" in str(module)
        else "Root"
    )


def construct_markdown_table(
    data: List[Tuple[str, str]], repository: str, project_name: str
) -> str:
    """Builds a Markdown table from the provided data."""
    headers = ["File", "Summary"]
    table_rows = [headers, ["---"] * len(headers)]

    for module, summary in data:
        file_name = str(Path(module).name)
        hyperlink = create_hyperlink(
            file_name, project_name, module, repository
        )
        table_rows.append([hyperlink, summary])

    return format_as_markdown_table(table_rows)


def create_hyperlink(
    file_name: str, full_name: str, module: str, repo_url: str
) -> str:
    """Creates a hyperlink for a file, using its Git URL if possible."""
    if "invalid" in full_name.lower():
        return file_name
    git_file_link = vcs.get_remote_file_url(module, full_name, repo_url)
    return f"[{file_name}]({git_file_link})"


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
