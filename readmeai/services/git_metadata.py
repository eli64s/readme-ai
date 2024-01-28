"""Git host providers helper methods to retrieve repository metadata."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

import aiohttp

from readmeai.core.logger import Logger
from readmeai.services.git_utils import fetch_git_api_url

logger = Logger(__name__)


@dataclass
class RepositoryMetadata:
    """Dataclass to store GitHub repository metadata."""

    name: str
    full_name: str
    owner: str
    owner_url: Optional[str]
    description: Optional[str]

    # Repository statistics
    stars_count: int
    forks_count: int
    watchers_count: int
    open_issues_count: int

    # Repository details
    default_branch: str
    created_at: str
    updated_at: str
    pushed_at: str
    size_kb: int

    # Repository URLs
    clone_url_http: str
    clone_url_ssh: str
    contributors_url: Optional[str]
    languages_url: str
    issues_url: Optional[str]

    # Programming languages and topics
    language: Optional[str]
    languages: List[str]
    topics: List[str]

    # Additional repository settings
    has_wiki: bool
    has_issues: bool
    has_projects: bool
    is_private: bool
    homepage_url: Optional[str]

    # License information
    license_name: Optional[str]
    license_url: Optional[str]


def _parse_repository_metadata(repo_data: dict) -> RepositoryMetadata:
    """Converts raw repository data from GitHub API into dataclass."""
    languages = repo_data.get("languages", {})
    license_info = repo_data.get("license", {}) or {}
    owner_info = repo_data.get("owner", {}) or {}

    return RepositoryMetadata(
        name=repo_data.get("name", ""),
        full_name=repo_data.get("full_name", ""),
        owner=owner_info.get("login", ""),
        owner_url=owner_info.get("html_url", ""),
        description=repo_data.get("description", ""),
        stars_count=repo_data.get("stargazers_count", 0),
        forks_count=repo_data.get("forks_count", 0),
        watchers_count=repo_data.get("watchers_count", 0),
        open_issues_count=repo_data.get("open_issues_count", 0),
        default_branch=repo_data.get("default_branch", ""),
        created_at=repo_data.get("created_at", ""),
        updated_at=repo_data.get("updated_at", ""),
        pushed_at=repo_data.get("pushed_at", ""),
        size_kb=repo_data.get("size", 0),
        clone_url_http=repo_data.get("clone_url", ""),
        clone_url_ssh=repo_data.get("ssh_url", ""),
        contributors_url=repo_data.get("contributors_url"),
        languages_url=repo_data.get("languages_url", ""),
        issues_url=repo_data.get("issues_url"),
        language=repo_data.get("language", ""),
        languages=list(languages.keys()) if languages else [],
        topics=repo_data.get("topics", []),
        has_wiki=repo_data.get("has_wiki", False),
        has_issues=repo_data.get("has_issues", False),
        has_projects=repo_data.get("has_projects", False),
        is_private=repo_data.get("private", False),
        homepage_url=repo_data.get("homepage", ""),
        license_name=license_info.get("name", ""),
        license_url=license_info.get("url", ""),
    )


async def _fetch_repository_metadata(
    session: aiohttp.ClientSession, url: str, **kwargs
) -> Dict[str, Any]:
    """Fetches repository metadata from the git host provider."""
    async with session.get(url, **kwargs) as response:
        response.raise_for_status()
        if response.status != 200:
            raise aiohttp.ClientResponseError(
                request_info=response.request_info,
                history=response.history,
                status=response.status,
            )
        return await response.json()


async def fetch_git_repository_metadata(
    session: aiohttp.ClientSession, repository: str
) -> Optional[RepositoryMetadata]:
    """Retrieves GitHub repository metadata and returns a dataclass."""
    api_url = await fetch_git_api_url(repository)
    if not api_url:
        return None

    try:
        metadata = await _fetch_repository_metadata(session, api_url)
        return _parse_repository_metadata(metadata) if metadata else None

    except aiohttp.ClientError as exc:
        logger.error(f"Client error while fetching repository metadata: {exc}")
        return None
