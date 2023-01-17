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
    dict = {}
    paths = Path(dir).rglob("src/*.py")
    for path in paths:
        with open(path) as f:
            contents = "".join(f.readlines())
            key = "/".join(str(path).split("/")[-2:])
            dict[key] = contents
    return dict
