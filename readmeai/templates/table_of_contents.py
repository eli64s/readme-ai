import re
from typing import Any, ClassVar

from readmeai.config.constants import TocStyleOptions
from readmeai.templates.base import BaseTemplate


class TocTemplate(BaseTemplate):
    """
    Class variable for rendering the README.md Table of Contents.
    """

    TOC_TEMPLATES: ClassVar[dict] = {
        TocStyleOptions.BULLET: """## 🔗 Table of Contents\n\n{toc_items}\n---\n""",
        TocStyleOptions.FOLD: """<details><summary>Table of Contents</summary>\n\n{toc_items}\n</details>\n<hr>\n""",
        TocStyleOptions.NUMBER: """## 🔗 Table of Contents\n\n{toc_items}\n---\n""",
        TocStyleOptions.LINKS: """## 🔗 Quick Links\n\n{toc_items}\n---\n""",
        TocStyleOptions.ROMAN: """## 🔗 Table of Contents\n\n{toc_items}\n---\n""",
    }

    TOC_ITEM_TEMPLATES: ClassVar[dict[TocStyleOptions, str]] = {
        TocStyleOptions.BULLET: "- [{title}](#{anchor})\n",
        TocStyleOptions.FOLD: "- [{title}](#{anchor})\n",
        TocStyleOptions.NUMBER: "{number}. [{title}](#{anchor})\n",
        TocStyleOptions.LINKS: "- [{title}](#{anchor})\n",
        TocStyleOptions.ROMAN: "{number}. [{title}](#{anchor})\n",
    }

    def __init__(self, style: str = TocStyleOptions.BULLET.value) -> None:
        self.style = TocStyleOptions(style)

    @staticmethod
    def generate_anchor(title: str) -> str:
        """Generate an anchor link from the given title.
        # #-table-of-contents
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
        title = emoji_pattern.sub("", title)
        return title.lower().replace(" ", "-")

    def _generate_toc_items(
        self,
        sections: list[dict[str, Any]],
        level: int = 0,
        parent_number: str = "",
    ) -> str:
        """Generate Table of Contents items recursively."""
        toc = ""
        for index, section in enumerate(sections, start=1):
            if self.style == TocStyleOptions.ROMAN and level > 0:
                continue

            indent = "  " * level
            title = section["title"]
            anchor = self.generate_anchor(title)

            if self.style in {TocStyleOptions.NUMBER, TocStyleOptions.ROMAN}:
                if self.style == TocStyleOptions.ROMAN:
                    number = (
                        f"{parent_number}{self._int_to_roman(index)}"
                        if parent_number
                        else self._int_to_roman(index)
                    )
                else:
                    number = (
                        f"{parent_number}{index}"
                        if parent_number
                        else str(index)
                    )
                item = self.TOC_ITEM_TEMPLATES[self.style].format(
                    number=number,
                    title=title,
                    anchor=anchor,
                )
            else:
                item = self.TOC_ITEM_TEMPLATES[self.style].format(
                    title=title,
                    anchor=anchor,
                )

            toc += f"{indent}{item}"

            if (
                "subsections" in section
                and self.style != TocStyleOptions.ROMAN
            ):
                toc += self._generate_toc_items(
                    section["subsections"],
                    level + 1,
                    f"{number}."
                    if self.style == TocStyleOptions.NUMBER
                    else "",
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
        """Render Table of Contents based on the current style and data."""
        toc_items = self._generate_toc_items(data["sections"])
        template = self.TOC_TEMPLATES[self.style]
        return template.format(toc_items=toc_items)

    @staticmethod
    def get_toc_template(template: str) -> str:
        """Get the Table of Contents template for the given style."""
        return TocTemplate.TOC_TEMPLATES[TocStyleOptions(template)]
