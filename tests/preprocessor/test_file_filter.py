from pathlib import Path
from typing import Any

import pytest

from readmeai.preprocessor.file_filter import is_excluded


@pytest.fixture
def repo_path() -> Path:
    return Path("/home/user/project")


@pytest.fixture
def ignore_list() -> dict[str, Any]:
    return {
        "directories": ["node_modules", ".git"],
        "extensions": ["pyc", "tmp"],
        "files": [".DS_Store", "Thumbs.db"],
    }


@pytest.mark.parametrize(
    "file_path,expected",
    [
        (Path("/home/user/project/src/main.py"), False),
        (Path("/home/user/project/node_modules/package.json"), True),
        (Path("/home/user/project/.git/config"), True),
        (Path("/home/user/project/build/output.pyc"), True),
        (Path("/home/user/project/temp.tmp"), True),
        (Path("/home/user/project/.DS_Store"), True),
        (Path("/home/user/project/docs/Thumbs.db"), True),
        (Path("/home/user/project/src/utils.py"), False),
    ],
)
def test_is_excluded(
    file_path: Path,
    expected: bool,
    repo_path: Path,
    ignore_list: dict[str, Any],
) -> None:
    assert is_excluded(ignore_list, file_path, repo_path) == expected


def test_is_excluded_empty_ignore_list(repo_path: Path):
    empty_ignore_list = {"directories": [], "extensions": [], "files": []}
    file_path = Path("/home/user/project/src/main.py")
    assert not is_excluded(empty_ignore_list, file_path, repo_path)


def test_is_excluded_no_match(repo_path: Path, ignore_list: dict[str, Any]):
    file_path = Path("/home/user/project/src/app.js")
    assert not is_excluded(ignore_list, file_path, repo_path)


def test_is_excluded_case_sensitivity(
    repo_path: Path, ignore_list: dict[str, Any]
):
    file_path = Path("/home/user/project/.GIT/config")
    assert not is_excluded(ignore_list, file_path, repo_path)


def test_is_excluded_nested_directory(
    repo_path: Path, ignore_list: dict[str, Any]
):
    file_path = Path("/home/user/project/src/node_modules/package.json")
    assert is_excluded(ignore_list, file_path, repo_path)
