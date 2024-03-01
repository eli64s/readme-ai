"""
Tests for the custom exceptions module.
"""

from readmeai._exceptions import (
    FileReadError,
    FileSystemError,
    FileWriteError,
    GitCloneError,
    GitValidationError,
    ReadmeAIError,
    ReadmeGeneratorError,
    UnsupportedServiceError,
)


def test_readme_ai_exception():
    """Test the ReadmeAIError class."""
    ex = ReadmeAIError("General error")
    assert isinstance(ex, Exception)


def test_git_clone_exception():
    """Test the RepositoryCloneException class."""
    ex = GitCloneError("https://example.com/repo", "Traceback")
    assert isinstance(ex, ReadmeAIError)


def test_git_validation_exception():
    """Test the GitValidatorException class."""
    ex = GitValidationError("repository", "Traceback")
    assert isinstance(ex, ReadmeAIError)


def test_read_file_exception():
    """Test the ReadFileException class."""
    ex = FileReadError("/path/to/file", FileNotFoundError())
    assert isinstance(ex, FileSystemError)


def test_write_file_exception():
    """Test the WriteFileException class."""
    ex = FileWriteError("/path/to/file", FileNotFoundError())
    assert isinstance(ex, FileSystemError)


def test_readme_generation_exception():
    """Test the ReadmeGenerationException class."""
    ex = ReadmeGeneratorError("Traceback")
    assert isinstance(ex, ReadmeAIError)


def test_unsupported_file_type_exception():
    """Test the UnsupportedFileTypeException class."""
    ex = UnsupportedServiceError("openai_sam_altman")
    assert isinstance(ex, ReadmeAIError)
