"""Utilities to remove default emojis from markdown content."""

import re
from typing import List

EMOJI_PATTERN = re.compile(
    pattern="["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "\U000024C2-\U0001F251"  # flags (iOS)
    "]+",
    flags=re.UNICODE,
)


def remove_emojis(md_content: List[str]) -> List[str]:
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
