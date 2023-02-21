"""src/utils.py."""
import contextlib
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import git


def clone_codebase(file_type, url):
    """Runs git clone to retrieve
        project input data.

    Args:
        url (str): GitHub

    Returns:
        Dict: map of all repo contents
    """
    with make_temp_directory() as temp_dir:
        git.Repo.clone_from(url, temp_dir)
        files = parse_codebase(file_type, temp_dir)
        files["packages"] = get_packages(temp_dir)
        files["extensions"] = get_extensions(temp_dir)
    return files


def get_extensions(temp_dir):
    """Get file extensions to help
        generate project badge icons.

    Args:
        temp_dir (str): temp directory

    Returns:
        List: file extensions
    """
    file_list = os.walk(temp_dir)
    file_types = set()
    for walk_output in file_list:
        for file_name in walk_output[-1]:
            file_types.add(file_name.split(".")[-1])
    return list(file_types)


def get_packages(temp_dir):
    """Get codebase packages to help
        generate project badge icons.

    Args:
        temp_dir (str): temp directory

    Returns:
        List: codebase packages
    """
    subprocess.run(["pipreqs", temp_dir], check=True)
    with open(f"{temp_dir}/requirements.txt", "r") as f:
        lines = f.read().splitlines()
        pkgs = ["".join(r) for r in lines]
        pkgs = [r.split("=")[0] for r in lines]
    return pkgs


@contextlib.contextmanager
def make_temp_directory():
    """Clone GitHub repository
        to temporary directory.

    Yields:
        iterator: files
    """
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def parse_codebase(file_type, dir):
    """Get each file as a raw string.

    Args:
        dir (str): temp directory

    Returns:
        Dict: map of all repo contents
    """
    artifacts = {}
    paths = Path(dir).rglob(file_type)
    for path in paths:
        with open(path) as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            artifacts[key] = contents
    return artifacts
