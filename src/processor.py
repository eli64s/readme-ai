""" Methods to process the GitHub repository """
import contextlib
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List

import git

import file_parser
from logger import Logger

LOGGER = Logger("readme_ai_logger")


def add_space_between_sentences(text):
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


def clone_codebase(url: str) -> Dict[str, str]:
    """Clone GitHub repository to a temporary
        directory and return the file contents.

    Parameters
    ----------
    cwd_path
        cwd_path (str): current working directory path
    url
        url (str): the GitHub URL to clone

    Returns
    -------
        Dict: a dictionary mapping file paths to their contents
    """
    with make_temp_directory() as temp_dir:
        git.Repo.clone_from(url, temp_dir)
        files = get_file_contents(temp_dir)
    return files


def get_file_contents(directory: str, exclude: List[str] = []) -> Dict[str, str]:
    contents = {}
    exclude += [
        ".gitignore",
        ".md",
        "__init__.py",
        "badges",
        "CODE_OF_CONDUCT.md",
        "CONTRIBUTING",
        "LICENSE",
        "README.md",
        "conf",
        "docs",
        "imgs",
        "setup",
        "setup.py",
        "tests",
    ]
    for path in Path(directory).rglob("*"):
        if path.is_file() and not any(ex in path.parts for ex in exclude):
            try:
                with path.open(encoding="utf-8") as f:
                    contents[path.relative_to(directory)] = f.read()
            except UnicodeDecodeError:
                contents[
                    path.relative_to(directory)
                ] = "Could not decode content: non-text or non-UTF-8 file"
    return contents


@contextlib.contextmanager
def make_temp_directory() -> str:
    """Create a temporary directory for the cloned GitHub repository.

    Returns
    -------

    Yields
    ------
        The path to the temporary directory
    """
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def get_project_dependencies(file_names: list[str]) -> list[str]:
    cwd_dir = Path.cwd().resolve().parent
    dependency_list = file_parser.list_files(cwd_dir)
    dependency_files = [f for f in dependency_list if f.split("/")[-1] in file_names]
    dependencies = []
    for f in dependency_files:
        fn = Path(f).name

        if fn == "requirements.txt":
            packages = file_parser.parse_requirements_file(f)
            dependencies.append(packages)

        if fn == "environment.yaml" or f == "environment.yml":
            packages = file_parser.parse_conda_env_file(f)
            dependencies.append(packages)

    packages = sum(dependencies, [])

    return list(set(packages))
