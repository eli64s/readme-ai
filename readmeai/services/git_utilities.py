"""Git service utilities to retrieve repository metadata."""

from pathlib import Path

from readmeai.config.settings import GitService
from readmeai.core.logger import Logger

logger = Logger(__name__)


def get_remote_file_url(file_path: str, full_name: str, repo_url: str) -> str:
    """Returns the URL of the file in the remote repository."""
    if Path(repo_url).exists():
        return GitService.LOCAL.file_url_template.format(file_path=file_path)

    for service in GitService:
        if service in repo_url:
            return service.file_url_template.format(
                full_name=full_name, file_path=file_path
            )

    return file_path


async def parse_repo_url(repo_url: str) -> str:
    """Parses the repository URL and returns the API URL."""
    try:
        parts = repo_url.rstrip("/").split("/")
        repo_name = f"{parts[-2]}/{parts[-1]}"
        for service in GitService:
            if service in repo_url:
                api_url = f"{service.api_url}{repo_name}"
                logger.info(f"{service.name.upper()} API URL: {api_url}")
                return api_url

        raise ValueError("Unsupported Git service.")

    except (IndexError, ValueError) as exc_info:
        raise ValueError(f"Invalid repository URL: {repo_url}") from exc_info
