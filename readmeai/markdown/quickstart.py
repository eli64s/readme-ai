"""Creates the 'Getting Started' section of the README file."""

from pathlib import Path

from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.core import logger

logger = logger.Logger(__name__)


def create_instructions(
    conf: AppConfig, helper: ConfigHelper, summaries: list
):
    """Creates the 'Getting Started' section of the README file."""
    try:
        default_install_command = (
            default_run_command
        ) = default_test_command = conf.md.default

        language_counts = {}
        for module, _ in summaries:
            language = Path(module).suffix[1:]
            if language and language not in helper.ignore_files:
                if language in language_counts:
                    language_counts[language] += 1
                else:
                    language_counts[language] = 1

        if language_counts:
            language_top = max(language_counts, key=language_counts.get)
            language_name = helper.language_names.get(language_top, "Unknown")
            language_setup = helper.language_setup.get(language_name, [])

            logger.info(f"{language_name} setup guide: {language_setup}")

            if len(language_setup) >= 3:
                default_install_command = language_setup[0]
                default_run_command = language_setup[1]
                default_test_command = language_setup[2]

    except Exception as exc:
        logger.debug(
            f"Error: {exc}\nUsing default setup: {default_run_command}"
        )

    return (default_install_command, default_run_command, default_test_command)
