"""Pytest configuration settings."""

import asyncio
from unittest.mock import MagicMock

import pytest

from readmeai.config.settings import (
    AppConfigModel,
    load_config,
    load_config_helper,
)
from readmeai.core.preprocess import FileContext, RepoProcessor


@pytest.fixture(scope="session")
def mock_config():
    """Returns the default configuration."""
    return load_config()


@pytest.fixture(scope="session")
def mock_config_helper(mock_config):
    """Returns the default configuration helper."""
    conf_model = AppConfigModel(app=mock_config)
    return load_config_helper(conf_model)


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
        tokens=10,
        dependencies=mock_dependencies,
    )


@pytest.fixture(scope="session")
def repo_processor(mock_config, mock_config_helper):
    """Fixture for RepoProcessor class."""
    return RepoProcessor(mock_config, mock_config_helper)


@pytest.fixture
def mock_http_client():
    return MagicMock()


@pytest.fixture
def rate_limit_semaphore():
    semaphore = asyncio.Semaphore(5)
    asyncio.set_event_loop(asyncio.new_event_loop())
    return semaphore


@pytest.fixture
def prompts_instances():
    return {}


@pytest.fixture
def openai_handler_config():
    return MagicMock()


@pytest.fixture
def vertexai_handler_config():
    return MagicMock()


@pytest.fixture
def openai_response():
    return {
        "summaries_response": "test_summaries",
        "features_response": "test_features",
        "overview_response": "test_overview",
        "slogan_response": "test_slogan",
    }


@pytest.fixture
def vertex_response():
    return {
        "summaries_response": "test_summaries",
        "features_response": "test_features",
        "overview_response": "test_overview",
        "slogan_response": "test_slogan",
    }
