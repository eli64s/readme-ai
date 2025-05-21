from pathlib import Path
from unittest.mock import ANY, AsyncMock, MagicMock, patch

import git
import pytest
from readmeai.core.errors import GitCloneError
from readmeai.retrievers.git.repository import (
    clone_repository,
    copy_directory,
    load_data,
    remove_directory,
    remove_hidden_contents,
)


@pytest.fixture
def mock_git_repo():
    with patch("git.Repo") as mock:
        yield mock


@pytest.mark.asyncio
async def test_clone_repository(mock_git_repo: MagicMock | AsyncMock):
    repo_url = "https://github.com/example/repo.git"
    target = Path("/tmp/target")
    depth = 1

    await clone_repository(repo_url, target, depth)

    mock_git_repo.clone_from.assert_called_once_with(
        repo_url,
        str(target),
        depth=depth,
        single_branch=True,
    )


@pytest.mark.asyncio
async def test_copy_directory_windows():
    with (
        patch("platform.system", return_value="Windows"),
        patch("os.system") as mock_system,
    ):
        source = Path("/source")
        target = Path("/target")

        await copy_directory(source, target)

        mock_system.assert_called_once_with(
            f'xcopy "{source}" "{target}" /E /I /H /Y',
        )


@pytest.mark.asyncio
async def test_copy_directory_non_windows():
    with (
        patch("platform.system", return_value="Linux"),
        patch("shutil.copytree") as mock_copytree,
    ):
        source = Path("/source")
        target = Path("/target")

        await copy_directory(source, target)

        mock_copytree.assert_called_once_with(
            source,
            target,
            dirs_exist_ok=True,
            ignore=ANY,
        )


@pytest.mark.asyncio
async def test_remove_directory_windows():
    with (
        patch("platform.system", return_value="Windows"),
        patch("os.system") as mock_system,
    ):
        path = Path("/tmp/dir")

        await remove_directory(path)

        mock_system.assert_called_once_with(f'rmdir /S /Q "{path}"')


@pytest.mark.asyncio
async def test_remove_directory_non_windows():
    with (
        patch("platform.system", return_value="Linux"),
        patch("shutil.rmtree") as mock_rmtree,
    ):
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


@pytest.mark.skip
@pytest.mark.asyncio
async def test_load_data_local():
    raise NotImplementedError


@pytest.mark.skip
@pytest.mark.asyncio
async def test_load_data_remote():
    raise NotImplementedError


@pytest.mark.asyncio
async def test_load_data_git_error():
    with (
        patch("readmeai.retrievers.git.repository.remove_directory"),
        patch(
            "readmeai.retrievers.git.repository.clone_repository",
            side_effect=git.GitCommandError("clone", "error"),
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
