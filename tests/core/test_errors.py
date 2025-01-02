from readmeai.core.errors import (
    FileReadError,
    FileSystemError,
    FileWriteError,
    ReadmeAIError,
    ReadmeGeneratorError,
    UnsupportedServiceError,
)


def test_readme_ai_exception():
    """Test the ReadmeAIError class."""
    ex = ReadmeAIError("General error")
    assert isinstance(ex, Exception)


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
    ex = ReadmeGeneratorError("Error", "Traceback")
    assert isinstance(ex, Exception)


def test_unsupported_file_type_exception():
    """Test the UnsupportedFileTypeException class."""
    ex = UnsupportedServiceError("openai_sam_altman")
    assert isinstance(ex, ReadmeAIError)
