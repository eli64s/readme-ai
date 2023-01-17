"""src/utils.py."""

import os
import shutil
from pathlib import Path

import git


def get_tmpdir():
    base = Path(".").absolute()
    path = f"{base}/_tmp"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    return path


def clone_codebase(url):
    tmpdir = get_tmpdir()
    git.Repo.clone_from(url, tmpdir)
    return tmpdir


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
        with open(path) as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            dict[key] = contents
    return dict
