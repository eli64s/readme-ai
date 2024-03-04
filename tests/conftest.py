"""
Pytest fixtures for reuse across the test suite.
"""

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

from readmeai.config.settings import ConfigLoader
from readmeai.core.preprocess import FileContext, RepositoryProcessor
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.utils.file_handler import FileHandler

if sys.version_info < (3, 11):
    import toml
else:
    import tomllib as toml


# General fixtures
@pytest.fixture
def temp_dir(tmpdir):
    """Create a temporary directory."""
    return tmpdir


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


# Model handler fixtures
@pytest.fixture
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
def openai_handler(mock_configs):
    """Fixture for OpenAIHandler class."""
    mock_configs.config.llm.api = "OPENAI"
    mock_configs.config.llm.model = "gpt-3.5-turbo"
    return OpenAIHandler(mock_configs)


@pytest.fixture
def offline_handler(mock_configs):
    """Fixture for OpenAIHandler class."""
    with patch.dict("os.environ", {}, clear=True):
        mock_configs.config.llm.api = "OFFLINE"
        mock_configs.config.llm.model = "offline"
        yield OfflineHandler(mock_configs)


@pytest.fixture
def gemini_handler(mock_configs):
    """Fixture for OpenAIHandler class."""
    with patch.dict(
        "os.environ",
        {
            "GOOGLE_API_KEY": "sk-test-key",
        },
    ):
        mock_configs.config.llm.api = "GEMINI"
        mock_configs.config.llm.model = "gemini-pro"
        yield GeminiHandler(mock_configs)


# File handler fixtures
@pytest.fixture
def file_handler():
    """Return a FileHandler instance."""
    return FileHandler()


@pytest.fixture
def mock_json_file_path():
    """Return a mock file path."""
    return Path("mock/path/file.json")


@pytest.fixture
def mock_json_data():
    """Return a JSON string."""
    return json.dumps({"key": "value"})


@pytest.fixture
def mock_toml_file_path():
    """Return a mock file path for a TOML file."""
    return Path("mock/path/file.toml")


@pytest.fixture
def mock_toml_data():
    """Return a TOML string."""
    return toml.dumps({"key": "value"})


# Repository preprocessor fixtures
@pytest.fixture(scope="session")
def repo_processor(mock_configs):
    """Fixture for RepositoryProcessor class."""
    return RepositoryProcessor(mock_configs)


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
def mock_file_data():
    """Returns the default file data."""
    return [
        FileContext(
            file_path="path/to/file1.py",
            file_name="file1.py",
            content="",
            file_ext="py",
            dependencies=["dependency1"],
        ),
        FileContext(
            file_path="path/to/file2.js",
            file_name="file2.js",
            content="",
            file_ext="js",
            dependencies=["dependency2"],
        ),
        FileContext(
            file_path="path/to/file3.txt",
            file_name="file3.txt",
            content="",
            file_ext="txt",
            dependencies=[],
        ),
    ]
