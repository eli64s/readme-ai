import asyncio
import shutil
from pathlib import Path
from typing import Union

from readmeai.core.errors import GitCloneError
from readmeai.core.logger import get_logger
from readmeai.preprocessor.directory_cleaner import (
    remove_directory,
    remove_hidden_contents,
)

_logger = get_logger(__name__)


async def clone_repository(repo_url: str, target: Path, depth: int = 1) -> None:
    """Clone a Git repository to the specified target directory using native subprocess."""
    proc = await asyncio.create_subprocess_exec(
        "git",
        "clone",
        "--depth",
        str(depth),
        "--single-branch",
        str(repo_url),
        str(target),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    _, stderr = await proc.communicate()
    if proc.returncode != 0:
        error_msg = (
            stderr.decode().strip()
            if stderr
            else f"process exited with code {proc.returncode}"
        )
        raise GitCloneError(f"Failed to clone repository {repo_url}: {error_msg}")


async def copy_directory(source: Path, target: Path) -> None:
    """Copy a directory and its contents to a new location safely cross-platform."""
    await asyncio.to_thread(
        shutil.copytree,
        source,
        target,
        dirs_exist_ok=True,
        symlinks=True,
        ignore_dangling_symlinks=True,
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

    except GitCloneError:
        raise

    except Exception as e:
        _logger.error(
            f"Unexpected error while cloning repository {repository}: {e}",
        )
        raise GitCloneError(
            f"Unexpected error while cloning repository {repository}: {e}",
        ) from e
