"""Converts markdown syntax to HTML elements in a given piece of text.

Syntax supported:
- Bold (**text**)
- Italic (*text*)
- Links ([text](url))
- Headers (# Header)
- Lists (unordered and ordered)

Notes:
- Ensures compatibility with ReadmeAI's HTML-based table content used in the README.
- All regular expressions are precompiled at the module level to avoid repeated compilation.
"""

import re
from typing import Any

BOLD_RE: re.Pattern[str] = re.compile(r"\*\*(.+?)\*\*")

INLINE_CODE_RE: re.Pattern[str] = re.compile(r"`([^`\n]+)`")

ITALIC_RE: re.Pattern[str] = re.compile(r"\*(.+?)\*")

LINK_RE: re.Pattern[str] = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

ORDERED_LIST_RE: re.Pattern[str] = re.compile(r"^(\s*)\d+\.\s(.+)$", re.MULTILINE)

UNORDERED_LIST_RE: re.Pattern[str] = re.compile(r"^(\s*)[-*+]\s(.+)$", re.MULTILINE)

HEADER_RE: list[re.Pattern[str]] = [
    re.compile(f"^{'#' * i} (.+)$", re.MULTILINE) for i in range(6, 0, -1)
]


def convert(text: str) -> str:
    """Convert any markdown syntax in the given text to HTML."""

    def process_inline(content: str) -> str:
        """Process inline markdown syntax."""

        def nested_format(match) -> str | Any:
            """Handle nested formatting within inline elements."""
            inner_content = process_inline(match.group(1))
            if match.re == BOLD_RE:
                return f"<strong>{inner_content}</strong>"
            elif match.re == ITALIC_RE:
                return f"<em>{inner_content}</em>"
            return match.group(0)

        content = INLINE_CODE_RE.sub(r"<code>\1</code>", content)
        content = BOLD_RE.sub(nested_format, content)
        content = ITALIC_RE.sub(nested_format, content)
        content = LINK_RE.sub(r'<a href="\2">\1</a>', content)
        return content

    for i, pattern in enumerate(HEADER_RE, start=1):
        text = pattern.sub(
            lambda m: f"<h{7 - i}>{process_inline(m.group(1))}</h{7 - i}>", text
        )

    lines = text.split("\n")
    in_list = False
    list_type = None
    list_indent = ""
    result = []

    for line in lines:
        unordered_match = UNORDERED_LIST_RE.match(line)
        ordered_match = ORDERED_LIST_RE.match(line)

        if unordered_match or ordered_match:
            match = unordered_match or ordered_match
            indent, content = match.groups()

            if not in_list:
                list_indent = indent
                list_type = "ul" if unordered_match else "ol"
                result.append(f"{indent}<{list_type}>")
                in_list = True
            elif (
                list_type != ("ul" if unordered_match else "ol")
                or indent != list_indent
            ):
                result.append(f"{list_indent}</{list_type}>")
                list_indent = indent
                list_type = "ul" if unordered_match else "ol"
                result.append(f"{indent}<{list_type}>")

            result.append(f"{indent}<li>{process_inline(content)}</li>")
        else:
            if in_list:
                result.append(f"{list_indent}</{list_type}>")
                in_list = False
                list_type = None
            result.append(process_inline(line))

    if in_list:
        result.append(f"{list_indent}</{list_type}>")

    return "\n".join(result)
