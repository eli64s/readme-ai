"""Creates Markdown tables used to format the LLM generated code summaries."""

from pathlib import Path
from typing import List, Tuple

from readmeai.core import logger
from readmeai.utils import git

logger = logger.Logger(__name__)


def create_markdown_tables(
    placeholder: str, code_summary: Tuple[str, str]
) -> List[Tuple[str, str]]:
    """Formats the generated code code_summary into a list."""
    summary_list = []
    for summary in code_summary:
        if isinstance(summary, tuple) and len(summary) == 2:
            module, summary_text = summary
        else:
            module, summary_text = summary, placeholder
        summary_list.append((module, summary_text))
    return summary_list


def create_tables(
    summary_list: List[Tuple[str, str]],
    dropdown: str,
    repository: str,
    user_repo_name: str,
) -> str:
    """Creates Markdown tables for each sub-directory in the project."""
    sub_folder_map = {}
    for module, summary in summary_list:
        sub_folder = (
            str(module).split("/")[-2].capitalize()
            if "/" in str(module)
            else "Root"
        )
        if sub_folder in sub_folder_map:
            sub_folder_map[sub_folder].append((module, summary))
        else:
            sub_folder_map[sub_folder] = [(module, summary)]

    tables = []
    for sub_folder, entries in sub_folder_map.items():
        table_data = entries
        table = create_table(table_data, repository, user_repo_name)
        table_wrappers = dropdown.format(sub_folder, table)
        tables.append(table_wrappers)
    return "\n".join(tables)


def create_table(
    data: List[Tuple[str, str]], repository, user_repo_name: str
) -> str:
    """Creates a Markdown table from the given data."""
    headers = ["File", "Summary"]
    lines = [headers, ["---"] * len(headers)]
    for row in data:
        module, summary = row
        filename = str(Path(module).name)
        if "invalid" in user_repo_name.lower():
            link = filename
        else:
            github_url = git.get_github_file_link(
                module, repository, user_repo_name
            )
            link = f"[{filename}]({github_url})"
        lines.append([link, summary])

    max_len = [
        max(len(str(row[i])) for row in lines) for i in range(len(headers))
    ]
    formatted_lines = []
    for line in lines:
        formatted_line = (
            "| "
            + " | ".join(
                str(item).ljust(length) for item, length in zip(line, max_len)
            )
            + " |"
        )
        formatted_lines.append(formatted_line)

    return "\n".join(formatted_lines)


def build_recursive_tables(base_url: str, directory: Path, placeholder) -> str:
    """Creates a Markdown table structure for the given directory."""
    markdown = ""
    markdown += "| File | Summary |\n"
    markdown += "| --- | --- |\n"

    for item in sorted(directory.iterdir()):
        if item.is_file():
            markdown += f"| [{item.name}]({item.name}) | {placeholder} |\n"

    for item in sorted(directory.iterdir()):
        if item.is_dir():
            # If it is a sub-directory, create a collapsible section
            markdown += f"\n<details closed><summary>{item.name}</summary>\n\n"
            # Recursive call for sub-directory
            markdown += build_recursive_tables(base_url, item, placeholder)
            # Close the collapsible section
            markdown += "\n</details>\n\n"

    return markdown
