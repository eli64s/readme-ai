import asyncio
import os
import platform
import shutil
from pathlib import Path
from typing import Union

import git
from readmeai.core.errors import GitCloneError
from readmeai.core.logger import get_logger
from readmeai.preprocessor.directory_cleaner import (
    remove_directory,
    remove_hidden_contents,
)

_logger = get_logger(__name__)


async def clone_repository(repo_url: str, target: Path, depth: int = 1) -> None:
    """Clone a Git repository to the specified target directory."""
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
    """Copy a directory and its contents to a new location."""
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


async def load_data(repository: Union[str, Path], temp_dir: str) -> str:
    """Clone repository to temporary directory and return the path."""
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
    ) as e:
        _logger.error(f"Failed to clone repository {repository}: {e}")
        raise GitCloneError(
            f"Failed to clone repository {repository}",
        ) from e

    except Exception as e:
        _logger.error(
            f"Unexpected error while cloning repository {repository}: {e}",
        )
        raise GitCloneError(
            f"Unexpected error while cloning repository {repository}",
        ) from e
