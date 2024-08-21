import re
from enum import Enum
from typing import Any, ClassVar

from .base_template import BaseTemplate


class ToCStyle(Enum):
    """
    Enum for Table of Contents template styles.
    """

    BULLET = "bullet"
    FOLD = "fold"
    LINKS = "links"
    NUMBER = "number"


class ToCTemplate(BaseTemplate):
    """
    Class variable for rendering the README.md Table of Contents.
    """

    TOC_TEMPLATES: ClassVar[dict] = {
        ToCStyle.BULLET: """##### 🔗 Table of Contents\n\n{toc_items}\n---\n""",
        ToCStyle.FOLD: """<details><summary>Table of Contents</summary>\n\n{toc_items}\n</details>\n<hr>\n""",
        ToCStyle.NUMBER: """##### 📖 Table of Contents\n\n{toc_items}\n---\n""",
        ToCStyle.LINKS: """##### 🔗 Quick Links\n\n{toc_items}\n---\n""",
    }

    TOC_ITEM_TEMPLATES: ClassVar[dict[ToCStyle, str]] = {
        ToCStyle.BULLET: "- [{title}](#{anchor})\n",
        ToCStyle.FOLD: "- [{title}](#{anchor})\n",
        ToCStyle.NUMBER: "{number}. [{title}](#{anchor})\n",
        ToCStyle.LINKS: "- [{title}](#{anchor})\n",
    }

    def __init__(self, style: str = ToCStyle.BULLET.value) -> None:
        """
        Initialize the Table of Contents template with the given style.
        """
        self.style = ToCStyle(style)

    @staticmethod
    def generate_anchor(title: str) -> str:
        """
        Generate an anchor link from the given title.
        """
        title = re.sub(r":[a-zA-Z0-9_+-]+:", "", title)
        anchor = title.lower().replace(" ", "-")
        anchor = re.sub(r"[^\w-]", "", anchor)
        return anchor

    def _generate_toc_items(
        self,
        sections: list[dict[str, Any]],
        level: int = 0,
        parent_number: str = "",
    ) -> str:
        """
        Generate Table of Contents items recursively.
        """
        toc = ""
        for index, section in enumerate(sections, start=1):
            indent = "  " * level
            anchor = self.generate_anchor(section["title"])
            if self.style == ToCStyle.NUMBER:
                number = (
                    f"{parent_number}{index}" if parent_number else str(index)
                )
                item = self.TOC_ITEM_TEMPLATES[self.style].format(
                    number=number,
                    title=section["title"],
                    anchor=anchor,
                )
            else:
                item = self.TOC_ITEM_TEMPLATES[self.style].format(
                    title=section["title"],
                    anchor=anchor,
                )
            toc += f"{indent}{item}"
            if "subsections" in section:
                toc += self._generate_toc_items(
                    section["subsections"],
                    level + 2,
                    f"{number}." if self.style == ToCStyle.NUMBER else "",
                )
        return toc

    def render(self, data: dict[str, Any]) -> str:
        """
        Render Table of Contents based on the current style and data.
        """
        toc_items = self._generate_toc_items(data["sections"])
        template = self.TOC_TEMPLATES[self.style]
        return template.format(toc_items=toc_items)

    @staticmethod
    def get_toc_template(template: str) -> str:
        """
        Get the Table of Contents template for the given style.
        """
        return ToCTemplate.TOC_TEMPLATES[ToCStyle(template)]
