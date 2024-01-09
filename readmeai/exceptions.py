"""Custom exceptions class for the readme-ai application."""

from __future__ import annotations


class ReadmeAiException(Exception):
    """Base exception for the readme-ai application."""

    pass


class RepositoryError(ReadmeAiException):
    """Exceptions related to repository operations."""

    pass


class GitCloneError(RepositoryError):
    """Could not clone repository."""

    def __init__(self, repository: str, *args):
        self.repository = repository
        super().__init__(f"Failed to clone repository: {repository}", *args)


class ReadmeGenerationError(ReadmeAiException):
    """Exceptions related to readme generation."""

    pass


class ApiCommunicationError(ReadmeAiException):
    """Exceptions related to external APIs."""

    pass


class FileSystemError(ReadmeAiException):
    """Exceptions related to file system operations."""

    def __init__(self, message, path, *args):
        self.file_path = path
        super().__init__(f"{message}: {path}", *args)


class FileReadError(FileSystemError):
    """Could not read file."""

    pass


class FileWriteError(FileSystemError):
    """Could not write file."""

    pass
