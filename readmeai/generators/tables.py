# Updated Script with Corrected 'Current Directory' Path Format
from pathlib import Path

from readmeai.core.logger import get_logger

_logger = get_logger(__name__)


def _generate_nested_module_content(
    module_data: dict[str, dict | list[tuple[str, str]]] | list[tuple[str, str]],
    repo_path: str | Path,
    is_local_repo: bool,
    repo_url: str,
    indent: str = "",
) -> list[str]:
    """Generates nested content for modules and submodules using HTML tables."""
    content = []

    if isinstance(module_data, list):
        # module_data is a list of files
        content.append(f"{indent}<table>")
        content.extend(
            _generate_table_rows(
                module_data,
                repo_path,
                is_local_repo,
                repo_url,
                indent=indent,
            )
        )
        content.append(f"{indent}</table>")
    elif isinstance(module_data, dict):
        # Check if there are files at this module level
        files = module_data.get("", [])
        if files:
            content.append(f"{indent}<table>")
            content.extend(
                _generate_table_rows(
                    files,
                    repo_path,
                    is_local_repo,
                    repo_url,
                    indent=indent,
                )
            )
            content.append(f"{indent}</table>")
        # Process submodules
        for submodule_name, submodule_data in module_data.items():
            if submodule_name == "":
                continue
            content.extend((
                f"{indent}<details>",
                f"{indent}\t<summary><b>{submodule_name}</b></summary>",
                f"{indent}\t<blockquote>",
            ))
            # Recurse into submodule
            content.extend(
                _generate_nested_module_content(
                    submodule_data,
                    repo_path,
                    is_local_repo,
                    repo_url,
                    indent=indent + "\t\t",
                )
            )
            content.extend((f"{indent}\t</blockquote>", f"{indent}</details>"))
    else:
        _logger.warning(f"Unexpected data type in module data: {type(module_data)}")
    return content


def generate_nested_module_tables(
    summaries: list[tuple[str, str]],
    project_path: str | Path,
    repository_url: str,
) -> str:
    """Create structured Markdown tables with nested submodules."""
    summaries_by_module = group_summaries_by_nested_module(summaries)
    return build_submodule_disclosure_widget(
        summaries_by_module, project_path, repository_url
    )


def build_submodule_disclosure_widget(
    data: dict[str, dict | list[tuple[str, str]]],
    repo_path: str | Path,
    repo_url: str,
) -> str:
    """
    Builds expandable sections via <details> HTML element,
    for each module with nested submodules using HTML tables.
    Includes breadcrumb-style path navigation and column headers.
    """
    if not data:
        return ""

    is_local_repo = Path(repo_path).exists()
    project_name = (
        Path(repo_path).name if is_local_repo else repo_url.rstrip("/").split("/")[-1]
    )

    sections = [
        "<details open>",
        f"\t<summary><b><code>{project_name.upper()}/</code></b></summary>",
    ]

    def add_path_header(current_path: list[str], indent: str) -> list[str]:
        """Creates a header showing the current directory path."""
        if not current_path:
            return []
        path_parts = ".".join(current_path)
        return [
            f"{indent}<div class='directory-path' style='padding: 8px 0; color: #666;'>",
            f"{indent}\t<code><b>⦿ {path_parts}</b></code>",
        ]

    def create_table_header(indent: str) -> list[str]:
        """Creates a standardized table header."""
        return [
            f"{indent}<table style='width: 100%; border-collapse: collapse;'>",
            f"{indent}<thead>",
            f"{indent}\t<tr style='background-color: #f8f9fa;'>",
            f"{indent}\t\t<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>",
            f"{indent}\t\t<th style='text-align: left; padding: 8px;'>Summary</th>",
            f"{indent}\t</tr>",
            f"{indent}</thead>",
        ]

    def process_module(
        module_name: str, module_data: dict | list, current_path: list[str], indent: str
    ) -> list[str]:
        """Processes a module and its contents recursively."""
        section = []

        # Add module header with current path
        section.extend([
            f"{indent}<!-- {module_name} Submodule -->",
            f"{indent}<details>",
            f"{indent}\t<summary><b>{module_name}</b></summary>",
            f"{indent}\t<blockquote>",
        ])

        # Add path navigation
        section.extend(add_path_header(current_path + [module_name], indent + "\t\t"))

        if isinstance(module_data, list):
            # Handle files at this level
            section.extend(create_table_header(indent + "\t\t"))
            section.extend(
                _generate_table_rows(
                    module_data,
                    repo_path,
                    is_local_repo,
                    repo_url,
                    indent=indent + "\t\t\t",
                )
            )
            section.append(f"{indent}\t\t</table>")
        elif isinstance(module_data, dict):
            # Handle nested structure
            files = module_data.get("", [])
            if files:
                section.extend(create_table_header(indent + "\t\t"))
                section.extend(
                    _generate_table_rows(
                        files,
                        repo_path,
                        is_local_repo,
                        repo_url,
                        indent=indent + "\t\t\t",
                    )
                )
                section.append(f"{indent}\t\t</table>")

            # Process submodules
            for submodule_name, submodule_data in module_data.items():
                if submodule_name == "":
                    continue
                section.extend(
                    process_module(
                        submodule_name,
                        submodule_data,
                        current_path + [module_name],
                        indent + "\t\t",
                    )
                )

        section.extend([f"{indent}\t</blockquote>", f"{indent}</details>"])
        return section

    # Process each top-level module
    for module_name, module_data in data.items():
        sections.extend(process_module(module_name, module_data, [], "\t"))

    sections.append("</details>")
    return "\n".join(sections)


