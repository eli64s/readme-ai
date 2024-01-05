"""Creates a directory tree structure for a code repository."""

from pathlib import Path

from readmeai.config.settings import ConfigHelper
from readmeai.core import utils
from readmeai.core.logger import Logger

logger = Logger(__name__)


class TreeGenerator:
    """Generates a directory tree structure for a code repository."""

    def __init__(
        self,
        conf_helper: ConfigHelper,
        repo_name: str,
        repo_url: Path,
        root_dir: Path,
        max_depth: int = 3,
    ):
        self.config_helper = conf_helper
        self.repo_name = repo_name
        self.repo_url = repo_url
        self.root_dir = Path(root_dir)
        self.max_depth = max_depth

    def run(self) -> str:
        """Generates and formats a tree structure."""
        tree_str = self._generate_tree(self.root_dir)
        return tree_str.replace(self.root_dir.name, f"{self.repo_name}/")

    def _generate_tree(
        self,
        directory: Path,
        prefix: str = "",
        is_last: bool = True,
        depth: int = 0,
    ) -> str:
        """Generates a tree structure for a given directory."""
        if depth > self.max_depth or utils.should_ignore(
            self.config_helper, directory
        ):
            return ""

        children = sorted(directory.iterdir()) if directory.is_dir() else []
        children = [
            child
            for child in children
            if not utils.should_ignore(self.config_helper, child)
        ]

        if not children and directory.is_dir():
            return ""

        parts = [f"{prefix}{'└── ' if is_last else '├── '}{directory.name}"]

        for index, child in enumerate(children):
            child_prefix = prefix + ("    " if is_last else "│   ")
            child_tree = self._generate_tree(
                child, child_prefix, index == len(children) - 1, depth + 1
            )

            if child_tree:
                parts.append(child_tree)

        return "\n".join(parts)
