"""Unit tests for the markdown tree generator."""

import pytest

from readmeai.markdown.tree import TreeGenerator


@pytest.fixture
def tree_gen(tmp_path):
    """Fixture for the TreeGenerator class."""
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    (dir1 / "file1.txt").touch()
    (tmp_path / "dir2").mkdir()
    return TreeGenerator(
        repo_name="TestProject",
        root_dir=tmp_path,
        repo_url=tmp_path,
        max_depth=3,
    )


def test_initialization(tree_gen):
    """Test initialization of the TreeGenerator class."""
    assert tree_gen.root_dir.is_dir()
    assert tree_gen.repo_name == "TestProject"
    assert tree_gen.max_depth == 3


def test_build_tree(tree_gen, tmp_path):
    """Test the _build_tree method."""
    tree = tree_gen._build_tree(tmp_path)
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
    """Test the _build_tree method."""
    tree_gen.max_depth = depth
    tree = tree_gen._build_tree(tmp_path)
    expected_tree = f"└── {tmp_path.name}{expected_suffix}"
    assert tree == expected_tree


def test_tree_method(tree_gen):
    """Test the tree method."""
    expected_tree = tree_gen.tree()
    assert "TestProject" in expected_tree
    assert "dir1" in expected_tree
    assert "file1.txt" in expected_tree
