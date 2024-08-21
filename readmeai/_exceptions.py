"""
Custom exceptions classes for the readme-ai package.
"""

from __future__ import annotations


class ReadmeAIError(Exception):
    """
    Base class for exceptions in this module.
    """

    ...


class ReadmeGeneratorError(Exception):
    """
    Raised when an error occurs during README generation.
    """

    def __init__(self, exc, traceback):
        self.exc = exc
        self.traceback = traceback
        super().__init__(f"README generation error occurred: {exc}")


# ----------------- CLI ----------------------------------


class CLIError(ReadmeAIError):
    """Exceptions related to the CLI."""

    def __init__(self, message, *args):
        super().__init__(f"Invalid option provided to CLI: {message}", *args)


# ----------------- File System ----------------------------------


class FileSystemError(ReadmeAIError):
    """
    Exceptions related to file system operations.
    """

    def __init__(self, message, path, *args):
        self.file_path = path
        super().__init__(f"{message}: {path}", *args)


class FileReadError(FileSystemError):
    """
    Raised when a file cannot be read.
    """

    ...


class FileWriteError(FileSystemError):
    """
    Raised when a file cannot be written to.
    """

    ...


# ----------------- LLM API ----------------------------------


class UnsupportedServiceError(ReadmeAIError):
    """
    Raised when an unsupported LLM service is provided.
    """

    def __init__(self, message, *args):
        super().__init__(message, *args)
