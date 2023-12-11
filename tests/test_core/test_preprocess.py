"""Unit tests for preprocess module."""

import pytest

from readmeai.core.preprocess import RepositoryParser


@pytest.fixture
def parser(config, config_helper):
    """Fixture for RepositoryParser."""
    return RepositoryParser(config, config_helper)


def test_analyze(parser):
    """Test analyze method."""
    temp_dir = "/path/to/temp/dir"
    result = parser.analyze(temp_dir)
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)


def test_generate_contents(parser):
    """Test generate_contents method."""
    repo_path = "/path/to/repo"
    result = parser.generate_contents(repo_path)
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)


def test_get_dependency_file_contents(parser):
    """Test get_dependency_file_contents method."""
    contents = [
        {
            "name": "requirements.txt",
            "path": "/path/to/requirements.txt",
            "content": "requests==2.25.1\n",
            "extension": "txt",
        },
        {
            "name": "setup.py",
            "path": "/path/to/setup.py",
            "content": "import setuptools\n",
            "extension": "py",
        },
    ]
    result = parser.get_dependency_file_contents(contents)
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)
