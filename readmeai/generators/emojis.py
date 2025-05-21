"""Theme manager for handling emoji header themes in README documentation."""

import re
from typing import Dict, List, Optional

import yaml
from pydantic import BaseModel, Field
from readmeai.config.settings import Settings
from readmeai.core.logger import get_logger
from readmeai.utilities.resource_manager import build_resource_path

logger = get_logger(__name__)


class Section(BaseModel):
    """
    Represents a section in the README with optional subsections.
    """

    title: str
    subsections: Optional[List["Section"]] = None

    def get_emoji(self) -> Optional[str]:
        """Extract emoji prefix from section title if present."""
        # Match emoji characters at the start of the title
        emoji_pattern = re.compile(
            r"^["
            "\U0001f300-\U0001f5ff"  # Symbols & pictographs
            "\U0001f600-\U0001f64f"  # Emoticons
            "\U0001f680-\U0001f6ff"  # Transport & map symbols
            "\U0001f700-\U0001f77f"  # Alchemical symbols
            "\U0001f780-\U0001f7ff"  # Geometric Shapes
            "\U0001f800-\U0001f8ff"  # Supplemental Arrows-C
            "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
            "\U0001fa00-\U0001fa6f"  # Chess Symbols
            "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027b0"  # Dingbats
            "]+\\s"  # Must be followed by whitespace
        )

        match = emoji_pattern.search(self.title)
        return match.group(0).strip() if match else None

    def get_clean_title(self) -> str:
        """Get title without emoji prefix."""
        emoji = self.get_emoji()
        return self.title[len(emoji) :].strip() if emoji else self.title


def normalize_section_name(name: str) -> str:
    """Normalize a section name for consistent matching.

    This function standardizes section names by:
    1. Converting to lowercase
    2. Replacing underscores and multiple spaces with single spaces
    3. Removing special characters
    4. Trimming whitespace

    Example: "Project_Index" -> "project index"
    """
    if not name:
        return ""
    # Convert to lowercase and replace underscores
    normalized = str(name).lower().replace("_", " ")
    # Remove special characters except spaces
    normalized = re.sub(r"[^a-z0-9\s]", "", normalized)
    # Replace multiple spaces with single space and trim
    normalized = " ".join(normalized.split())
    return normalized


class Theme(BaseModel):
    """Represents a complete emoji theme with metadata and sections."""

    name: str
    description: str
    sections: List[Section]

    def get_section(self, section_name: str) -> Optional[Section]:
        """Find a section by its name with robust matching."""
        if not section_name:
            return None

        # Normalize the input section name
        normalized_target = normalize_section_name(section_name)

        # First try exact matching with normalized names
        for section in self.sections:
            normalized_section = normalize_section_name(section.get_clean_title())
            if normalized_section == normalized_target:
                return section

        # If no exact match, try partial matching for special cases
        # This helps match variations like "project_index" with "Project Index"
        for section in self.sections:
            normalized_section = normalize_section_name(section.get_clean_title())
            if (
                normalized_target in normalized_section
                or normalized_section in normalized_target
            ):
                return section

        return None

    def get_subsection(
        self, section_name: str, subsection_name: str
    ) -> Optional[Section]:
        """Find a subsection within a specific section."""
        section = self.get_section(section_name)
        if not section or not section.subsections:
            return None

        normalized_target = normalize_section_name(subsection_name)

        for subsection in section.subsections:
            normalized_subsection = normalize_section_name(subsection.get_clean_title())
            if normalized_subsection == normalized_target:
                return subsection

        return None


class ThemeRegistry(BaseModel):
    """Container for all available emoji themes."""

    themes: Dict[str, Theme] = Field(default_factory=dict)

    def get_theme(self, theme_name: str) -> Theme:
        """Get a theme by name, falling back to default if not found."""
        return self.themes.get(theme_name, self.themes.get("default"))

    def list_themes(self) -> List[Dict[str, str]]:
        """List all available themes with their descriptions."""
        return [
            {
                "id": theme_id,
                "name": theme.name,
                "description": theme.description,
            }
            for theme_id, theme in self.themes.items()
        ]


