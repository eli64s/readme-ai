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


async def remove_hidden_contents(directory: Path) -> None:
    """Remove hidden files and directories from a specified directory."""
    for item in directory.iterdir():
        if ".github" in item.parts:
            continue
        if item.name.startswith("."):
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
