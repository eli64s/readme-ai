"""
src/utils.py
"""
import json

from markdownify import markdownify as md


def get_pkgs_list():
    """Get a list of packages from the requirements.txt file.

    Args:
        None

    Returns:
        list: A list of packages.

    Raises:
        None
    """
    with open("_tmp/requirements.txt", "r") as f:
        lines = f.read().splitlines()
    reqs = ["".join(r) for r in lines]
    reqs = [r.split("=")[0] for r in lines]
    return reqs


def read_json(path):
    """Reads a json file and returns the contents as a dictionary.

    Args:
        path (str): The path to the json file.

    Returns:
        dict: The contents of the json file.
    """
    with open(path, "r", encoding="utf8") as j:
        contents = json.load(j)
    return contents


def write_file(html, html_path, md_path):
    with open(html_path, "w", encoding="utf-8") as file:
        file.write(html)
    with open(md_path, "w", encoding="utf-8") as file:
        file.write(md(html))
