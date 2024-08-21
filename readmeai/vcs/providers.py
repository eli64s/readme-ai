from enum import Enum
from pathlib import Path

from pydantic import HttpUrl

from .errors import GitURLError


class GitHost(Enum):
    """
    Enum for supported Git repository hosting services.
    """

    GITHUB = (
        "github.com",
        "https://api.github.com/repos/",
        "https://github.com/{full_name}/blob/main/{file_path}",
    )
    GITLAB = (
        "gitlab.com",
        "https://gitlab.com/api/v4/projects/",
        "https://gitlab.com/{full_name}/-/blob/main/{file_path}",
    )
    BITBUCKET = (
        "bitbucket.org",
        "https://api.bitbucket.org/2.0/repositories/",
        "https://bitbucket.org/{full_name}/src/master/{file_path}",
    )
    LOCAL = ("local", "", "{file_path}")

    def __init__(self, name: str, api_url: str, file_url_template: str):
        """
        Initialize git host domain, REST API URL, and file URL template.
        """
        self.domain = name
        self.api_url = api_url
        self.file_url_template = file_url_template


def parse_git_url(url: str | Path) -> tuple[str, str, str, str]:
    """
    Parse Git repository URL and return host, full name, and project name.
    """
    if isinstance(url, Path) or (isinstance(url, str) and Path(url).is_dir()):
        host_domain = host = GitHost.LOCAL.name
        name = Path(url).name
        full_name = f"{Path(url).parent.name}/{name}"
    else:
        try:
            parsed_url = HttpUrl(url)
            if parsed_url.scheme not in ["http", "https"]:
                raise GitURLError(
                    url,
                    f"Uknown scheme provided: {parsed_url.scheme}",
                )
        except ValueError as e:
            raise GitURLError(url) from e

        assert (
            parsed_url.host and parsed_url.path
        ), f"Invalid Git repository URL: {parsed_url}"
        path_parts = parsed_url.path.strip("/").split("/")
        host_domain = parsed_url.host
        host = parsed_url.host.split(".")[0].lower()
        name = path_parts[-1]
        full_name = "/".join(path_parts[:2])

    return host_domain, host, name, full_name


def get_file_url(host: GitHost, full_name: str, file_path: str) -> str:
    """
    Return the URL of the file in the remote repository.
    """
    return host.file_url_template.format(
        full_name=full_name,
        file_path=file_path,
    )
