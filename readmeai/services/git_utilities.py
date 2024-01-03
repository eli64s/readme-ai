"""Git service utilities to retrieve repository metadata."""

import os
import re
from pathlib import Path
from typing import Tuple

from readmeai.config.settings import GitService
from readmeai.core.logger import Logger

logger = Logger(__name__)


def get_remote_file_url(file_path: str, full_name: str, repo_url: str) -> str:
    """Returns the URL of the file in the remote repository."""
    if Path(repo_url).exists():
        return GitService.LOCAL.file_url.format(file_path=file_path)

    for service in GitService:
        if service.host in repo_url:
            return service.file_url.format(
                full_name=full_name, file_path=file_path
            )

    raise ValueError("Unsupported Git service for URL generation.")


def get_remote_full_name(url_or_path) -> Tuple[str, str]:
    """Returns the full name of the repository."""
    if os.path.exists(url_or_path):
        return "local", os.path.basename(url_or_path)

    patterns = {
        GitService.GITHUB.host: r"https?://github.com/([^/]+)/([^/]+)",
        GitService.GITLAB.host: r"https?://gitlab.com/([^/]+)/([^/]+)",
        GitService.BITBUCKET.host: r"https?://bitbucket.org/([^/]+)/([^/]+)",
    }

    for host, pattern in patterns.items():
        match = re.match(pattern, url_or_path)
        if match:
            username, repo_name = match.groups()
            return username, repo_name

    raise ValueError("Error: invalid repository URL or path.")


async def parse_repo_url(repo_url: str) -> str:
    """Parses the repository URL and returns the API URL."""
    try:
        parts = repo_url.rstrip("/").split("/")
        repo_name = f"{parts[-2]}/{parts[-1]}"

        for service in GitService:
            if service.host in repo_url:
                api_url = f"{service.api_url}{repo_name}"
                logger.info(f"{service.name.upper()} API URL: {api_url}")
                return api_url

        raise ValueError("Unsupported Git service.")

    except (IndexError, ValueError) as exc_info:
        raise ValueError(f"Invalid repository URL: {repo_url}") from exc_info
