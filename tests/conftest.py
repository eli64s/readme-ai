"""Pytest configuration settings."""

from unittest.mock import patch

import pytest

from readmeai.config.settings import ConfigLoader
from readmeai.core.preprocess import FileContext, RepositoryProcessor
from readmeai.models.openai import OpenAIHandler


@pytest.fixture(scope="session")
def mock_config():
    """Returns the default configuration."""
    config_loader = ConfigLoader()
    return config_loader.config


@pytest.fixture(scope="session")
def mock_configs(mock_config):
    """Returns the default configuration helper."""
    config_loader = ConfigLoader()
    return config_loader


@pytest.fixture
def handler(mock_config, mock_configs):
    """Fixture for OpenAIHandler class."""
    with patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}):
        yield OpenAIHandler(mock_config, mock_configs)


@pytest.fixture(scope="session")
def mock_dependencies():
    """Returns the default dependencies."""
    return ["python", "pytest", "pytest-cov", "black", "flake8", "mypy"]


@pytest.fixture(scope="session")
def mock_summaries():
    """Returns the default summaries."""
    return [
        ("/path/to/file1.py", "This is summary for file1.py"),
        ("/path/to/file2.py", "This is summary for file2.py"),
        (".github/workflows/ci.yml", "This is summary for ci.yml"),
    ]


@pytest.fixture(scope="session")
def mock_file_data(mock_dependencies):
    """Returns the default file data."""
    return FileContext(
        file_path="/path/to/file1.py",
        file_name="file1.py",
        file_ext="py",
        content="This is content of file1.py",
        dependencies=mock_dependencies,
    )


@pytest.fixture(scope="session")
def repo_processor(mock_configs):
    """Fixture for RepositoryProcessor class."""
    return RepositoryProcessor(mock_configs)
