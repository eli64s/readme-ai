"""src/utils.py."""
import contextlib
import logging
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import git


logger = logging.getLogger(__name__)


@contextlib.contextmanager
def make_temp_directory():
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def clone_codebase(url):
    with make_temp_directory() as temp_dir:
        git.Repo.clone_from(url, temp_dir)
        files = parse_codebase(temp_dir)
        files["packages"] = get_packages(temp_dir)
        files["extensions"] = get_file_extensions(temp_dir)
    return files


def get_file_extensions(temp_dir):
    file_list = os.walk(temp_dir)
    file_types = set()
    for walk_output in file_list:
        for file_name in walk_output[-1]:
            file_types.add(file_name.split(".")[-1])
    return list(file_types)


def get_packages(temp_dir):
    subprocess.run(f"pipreqs {temp_dir} --force", shell=True)
    logger.info(f"{temp_dir}\n")
    with open(Path("requirements.txt").resolve()) as f:
        lines = f.read().splitlines()
        pkgs = ["".join(r) for r in lines]
        pkgs = [r.split("=")[0] for r in lines]
    return pkgs


def parse_codebase(dir):
    dict = {}
    paths = Path(dir).rglob("*/*.py")
    for path in paths:
        with open(path) as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            dict[key] = contents
    return dict
