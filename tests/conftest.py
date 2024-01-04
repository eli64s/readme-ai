"""Pytest configuration file."""

import pytest

from readmeai.config.settings import (
    AppConfigModel,
    load_config,
    load_config_helper,
)


@pytest.fixture(scope="session")
def config():
    """Returns the default configuration."""
    return load_config()


@pytest.fixture(scope="session")
def config_helper(config):
    """Returns the default configuration helper."""
    conf_model = AppConfigModel(app=config)
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
def mock_temp_dir(tmp_path_factory):
    """Returns a temporary directory for the test session."""
    return tmp_path_factory.mktemp("test_readmeai_temp_dir")
