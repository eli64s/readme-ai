"""Utility methods for the readme-ai application."""

import os
import platform
import re
from pathlib import Path
from typing import List, Optional

import git
from tiktoken import get_encoding

from . import conf, logger

logger = logger.Logger(__name__)


def clone_repository(repo_path: str, temp_dir: Path) -> None:
    """Clone a repository to a temporary directory."""
    git_exec_path = find_git_executable()

    validate_git_executable(git_exec_path)

    env = os.environ.copy()
    env["GIT_PYTHON_GIT_EXECUTABLE"] = str(git_exec_path)

    try:
        git.Repo.clone_from(repo_path, temp_dir, depth=1, env=env)
        logger.info(f"Successfully cloned {repo_path} to {temp_dir}.")

    except git.GitCommandError as excinfo:
        raise ValueError(f"Git clone error: {excinfo}") from excinfo

    except Exception as excinfo:
        raise (f"Error cloning git repository: {excinfo}")

    # validate_file_permissions(temp_dir)


def find_git_executable() -> Optional[Path]:
    """Find the path to the git executable, if available."""

    git_exec_path = os.environ.get("GIT_PYTHON_GIT_EXECUTABLE")

    if git_exec_path:
        return Path(git_exec_path)

    # For Windows, set default known location for git executable
    if platform.system() == "Windows":
        default_windows_path = Path("C:\\Program Files\\Git\\cmd\\git.EXE")
        if default_windows_path.exists():
            return default_windows_path

    # For other OS (including Linux), set executable by looking into PATH
    paths = os.environ["PATH"].split(os.pathsep)
    for path in paths:
        git_path = Path(path) / "git"
        if git_path.exists():
            return git_path

    return None


def validate_git_executable(git_exec_path: Optional[str]) -> None:
    """Validate the path to the git executable."""
    if not git_exec_path or not Path(git_exec_path).exists():
        raise ValueError(f"Git executable not found at {git_exec_path}")


def validate_file_permissions(temp_dir: Path) -> None:
    """Validates file permissions of the cloned repository."""
    if platform.system() != "Windows":
        if isinstance(temp_dir, str):
            temp_dir = Path(temp_dir)
        permissions = temp_dir.stat().st_mode & 0o777
        if permissions != 0o700:
            raise ValueError(
                "Error: file permissions of cloned repository must be set to 0o700."
            )


def get_github_file_link(file: str, user_repo_name: str) -> str:
    """Returns the GitHub URL for a given file."""
    return f"https://github.com/{user_repo_name}/blob/main/{file}"


def get_user_repository_name(url_or_path) -> str:
    """Extract username and repository name from a GitHub URL or local path."""

    if os.path.exists(url_or_path):
        return os.path.basename(url_or_path)

    pattern = r"https?://github.com/([^/]+)/([^/]+)"
    match = re.match(pattern, url_or_path)

    if match:
        username, reponame = match.groups()
        return f"{username}/{reponame}"
    else:
        raise ValueError("Error: invalid remote repository URL or local path.")


def adjust_max_tokens(max_tokens: int, prompt: str, target: str = "Hello!") -> int:
    """Adjust the maximum number of tokens based on the specific prompt."""
    is_valid_prompt = prompt.strip().startswith(target.strip())
    adjusted_max_tokens = max_tokens if is_valid_prompt else max_tokens // 3
    return adjusted_max_tokens


def get_token_count(text: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = get_encoding(encoding_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens


def truncate_text_tokens(text: str, encoding_name: str, max_tokens: int) -> str:
    """Truncate a text string to a maximum number of tokens."""
    encoding = get_encoding(encoding_name)
    encoded_text = encoding.encode(text)[:max_tokens]
    truncated_text = encoding.decode(encoded_text)
    return truncated_text


def is_valid_file(helper: conf.ConfigHelper, path: Path) -> bool:
    """Checks if a file is valid for processing."""
    ignore_dirs = helper.ignore_files.get("directories", [])
    ignore_files = helper.ignore_files.get("filenames", [])
    ignore_extensions = helper.ignore_files.get("extensions", [])
    return (
        path.is_file()
        and all(dir not in path.parts for dir in ignore_dirs)
        and path.name not in ignore_files
        and path.suffix not in ignore_extensions
    )


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
    output_string = re.sub(pattern, "</p>\n</div>", input_string, flags=re.DOTALL)
    return output_string
