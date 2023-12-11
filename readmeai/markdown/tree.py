"""Generates a directory tree structure for a code repository."""

from pathlib import Path

from readmeai.config.settings import ConfigHelper
from readmeai.core import logger
from readmeai.utils import utils

logger = logger.Logger(__name__)


class TreeGenerator:
    """Generates a directory tree structure for a code repository."""

    def __init__(
        self,
        conf_helper: ConfigHelper,
        root_directory: Path,
        repo_url: str,
        project_name: str,
        max_depth: int = 3,
    ):
        self.config_helper = conf_helper
        self.root_directory = root_directory
        self.project_name = project_name
        self.repo_url = repo_url
        self.max_depth = max_depth

    def generate_and_format_tree(self) -> str:
        """Generates and formats a tree structure."""
        tree_str = self._generate_tree(self.root_directory)
        formatted_tree_str = self._format_tree(tree_str)
        return formatted_tree_str

    def _generate_tree(
        self,
        directory: Path,
        prefix: str = "",
        is_last: bool = True,
        parent_prefix: str = "",
        depth: int = 0,
    ) -> str:
        """Generates a tree structure for a given directory."""
        if depth > self.max_depth:
            return ""

        if utils.should_ignore(self.config_helper, directory):
            return ""

        display_name = "." if directory == self.repo_url else directory.name
        box_branch = "└── " if is_last else "├── "
        parts = [parent_prefix + box_branch + display_name]

        if directory.is_dir():
            parts.append("/\n")
            children = sorted(
                [
                    child
                    for child in directory.iterdir()
                    if child.name != ".git"
                ]
            )
            for index, child in enumerate(children):
                is_last_child = index == len(children) - 1
                child_prefix = "    " if is_last else "│   "
                parts.append(
                    self._generate_tree(
                        child,
                        box_branch,
                        is_last_child,
                        f"{parent_prefix}{child_prefix}",
                        depth + 1,
                    )
                )
        else:
            parts.append("\n")

        return "".join(parts)

    def _format_tree(self, tree_str: str) -> str:
        """Formats the directory tree structure."""
        tree_str = tree_str.split("\n", 1)
        tree_str[0] = f"└── {self.project_name}/"
        return "\n".join(tree_str)
