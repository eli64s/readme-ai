"""Dynamically creates the 'Quickstart' section of the README file."""

import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.core.logger import Logger

logger = Logger(__name__)


@dataclass
class ProjectSetup:
    """Information about using, running, and testing a repository."""

    install_command: str
    run_command: str
    test_command: str
    requirements: str
    language_counts: Dict[str, int]
    top_language: str
    top_language_full_name: str = None


def count_languages(
    summaries: List[str], helper: ConfigHelper
) -> Dict[str, int]:
    """
    Counts the occurrences of each language in the summaries.
    """
    dependency_files = helper.dependency_files.get("dependency_files")

    language_counts = {}

    for file_path, _ in summaries:
        language = Path(file_path).suffix[1:]

        if str(file_path) in [
            dependency_file for dependency_file in dependency_files
        ]:
            continue

        if language and language not in helper.ignore_files:
            language_counts[language] = language_counts.get(language, 0) + 1

    return language_counts


def get_top_language(language_counts: Dict[str, int]) -> str:
    """
    Determines the top language.
    """
    if not language_counts:
        return None

    return max(sorted(language_counts), key=language_counts.get)


def get_top_language_setup(
    language_counts: Dict[str, int], conf: AppConfig, helper: ConfigHelper
) -> ProjectSetup:
    """
    Determines the top language and retrieves its setup commands.
    """
    if not language_counts:
        return None

    language_key = get_top_language(language_counts)
    language_name = helper.language_names.get(language_key, conf.md.default)
    requirements = f"**{language_name}**: `version x.y.z`"
    setup_commands = helper.language_setup.get(
        language_name, helper.language_setup.get("default", "n/a")
    )

    return ProjectSetup(
        *setup_commands,
        requirements,
        language_counts,
        language_key,
        language_name,
    )


def setup_guide(
    conf: AppConfig, helper: ConfigHelper, summaries: List[str]
) -> ProjectSetup:
    """
    Generates the 'Quick Start' section of the README file.
    """
    default_setup = ProjectSetup("", "", "", {}, "", "")

    try:
        language_counts = count_languages(summaries, helper)
        setup = (
            get_top_language_setup(language_counts, conf, helper)
            or default_setup
        )

    except Exception as exc:
        logger.debug(f"Exception: {exc}\n{traceback.format_exc()}")
        setup = default_setup

    logger.info(f"Quickstart data: {setup}")

    return setup
