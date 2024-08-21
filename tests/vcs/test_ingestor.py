from pathlib import Path
from unittest.mock import ANY, MagicMock, patch

import git
import pytest

from readmeai.vcs.errors import GitCloneError
from readmeai.vcs.ingestor import (
    clone_repository,
    copy_directory,
    remove_directory,
    remove_hidden_contents,
    retrieve_repository,
)


@pytest.fixture
def mock_logger():
    with patch("readmeai.vcs.ingestor._logger") as mock:
        yield mock


@pytest.fixture
def mock_git_repo():
    with patch("git.Repo") as mock:
        yield mock


@pytest.mark.asyncio
async def test_clone_repository(mock_git_repo):
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
async def test_retrieve_repository_local(mock_logger):
    raise NotImplementedError


@pytest.mark.skip
@pytest.mark.asyncio
async def test_retrieve_repository_remote(mock_logger):
    raise NotImplementedError


@pytest.mark.asyncio
async def test_retrieve_repository_git_error(mock_logger):
    with (
        patch("readmeai.vcs.ingestor.remove_directory"),
        patch(
            "readmeai.vcs.ingestor.clone_repository",
            side_effect=git.GitCommandError("clone", "error"),
        ),
        patch("pathlib.Path.is_dir", return_value=False),
    ):
        repository = "https://github.com/example/repo.git"
        temp_dir = "/tmp/temp_dir"

        with pytest.raises(GitCloneError):
            await retrieve_repository(repository, temp_dir)


@pytest.mark.asyncio
async def test_retrieve_repository_unexpected_error(mock_logger):
    with (
        patch("readmeai.vcs.ingestor.remove_directory"),
        patch(
            "readmeai.vcs.ingestor.clone_repository",
            side_effect=Exception("Unexpected error"),
        ),
        patch("pathlib.Path.is_dir", return_value=False),
    ):
        repository = "https://github.com/example/repo.git"
        temp_dir = "/tmp/temp_dir"

        with pytest.raises(GitCloneError):
            await retrieve_repository(repository, temp_dir)
