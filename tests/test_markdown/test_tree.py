"""Unit tests for the markdown tree generator."""

import pytest

from readmeai.markdown.tree import TreeGenerator


@pytest.fixture
def tree_gen(config_helper, tmp_path):
    """Fixture for the TreeGenerator class."""
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    (dir1 / "file1.txt").touch()
    (tmp_path / "dir2").mkdir()
    return TreeGenerator(
        conf_helper=config_helper,
        repo_name="TestProject",
        repo_url=tmp_path,
        root_dir=tmp_path,
        max_depth=3,
    )


def test_initialization(tree_gen):
    """Test initialization of the TreeGenerator class."""
    assert tree_gen.root_dir.is_dir()
    assert tree_gen.repo_name == "TestProject"
    assert tree_gen.max_depth == 3


def test_generate_tree(tree_gen, tmp_path):
    """Test the _generate_tree method."""
    tree = tree_gen._generate_tree(tmp_path)
    expected_tree = (
        f"└── {tmp_path.name}\n" "    ├── dir1\n" "    │   └── file1.txt"
    )
    assert tree == expected_tree


@pytest.mark.parametrize(
    "depth, expected_suffix",
    [
        (0, ""),
        (1, "\n    ├── dir1"),
    ],
)
def test_max_depth_param(tree_gen, depth, expected_suffix, tmp_path):
    """Test the _generate_tree method."""
    tree_gen.max_depth = depth
    tree = tree_gen._generate_tree(tmp_path)
    expected_tree = f"└── {tmp_path.name}{expected_suffix}"
    assert tree == expected_tree


def test_run_method(tree_gen):
    """Test the run method."""
    expected_tree = tree_gen.run()
    assert "TestProject" in expected_tree
    assert "dir1" in expected_tree
    assert "file1.txt" in expected_tree


def test_ignore_files(tree_gen, tmp_path):
    """Test that the tree generator ignores files."""
    (tmp_path / "dir1" / "__pycache__").mkdir()
    (tmp_path / "dir1" / "file.pyc").touch()
    tree = tree_gen._generate_tree(tmp_path)
    assert "__pycache__" not in tree
    assert "file.pyc" not in tree
