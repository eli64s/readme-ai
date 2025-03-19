import asyncio
import os
import platform
import shutil
from pathlib import Path


async def remove_directory(path: Path) -> None:
    """Remove a temporary directory and its contents."""
    if platform.system() == "Windows":
        os.system(f'rmdir /S /Q "{path}"')
    else:
        await asyncio.to_thread(shutil.rmtree, path, ignore_errors=True)


def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    Windows may experience an access error when a file is labeled "read
    only". In this instance, the function will attempt to add write
    permissions and then retry the function. If the error persists or raises
    for another reason, the original error gets re-raised.

    Usage: ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat

    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


async def remove_hidden_contents(directory: Path) -> None:
    """Remove hidden files and directories from a specified directory."""
    for item in directory.iterdir():
        if ".github" in item.parts:
            continue
        if item.name.startswith("."):
            if item.is_dir():
                shutil.rmtree(item, onerror=onerror)
            else:
                item.unlink()