class ThemeManager:
    """Manages emoji themes for README documentation."""

    def __init__(self, config: Settings) -> None:
        """Initialize theme manager with configuration."""
        self.config = config
        self.theme_registry = self._load_themes()
        self.current_theme = self.theme_registry.get_theme(config.md.emojis)
        self._header_cache: Dict[str, str] = {}

    def _load_themes(self) -> ThemeRegistry:
        """Load all themes from the YAML configuration."""
        try:
            theme_path = build_resource_path(
                file_path="themes/emojis.yaml",
                module="readmeai.config",
                submodule="settings",
            )

            with open(theme_path, encoding="utf-8") as f:
                theme_data = yaml.safe_load(f)

            themes = {
                theme_id: Theme(**theme_config)
                for theme_id, theme_config in theme_data.get("themes", {}).items()
            }

            return ThemeRegistry(themes=themes)

        except Exception as e:
            logger.error(f"Error loading themes: {e}")
            return ThemeRegistry(
                themes={
                    "default": Theme(
                        name="Default Theme",
                        description="Basic documentation theme without emojis",
                        sections=[
                            Section(title="Table of Contents"),
                            Section(title="Overview"),
                            Section(title="Features"),
                            Section(
                                title="Project Structure",
                                subsections=[Section(title="Project Index")],
                            ),
                            Section(
                                title="Getting Started",
                                subsections=[
                                    Section(title="Prerequisites"),
                                    Section(title="Installation"),
                                    Section(title="Usage"),
                                    Section(title="Testing"),
                                ],
                            ),
                            Section(title="Roadmap"),
                            Section(title="Contributing"),
                            Section(title="License"),
                            Section(title="Acknowledgment"),
                        ],
                    )
                }
            )

    def apply_theme_to_headers(self, headers: Dict[str, str]) -> Dict[str, str]:
        """Apply the current theme to a set of section headers."""
        themed_headers = {}

        for key, value in headers.items():
            # Handle both direct section names and header keys
            section_name = self._header_key_to_section(key)

            if not section_name:
                # If not a header key, try using the key directly as a section name
                section_name = key

            # Look up the themed version and cache it
            cache_key = f"header::{section_name}"
            if cache_key not in self._header_cache:
                section = self.current_theme.get_section(section_name)
                self._header_cache[cache_key] = section.title if section else value

            themed_headers[key] = self._header_cache[cache_key]

        return themed_headers

    def apply_theme_to_section(
        self, section_name: str, subsection_name: Optional[str] = None
    ) -> str:
        """Get the themed title for a specific section/subsection."""
        cache_key = (
            f"section::{section_name}::{subsection_name}"
            if subsection_name
            else f"section::{section_name}"
        )

        if cache_key not in self._header_cache:
            if subsection_name:
                section = self.current_theme.get_subsection(
                    section_name, subsection_name
                )
            else:
                section = self.current_theme.get_section(section_name)

            self._header_cache[cache_key] = section.title if section else section_name

        return self._header_cache[cache_key]

    def get_themed_toc(self) -> Dict[str, list]:
        """Generate themed table of contents data."""
        return {
            "sections": [
                {
                    "title": section.title,
                    "subsections": [
                        {"title": sub.title} for sub in (section.subsections or [])
                    ]
                    if section.subsections
                    else None,
                }
                for section in self.current_theme.sections
            ]
        }

    @staticmethod
    def _header_key_to_section(key: str) -> Optional[str]:
        """Convert a header key to a section name."""
        # Special handling for known problematic sections
        if key.lower() in {"project_index", "acknowledgment"}:
            return key.replace("_", " ").title()

        if key.endswith("_HEADER"):
            # Remove _HEADER suffix and convert to title case
            return " ".join(
                word.capitalize() for word in key[:-7].lower().replace("_", " ").split()
            )

        return None
