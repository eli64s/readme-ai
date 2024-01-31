"""Utility methods for processing files and text."""

import re
from importlib import resources
from pathlib import Path

from readmeai.config.settings import ConfigHelper
from readmeai.core.logger import Logger

logger = Logger(__name__)


def format_md_table(text: str) -> str:
    """
    Pattern to match a Markdown table. Looks for a
    header row with at least two columns. followed by
    a separator row, and then one or more data rows.
    """
    pattern = r"(\|.*\|.*\n\|[-: ]+\|[-: ]+\|.*\n(?:\|.*\|.*\n)*)"
    match = re.search(pattern, text, re.MULTILINE)
    return match.group(0) if match else ""


def format_md_text(text: str) -> str:
    """Format and clean generated text from the LLM."""
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


def format_response(prompt_type: str, response_text: str) -> str:
    """Post-processes the response from the LLM."""
    return (
        format_md_text(response_text)
        if prompt_type != "features"
        else format_md_table(response_text)
    )


def get_resource_path(package: str, resource_name: str) -> Path:
    """Use importlib.resources or pkg_resources to get resource path.
    Python 3.9+ uses importlib.resources, older versions use pkg_resources.

    Parameters
    ----------
    package
        Python package name.
    resource_name
        Name of the resource to get the path for.

    Returns
    -------
    Path
        The path to the resource file.
    """
    try:
        resource_path = resources.files(package) / resource_name

    except (TypeError, FileNotFoundError):
        import pkg_resources

        resource_path = pkg_resources.resource_filename(package, resource_name)

    return resource_path


def is_file_ignored(conf_helper: ConfigHelper, file_path: Path) -> bool:
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
        return True

    return False
