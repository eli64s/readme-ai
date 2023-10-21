"""Utility methods for the readme-ai application."""

import re
from pathlib import Path
from typing import List

from readmeai.config.settings import ConfigHelper
from readmeai.core import logger

logger = logger.Logger(__name__)


def should_ignore(conf_helper: ConfigHelper, file_path: Path) -> bool:
    """Filters out files that should be ignored."""
    for directory in conf_helper.ignore_files["directories"]:
        if directory in file_path.parts:
            logger.debug(f"Ignoring directory: {file_path}")
            return True

    if file_path.name in conf_helper.ignore_files["files"]:
        logger.debug(f"Ignoring file: {file_path}")
        return True

    if file_path.suffix[1:] in conf_helper.ignore_files["extensions"]:
        logger.debug(f"Ignoring extension: {file_path}")
        return True

    return False


def is_valid_url(url: str) -> bool:
    """Check if a given string is a valid URL."""
    regex = re.compile(
        r"^(?:http|ftp)s?://"
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,63}|[A-Z]{2,63}\.[A-Z]{2,63}))"
        r"(?::\d+)?"
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(regex.match(url))


def flatten_list(nested_list: List) -> List:
    """Flattens a nested list."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def format_sentence(text: str) -> str:
    """Clean and format the generated text from the model."""
    # Remove newlines and tabs
    text = text.replace("\n", "").replace("\t", "")

    # Remove non-letter characters from the beginning of the string
    text = re.sub(r"^[^a-zA-Z]*", "", text)

    # Remove extra white space around punctuation except for '('
    text = re.sub(r"\s*([)'.!,?;:])(?!\.\s*\w)", r"\1", text)

    # Remove extra white space before opening parentheses
    text = re.sub(r"(\()\s*", r"\1", text)

    # Replace multiple consecutive spaces with a single space
    text = re.sub(r" +", " ", text)

    # Remove extra white space around hyphens
    text = re.sub(r"\s*-\s*", "-", text)

    return text.strip().strip('"')


def remove_substring(input_string: str) -> str:
    """Remove text between HTML tags."""
    pattern = r"</p>.*?</div>"
    output_string = re.sub(
        pattern, "</p>\n</div>", input_string, flags=re.DOTALL
    )
    return output_string
