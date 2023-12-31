"""Dynamically creates the 'Quick Start' section of the README file."""

import traceback
from pathlib import Path
from typing import List

from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.core.logger import Logger

logger = Logger(__name__)


def getting_started(
    conf: AppConfig,
    helper: ConfigHelper,
    deps: List[str],
    summaries: List[str],
):
    """Generates the 'Quick Start' section of the README file."""
    install_command = run_command = test_command = conf.md.default

    try:
        language_counts = {}
        for file_path, file_content in summaries:
            logger.info(f"Code summary: {file_path} - {file_content}")

            language = Path(file_path).suffix[1:]
            if language and language not in helper.ignore_files:
                if language in language_counts:
                    language_counts[language] += 1
                else:
                    language_counts[language] = 1

        if language_counts:
            language_top = max(language_counts, key=language_counts.get)

            if "streamlit" in deps:
                language_top = "streamlit"

            language_name = helper.language_names.get(language_top, "n/a")
            language_setup = helper.language_setup.get(language_name, [])

            logger.info(f"Language counts {language_counts}")
            logger.info(f"Getting started commands: {language_setup}")

            if len(language_setup) >= 3:
                install_command = language_setup[0]
                run_command = language_setup[1]
                test_command = language_setup[2]

    except Exception as exc_info:
        logger.debug(
            f"Exception occurred: {exc_info}\n{traceback.format_exc()}"
        )

    return (install_command, run_command, test_command)
