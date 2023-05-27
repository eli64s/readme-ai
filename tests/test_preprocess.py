"""Unit tests for preprocess.py."""

import sys

sys.path.append("src")

from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlparse

import git
import pytest

from src.preprocess import (
    _clone_or_copy_repository,
    _extract_repository_contents,
    _get_file_extensions,
    _get_file_parsers,
    _get_remote_repository,
    _map_extensions_to_languages,
    additional_dependencies,
    get_repository,
    get_repository_name,
)


@pytest.fixture
def setup_files(tmpdir_factory):
    fn = tmpdir_factory.mktemp("data").join("hello.txt")
    with open(fn, "w") as f:
        f.write("content")
    return str(fn)


def test_clone_repository(tmp_path):
    repo_url = "https://github.com/user/repo.git"
    hosts = [urlparse(repo_url).hostname]
    with patch.object(git.Repo, "clone_from") as mocked_clone_from:
        _clone_or_copy_repository(hosts, repo_url, tmp_path)
    mocked_clone_from.assert_called_once_with(repo_url, tmp_path)


def test_copy_repository(tmp_path):
    source_dir = tmp_path / "source_dir"
    source_dir.mkdir()
    (source_dir / "file.txt").touch()
    dest_dir = tmp_path / "dest_dir"

    hosts = ["github.com"]
    _clone_or_copy_repository(hosts, str(source_dir), str(dest_dir))

    assert (dest_dir / "file.txt").exists()


def test_copy_repository_dest_dir_exists(tmp_path):
    source_dir = tmp_path / "source_dir"
    source_dir.mkdir()
    (source_dir / "file.txt").touch()
    dest_dir = tmp_path / "dest_dir"
    dest_dir.mkdir()
    (dest_dir / "old_file.txt").touch()

    hosts = ["github.com"]
    _clone_or_copy_repository(hosts, str(source_dir), str(dest_dir))

    assert not (dest_dir / "old_file.txt").exists()
    assert (dest_dir / "file.txt").exists()


def test_invalid_source(tmp_path):
    invalid_path = "/invalid/path"
    hosts = ["github.com"]
    with pytest.raises(
        ValueError, match="Repository path or URL is not valid."
    ):
        _clone_or_copy_repository(hosts, invalid_path, tmp_path)


def test_extract_repository_contents(tmp_path):
    # Arrange
    (tmp_path / "test.txt").write_text("hello world!")
    (tmp_path / "test2.txt").write_text("hello again!")
    (tmp_path / ".git").mkdir()
    (tmp_path / ".git" / "config").write_text(
        "[core]\n    repositoryformatversion = 0"
    )
    contents = _extract_repository_contents(str(tmp_path))
    assert contents == {
        Path("test.txt"): "hello world!",
        Path("test2.txt"): "hello again!",
    }


def test_extract_repository_contents_with_non_utf8(tmp_path):
    (tmp_path / "test.txt").write_bytes(b"\x80abc")  # non-UTF8 content
    contents = _extract_repository_contents(str(tmp_path))
    assert contents == {
        Path(
            "test.txt"
        ): "Could not decode content: non-text or non-UTF-8 file."
    }


def test_extract_repository_contents_empty_directory(tmp_path):
    contents = _extract_repository_contents(str(tmp_path))
    assert contents == {}


def test_get_file_extensions():
    files = ["file1.txt", "file2.py", "file3.py", "file4.java"]
    expected_result = ["txt", "py", "java"]
    assert sorted(_get_file_extensions(files)) == sorted(expected_result)


def test_map_extensions_to_languages():
    ext_list = ["py", "js", "java", "txt"]
    languages = {
        "py": "Python",
        "js": "JavaScript",
        "java": "Java",
    }
    expected_result = [
        "py",
        "js",
        "java",
        "txt",
        "Python",
        "JavaScript",
        "Java",
    ]
    assert sorted(_map_extensions_to_languages(ext_list, languages)) == sorted(
        expected_result
    )


def test_get_file_parsers():
    parsers = _get_file_parsers()
    assert isinstance(parsers, dict)
    assert "build.gradle" in parsers


def test_get_remote_repository(mocker):
    mocker.patch("git.Repo.clone_from")
    mocker.patch("tempfile.TemporaryDirectory")
    mocker.patch("src.preprocess._extract_repository_contents")

    assert _get_remote_repository("https://test-repo-url.com") is not None


def test_get_repository(mocker):
    mocker.patch("src.preprocess.utils.valid_url", return_value=True)
    mocker.patch("src.preprocess._get_remote_repository")
    assert get_repository("https://test-repo-url.com") is not None

    mocker.patch("src.preprocess.utils.valid_url", return_value=False)
    mocker.patch("src.preprocess._extract_repository_contents")
    assert get_repository("/local/path/to/repo") is not None


def test_get_repository_name():
    hosts = ["github.com", "gitlab.com"]
    assert (
        get_repository_name(hosts, "https://github.com/user/repo.git")
        == "repo"
    )
    assert get_repository_name(hosts, "/local/path/to/repo") == "repo"


def test_additional_dependencies():
    files = [
        Path("docker/compose.yml"),
        Path(".github/workflows/main.yml"),
        Path("src/app.py"),
    ]
    expected_result = ["docker", "github actions"]
    assert sorted(additional_dependencies(files)) == sorted(expected_result)
