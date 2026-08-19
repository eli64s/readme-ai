from pathlib import Path
from unittest.mock import ANY, AsyncMock, MagicMock, patch

import pytest
from readmeai.core.errors import GitCloneError
from readmeai.retrievers.git.repository import (
    clone_repository,
    copy_directory,
    load_data,
    remove_directory,
    remove_hidden_contents,
)


@pytest.mark.asyncio
async def test_clone_repository_success():
    repo_url = "https://github.com/example/repo.git"
    target = Path("/tmp/target")
    depth = 1

    mock_proc = AsyncMock()
    mock_proc.communicate.return_value = (b"", b"")
    mock_proc.returncode = 0

    with patch("asyncio.create_subprocess_exec", return_value=mock_proc) as mock_exec:
        await clone_repository(repo_url, target, depth)
        mock_exec.assert_called_once_with(
            "git",
            "clone",
            "--depth",
            "1",
            "--single-branch",
            repo_url,
            str(target),
            stdout=ANY,
            stderr=ANY,
        )


@pytest.mark.asyncio
async def test_clone_repository_failure():
    repo_url = "https://github.com/example/repo.git"
    target = Path("/tmp/target")

    mock_proc = AsyncMock()
    mock_proc.communicate.return_value = (b"", b"fatal: repository not found")
    mock_proc.returncode = 128

    with (
        patch("asyncio.create_subprocess_exec", return_value=mock_proc),
        pytest.raises(GitCloneError, match="fatal: repository not found"),
    ):
        await clone_repository(repo_url, target)


@pytest.mark.asyncio
async def test_copy_directory():
    with patch("shutil.copytree") as mock_copytree:
        source = Path("/source")
        target = Path("/target")

        await copy_directory(source, target)

        mock_copytree.assert_called_once_with(
            source,
            target,
            dirs_exist_ok=True,
            symlinks=True,
            ignore_dangling_symlinks=True,
            ignore=ANY,
        )


@pytest.mark.asyncio
async def test_remove_directory():
    with patch("shutil.rmtree") as mock_rmtree:
        path = Path("/tmp/dir")

        await remove_directory(path)

        mock_rmtree.assert_called_once_with(path, ignore_errors=True)


@pytest.mark.asyncio
async def test_remove_hidden_contents():
    mock_dir = MagicMock(spec=Path)
    mock_dir.iterdir.return_value = [
        MagicMock(name=".git", is_dir=lambda: True),
        MagicMock(name=".hidden_file", is_dir=lambda: False),
        MagicMock(name="visible_file", is_dir=lambda: False),
        MagicMock(name=".github", is_dir=lambda: True),
    ]

    with (
        patch("shutil.rmtree") as mock_rmtree,
        patch("pathlib.Path.unlink") as mock_unlink,
    ):
        await remove_hidden_contents(mock_dir)
        mock_rmtree.assert_called()
        mock_unlink.assert_not_called()


@pytest.mark.asyncio
async def test_load_data_git_error():
    with (
        patch("readmeai.retrievers.git.repository.remove_directory"),
        patch(
            "readmeai.retrievers.git.repository.clone_repository",
            side_effect=GitCloneError("clone error"),
        ),
        patch("pathlib.Path.is_dir", return_value=False),
    ):
        repository = "https://github.com/example/repo.git"
        temp_dir = "/tmp/temp_dir"

        with pytest.raises(GitCloneError):
            await load_data(repository, temp_dir)


@pytest.mark.asyncio
async def test_load_data_unexpected_error():
    with (
        patch("readmeai.retrievers.git.repository.remove_directory"),
        patch(
            "readmeai.retrievers.git.repository.clone_repository",
            side_effect=Exception("Unexpected error"),
        ),
        patch("pathlib.Path.is_dir", return_value=False),
    ):
        repository = "https://github.com/example/repo.git"
        temp_dir = "/tmp/temp_dir"

        with pytest.raises(GitCloneError):
            await load_data(repository, temp_dir)
