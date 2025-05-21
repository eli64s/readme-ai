"""Utility methods to build prompts for LLM text generation."""

from readmeai.config.settings import Settings
from readmeai.core.logger import get_logger
from readmeai.extractors.models import RepositoryContext

_logger = get_logger(__name__)


def get_prompt_context(prompts: dict, prompt_type: str, context: dict) -> str:
    """Generates a prompt for the LLM API."""
    prompt_template = get_prompt_template(prompts, prompt_type)

    if not prompt_template:
        _logger.error(f"Prompt type '{prompt_type}' not found.")
        return ""

    return inject_prompt_context(prompt_template, context)


def get_prompt_template(prompts: dict, prompt_type: str) -> str:
    """Retrieves the template for the given prompt type."""
    prompt_templates = {
        "features_table": prompts["prompts"]["features_table"],
        "overview": prompts["prompts"]["overview"],
        "tagline": prompts["prompts"]["tagline"],
    }
    return prompt_templates.get(prompt_type, "")


def inject_prompt_context(template: str, context: dict) -> str:
    """Format the template with the provided context."""
    try:
        return template.format(*[context[key] for key in context])
    except KeyError as e:
        _logger.error(f"Missing context for prompt key: {e!r}")
        return ""
    except Exception as e:
        _logger.error(f"Failed to format prompt template: {e!r}")
        return ""


def set_additional_contexts(
    config: Settings,
    repo_context: RepositoryContext,
    file_summaries: list[tuple[str, str]],
) -> list[dict]:
    """Build additional prompts for README content generation."""
    return [
        {"type": prompt_type, "context": context}
        for prompt_type, context in [
            (
                "features_table",
                {
                    "project_name": config.git.name,
                    "repository": config.git.repository,
                    "languages": repo_context.languages,
                    "dependencies": repo_context.dependencies,
                    "cicd": repo_context.metadata.get("cicd", []),
                    "containers": repo_context.metadata.get("containers", []),
                    "documentation": repo_context.metadata.get("documentation", []),
                    "package_managers": repo_context.metadata.get(
                        "package_managers", []
                    ),
                    "file_summaries": file_summaries,
                },
            ),
            (
                "overview",
                {
                    "project_name": config.git.name,
                    "file_summary": file_summaries,
                },
            ),
            (
                "tagline",
                {
                    "name": config.git.name,
                    "repo": config.git.repository,
                    "file_summary": file_summaries,
                },
            ),
        ]
    ]


def set_summary_context(
    config: Settings,
    repo_files: list[tuple[str, str]],
) -> list[dict]:
    """Generates the summary prompts to be used by the LLM API."""
    return [
        {"type": prompt_type, "context": context}
        for prompt_type, context in [
            (
                "file_summary",
                {
                    "tree": config.md.directory_structure,
                    "repo_files": repo_files,
                },
            ),
        ]
    ]
