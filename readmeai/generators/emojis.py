from dataclasses import dataclass
from typing import Dict, List, Optional

from readmeai.config.settings import Settings


@dataclass
class Section:
    """Represents a section in the README with optional subsections."""

    title: str
    subsections: Optional[List["Section"]] = None


@dataclass
class Theme:
    """Represents a complete theme with metadata and sections."""

    name: str
    description: str
    sections: List[Section]


class ThemeManager:
    """Manages emoji themes and section headers for the README file."""

    def __init__(self, config: Settings) -> None:
        self.config = config
        self.current_theme = "default"
        self.themes: Dict[str, Theme] = self._process_themes()

    def _process_themes(self) -> Dict[str, Theme]:
        """Process theme configurations from Settings."""
        processed_themes = {}

        try:
            for theme_id, theme_data in self.config.themes.items():
                sections = []
                for section_data in theme_data.get("sections", []):
                    subsections = [
                        Section(title=subsection["title"])
                        for subsection in section_data.get("subsections", [])
                    ]
                    sections.append(
                        Section(
                            title=section_data["title"],
                            subsections=subsections or None,
                        )
                    )

                processed_themes[theme_id] = Theme(
                    name=theme_data.get("name", theme_id.title()),
                    description=theme_data.get("description", ""),
                    sections=sections,
                )

            return processed_themes

        except Exception as e:
            raise ValueError(
                f"Error processing theme configurations: {e!r}"
            ) from e

    def get_headers(self, include_subsections: bool = True) -> Dict[str, str]:
        """Get all section headers for the current theme."""
        theme = self.themes[self.current_theme]

        toc_title = next(
            (
                section.title
                for section in theme.sections
                if self._slugify(self._strip_emoji(section.title))
                == "table-of-contents"
            ),
            "Table of Contents",
        )

        headers = {"table-of-contents": toc_title, "TOC_HEADER": toc_title}

        for section in theme.sections:
            slug = self._slugify(self._strip_emoji(section.title))
            headers[f"{slug}"] = section.title
            headers[f"{slug.upper()}_HEADER"] = section.title

            if include_subsections and section.subsections:
                for subsection in section.subsections:
                    subslug = self._slugify(
                        self._strip_emoji(subsection.title)
                    )
                    headers[f"{subslug}"] = subsection.title
                    headers[f"{subslug.upper()}_HEADER"] = subsection.title

        return headers

    def get_section_title(
        self, section_index: int, subsection_index: Optional[int] = None
    ) -> str:
        """Get the title for a specific section and optional subsection."""
        theme = self.themes[self.current_theme]

        if section_index >= len(theme.sections):
            return ""

        section = theme.sections[section_index]

        if subsection_index is not None:
            if not section.subsections or subsection_index >= len(
                section.subsections
            ):
                return ""
            return section.subsections[subsection_index].title

        return section.title

    def get_theme_section(
        self, theme_id: str, section_name: str
    ) -> Optional[Section]:
        """Get a specific section from a theme by its name."""
        if theme_id not in self.themes:
            return None

        theme = self.themes[theme_id]
        return next(
            (
                section
                for section in theme.sections
                if self._slugify(self._strip_emoji(section.title))
                == self._slugify(section_name)
            ),
            None,
        )

    def generate_toc_data(self) -> List[Dict]:
        """Generate table of contents data structure."""
        theme = self.themes[self.current_theme]
        toc_data = []

        for section in theme.sections:
            section_data = {
                "title": section.title,
                "id": self._slugify(self._strip_emoji(section.title)),
            }

            if section.subsections:
                section_data["subsections"] = [
                    {
                        "title": subsection.title,
                        "id": self._slugify(
                            self._strip_emoji(subsection.title)
                        ),
                    }
                    for subsection in section.subsections
                ]

            toc_data.append(section_data)

        return toc_data

    def list_available_themes(self) -> List[Dict[str, str]]:
        """List all available themes with their descriptions."""
        return [
            {
                "id": theme_id,
                "name": theme.name,
                "description": theme.description,
            }
            for theme_id, theme in self.themes.items()
        ]

    def set_theme(self, theme_id: str) -> None:
        """Set the current theme."""
        if theme_id not in self.themes:
            raise ValueError(f"Theme '{theme_id}' not found")
        self.current_theme = theme_id

    @staticmethod
    def _slugify(text: str) -> str:
        """Convert text to lowercase with hyphens."""
        import re

        text = text.lower()
        text = re.sub(r"[^\w\s-]", "", text)
        text = re.sub(r"[-\s]+", "-", text)
        return text.strip("-")

    @staticmethod
    def _strip_emoji(text: str) -> str:
        """Remove emoji characters from text while preserving the rest."""
        import re

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
        return emoji_pattern.sub("", text).strip()
