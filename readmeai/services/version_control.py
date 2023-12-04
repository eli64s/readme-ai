"""Version control service for retrieving repository metadata."""

import os
import platform
import re
import tempfile
from pathlib import Path
from typing import Optional

import git
import requests

from readmeai.config.settings import GitApiUrl, GitFileUrl, GitHost
from readmeai.core import logger

logger = logger.Logger(__name__)


def clone_repo_to_temp_dir(repo_path: str) -> Path:
    """Clone user repository to a temporary directory."""
    if Path(repo_path).exists():
        return Path(repo_path)

    temp_dir = tempfile.mkdtemp()
    try:
        git.Repo.clone_from(repo_path, temp_dir, depth=1, single_branch=True)

        return Path(temp_dir)

    except git.GitCommandError as excinfo:
        raise ValueError(f"Git clone error: {excinfo}") from excinfo

    except Exception as excinfo:
        raise ValueError(
            f"Error cloning git repository: {excinfo}"
        ) from excinfo


def make_request(url: str, **kwargs) -> dict:
    """Makes an HTTP request for the given remote repository provider."""
    try:
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        if response.status_code == 204:
            return {}
        elif response.status_code == 200:
            return response.json()
        else:
            raise ValueError(
                f"Error retrieving repository metadata: {response.status_code}"
            )
    except requests.RequestException as excinfo:
        raise ValueError(
            f"Error retrieving repository metadata: {excinfo}"
        ) from excinfo


def get_github_repo_metadata(repo_url: str) -> dict:
    """Retrieves metadata about a GitHub repository."""
    api_url = parse_repo_url(repo_url, GitHost.GITHUB.value)
    repo_metadata = make_request(api_url)
    return repo_metadata


def get_gitlab_repo_metadata(repo_url):
    """Retrieves metadata about a GitLab repository."""
    api_url = parse_repo_url(repo_url, GitHost.GITLAB.value)
    repo_metadata = make_request(api_url)
    return repo_metadata


def get_bitbucket_repo_metadata(repo_url: str) -> dict:
    """Retrieves metadata about a Bitbucket repository."""
    api_url = parse_repo_url(repo_url, GitHost.BITBUCKET.value)
    repo_metadata = make_request(api_url)
    return repo_metadata


def get_remote_full_name(url_or_path):
    """Extract user and repository name from a URL or path."""
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

    raise ValueError("Error: invalid repository URL or path.")


def get_remote_repo_url(file_name: str, repo: str, repo_name: str) -> str:
    """Returns the file URL for a given file based on the platform."""
    if Path(repo).exists():
        return GitFileUrl.LOCAL.value

    base_urls = {
        GitHost.GITHUB: GitFileUrl.GITHUB.value,
        GitHost.GITLAB: GitFileUrl.GITLAB.value,
        GitHost.BITBUCKET: GitFileUrl.BITBUCKET.value,
    }

    domain = repo.split("/")[2]

    url_template = base_urls.get(domain, GitFileUrl.GITHUB.value)

    return url_template.format(repo_name=repo_name, file_name=file_name)


def parse_repo_url(repo_url: str, provider: str) -> str:
    """Parses the repository URL and constructs the API URL."""
    parts = repo_url.rstrip("/").split("/")

    repo_name = f"{parts[-2]}/{parts[-1]}"

    api_url_mapping = {
        GitHost.GITHUB.value: f"{GitApiUrl.GITHUB.value}/repos/{repo_name}",
        GitHost.GITLAB.value: f"{GitApiUrl.GITLAB.value}/v4/projects/{repo_name.replace('/', '%2F')}",
        GitHost.BITBUCKET.value: f"{GitApiUrl.BITBUCKET.value}/2.0/repositories/{repo_name}",
    }

    return api_url_mapping.get(provider.lower())


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


def validate_file_permissions(temp_dir: Path) -> None:
    """Validates file permissions of the cloned repository."""
    if platform.system() != "Windows":
        if isinstance(temp_dir, str):
            temp_dir = Path(temp_dir)
        permissions = temp_dir.stat().st_mode & 0o777
        if permissions != 0o700:
            raise ValueError(
                "Error: file permissions of cloned repo must be set to 0o700."
            )


def validate_git_executable(git_exec_path: Optional[str]) -> None:
    """Validate the path to the git executable."""
    if not git_exec_path or not Path(git_exec_path).exists():
        raise ValueError(f"Git executable not found at {git_exec_path}")
