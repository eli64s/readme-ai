""" Methods to process the GitHub repository """
import contextlib
import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlparse

import git

import file_parser
from logger import Logger

LOGGER = Logger("readme_ai_logger")


def add_space_between_sentences(text):
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


def get_repo_name(path: Union[str, os.PathLike]) -> str:
    if "github.com" in path:
        # GitHub URL
        repo_path = urlparse(path).path
        repo_name = repo_path.split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
    else:
        # Local path
        repo_name = os.path.basename(os.path.normpath(path))

    return repo_name


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


def get_local_codebase(local_directory: str) -> Dict[str, str]:
    repo_contents = {}
    base_path = Path(local_directory)

    for file_path in base_path.rglob("*"):
        if file_path.is_file():
            try:
                content = file_path.read_text(encoding="utf-8")
                repo_contents[str(file_path)] = content
            except UnicodeDecodeError:
                # Skip non-text files
                continue

    return repo_contents


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

    def parse_requirements_file(file_path):
        return file_parser.parse_requirements_file(file_path)

    def parse_conda_env_file(file_path):
        return file_parser.parse_conda_env_file(file_path)

    def parse_pipfile(file_path):
        return file_parser.parse_pipfile(file_path)

    def parse_pyproject_toml(file_path):
        return file_parser.parse_pyproject_toml(file_path)

    file_parsers = {
        "requirements.txt": parse_requirements_file,
        "environment.yaml": parse_conda_env_file,
        "environment.yml": parse_conda_env_file,
        "Pipfile": parse_pipfile,
        "pyproject.toml": parse_pyproject_toml,
    }

    dependencies = []

    for f in dependency_files:
        fn = Path(f).name
        parse_fn = file_parsers.get(fn)

        if parse_fn:
            packages = parse_fn(f)
            dependencies.append(packages)

    packages = sum(dependencies, [])

    return list(set(packages))
