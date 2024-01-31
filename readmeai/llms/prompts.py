"""Prompt manager for LLM API calls."""

from typing import List

import readmeai.config.settings as AppConfig
from readmeai.core.logger import Logger

logger = Logger(__name__)


def get_prompt_context(
    config: AppConfig, prompt_type: str, context: dict
) -> str:
    """Generates a prompt for the LLM API."""
    prompt_template = get_prompt_template(config.prompts, prompt_type)

    if not prompt_template:
        logger.error(f"Prompt type '{prompt_type}' not found.")
        return ""

    return inject_prompt_context(prompt_template, context)


def get_prompt_template(prompts: dict, prompt_type: str) -> str:
    """Retrieves the template for the given prompt type."""
    prompt_templates = {
        "features": prompts.features,
        "overview": prompts.overview,
        "slogan": prompts.slogan,
    }
    return prompt_templates.get(prompt_type, "")


def inject_prompt_context(template: str, context: dict) -> str:
    """Formats the template with the provided context."""
    try:
        return template.format(*[context[key] for key in context])
    except KeyError as exc:
        logger.error(f"Missing context for prompt key: {exc}")
        return ""


async def set_prompt_context(
    config: AppConfig,
    dependencies: List[str],
    summaries: List[str],
) -> List[dict]:
    """Generates the prompts to be used by the LLM API."""
    return [
        {"type": prompt_type, "context": context}
        for prompt_type, context in [
            (
                "summaries",
                {
                    "tree": config.md.tree,
                    "dependencies": dependencies,
                    "summaries": summaries,
                },
            ),
        ]
    ]


async def set_other_prompt_context(
    config: AppConfig,
    dependencies: List[str],
    summaries: List[str],
) -> List[dict]:
    """Generates the prompts to be used by the LLM API."""
    return [
        {"type": prompt_type, "context": context}
        for prompt_type, context in [
            (
                "features",
                {
                    "repo": config.git.repository,
                    "dependencies": dependencies,
                    "summaries": summaries,
                },
            ),
            (
                "overview",
                {
                    "name": config.git.name,
                    "repo": config.git.repository,
                    "summaries": summaries,
                },
            ),
            (
                "slogan",
                {
                    "name": config.git.name,
                    "repo": config.git.repository,
                    "summaries": summaries,
                },
            ),
        ]
    ]
