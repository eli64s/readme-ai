"""src/utils.py."""
import contextlib
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import git


REPO_PATH = "src/*.py"


def get_tree() -> None:
    """_summary_"""
    cwd_path = Path.cwd()
    bash_path = f"{cwd_path}/scripts/build_md.sh"
    subprocess.call(["bash", bash_path])


@contextlib.contextmanager
def make_temp_directory():
    """Clone GitHub repository
        to temporary directory.

    Yields:
        iterator: files
    """
    # Logger.debug("Creating temp directory")

    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        # LOGGER.info(f"\nRemoving temp folder: {temp_dir}\n")
        shutil.rmtree(temp_dir)


def clone_codebase(url):
    """Runs git clone to retrieve
        project input data.

    Args:
        url (str): GitHub

    Returns:
        Dict: map of all repo contents
    """
    with make_temp_directory() as temp_dir:
        # LOGGER.info(f"\nCloning git repo: {url}\n")
        git.Repo.clone_from(url, temp_dir)
        # LOGGER.info("\nParsing the repository.\n")
        files = parse_codebase(temp_dir)
        files["packages"] = get_packages()
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


def get_packages():
    """Get codebase packages to help
        generate project badge icons.

    Args:
        temp_dir (str): temp directory

    Returns:
        List: codebase packages
    """
    subprocess.run(f"pipreqs . --force", shell=True)
    with open(Path("requirements.txt").resolve()) as f:
        lines = f.read().splitlines()
        pkgs = ["".join(r) for r in lines]
        pkgs = [r.split("=")[0] for r in lines]
    return pkgs


def parse_codebase(dir):
    """Get each file as a raw string.

    Args:
        dir (str): temp directory

    Returns:
        Dict: map of all repo contents
    """
    dict = {}
    paths = Path(dir).rglob(REPO_PATH)
    for path in paths:
        with open(path) as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            dict[key] = contents
    return dict
