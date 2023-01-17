"""
src/utils.py
"""
import os
import shutil
from pathlib import Path


def create_dir():
    """Create a directory to store data.

    Args:
        None

    Returns:
        path: path to the directory
    """
    base = Path(".").absolute()
    path = f"{base}/_tmp"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    return path


def clone_codebase(path):
    """Clone a git repository to a temporary directory.

    Args:
        path (str): The path to the git repository.

    Returns:
        str: The path to the cloned repository.
    """
    clone_path = create_dir()
    clone_cmd = f"git clone {path}"
    os.chdir(clone_path)
    os.system(clone_cmd)
    return clone_path


def parse_codebase(dir):
    """This function takes in a file path and returns the contents of the file.
    Args:
        file (str): The file path to the file to be read.
    Returns:
        str: The contents of the file.
    """
    dict = {}
    path_list = Path(dir).rglob("*.py")
    for path in path_list:
        with open(path, "r") as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            dict[key] = contents
    return dict
