from functools import lru_cache
from pathlib import Path
from typing import Dict, Optional

from readmeai.config.settings import Settings
from readmeai.prompts.models import (
    PromptTemplate,
    Section,
    SectionConfig,
    Style,
)
from readmeai.utils.file_handler import FileHandler


class PromptManager:
    """Manager for README section prompts."""

    def __init__(self, settings: Settings):
        self.settings = settings
        self.file_handler = FileHandler()
        self._load_prompts()

    def _load_prompts(self) -> None:
        """Load prompt configurations."""
        self.sections: Dict[Section, SectionConfig] = {}

        # Load section configs
        for section in Section:
            section_path = (
                self.settings.resources.config.prompts.sections.full_path
                / f"{section.value}.toml"
            )
            self.sections[section] = self._load_section_config(section_path)

    def _load_section_config(self, path: Path) -> SectionConfig:
        """Load configuration for a section."""
        config = self.file_handler.read(path)
        return SectionConfig(**config)

    @lru_cache(maxsize=32)
    def get_template(
        self, section: Section, style: Optional[Style] = None
    ) -> PromptTemplate:
        """Get prompt template for section and style."""
        if section not in self.sections:
            raise ValueError(f"Unknown section: {section}")

        section_config = self.sections[section]
        style = style or section_config.default_style

        if style not in section_config.templates:
            raise ValueError(f"Style '{style}' not available for {section}")

        return section_config.templates[style]
