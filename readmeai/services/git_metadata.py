"""Git provider API helper methods."""

import requests

from readmeai.config.settings import GitApiUrl, GitHost


def github_repo_metadata(repo_url: str) -> dict:
    """Retrieves metadata about a GitHub repository."""
    return repo_metadata(repo_url, GitHost.GITHUB)


def gitlab_repo_metadata(repo_url: str) -> dict:
    """Retrieves metadata about a GitLab repository."""
    return repo_metadata(repo_url, GitHost.GITLAB)


def bitbucket_repo_metadata(repo_url: str) -> dict:
    """Retrieves metadata about a Bitbucket repository."""
    return repo_metadata(repo_url, GitHost.BITBUCKET)


def fetch_api_data(url: str, **kwargs) -> dict:
    """Makes an HTTP request to the API endpoint."""
    try:
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        if response.status_code == 204:
            return {}
        elif response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f"API error: {response.status_code}")
    except requests.RequestException as error:
        raise ValueError(f"API request failed: {error}") from error


def parse_repo_url(repo_url: str, provider: str) -> str:
    """Parses the repository URL and returns the API URL."""
    parts = repo_url.rstrip("/").split("/")
    repo_name = f"{parts[-2]}/{parts[-1]}"
    if provider == GitHost.GITHUB:
        return f"{GitApiUrl.GITHUB.value}{repo_name}"
    elif provider == GitHost.GITLAB:
        return f"{GitApiUrl.GITLAB.value}{repo_name.replace('/', '%2F')}"
    elif provider == GitHost.BITBUCKET:
        return f"{GitApiUrl.BITBUCKET.value}{repo_name}"
    else:
        raise ValueError(f"Unsupported provider: {provider}")


def repo_metadata(repo_url: str) -> dict:
    """Retrieves repository metadata for the given provider."""
    provider = GitHost.from_url(repo_url)
    api_url = parse_repo_url(repo_url, provider)
    if not api_url:
        raise ValueError("Failed to construct API URL.")
    return fetch_api_data(api_url)
