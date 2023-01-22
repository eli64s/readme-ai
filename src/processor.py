"""src/utils.py."""
import os
import shutil
from pathlib import Path

import git


def clone_codebase(url):
    """Clones a git repository and installs the requirements.txt file.

    Args:
        url (str): The url of the git repository.

    Returns:
        str: The path to the cloned repository.
    """
    tmpdir = get_tmpdir()
    git.Repo.clone_from(url, tmpdir)
    os.system("pipreqs _tmp/ --force")
    return tmpdir


def get_file_extensions():
    file_list = os.walk(os.getcwd())
    file_types = set()
    for walk_output in file_list:
        for file_name in walk_output[-1]:
            file_types.add(file_name.split(".")[-1])
    return list(file_types)


def get_tmpdir():
    """Returns a temporary directory path. If the
    directory already exists, it is overrided."""
    base = Path(".").absolute()
    path = f"{base}/_tmp"
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    return path


def parse_codebase(dir):
    """Parses a directory of python files and returns a dictionary of the file contents.

    Args:
        dir (str): The directory to parse.

    Returns:
        dict: A dictionary of the file contents.
    """
    dict = {}
    paths = Path(dir).rglob("*/*.py")
    for path in paths:
        with open(path) as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            dict[key] = contents
    return dict
