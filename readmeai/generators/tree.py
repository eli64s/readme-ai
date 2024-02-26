"""Generates a directory tree structure for a code repository."""

from pathlib import Path


class TreeGenerator:
    """Generates a directory tree structure for a code repository."""

    def __init__(
        self, repo_name: str, root_dir: Path, repo_url: Path, max_depth: int
    ):
        self.repo_name = repo_name
        self.root_dir = root_dir
        self.repo_url = repo_url
        self.max_depth = max_depth

    def _build_tree(
        self,
        directory: Path,
        prefix: str = "",
        is_last: bool = True,
        depth: int = 0,
    ) -> str:
        """Generates a tree structure for a given directory."""
        if depth > self.max_depth:
            return ""

        children = sorted(directory.iterdir()) if directory.is_dir() else []
        children = [child for child in children]

        if not children and directory.is_dir():
            return ""

        """
        dir_name = directory.name
        if depth == 2 and directory.is_dir():
            dir_name += "               ► summary of directory"
        parts = [f"{prefix}{'└── ' if is_last else '├── '}{dir_name}"]
        """
        parts = [f"{prefix}{'└── ' if is_last else '├── '}{directory.name}"]

        for index, child in enumerate(children):
            child_prefix = prefix + ("    " if is_last else "│   ")
            child_tree = self._build_tree(
                child, child_prefix, index == len(children) - 1, depth + 1
            )

            if child_tree:
                parts.append(child_tree)

        return "\n".join(parts)

    def tree(self) -> str:
        """Generates and formats a tree structure."""
        md_tree = self._build_tree(self.root_dir)
        formatted_md_tree = md_tree.replace(
            self.root_dir.name, f"{self.repo_name}/"
        )
        return formatted_md_tree
