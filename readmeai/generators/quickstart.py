"""
Dynamically generate 'Quickstart' guides for the README file.
"""

import traceback
from dataclasses import dataclass
from pathlib import Path

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import Logger

_logger = Logger(__name__)


@dataclass
class QuickStart:
    """
    Information about using, running, and testing a repository.
    """

    install_command: str
    run_command: str
    test_command: str
    prerequisites: str
    language_counts: dict[str, int]
    language_key: str | None
    language_name: str | None = None


def count_languages(
    summaries: tuple,
    config_loader: ConfigLoader,
) -> dict[str, int]:
    """
    Counts the occurrences of each language in the summaries.
    """
    parser_files = config_loader.parsers.get("parsers")

    language_counts: dict[str, int] = {}

    for file_path, _ in summaries:
        language = Path(file_path).suffix[1:] or None

        if str(file_path) in [
            dependency_file for dependency_file in parser_files
        ]:
            continue

        if (
            language
            and language.strip()
            and language not in config_loader.ignore_list
        ):
            language_counts[language] = language_counts.get(language, 0) + 1

    return language_counts


def get_top_language(language_counts: dict[str, int]) -> str | None:
    """
    Determines the top language.
    """
    if not language_counts:
        return None
    else:
        return max(sorted(language_counts), key=language_counts.get)


def get_top_language_setup(
    language_counts: dict,
    config_loader: ConfigLoader,
) -> QuickStart:
    """
    Determines the top language and retrieves its setup commands.
    """
    languages = config_loader.languages.get("language_names")
    commands = config_loader.commands.get("quickstart_guide")

    language_key = get_top_language(language_counts)
    language_name = languages.get(language_key, languages.get("default"))
    quickstart_commands = commands.get(language_name, commands.get("default"))
    prerequisites = f"**{language_name}**: `version x.y.z`"

    return QuickStart(
        *quickstart_commands,
        prerequisites=prerequisites,
        language_counts=language_counts,
        language_key=language_key,
        language_name=language_name,
    )


def get_setup_data(
    config_loader: ConfigLoader,
    summaries: tuple,
) -> QuickStart:
    """
    Generates the 'Quick Start' section of the README file.
    """
    default_setup = QuickStart("", "", "", {}, "", "")

    try:
        language_counts = count_languages(summaries, config_loader)
        setup = (
            get_top_language_setup(language_counts, config_loader)
            or default_setup
        )

    except Exception as exc:
        _logger.debug(f"Exception: {exc}\n{traceback.format_exc()}")
        setup = default_setup

    _logger.info(f"Quickstart information: {setup}")

    return setup
