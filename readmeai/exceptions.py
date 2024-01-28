"""Custom exceptions class for the readme-ai application."""

from __future__ import annotations


class ReadmeAiException(Exception):
    """Base exception for the readme-ai application."""

    ...


class GitCloneError(ReadmeAiException):
    """Could not clone repository."""

    def __init__(self, repository: str, *args):
        self.repository = repository
        super().__init__(f"Failed to clone repository: {repository}", *args)


class GitValidationError(ReadmeAiException):
    """Could not validate repository."""

    def __init__(self, repository: str, *args):
        self.repository = repository
        super().__init__(
            f"Failed to validate the provided repository: {repository}", *args
        )


class ReadmeGeneratorError(ReadmeAiException):
    """Exceptions related to readme generation."""

    def __init__(self, traceback, *args):
        self.traceback = traceback
        super().__init__(f"Error generating readme: {traceback}", *args)


class FileSystemError(ReadmeAiException):
    """Exceptions related to file system operations."""

    def __init__(self, message, path, *args):
        self.file_path = path
        super().__init__(f"{message}: {path}", *args)


class FileReadError(FileSystemError):
    """Could not read file."""

    ...


class FileWriteError(FileSystemError):
    """Could not write file."""

    ...
