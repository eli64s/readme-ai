import re
from typing import Any, ClassVar, Optional

from readmeai.config.constants import EmojiThemeOptions, TocStyleOptions


class TocTemplate:
    """
    Class for rendering GitHub-compatible Table of Contents.
    """

    TOC_TEMPLATES: ClassVar[dict] = {
        TocStyleOptions.BULLET: "{toc_items}",
        TocStyleOptions.FOLD: """<details><summary>Click to expand</summary>\n\n{toc_items}\n</details>\n""",
        TocStyleOptions.NUMBER: "{toc_items}",
        TocStyleOptions.LINKS: "{toc_items}",
        TocStyleOptions.ROMAN: "{toc_items}",
    }

    TOC_ITEM_TEMPLATES: ClassVar[dict[TocStyleOptions, str]] = {
        TocStyleOptions.BULLET: "{indent}- [{title}](#{anchor})\n",
        TocStyleOptions.FOLD: "{indent}- [{title}](#{anchor})\n",
        TocStyleOptions.NUMBER: "{indent}{number}. [{title}](#{anchor})\n",
        TocStyleOptions.LINKS: "{indent}- [{title}](#{anchor})\n",
        TocStyleOptions.ROMAN: "{indent}{number}. [{title}](#{anchor})\n",
    }

    def __init__(
        self,
        emoji_theme: Optional[str] = None,
        style: str = TocStyleOptions.BULLET.value,
    ) -> None:
        self.style = TocStyleOptions(style)
        self.emoji_theme = emoji_theme or EmojiThemeOptions.DEFAULT.value

    def _generate_toc_items(
        self,
        sections: list[dict[str, Any]],
        level: int = 0,
        parent_number: str = "",
    ) -> str:
        """Generate GitHub-compatible TOC items with correct nesting."""
        toc = ""
        for index, section in enumerate(sections, start=1):
            indent = "    " * level if level > 0 else ""
            title = section["title"]
            anchor = self.generate_anchor(title)

            if self.style in {TocStyleOptions.NUMBER, TocStyleOptions.ROMAN}:
                if self.style == TocStyleOptions.ROMAN:
                    indent = (
                        "&nbsp;&nbsp;&nbsp;&nbsp;" * level if level > 0 else ""
                    )
                    if level == 0:
                        number = self._int_to_roman(index)
                    else:
                        number = self._int_to_roman(index).lower()
                else:
                    number = (
                        f"{parent_number}{index}"
                        if parent_number
                        else str(index)
                    )

                item = self.TOC_ITEM_TEMPLATES[self.style].format(
                    indent=indent,
                    number=number,
                    title=title,
                    anchor=anchor,
                )
            else:
                item = self.TOC_ITEM_TEMPLATES[self.style].format(
                    indent=indent,
                    title=title,
                    anchor=anchor,
                )

            toc += item

            if section.get("subsections"):
                next_level = level + 1
                if self.style == TocStyleOptions.NUMBER:
                    next_parent = f"{parent_number}{index}."
                else:
                    next_parent = ""

                toc += self._generate_toc_items(
                    section["subsections"], next_level, next_parent
                )

        return toc

    @staticmethod
    def _int_to_roman(number: int) -> str:
        """Convert an integer to a Roman numeral."""
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        roman_num = ""
        i = 0
        while number > 0:
            for _ in range(number // val[i]):
                roman_num += syb[i]
                number -= val[i]
            i += 1
        return roman_num

    def render(self, data: dict[str, Any]) -> str:
        """Render Table of Contents with themed sections."""
        sections = data.get("sections", {})
        toc_items = self._generate_toc_items(sections)
        template = self.TOC_TEMPLATES[self.style]
        return template.format(toc_items=toc_items)

    @staticmethod
    def get_toc_template(template: str) -> str:
        """Get the Table of Contents template for the given style."""
        return TocTemplate.TOC_TEMPLATES[TocStyleOptions(template)]

    @staticmethod
    def generate_anchor(title: str) -> str:
        """
        Generate GitHub-compatible anchor links.
        GitHub prepends a hyphen to headers that start with emoji.
        """
        emoji_pattern = re.compile(
            "["
            "\U0001f600-\U0001f64f"  # emoticons
            "\U0001f300-\U0001f5ff"  # symbols & pictographs
            "\U0001f680-\U0001f6ff"  # transport & map symbols
            "\U0001f1e0-\U0001f1ff"  # flags (iOS)
            "\U00002702-\U000027b0"
            "\U000024c2-\U0001f251"
            "]+",
            flags=re.UNICODE,
        )

        first_char = title[0] if title else ""
        starts_with_emoji = bool(emoji_pattern.match(first_char))

        clean_title = emoji_pattern.sub("", title).strip()
        clean_title = clean_title.lower()
        clean_title = re.sub(r"[^\w\- ]", "", clean_title)
        clean_title = re.sub(r"\s+", "-", clean_title)
        clean_title = re.sub(r"-+", "-", clean_title)
        clean_title = clean_title.strip("-")

        if starts_with_emoji:
            clean_title = f"-{clean_title}"

        return clean_title
