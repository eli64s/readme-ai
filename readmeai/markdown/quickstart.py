"""Dynamically creates the 'Quick Start' section of the README file."""

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
    language_counts: Dict[str, int]
    top_language: str
    top_language_full_name: str = None


def count_languages(
    summaries: List[str], helper: ConfigHelper
) -> Dict[str, int]:
    """
    Counts the occurrences of each language in the summaries.
    """
    language_counts = {}
    for file_path, _ in summaries:
        language = Path(file_path).suffix[1:]
        if language and language not in helper.ignore_files:
            language_counts[language] = language_counts.get(language, 0) + 1
    return language_counts


def get_top_language(language_counts: Dict[str, int]) -> str:
    """
    Determines the top language.
    """
    if not language_counts:
        return None
    return max(language_counts, key=language_counts.get)


def get_top_language_setup(
    language_counts: Dict[str, int], conf: AppConfig, helper: ConfigHelper
) -> ProjectSetup:
    """
    Determines the top language and retrieves its setup commands.
    """
    if not language_counts:
        return None

    top_language_key = get_top_language(language_counts)
    language_name = helper.language_names.get(top_language_key, "n/a")
    setup_commands = helper.language_setup.get(
        language_name, helper.language_setup.get("default", "n/a")
    )
    top_language_full_name = language_name

    return ProjectSetup(
        *setup_commands,
        language_counts,
        top_language_key,
        top_language_full_name,
    )


def getting_started(
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

        logger.info(f"Language counts {language_counts}")
        logger.info(f"Getting started commands: {setup}")

    except Exception as exc_info:
        logger.debug(
            f"Exception occurred: {exc_info}\n{traceback.format_exc()}"
        )
        setup = default_setup

    return setup
