"""Utilities to remove emojis from the default markdown template headers.

Example:
    Default Header:
            ## 🚀 Getting Started
    After Removing Emojis:
            ## Getting Started

Feature is enabled by default and can be disabled
in the CLI by passing '--emoji'. or '-e' flag.
"""

import re

EMOJI_PATTERN = re.compile(
    pattern="["
    "\U0001f600-\U0001f64f"  # emoticons
    "\U0001f300-\U0001f5ff"  # symbols & pictographs
    "\U0001f680-\U0001f6ff"  # transport & map symbols
    "\U0001f700-\U0001f77f"  # alchemical symbols
    "\U0001f780-\U0001f7ff"  # Geometric Shapes Extended
    "\U0001f800-\U0001f8ff"  # Supplemental Arrows-C
    "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
    "\U0001fa00-\U0001fa6f"  # Chess Symbols
    "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027b0"  # Dingbats
    "\U000024c2-\U0001f251"  # flags (iOS)
    "]+",
    flags=re.UNICODE,
)


def remove_emojis(md_content: list[str]) -> list[str]:
    """Removes emojis from the content list."""
    modified_content = []

    for section in md_content:
        lines = section.split("\n")
        for index, line in enumerate(lines):
            if (
                line.startswith("#")
                or "Table of Contents" in section
                or "Quick Links" in section
            ):
                lines[index] = EMOJI_PATTERN.sub("", line)
        modified_content.append("\n".join(lines))

    return modified_content
