"""Git utility helper methods."""

import os
import re
from pathlib import Path

from readmeai.config.settings import GitFileUrl, GitHost


def get_remote_file_url(file_path: str, full_name: str, repo_url: str) -> str:
    """Returns the file URL for a given file based on the platform."""
    if Path(repo_url).exists():
        return GitFileUrl.LOCAL.value

    base_urls = {
        GitHost.GITHUB: GitFileUrl.GITHUB.value,
        GitHost.GITLAB: GitFileUrl.GITLAB.value,
        GitHost.BITBUCKET: GitFileUrl.BITBUCKET.value,
    }

    domain = repo_url.split("/")[2]
    url_template = base_urls.get(domain, GitFileUrl.GITHUB.value)

    return url_template.format(full_name=full_name, file_path=file_path)


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
            user, repo = match.groups()
            return user, repo

    raise ValueError("Error: invalid repository URL or path.")
