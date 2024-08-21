import functools

from pydantic import (
    BaseModel,
    Field,
    HttpUrl,
    field_validator,
    model_validator,
)

from .providers import GitHost, get_file_url, parse_git_url


class GitURL(BaseModel):
    """
    Git repository URL model with validation and parsing methods.
    """

    url: HttpUrl
    host: GitHost | None = Field(default=None)
    host_domain: str = Field(default="")
    name: str = Field(default="")
    full_name: str = Field(default="")

    model_config = {
        "frozen": True,
        "use_enum_values": True,
        "extra": "forbid",
        "arbitrary_types_allowed": True,
    }

    @field_validator("url")
    @classmethod
    def validate_url(cls, v: HttpUrl) -> HttpUrl:
        """
        Validates the Git repository URL.
        """
        try:
            parse_git_url(str(v))
        except ValueError as e:
            raise ValueError(f"Invalid Git repository URL: {v}") from e
        return v

    @model_validator(mode="after")
    def set_attributes(self) -> "GitURL":
        """
        Sets the Git URL attributes based on the URL.
        """
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

    @classmethod
    @functools.lru_cache(maxsize=100)
    def create(cls, url: HttpUrl) -> "GitURL":
        """
        Create a GitURL object from a string URL.
        """
        return cls(url=url)

    def get_api_url(self) -> str:
        """
        Return the REST API endpoint URL for a git repository.
        """
        # Ensure self.host is not None and self.host is not GitHost.LOCAL
        if self.host is not None and self.host != GitHost.LOCAL:
            # Ensure self.full_name is not None or empty
            if self.full_name:
                return f"{self.host.api_url}/{self.full_name}"
            else:
                raise ValueError("Repository full name is required.")
        else:
            raise ValueError(
                f"Unsupported Git host or local repository: {self.url}",
            )

    def get_file_url(self, file_path: str) -> str:
        """
        Return the URL of the file in the remote repository.
        """
        if self.host:
            return get_file_url(self.host, self.full_name, file_path)
        raise ValueError(f"Unsupported Git host: {self.url}")
