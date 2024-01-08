"""Tests for the custom exceptions module."""

from readmeai.exceptions import (
    ApiCommunicationError,
    FileReadError,
    FileSystemError,
    FileWriteError,
    ReadmeAiException,
    ReadmeGenerationError,
    RepositoryCloneError,
)


def test_readme_ai_exception():
    """Test the ReadmeAIException class."""
    ex = ReadmeAiException("General error")
    assert str(ex) == "General error"


def test_repository_clone_exception():
    """Test the RepositoryCloneException class."""
    ex = RepositoryCloneError("https://example.com/repo", ValueError())
    assert "Failed to clone repository" in str(ex)


def test_readme_generation_exception():
    """Test the ReadmeGenerationException class."""
    ex = ReadmeGenerationError("Error during README generation")
    assert str(ex) == "Error during README generation"


def test_api_communication_exception():
    """Test the APICommunicationException class."""
    ex = ApiCommunicationError("API communication error")
    assert str(ex) == "API communication error"


def test_read_file_exception():
    """Test the ReadFileException class."""
    ex = FileReadError("/path/to/file", FileNotFoundError())
    assert isinstance(ex, FileSystemError)


def test_write_file_exception():
    """Test the WriteFileException class."""
    ex = FileWriteError("/path/to/file", FileNotFoundError())
    assert isinstance(ex, FileSystemError)
