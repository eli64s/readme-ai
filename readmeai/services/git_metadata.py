"""Git host providers helper methods to retrieve repository metadata."""

import requests

from readmeai.config.settings import GitService


def fetch_git_api(url: str, **kwargs) -> dict:
    """Makes an HTTP request to the API endpoint."""
    try:
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        return response.json() if response.status_code == 200 else {}
    except requests.RequestException as exc_info:
        raise ValueError(f"API request failed: {exc_info}") from exc_info


def parse_repo_url(repo_url: str) -> str:
    """Parses the repository URL and returns the API URL."""
    try:
        parts = repo_url.rstrip("/").split("/")
        repo_name = f"{parts[-2]}/{parts[-1]}"
        for service in GitService:
            if service.host in repo_url:
                api_url = service.api_url + repo_name
                return api_url
        raise ValueError("Unsupported Git service.")
    except (IndexError, ValueError) as exc_info:
        raise ValueError(f"Invalid repository URL: {repo_url}") from exc_info


def repo_metadata(repo_url: str) -> dict:
    """Retrieves repository metadata for the given provider."""
    api_url = parse_repo_url(repo_url)
    if not api_url:
        raise ValueError("Failed to construct API URL.")
    return fetch_git_api(api_url)
