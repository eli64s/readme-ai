"""Utility methods for the readme-ai application."""

import os
import platform
import re
import tempfile
from pathlib import Path
from typing import Optional

import git

from readmeai.core import logger

logger = logger.Logger(__name__)


def clone_repo_to_temp_dir(repo_path: str) -> Path:
    """Clone a repository to a temporary directory and remove the .git directory."""
    # git_exec_path = find_git_executable()
    # validate_git_executable(git_exec_path)
    # env = os.environ.copy()
    # env["GIT_PYTHON_GIT_EXECUTABLE"] = str(git_exec_path)

    temp_dir = tempfile.mkdtemp()
    try:
        git.Repo.clone_from(repo_path, temp_dir, depth=1)
        # git_dir = Path(temp_dir) / ".git"
        # if git_dir.exists():
        #    shutil.rmtree(git_dir)
        return Path(temp_dir)

    except git.GitCommandError as excinfo:
        raise ValueError(f"Git clone error: {excinfo}") from excinfo

    except Exception as excinfo:
        raise ValueError(
            f"Error cloning git repository: {excinfo}"
        ) from excinfo


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


def get_github_file_link(file: str, repo: str, user_repo_name: str) -> str:
    """Returns the file URL for a given file based on the platform."""
    base_urls = {
        "github.com": f"https://github.com/{user_repo_name}/blob/main/{file}",
        "bitbucket.org": f"https://bitbucket.org/{user_repo_name}/src/master/{file}",
        "gitlab.com": f"https://gitlab.com/{user_repo_name}/-/blob/master/{file}",
    }

    for domain in base_urls:
        if domain in repo:
            return base_urls[domain]

    return base_urls["github.com"]


def get_user_repository_name(url_or_path):
    """
    Extract username and repository name from a
    GitHub, Bitbucket, or GitLab URL or local path.
    """

    if os.path.exists(url_or_path):
        return "local", os.path.basename(url_or_path)

    patterns = {
        "github": r"https?://github.com/([^/]+)/([^/]+)",
        "bitbucket": r"https?://bitbucket.org/([^/]+)/([^/]+)",
        "gitlab": r"https?://gitlab.com/([^/]+)/([^/]+)",
    }

    for _, pattern in patterns.items():
        match = re.match(pattern, url_or_path)
        if match:
            username, reponame = match.groups()
            return username, reponame

    raise ValueError("Error: invalid remote repository URL or local path.")
