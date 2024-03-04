"""
Pydantic validators for the CLI inputs and package settings.
"""

import re
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urlparse, urlsplit

from readmeai._exceptions import GitValidationError
from readmeai.core.logger import Logger
from readmeai.services.git import GitHost

_logger = Logger(__name__)


class GitValidator:
    """Validator class for GitSettings."""

    @classmethod
    def validate_repository(cls, value: Union[str, Path]) -> Union[str, Path]:
        """Validate the repository URL or path."""
        value_str = str(value)
        if (
            any(service.value in value_str for service in GitHost) is False
            and not Path(value_str).is_dir()
        ):
            raise GitValidationError(value)

        if isinstance(value, str):
            path = Path(value)
            if path.is_dir():
                return value
            try:
                parsed_url = urlparse(value)
                if parsed_url.scheme in ["http", "https"] and any(
                    service in parsed_url.netloc for service in GitHost
                ):
                    return value

            except Exception as exc:
                _logger.error(f"Error validating repository: {exc}")
                raise GitValidationError(value) from exc

        elif isinstance(value, Path) and value.is_dir():
            return value

        raise GitValidationError(value)

    @classmethod
    def validate_full_name(cls, value: Optional[str], values: dict) -> str:
        """Validator for getting the full name of the repository."""
        url_or_path = values.get("repository")

        path = (
            url_or_path if isinstance(url_or_path, Path) else Path(url_or_path)
        )
        if path.exists():
            return str(path.name)

        patterns = {
            GitHost.GITHUB: r"https?://github.com/([^/]+)/([^/]+)",
            GitHost.GITLAB: r"https?://gitlab.com/([^/]+)/([^/]+)",
            GitHost.BITBUCKET: r"https?://bitbucket.org/([^/]+)/([^/]+)",
        }

        for _, pattern in patterns.items():
            match = re.match(pattern, url_or_path)
            if match:
                user_name, repo_name = match.groups()
                return f"{user_name}/{repo_name}"

        raise GitValidationError(url_or_path)

    @classmethod
    def set_host_domain(cls, value: Optional[str], values: dict) -> str:
        """Sets the Git service host from the repository provided."""
        repo = values.get("repository")
        if isinstance(repo, Path) or (
            isinstance(repo, str) and Path(repo).is_dir()
        ):
            return GitHost.LOCAL

        parsed_url = urlparse(str(repo))
        for service in GitHost:
            if service in parsed_url.netloc:
                return service

        return GitHost.LOCAL

    @classmethod
    def set_host(cls, value: Optional[str], values: dict) -> str:
        """Set the host based on the repository URL."""
        repo = values.get("repository")
        if isinstance(repo, Path) or (
            isinstance(repo, str) and Path(repo).is_dir()
        ):
            return GitHost.LOCAL.value.lower()
        parsed_url = urlsplit(repo)
        return parsed_url.netloc.split(".")[0]

    @classmethod
    def set_name(cls, value: Optional[str], values: dict) -> str:
        """Sets the repository name from the repository provided."""
        repo = values.get("repository")
        if isinstance(repo, Path):
            return repo.name
        elif isinstance(repo, str):
            parsed_url = urlsplit(repo)
            name = parsed_url.path.split("/")[-1]
            return name.removesuffix(".git")
        return "n/a"
