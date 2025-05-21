"""Table of contents and navigation menu generation for the documentation."""

import re
from typing import Any, Dict, Optional

from readmeai.core.logger import get_logger
from readmeai.generators.enums import NavigationStyles
from readmeai.generators.headers import HeaderRegistry

logger = get_logger(__name__)


class NavigationTemplate:
    """
    Render a table of contents or navigation menu for the README file.
    """

    def __init__(self, style: str, header_registry: HeaderRegistry) -> None:
        try:
            self.style = NavigationStyles(style.lower())
        except ValueError:
            logger.warning(f"Invalid navigation style: {style}. Defaulting to bullet.")
            self.style = NavigationStyles.BULLET

        self.header_registry = header_registry
        self.using_emojis = header_registry.emoji_theme.lower()
        logger.debug(f"Initialized navigation style: {self.style}")
        logger.debug(f"Using emojis: {self.using_emojis}")

    def render(self, data: Dict[str, Any]) -> str:
        """Render complete table of contents with proper markdown formatting."""
        toc_lines = []

        sections = data.get("sections", [])
        for i, section in enumerate(sections, 1):
            title = self.header_registry.get_themed_title(section["title"])
            toc_lines.append(self._format_link(title, level=0, index=i))

            if section.get("subsections"):
                for j, subsection in enumerate(section["subsections"], 1):
                    sub_title = self.header_registry.get_themed_title(
                        subsection["title"]
                    )
                    toc_lines.append(
                        self._format_link(
                            sub_title,
                            level=1,
                            index=i,
                            sub_index=j,
                        )
                    )

        content = "".join(toc_lines)

        if self.style == NavigationStyles.ACCORDION:
            summary_title = self.header_registry.get_themed_title("Table of Contents")
            return (
                "<details>\n"
                f"<summary>{summary_title}</summary>\n\n"
                f"{content}"
                "\n</details>\n"
            )

        return content

    def _format_link(
        self,
        title: str,
        level: int = 0,
        index: Optional[int] = None,
        sub_index: Optional[int] = None,
    ) -> str:
        """Format a single navigation link with proper markdown formatting."""
        display_title = title.strip()
        clean_anchor = self._generate_anchor(title)
        indent = "    " * level if level > 0 else ""

        # Only add dash prefix to anchor if emojis are explicitly enabled
        anchor = f"-{clean_anchor}" if self.using_emojis else clean_anchor
        if self.using_emojis == "default":
            anchor = anchor.lstrip("-")

        if self.style == NavigationStyles.NUMBER:
            if sub_index is not None:
                return f"{indent}{index}.{sub_index}. [{display_title}](#{anchor})\n"
            return f"{indent}{index}. [{display_title}](#{anchor})\n"

        elif self.style == NavigationStyles.ROMAN:
            if sub_index is not None:
                # Explicitly set 4 spaces for proper rendering
                indent_ = "&nbsp;&nbsp;&nbsp;&nbsp;"
                # 97 is 'a' in ASCII
                subsection_letter = chr(96 + sub_index)
                prefix = f"{indent_}{self._to_roman(index)}.{subsection_letter}."
                # Reset indent since included in prefix
                indent = ""
            else:
                prefix = f"{self._to_roman(index)}."
            return f"{indent}{prefix} [{display_title}](#{anchor})<br>\n"
        else:
            prefix = "-"
            return f"{indent}{prefix} [{display_title}](#{anchor})\n"

    def _generate_anchor(self, title: str) -> str:
        """
        Generate GitHub-compatible anchor link.

        This follows GitHub's heading ID generation rules:
        1. Remove special characters (except alphanumeric, spaces, hyphens)
        2. Replace spaces with hyphens
        3. Convert to lowercase
        4. Remove extra hyphens
        """
        clean_title = self.header_registry._strip_emoji(title).strip()
        anchor = re.sub(r"[^\w\s-]", "", clean_title)
        anchor = re.sub(r"\s+", " ", anchor).strip()
        anchor = anchor.lower()
        anchor = re.sub(r"\s", "-", anchor)
        anchor = re.sub(r"-+", "-", anchor)
        return anchor

    def _to_roman(self, num: int) -> str:
        """Convert integer to Roman numeral."""
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
