from typing import Dict, Optional, Set

from pydantic import BaseModel, ConfigDict, Field

from readmeai.prompts.constants import Section, Style


class PromptTemplate(BaseModel):
    """Template for section content generation."""

    content: str
    style: Style
    section: Section
    variables: Set[str] = Field(default_factory=set)
    description: Optional[str] = None

    model_config = ConfigDict(frozen=True)


class SectionConfig(BaseModel):
    """Configuration for a README section."""

    templates: Dict[Style, PromptTemplate]
    default_style: Style
    required_variables: Set[str]
