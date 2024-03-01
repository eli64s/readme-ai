"""
Custom exceptions for the readme-ai package.
"""

from __future__ import annotations


class ReadmeAIError(Exception):
    """Base class for exceptions in this module."""

    ...


class CLIError(ReadmeAIError):
    """Exceptions related to the CLI."""

    def __init__(self, message, *args):
        super().__init__(f"Invalid option provided to CLI: {message}", *args)


class GitCloneError(ReadmeAIError):
    """Could not clone repository."""

    def __init__(self, repository: str, *args):
        self.repository = repository
        super().__init__(f"Failed to clone repository: {repository}", *args)


class GitValidationError(ReadmeAIError):
    """Could not validate repository."""

    def __init__(self, repository: str, *args):
        self.repository = repository
        super().__init__(f"Failed to validate repository: {repository}", *args)


class FileSystemError(ReadmeAIError):
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


class ReadmeGeneratorError(ReadmeAIError):
    """Exceptions related to readme generation."""

    def __init__(self, traceback, *args):
        self.traceback = traceback
        super().__init__(f"Error generating readme: {traceback}", *args)


class UnsupportedServiceError(ReadmeAIError):
    """Exceptions related to the LLMHandler class."""

    def __init__(self, message, *args):
        super().__init__(message, *args)
