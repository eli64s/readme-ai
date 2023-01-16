"""
src/utils.py
"""
import os
from pathlib import Path


def create_dir():
    wd = Path(".").absolute()
    path = f"{wd}/data"
    if not os.path.isdir(path):
        os.makedirs(path)
    return path


def clone_codebase(path):
    clone_path = create_dir()
    clone_cmd = f"git clone {path}"
    os.chdir(clone_path)
    os.system(clone_cmd)
    return clone_path


def get_file_names():
    pass


def parse_codebase(file):
    """
    Given a file path, this function reads the contents of the file and returns it as a single string.

    Parameters:
        file (str): The file path of the .py file to read.

    Returns:
        str: The contents of the file as a single string.
    """
    with open(file, "r") as f:
        file_contents = "".join(f.readlines())
    return file_contents
