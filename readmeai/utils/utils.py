"""Utility methods for the readme-ai application."""

import re
from pathlib import Path
from typing import List

from readmeai.config.settings import ConfigHelper
from readmeai.core import logger

logger = logger.Logger(__name__)


def is_valid_url(url: str) -> bool:
    """Validate a URL string.

    Parameters
    ----------
    url
        The URL string to validate.

    Returns
    -------
        True if the URL is valid, False otherwise.
    """
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|"  # ipv4
        r"\[?[A-F0-9]*:[A-F0-9:]+\]?)"  # ipv6
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return re.match(regex, url) is not None


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


def get_relative_path(absolute_path: str, base_path: str) -> str:
    """Get the relative path of a file."""
    absolute_path = Path(absolute_path)
    return absolute_path.relative_to(base_path)


def remove_substring(input_string: str) -> str:
    """Remove text between HTML tags."""
    pattern = r"</p>.*?</div>"
    output_string = re.sub(
        pattern, "</p>\n</div>", input_string, flags=re.DOTALL
    )
    return output_string


def should_ignore(conf_helper: ConfigHelper, file_path: Path) -> bool:
    """Filters out files that should be ignored."""
    ignore_files = conf_helper.ignore_files

    if (
        (file_path.name in ignore_files["files"])
        or (file_path.suffix.lstrip(".") in ignore_files["extensions"])
        or any(
            directory in file_path.parts
            for directory in ignore_files["directories"]
        )
    ):
        logger.debug(f"Ignoring: {file_path.name}")
        return True

    return False
