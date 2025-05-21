from pathlib import Path
from typing import Literal

import pytest
from readmeai.generators.tree import TreeGenerator


@pytest.fixture
def tree_gen(tmp_path: Path):
    """Fixture to create a TreeGenerator instance."""
    dir1 = tmp_path / "dir1"
    dir1.mkdir()
    (dir1 / "file1.txt").touch()
    (tmp_path / "dir2").mkdir()
    return TreeGenerator(
        repo_name=tmp_path.name,
        root_dir=tmp_path,
        repo_url=Path(tmp_path).as_uri(),
        max_depth=3,
    )


def test_initialization(tmp_path: Path, tree_gen: TreeGenerator):
    assert tree_gen.root_dir.is_dir()
    assert tree_gen.repo_name == tmp_path.name
    assert tree_gen.max_depth == 3


def test_generate(tmp_path: Path, tree_gen: TreeGenerator):
    tree = tree_gen.generate(tmp_path)
    expected_tree = f"└── {tmp_path.name}/\n    ├── dir1\n    │   └── file1.txt"
    assert tree == expected_tree


@pytest.mark.parametrize(
    "depth, expected_suffix",
    [
        (0, ""),
        (1, "\n    ├── dir1"),
    ],
)
def test_max_depth_param(
    tree_gen: TreeGenerator,
    depth: Literal[0] | Literal[1],
    expected_suffix: Literal[""] | Literal["\n    ├── dir1"],
    tmp_path: Path,
):
    tree_gen.max_depth = depth
    tree = tree_gen.generate(tmp_path)
    expected_tree = f"└── {tmp_path.name}/{expected_suffix}"
    assert tree == expected_tree


def test_tree_method(tmp_path: Path, tree_gen: TreeGenerator):
    expected_tree = tree_gen.generate(directory=tree_gen.root_dir)
    assert tmp_path.name in expected_tree
    assert "dir1" in expected_tree
    assert "file1.txt" in expected_tree


def test_format_tree_simple():
    tree_gen = TreeGenerator("repo", Path("/root/dir"), "https://repo.url", 3)
    parts = ["repo", "├── file1.py", "└── file2.py"]
    result = tree_gen._format_tree(parts)
    assert result == "repo\n├── file1.py\n└── file2.py"


def test_format_tree_nested(tmp_path: Path, tree_gen: TreeGenerator):
    parts = [
        tmp_path.name,
        "├── dir1",
        "│   └── file1.txt",
        "└── dir2",
    ]
    result = tree_gen._format_tree(parts)
    assert result == (f"{tmp_path.name}/\n├── dir1\n│   └── file1.txt\n└── dir2")


def test_format_tree_empty():
    tree_gen = TreeGenerator("repo", Path("/root/dir"), "https://repo.url", 3)
    parts = []
    result = tree_gen._format_tree(parts)
    assert result == ""
