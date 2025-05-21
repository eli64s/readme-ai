import enum
import functools
from pathlib import Path
from typing import Optional, Union

from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    field_validator,
    model_validator,
)
from readmeai.core.errors import GitURLError


class GitHost(enum.Enum):
    """
    Git repository hosting providers.
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
        self.domain = name
        self.api_url = api_url
        self.file_url_template = file_url_template


class GitURL(BaseModel):
    """
    Git repository URL model with validation and parsing methods.
    """

    url: HttpUrl
    host: Optional[GitHost] = Field(default=None)
    host_domain: str = Field(default="")
    name: str = Field(default="")
    full_name: str = Field(default="")

    model_config = {
        "frozen": True,
        "use_enum_values": True,
        "extra": "forbid",
        "arbitrary_types_allowed": True,
    }

    @classmethod
    @functools.lru_cache(maxsize=100)
    def create(cls, url: HttpUrl) -> "GitURL":
        """Create a GitURL object from a string URL."""
        return cls(url=url)

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: HttpUrl) -> HttpUrl:
        """Validates the Git repository URL."""
        try:
            parse_git_url(str(v))
        except ValueError as e:
            raise ValueError(f"Invalid Git repository URL: {v}") from e
        return v

    @model_validator(mode="after")
    def set_attributes(self) -> "GitURL":
        """Sets the Git URL attributes based on the URL."""
        try:
            host_domain, host, name, full_name = parse_git_url(str(self.url))
            object.__setattr__(self, "host_domain", host_domain)
            object.__setattr__(self, "name", name)
            object.__setattr__(self, "full_name", full_name)
            for git_host in GitHost:
                if git_host.name.lower() == host:
                    object.__setattr__(self, "host", git_host)
                    break
        except ValueError as e:
            raise ValueError(f"Failed to parse Git URL: {self.url}") from e
        return self

    def get_api_url(self) -> str:
        """Return the REST API endpoint URL for a git repository."""
        if self.host is None or self.host == GitHost.LOCAL:
            raise ValueError(
                f"Unsupported Git host or local repository: {self.url}",
            )
        if self.full_name:
            return f"{self.host.api_url}/{self.full_name}"
        else:
            raise ValueError("Repository full name is required.")

    def get_file_url(self, file_path: str) -> str:
        """Return the URL of the file in the remote repository."""
        if self.host:
            return self.host.file_url_template.format(
                full_name=self.full_name,
                file_path=file_path,
            )
        raise ValueError(f"Unsupported Git host: {self.url}")


def parse_git_url(url: Union[str, Path]) -> tuple[str, str, str, str]:
    """Parse repository URL and return host, full name, and project name."""
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

        assert parsed_url.host and parsed_url.path, (
            f"Invalid Git repository URL: {parsed_url}"
        )

        path_parts = parsed_url.path.strip("/").split("/")

        full_name = "/".join(path_parts[:2])

        host = parsed_url.host.split(".")[0].lower()

        host_domain = parsed_url.host

        name = path_parts[-1]

    return host_domain, host, name, full_name
