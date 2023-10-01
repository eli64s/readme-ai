"""Generates a tree structure for a given directory."""

from pathlib import Path


def generate_tree(
    directory: Path,
    repo_url: str,
    prefix: str = "",
    is_last: bool = True,
    parent_prefix: str = "",
    depth: int = 0,
    MAX_DEPTH: int = 2,
) -> str:
    """Recursively generates a tree structure for a given directory."""
    if depth > MAX_DEPTH:
        return ""

    if directory == repo_url:
        display_name = "."
    else:
        display_name = directory.name

    box_branch = "└── " if is_last else "├── "

    parts = [parent_prefix + box_branch + display_name]

    if directory.is_dir():
        parts.append("/\n")

        children = sorted(
            [child for child in directory.iterdir() if child.name != ".git"]
        )

        for index, child in enumerate(children):
            is_last_child = index == len(children) - 1
            child_prefix = "    " if is_last else "│   "
            parts.append(
                generate_tree(
                    child,
                    repo_url,
                    box_branch,
                    is_last_child,
                    f"{parent_prefix}{child_prefix}",
                    depth + 1,
                )
            )
    else:
        parts.append("\n")

    return "".join(parts)


def format_tree(name: str, tree_str: str) -> str:
    """Replaces tmp directory name with project name."""
    tree_str = tree_str.split("\n", 1)
    tree_str[0] = f"└── {name}/"
    tree_str = "\n".join(tree_str)
    tree = f"```sh\n{tree_str}```"
    return tree
