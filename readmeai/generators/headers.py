import re
from enum import Enum
from typing import Any, Dict, Final, List, Optional, TypedDict

from pydantic import BaseModel, ConfigDict, Field, computed_field
from readmeai.core.logger import get_logger
from readmeai.generators.enums import HeaderStyles
from readmeai.utilities.file_handler import FileHandler

_logger = get_logger(__name__)


class SectionType(str, Enum):
    """
    Standard section types for documentation.
    """

    TOC = "table_of_contents"
    OVERVIEW = "overview"
    FEATURES = "features"
    STRUCTURE = "project_structure"
    GETTING_STARTED = "getting_started"
    ROADMAP = "roadmap"
    CONTRIBUTING = "contributing"
    LICENSE = "license"
    ACKNOWLEDGMENTS = "acknowledgments"


SECTION_ORDER: Final[Dict[str, int]] = {
    SectionType.TOC.value: 0,
    SectionType.OVERVIEW.value: 1,
    SectionType.FEATURES.value: 2,
    SectionType.STRUCTURE.value: 3,
    SectionType.GETTING_STARTED.value: 4,
    SectionType.ROADMAP.value: 5,
    SectionType.CONTRIBUTING.value: 6,
    SectionType.LICENSE.value: 7,
    SectionType.ACKNOWLEDGMENTS.value: 8,
}

SECTION_ALIASES: Final[Dict[str, str]] = {
    "intro": SectionType.OVERVIEW.value,
    "introduction": SectionType.OVERVIEW.value,
    "summary": SectionType.OVERVIEW.value,
    "project_structure": SectionType.STRUCTURE.value,
    "directory": SectionType.STRUCTURE.value,
    "quickstart": SectionType.GETTING_STARTED.value,
    "setup": SectionType.GETTING_STARTED.value,
    "features": SectionType.FEATURES.value,
    "key_features": SectionType.FEATURES.value,
}


class HeaderData(TypedDict):
    """
    Type definition for header style template data.
    """

    align: str
    logo: str
    logo_size: str
    repo_name: str
    tagline: str
    shields_icons: str
    tech_stack_description: str
    tech_stack_icons: str


class HeaderTemplate(BaseModel):
    """
    Define the header templates for the README file.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
        use_enum_values=True,
    )

    file_handler: FileHandler = FileHandler()
    style: str = HeaderStyles.CLASSIC
    header_styles: HeaderStyles = file_handler.read(
        "readmeai/config/settings/templates/headers.toml"
    )
    templates: Dict[HeaderStyles, str] = {
        HeaderStyles(k): v["template"]
        for k, v in header_styles["header_styles"].items()
    }

    @computed_field
    def get_template(self) -> str:
        """Fetch the selected header style template."""
        return self.templates.get(
            HeaderStyles(self.style), self.templates[HeaderStyles.CLASSIC]
        )

    def render(self, header_data: HeaderData) -> str:
        """Render the header template with provided data."""
        template = self.templates.get(
            HeaderStyles(self.style), self.templates[HeaderStyles.CLASSIC]
        )
        return template.format(**header_data)


class HeaderConfig(BaseModel):
    """
    Configuration for header styling and theming.
    """

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
        populate_by_name=True,
        use_enum_values=True,
    )

    section: SectionType = Field(default=SectionType.OVERVIEW)
    variants: List[str] = []
    themed_title: Optional[str] = None
    plain_title: str
    level: int = Field(default=2, ge=1, le=6, description="Markdown header level")

    @property
    def markdown_prefix(self) -> str:
        """Generate markdown header prefix based on level"""
        return "#" * self.level


class HeaderRegistry:
    """
    Centralized registry for managing header templates and configurations.
    """

    def __init__(self, emoji_theme: str, theme_data: dict) -> None:
        self.emoji_theme = emoji_theme
        self.theme_mapping = theme_data.get("mapping", {})
        self.section_aliases = SECTION_ALIASES
        self.headers: Dict[str, HeaderConfig] = {}
        self.theme_data = theme_data.get("mapping", {})

    def prepare_section_data(self, sections: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Prepare section data with proper hierarchical structure for navigation."""
        formatted_sections = []
        for section in sections:
            formatted_section = {
                "title": section["title"],
                "level": 0,
                "subsections": [],
            }

            if "subsections" in section:
                for subsection in section["subsections"]:
                    formatted_subsection = {"title": subsection["title"], "level": 1}
                    formatted_section["subsections"].append(formatted_subsection)

            formatted_sections.append(formatted_section)

        return {"sections": formatted_sections}

    def get_themed_title(self, section: str) -> str:
        """Get themed version of section title with proper formatting."""
        normalized_section = normalize_section_name(section)
        standard_section = self.section_aliases.get(normalized_section, section)
        themed_title = self.theme_mapping.get(standard_section, section)

        # Ensure proper spacing after emoji if present
        emoji = self._extract_emoji(themed_title)
        if emoji:
            clean_title = self._strip_emoji(themed_title)
            return f"{emoji} {clean_title}"
        return themed_title

    def _extract_emoji(self, text: str) -> str:
        """Extract emoji from beginning of text if present."""
        emoji_pattern = re.compile(
            r"^(?:\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])"
        )
        match = emoji_pattern.search(text)
        return match.group(0) if match else ""

    def _strip_emoji(self, text: str) -> str:
        """Remove emoji from beginning of text."""
        emoji_pattern = re.compile(
            r"^(?:\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])"
        )
        return emoji_pattern.sub("", text).strip()

    @staticmethod
    def _remove_emoji(text: str) -> str:
        """
        Remove emoji characters from text while preserving the rest of the string.
        Uses regex pattern matching to identify and remove emoji unicode ranges.
        """
        emoji_pattern = re.compile(
            r"["
            r"\U0001f600-\U0001f64f"  # emoticons
            r"\U0001f300-\U0001f5ff"  # symbols & pictographs
            r"\U0001f680-\U0001f6ff"  # transport & map symbols
            r"\U0001f1e0-\U0001f1ff"  # flags (iOS)
            r"\U00002702-\U000027b0"  # dingbats
            r"\U000024c2-\U0001f251"
            r"]+",
            flags=re.UNICODE,
        )
        return emoji_pattern.sub("", text)


def normalize_section_name(name: str) -> str:
    """Normalize section name for header generation."""
    normalized = name.lower()
    normalized = re.sub(r"[^a-z0-9_]", "_", normalized)
    normalized = re.sub(r"_+", "_", normalized)
    return normalized.strip("_")
