import re
import textwrap


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
        dedent: bool = False,
    ):
        self.remove_empty_lines = remove_empty_lines
        self.remove_extra_whitespaces = remove_extra_whitespaces
        self.remove_trailing_whitespaces = remove_trailing_whitespaces
        self.normalize_indentation = normalize_indentation
        self.dedent = dedent

    def clean(self, code: str) -> str:
        """Clean the given document string."""
        lines = code.splitlines()

        if self.remove_empty_lines:
            lines = [line for line in lines if line.strip()]

        if self.remove_trailing_whitespaces:
            lines = [line.rstrip() for line in lines]

        if self.normalize_indentation:
            lines = self._normalize_indentation("\n".join(lines)).splitlines()

        result = "\n".join(lines)

        if self.dedent:
            result = textwrap.dedent(result)

        if self.remove_extra_whitespaces:
            # Only remove extra spaces within each line, preserving leading spaces
            lines = result.splitlines()
            lines = [
                self._preserve_indent_remove_extra_spaces(line)
                for line in lines
            ]
            result = "\n".join(lines)

        return result.rstrip()

    def _preserve_indent_remove_extra_spaces(self, line: str) -> str:
        """Remove extra whitespaces while preserving leading indentation."""
        if not line.strip():
            return ""
        indent = len(line) - len(line.lstrip())
        return " " * indent + re.sub(r"\s+", " ", line.lstrip())

    def _normalize_indentation(self, code: str) -> str:
        """Normalize indentation to spaces."""
        if not code:
            return code

        lines = code.splitlines()
        normalized_lines = []

        for line in lines:
            if not line.strip():
                normalized_lines.append("")
                continue

            # Calculate leading whitespace count, handling tabs
            leading_space_count = 0
            for char in line:
                if char == " ":
                    leading_space_count += 1
                elif char == "\t":
                    # Round up to the next multiple of 4
                    leading_space_count = (leading_space_count + 4) & ~3
                else:
                    break

            # Preserve the original indentation level
            normalized_line = " " * leading_space_count + line.lstrip()
            normalized_lines.append(normalized_line)

        return "\n".join(normalized_lines)

    def _remove_empty_lines(self, code: str) -> str:
        """Remove empty lines and lines with only whitespace."""
        return "\n".join(line for line in code.splitlines() if line.strip())

    def _remove_extra_whitespaces(self, code: str) -> str:
        """Remove extra whitespaces within lines while preserving newlines."""
        lines = code.splitlines()
        return "\n".join(
            self._preserve_indent_remove_extra_spaces(line) for line in lines
        )

    def _remove_trailing_whitespaces(self, code: str) -> str:
        """Remove trailing whitespaces from each line."""
        return "\n".join(line.rstrip() for line in code.splitlines())