def _generate_table_rows(
    files: list[tuple[str, str]],
    repo_path: str | Path,
    is_local_repo: bool,
    repo_url: str,
    indent: str = "",
) -> list[str]:
    """Generates table rows for files with improved styling."""
    content = []
    for file, summary in files:
        file_name = Path(file).name
        file_link = _get_file_hyperlink(file, repo_path, is_local_repo, repo_url)
        formatted_summary = format_summary(summary)
        content.append(
            f"{indent}<tr style='border-bottom: 1px solid #eee;'>"
            f"\n{indent}\t<td style='padding: 8px;'><b><a href='{file_link}'>{file_name}</a></b></td>"
            f"\n{indent}\t<td style='padding: 8px;'>{formatted_summary}</td>"
            f"\n{indent}</tr>"
        )
    return content


def _get_file_hyperlink(
    file_path_str: str,
    repo_path: str | Path,
    is_local: bool,
    repo_url: str,
) -> str:
    """Generates a hyperlink to the file in the remote git repository."""
    if not is_local:
        return f"{repo_url.rstrip('/')}/blob/master/{file_path_str}"
    file_path = Path(repo_path) / file_path_str
    return f"{file_path.as_posix()}"


def group_summaries_by_nested_module(
    summaries: list[tuple[str, str]],
) -> dict[str, dict | list[tuple[str, str]]]:
    """Group code summaries by their nested module structure."""
    module_map: dict[str, dict | list[tuple[str, str]]] = {"__root__": []}

    for module, summary in summaries:
        if not isinstance(module, str) or not isinstance(summary, str):
            _logger.error(f"Invalid entry: ({module}, {summary}). Skipping...")
            continue

        parts = Path(module).parts

        if len(parts) == 1:
            module_map["__root__"].append((module, summary))
        else:
            current = module_map
            for part in parts[:-1]:
                current = current.setdefault(part, {})
            current.setdefault("", []).append((module, summary))

    return module_map


def format_code_summaries(
    placeholder: str,
    code_summaries: list[tuple[str, str]],
) -> list:
    """Converts the given code summaries into a formatted list."""
    return [
        (module, summary_text)
        if isinstance(summary, tuple) and len(summary) == 2
        else (summary, placeholder)
        for summary in code_summaries
        for module, summary_text in (
            [summary]
            if isinstance(summary, tuple) and len(summary) == 2
            else [(summary, placeholder)]
        )
    ]


def format_summary(summary: str) -> str:
    """
    Formats the summary with multi-line support if needed.
    """
    lines = summary.strip().split(". ")
    if len(lines) > 1:
        return "<br>".join(f"- {line.strip()}" for line in lines)
    return summary.strip()
