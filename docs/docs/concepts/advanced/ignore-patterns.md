---
title: Ignore Files
description: Learn how to exclude specific files and directories from your README generation using .readmeai_ignore files.
---

# Ignore Files

When generating README documentation, you may want to exclude certain files or directories from the output. To achieve this, you can create a `.readmeai_ignore` file in your repository to specify patterns for files and directories that should be ignored during README generation.

## Creating an Ignore File

```text
# Ignore specific files
secret_file.txt
*.env

# Ignore directories
test_data/
**/temp/

# Ignore files by pattern
**/*.log
**/node_modules/
```

## Implementation

```python
"""Handling logic for .readmeai_ignore files."""

import pathlib
from typing import List, Set
import fnmatch

class ReadmeIgnoreHandler:
    """Handler for .readmeai_ignore file processing."""

    def __init__(self, repo_path: pathlib.Path) -> None:
        """Initialize the ignore handler with repository path."""
        self.repo_path = repo_path
        self.ignore_patterns: Set[str] = set()
        self._load_ignore_file()

    def _load_ignore_file(self) -> None:
        """Load patterns from .readmeai_ignore file if it exists."""
        ignore_file = self.repo_path / ".readmeai_ignore"

        if not ignore_file.exists():
            return

        with open(ignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove comments and whitespace
                line = line.split('#')[0].strip()
                if line:
                    self.ignore_patterns.add(line)

    def should_ignore(self, file_path: pathlib.Path) -> bool:
        """
        Check if a file should be ignored based on .readmeai_ignore patterns.

        Args:
            file_path: Path object relative to repository root

        Returns:
            bool: True if file should be ignored, False otherwise
        """
        # Convert path to string for pattern matching
        path_str = str(file_path.relative_to(self.repo_path))

        # Check each ignore pattern
        for pattern in self.ignore_patterns:
            if fnmatch.fnmatch(path_str, pattern):
                return True

        return False

    def get_ignore_patterns(self) -> List[str]:
        """Return list of current ignore patterns."""
        return sorted(self.ignore_patterns)

    def add_pattern(self, pattern: str) -> None:
        """Add a new ignore pattern."""
        self.ignore_patterns.add(pattern.strip())

    def remove_pattern(self, pattern: str) -> bool:
        """
        Remove an ignore pattern.

        Returns:
            bool: True if pattern was removed, False if not found
        """
        try:
            self.ignore_patterns.remove(pattern.strip())
            return True
        except KeyError:
            return False
```

---
