import asyncio
import os
import platform
import shutil
from pathlib import Path

import git

from ..core.logger import Logger
from .errors import GitCloneError

_logger = Logger(__name__)


async def clone_repository(
    repo_url: str,
    target: Path,
    depth: int = 1,
) -> None:
    """
    Clone a Git repository to the specified target directory.
    """
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(
        None,
        lambda: git.Repo.clone_from(
            repo_url,
            str(target),
            depth=depth,
            single_branch=True,
        ),
    )


async def copy_directory(source: Path, target: Path) -> None:
    """
    Copy a directory and its contents to a new location.
    """
    if platform.system() == "Windows":
        os.system(f'xcopy "{source}" "{target}" /E /I /H /Y')
    else:
        await asyncio.to_thread(
            shutil.copytree,
            source,
            target,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(".git"),
        )


async def remove_directory(path: Path) -> None:
    """
    Remove a temporary directory and its contents.
    """
    if platform.system() == "Windows":
        os.system(f'rmdir /S /Q "{path}"')
    else:
        await asyncio.to_thread(shutil.rmtree, path, ignore_errors=True)


async def remove_hidden_contents(directory: Path) -> None:
    """
    Remove hidden files and directories from a specified directory.
    """
    for item in directory.iterdir():
        if item.name.startswith(".") and item.name != ".github":
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()


async def retrieve_repository(repository: Path | str, temp_dir: str) -> str:
    """
    Clone repository to temporary directory and return the path.
    """
    temp_dir_path = Path(temp_dir)
    repo_path = Path(repository)

    try:
        if temp_dir_path.exists():
            await remove_directory(temp_dir_path)

        if repo_path.is_dir():
            await copy_directory(repo_path, temp_dir_path)
        else:
            await clone_repository(str(repository), temp_dir_path)

        await remove_hidden_contents(temp_dir_path)

        return str(temp_dir_path)

    except (
        git.GitCommandError,
        git.InvalidGitRepositoryError,
        git.NoSuchPathError,
    ) as exc:
        _logger.error(f"Failed to clone repository {repository}: {exc}")
        raise GitCloneError(
            f"Failed to clone repository {repository}",
        ) from exc

    except Exception as exc:
        _logger.error(
            f"Unexpected error while cloning repository {repository}: {exc}",
        )
        raise GitCloneError(
            f"Unexpected error while cloning repository {repository}",
        ) from exc
