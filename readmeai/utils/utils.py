"""Utility functions for the readmeai package."""

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


def flatten_list(nested_list: List[List]) -> List:
    """Flatten a nested list (list of lists converted to a single list).

    Parameters
    ----------
    nested_list
        The nested list to flatten.

    Returns
    -------
        A flattened list.
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def format_sentence(text: str) -> str:
    """Formats output text from the LLM model.
    i.e. removes extra white space, newlines, tabs, etc.

    Parameters
    ----------
    text
        The text to format.

    Returns
    -------
        The formatted text, used to generate the README.
    """
    # Remove single and double quotes around any text
    text = re.sub(r"(?<!\w)['\"](.*?)['\"](?!\w)", r"\1", text)

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

    return text.strip()


def get_relative_path(absolute_path: str, base_path: str) -> str:
    """Get the relative path of a file.

    Parameters
    ----------
    absolute_path
        Absolute path to the file i.e. the full path on the local machine.
    base_path
        Base path to use for the relative path i.e. the project root.

    Returns
    -------
        The relative path string of the file.
    """
    absolute_path = Path(absolute_path)
    return absolute_path.relative_to(base_path)


def remove_substring(
    input_string: str, pattern: str = r"</p>.*?</div>"
) -> str:
    """Remove a substring from a string.

    Parameters
    ----------
    input_string
        The string to remove the substring from.
    pattern, optional
        The substring to remove, by default r"</p>.*?</div>".

    Returns
    -------
        The input string with the substring removed.
    """
    output_string = re.sub(
        pattern, "</p>\n</div>", input_string, flags=re.DOTALL
    )
    return output_string


def should_ignore(conf_helper: ConfigHelper, file_path: Path) -> bool:
    """Check if a file should be ignored and not passed to the LLM API.
    Uses a default list of files - 'readmeai/settings/ignore_files.toml'.

    Parameters
    ----------
    conf_helper
        Configuration helper instance with the ignore files list.
    file_path
        The path to the file to check.

    Returns
    -------
        True if the file should be ignored, False otherwise.
    """
    ignore_files = conf_helper.ignore_files

    if (
        (file_path.name in ignore_files["files"])
        or (file_path.suffix.lstrip(".") in ignore_files["extensions"])
        or any(
            directory in file_path.parts
            for directory in ignore_files["directories"]
        )
    ):
        logger.debug(f"Ignoring item: {file_path.name}")
        return True

    return False
