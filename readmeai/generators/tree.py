from pathlib import Path


class TreeGenerator:
    """
    Generates a directory tree structure from a given root directory.
    """

    def __init__(
        self,
        repo_name: str,
        root_dir: Path,
        repo_url: str,
        max_depth: int,
    ):
        self.repo_name = repo_name
        self.root_dir = root_dir
        self.repo_url = repo_url
        self.max_depth = max_depth

    def generate(
        self,
        directory: Path,
        prefix: str = "",
        is_last: bool = True,
        depth: int = 0,
    ) -> str:
        """Build string representation of a directory tree."""
        if depth > self.max_depth:
            return ""

        children = sorted(directory.iterdir()) if directory.is_dir() else []
        children = list(children)

        if not children and directory.is_dir():
            return ""

        parts = [f"{prefix}{'└── ' if is_last else '├── '}{directory.name}"]

        for index, child in enumerate(children):
            child_prefix = prefix + ("    " if is_last else "│   ")
            if child_tree := self.generate(
                child,
                child_prefix,
                index == len(children) - 1,
                depth + 1,
            ):
                parts.append(child_tree)

        return self._format_tree(parts)

    def _format_tree(self, parts: list[str]) -> str:
        """Format tree structure and replace root directory name."""
        tree = "\n".join(parts)
        return tree.replace(self.root_dir.name, f"{self.repo_name}/")
