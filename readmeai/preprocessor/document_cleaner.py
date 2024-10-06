import re


class DocumentCleaner:
    """
    Document cleaner to preprocess repository content.
    """

    def __init__(
        self,
        remove_empty_lines: bool = True,
        remove_extra_whitespaces: bool = True,
        remove_trailing_whitespaces: bool = True,
        normalize_indentation: bool = True,
    ):
        self.remove_empty_lines = remove_empty_lines
        self.remove_extra_whitespaces = remove_extra_whitespaces
        self.remove_trailing_whitespaces = remove_trailing_whitespaces
        self.normalize_indentation = normalize_indentation

    def clean(self, code: str) -> str:
        """Clean the given document string."""
        if self.remove_empty_lines:
            code = self._remove_empty_lines(code)
        if self.remove_extra_whitespaces:
            code = self._remove_extra_whitespaces(code)
        if self.remove_trailing_whitespaces:
            code = self._remove_trailing_whitespaces(code)
        if self.normalize_indentation:
            code = self._normalize_indentation(code)
        return code.strip()

    def _remove_empty_lines(self, code: str) -> str:
        """Remove empty lines and lines with only whitespace."""
        return "\n".join(line for line in code.splitlines() if line.strip())

    def _remove_extra_whitespaces(self, code: str) -> str:
        """Remove extra whitespaces within lines."""
        return re.sub(r"\s+", " ", code)

    def _remove_trailing_whitespaces(self, code: str) -> str:
        """Remove trailing whitespaces from each line."""
        return "\n".join(line.rstrip() for line in code.splitlines())

    def _normalize_indentation(self, code: str) -> str:
        """Normalize indentation to spaces."""
        lines = code.splitlines()
        normalized_lines = []
        for line in lines:
            indent = len(line) - len(line.lstrip())
            normalized_lines.append(" " * indent + line.lstrip())
        return "\n".join(normalized_lines)
