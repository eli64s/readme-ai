from typing import Any, Optional

from readmeai.models.base import BaseModelHandler
from readmeai.prompts.manager import PromptManager
from readmeai.prompts.models import Section, Style


class ContentGenerator:
    """Generate README section content."""

    def __init__(self, prompt_manager: PromptManager, llm: BaseModelHandler):
        self.prompts = prompt_manager
        self.llm = llm

    async def generate_section(
        self, section: Section, style: Optional[Style] = None, **variables: Any
    ) -> str:
        """Generate content for a section."""
        # Get template
        template = self.prompts.get_template(section, style)

        # Validate variables
        required_vars = self.prompts.sections[section].required_variables
        missing_vars = required_vars - set(variables.keys())

        if missing_vars:
            raise ValueError(
                f"Missing required variables for {section}: {missing_vars}"
            )

        # Format prompt and generate
        prompt = template.format(**variables)
        return await self.llm.generate(prompt)
