"""
Custom exceptions for the utilities package.
"""

from __future__ import annotations

from readmeai._exceptions import ReadmeAIError


class GitValidationError(ReadmeAIError):
    """
    Base class errors validating Git repositories.
    """

    ...


class GitCloneError(GitValidationError):
    """
    Raised when a Git repository cannot be cloned.
    """

    def __init__(self, repository: str, *args):
        self.repository = repository
        super().__init__(f"Failed to clone repository: {repository}", *args)


class GitURLError(GitValidationError):
    """
    Raised when an invalid Git repository URL is provided.
    """

    def __init__(self, url: str, *args):
        self.url = url
        super().__init__(f"Invalid Git repository URL: {url}", *args)


class UnsupportedGitHostError(GitValidationError):
    """
    Raised when an unsupported Git host is provided.
    """

    def __init__(self, host: str, *args):
        self.host = host
        super().__init__(f"Unsupported Git host: {host}", *args)
