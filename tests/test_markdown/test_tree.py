"""Unit tests for the markdown tree generator."""

from pathlib import Path
from unittest.mock import Mock

import pytest

from readmeai.config.settings import ConfigHelper
from readmeai.markdown.tree import TreeGenerator


@pytest.fixture
def mock_config_helper():
    """Generates a mock ConfigHelper object."""
    mock_config_helper = Mock(ConfigHelper)
    mock_config_helper.ignore_files = {
        "files": ["*.pyc", "*.pyo"],
        "extensions": ["pyc", "pyo"],
        "directories": ["__pycache__", ".git"],
    }
    return mock_config_helper


@pytest.fixture
def tree_gen(mock_config_helper, tmp_path):
    """Generates a tree structure for a given directory."""
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "file1.txt").touch()
    (tmp_path / "dir2").mkdir()
    tree_gen = TreeGenerator(
        conf_helper=mock_config_helper,
        root_dir=tmp_path,
        repo_url="http://repo.url",
        repo_name="TestProject",
        max_depth=3,
    )
    return tree_gen


def test_initialization(mock_config_helper):
    """Tests the initialization of the TreeGenerator class."""
    tree_gen = TreeGenerator(
        conf_helper=mock_config_helper,
        root_dir=Path("/test/path"),
        repo_url="http://repo.url",
        repo_name="TestProject",
    )
    assert tree_gen.root_dir == Path("/test/path")
    assert tree_gen.repo_url == "http://repo.url"
    assert tree_gen.repo_name == "TestProject"
    assert tree_gen.max_depth == 3


def test_generate_tree(tree_gen, tmp_path):
    """Tests the _generate_tree method."""
    tree = tree_gen._generate_tree(tmp_path)
    expected_tree = """└── test_generate_tree0/
    ├── dir1/
    │   └── file1.txt
    └── dir2/\n"""
    assert tree == expected_tree


def test_format_tree(tree_gen, tmp_path):
    """Tests the _format_tree method."""
    tree = tree_gen._generate_tree(tmp_path)
    formatted_tree = tree_gen._format_tree(tree)
    expected_formatted_tree = """└── TestProject/
    ├── dir1/
    │   └── file1.txt
    └── dir2/\n"""
    assert formatted_tree == expected_formatted_tree


@pytest.mark.parametrize(
    "depth, expected",
    [
        (
            2,
            """└── TestProject/
    └── dir1/
        └── dir2/\n""",
        ),
        (
            5,
            """└── TestProject/
    └── dir1/
        └── dir2/
            └── dir3/
                └── dir4/\n""",
        ),
    ],
)
def test_max_depth(depth, expected, mock_config_helper, tmp_path):
    """Tests the max_depth parameter of the TreeGenerator class."""
    (tmp_path / "dir1").mkdir()
    (tmp_path / "dir1" / "dir2").mkdir()
    (tmp_path / "dir1" / "dir2" / "dir3").mkdir()
    (tmp_path / "dir1" / "dir2" / "dir3" / "dir4").mkdir()
    tree_gen = TreeGenerator(
        conf_helper=mock_config_helper,
        root_dir=tmp_path,
        repo_url="http://repo.url",
        repo_name="TestProject",
        max_depth=depth,
    )
    tree = tree_gen.run()
    assert tree == expected
