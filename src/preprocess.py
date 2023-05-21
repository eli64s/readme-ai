"""Handles preprocessing of the input codebase."""

import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlparse

import git

import parse
from logger import Logger
from utils import valid_url

ALLOWED_HOSTS = ["github.com", "gitlab.com"]
LOGGER = Logger("readmeai_logger")


def _clone_or_copy_repository(source: str, temp_dir: str) -> None:
    """Clone or copy a repository to a temporary directory.

    Parameters
    ----------
    source
        URL or path of the repository.
    temp_dir
        Path to the temporary directory.

    Raises
    ------
    ValueError
        If the repository path or URL is not valid.
    """
    temp_dir = Path(temp_dir)
    parsed_url = urlparse(source)

    if parsed_url.hostname in ALLOWED_HOSTS:
        git.Repo.clone_from(source, temp_dir)
        return

    if Path(source).is_dir():
        if temp_dir.exists() and temp_dir.is_dir():
            shutil.rmtree(temp_dir)
        shutil.copytree(source, temp_dir)
        return

    raise ValueError("Repository path or URL is not valid.")


def _extract_repository_contents(source: str) -> Dict[str, str]:
    """Extract the contents from the cloned or copied repository.

    Parameters
    ----------
    source
        Path to the repository.

    Returns
    -------
        Hashmap of file paths and their contents from the repository.
    """
    contents = {}
    for path in Path(source).rglob("*"):
        if path.is_file():
            try:
                with open(path, encoding="utf-8") as f:
                    lines = f.readlines()
                    contents[path.relative_to(source)] = "".join(lines)
            except UnicodeDecodeError:
                contents[
                    path.relative_to(source)
                ] = "Could not decode content: non-text or non-UTF-8 file."
    return contents


def _get_file_extensions(files: List[str]) -> List[str]:
    """Extract distinct file extensions that exist in the repository.

    Parameters
    ----------
    files
        List containing all file paths in the repository.

    Returns
    -------
        List containing distinct file extensions in the repository.
    """
    ext_list = list({Path(f).suffix[1:] for f in files})
    return ext_list


def _map_extensions_to_languages(
    ext_list: List[str], languages: Dict[str, str]
) -> List[str]:
    """Map file extensions to programming language names i.e. .py -> Python.

    Parameters
    ----------
    ext_list
        List containing distinct file extensions in the repository.
    languages
        Hashmap containing file extensions and their corresponding
        programming language names.

    Returns
    -------
        List containing programming language names in the repository.
    """
    lang_name = ext_list + [
        languages[key] for key in ext_list if key in languages
    ]
    return lang_name


def _get_file_parsers() -> Dict[str, callable]:
    """
    Returns a dictionary containing file parsers for various file types.

    Returns
    -------
    Dict[str, callable]
        A dictionary containing file parsers for various file types.
    """
    return {
        "build.gradle": parse.parse_gradle,
        "pom.xml": parse.parse_maven,
        "cargo.toml": parse.parse_cargo_toml,
        "cargo.lock": parse.parse_cargo_lock,
        "go.mod": parse.parse_go_mod,
        "go.sum": parse.parse_go_sum,
        "requirements.txt": parse.parse_requirements_file,
        "environment.yaml": parse.parse_conda_env_file,
        "environment.yml": parse.parse_conda_env_file,
        "Pipfile": parse.parse_pipfile,
        "pyproject.toml": parse.parse_pyproject_toml,
        "package.json": parse.parse_package_json,
        "yarn.lock": parse.parse_yarn_lock,
        "package-lock.json": parse.parse_package_lock_json,
        "CMakeLists.txt": parse.parse_cmake,
        "Makefile": parse.parse_makefile,
        "Makefile.am": parse.parse_makefile_am,
        "configure.ac": parse.parse_configure_ac,
    }


def _get_remote_repository(url: str) -> Dict[str, str]:
    """Clone a remote repository and return its contents.

    Parameters
    ----------
    url
        URL of the remote repository.

    Returns
    -------
        Hashmap of file paths and their contents from the repository.
    """
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            git.Repo.clone_from(url, temp_dir, depth=1)
            files = _extract_repository_contents(temp_dir)
            return files
    except git.GitCommandError as e:
        print(f"Error cloning repository from {url}: {e}")
        return {}


def extract_dependencies(
    dependency_files: List[str], languages: List[str], repository: str
) -> List[str]:
    """Search for dependency files in the repository and extract metadata.

    Parameters
    ----------
    dependency_files
        Dependency files to search for in the repository.
    languages
        List of programming languages
    repository
        Path or URL of the repository.

    Returns
    -------
        List of software and packages used by the codebase.
    """
    if not repository:
        return []

    with tempfile.TemporaryDirectory() as temp_dir:
        _clone_or_copy_repository(repository, temp_dir)

        file_parsers = _get_file_parsers()
        repo_files = get_repository_files(temp_dir)

        dependencies = []
        dependency_file_set = set(dependency_files)
        relevant_files = [
            file
            for file in repo_files
            if Path(file).name in dependency_file_set
        ]
        for file in relevant_files:
            parser = file_parsers.get(Path(file).name)
            if parser:
                dependencies.append(parser(file))

        file_exts = _get_file_extensions(repo_files)
        lang_name = _map_extensions_to_languages(file_exts, languages)
        dependencies.append(lang_name)
        dependencies = [
            name.lower() for sublist in dependencies for name in sublist
        ]

        if has_dockerfile(repo_files):
            dependencies.append("Docker")

        return list(set(dependencies))


def get_repository(source: str) -> Dict[str, str]:
    """Returns the contents of a repository from a URL or local path."""
    if valid_url(source):
        return _get_remote_repository(source)
    else:
        return _extract_repository_contents(source)


def get_repository_files(directory: str) -> List[str]:
    """Returns a list of file names in the provided directory."""
    file_list = []
    try:
        path = Path(directory)
        if not path.exists():
            LOGGER.error(f"Invalid repository path: {directory}.")
        else:
            file_list = [str(p) for p in path.glob("**/*") if p.is_file()]

    except (OSError, TypeError) as err:
        LOGGER.error(f"Error reading repository contents: {err}")

    return file_list


def get_repository_name(path: Union[str, Path]) -> str:
    """Extracts the repository name from a URL or local path."""
    parsed_url = urlparse(str(path))

    if parsed_url.hostname in ALLOWED_HOSTS:
        repo_path = parsed_url.path
        repo_name = repo_path.split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
    else:
        repo_name = Path(path).name

    return repo_name


def has_dockerfile(paths):
    """Checks if a Dockerfile exists in the repository."""
    return any("Dockerfile" in path for path in paths)
