import copy
from pathlib import Path
from typing import Dict, List

from readmeai.core.logger import get_logger

_logger = get_logger(__name__)


class IgnoreHandler:
    """
    Handles all logic for ignoring files and directories.
    1. Initializes with default ignore rules from the configuration.
    2. Default rules merged with user-defined rules from ".readmeaiignore" file.
    3. Provides a method to check if a path should be excluded.
    """

    def __init__(self, default_rules: Dict[str, List[str]]):
        # Start with deepcopy to prevent modifying original config
        self.ignore_rules = copy.deepcopy(default_rules)

    def load_user_rules(self, repo_path: Path):
        """Finds and merges rules from a .readmeaiignore file."""
        user_patterns = self._read_ignore_file(repo_path)
        if not user_patterns:
            _logger.debug("No user-defined ignore patterns found.")
            return
        else:
            _logger.debug(f"User-defined ignore patterns found: {user_patterns}")

        user_rules = self._parse_patterns(user_patterns)

        # Merge the user rules into the main ruleset
        for category, patterns in user_rules.items():
            if patterns:
                existing = set(self.ignore_rules.get(category, []))
                new = set(patterns)
                self.ignore_rules[category] = list(existing.union(new))

    def is_excluded(self, file_path: Path, repo_path: Path) -> bool:
        """
        Check if the file should be ignored based on the merged rules.
        This moves the logic from the global function into the class.
        """
        relative_path = file_path.relative_to(repo_path)

        for ignored_dir in self.ignore_rules.get("directories", []):
            if ignored_dir in relative_path.parts:
                return True

        if file_path.suffix.lstrip(".") in self.ignore_rules.get("extensions", []):
            return True

        return file_path.name in self.ignore_rules.get("files", [])

    def _read_ignore_file(self, repo_path: Path) -> List[str]:
        """Reads patterns from a .readmeaiignore file."""
        ignore_file = Path.cwd() / ".readmeaiignore"
        _logger.debug(f"Looking for ignore file at: {ignore_file}")
        if not ignore_file.is_file():
            return []

        with ignore_file.open("r", encoding="utf-8") as f:
            return [
                line
                for line in (line.strip() for line in f)
                if line and not line.startswith("#")
            ]

    def _parse_patterns(self, patterns: List[str]) -> Dict[str, List[str]]:
        """Parses a flat list of patterns into a structured dictionary."""
        categorized = {"directories": [], "extensions": [], "files": []}
        for p in patterns:
            if p.endswith("/"):
                categorized["directories"].append(p.strip("/"))
            elif p.startswith("*."):
                categorized["extensions"].append(p.lstrip("*."))
            else:
                categorized["files"].append(p)
        return categorized
