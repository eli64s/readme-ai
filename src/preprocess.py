"""Handles preprocessing of the input codebase."""

import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlparse

import git

import preprocess_helper as helper
from logger import Logger
from utils import valid_url

ALLOWED_HOSTS = ["github.com", "gitlab.com"]
LOGGER = Logger("readmeai_logger")


def _clone_or_copy_repository(repo: str, temp_dir: str) -> None:
    """
    Clones a git repository from the provided URL to a temporary
    directory or copies a local directory to the temporary
    directory if the provided URL is a directory.

    Parameters
    ----------
    repo : str
        The URL or local path of the repository to clone or copy.
    temp_dir : str
        The path of the temporary directory to which the repository
        will be cloned or copied.

    Raises
    ------
    ValueError
        If the provided repository link is not valid.
    """
    temp_dir = Path(temp_dir)
    parsed_url = urlparse(repo)

    if parsed_url.hostname in ALLOWED_HOSTS:
        git.Repo.clone_from(repo, temp_dir)
        return

    if Path(repo).is_dir():
        if temp_dir.exists() and temp_dir.is_dir():
            shutil.rmtree(temp_dir)
        shutil.copytree(repo, temp_dir)
        return

    raise ValueError("Repository path or URL is not valid.")


def _extract_programming_languages(
    files: List[str], language_names: Dict[str, str]
) -> List[str]:
    """
    Returns a list of unique file extensions present in the provided list
    of file paths, along with any additional file extensions defined in
    the language_names configuration.

    Parameters
    ----------
    files : List[str]
        A list of file paths.
    language_names : Dict[str, str]
        A dictionary mapping file extensions to their full name.

    Returns
    -------
    List[str]
        A list of unique file extensions present in the provided list of
        file paths, along with any additional file extensions defined in
        sthe language_names dictionary.
    """
    ext_list = list({Path(f).suffix[1:] for f in files})
    languages = ext_list + [
        language_names[key] for key in ext_list if key in language_names
    ]
    return languages


def _extract_repository_contents(source: str) -> Dict[str, str]:
    """
    Retrieve the contents of all the files from a local or remote repository.

    Parameters
    ----------
    source : str
        The path or url to the repository.

    Returns
    -------
    Dict[str, str]
        Hashmap of file paths and their contents.
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


def _get_file_parsers() -> Dict[str, callable]:
    """
    Returns a dictionary containing file parsers for various file types.

    Returns
    -------
    Dict[str, callable]
        A dictionary containing file parsers for various file types.
    """
    return {
        "build.gradle": helper.parse_gradle,
        "pom.xml": helper.parse_maven,
        "cargo.toml": helper.parse_cargo_toml,
        "cargo.lock": helper.parse_cargo_lock,
        "go.mod": helper.parse_go_mod,
        "go.sum": helper.parse_go_sum,
        "requirements.txt": helper.parse_requirements_file,
        "environment.yaml": helper.parse_conda_env_file,
        "environment.yml": helper.parse_conda_env_file,
        "Pipfile": helper.parse_pipfile,
        "pyproject.toml": helper.parse_pyproject_toml,
        "package.json": helper.parse_package_json,
        "yarn.lock": helper.parse_yarn_lock,
        "CMakeLists.txt": helper.parse_cmake,
        "Makefile": helper.parse_makefile,
        "Makefile.am": helper.parse_makefile_am,
        "configure.ac": helper.parse_configure_ac,
    }


def _get_remote_repository(url: str) -> Dict[str, str]:
    """
    Clone a remote repository and get the contents of all the files.

    Parameters
    ----------
    url : str
        The URL of the remote repository.

    Returns
    -------
    Dict[str, str]
        A dictionary where the keys are file paths and values are the contents of the files.
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
    """
    Extract the dependencies of a project.

    Parameters
    ----------
    dependency_file_names : List[str]
        A list of file names to consider.
    languages : List[str]
        A list of file extensions to consider.
    repository : str
        The URL of the repository or the path to the local directory.

    Returns
    -------
    List[str]
        List of project dependencies and software packages.
    """
    if not repository:
        return []

    with tempfile.TemporaryDirectory() as temp_dir:
        _clone_or_copy_repository(repository, temp_dir)

        file_parsers = _get_file_parsers()
        all_files = get_repository_files(temp_dir)

        dependencies = []
        dependency_file_set = set(dependency_files)
        relevant_files = [
            file for file in all_files if Path(file).name in dependency_file_set
        ]
        for file in relevant_files:
            parser = file_parsers.get(Path(file).name)
            if parser:
                dependencies.append(parser(file))

        languages = _extract_programming_languages(all_files, languages)
        dependencies.append(languages)
        packages = [tech.lower() for sublist in dependencies for tech in sublist]

        return list(set(packages))


def get_repository(source: str) -> Dict[str, str]:
    """
    Retrieves the contents of all the files from a local or remote repository.

    Parameters
    ----------
    source : str
        The path or url to the repository.
    Returns
    -------
    Dict[str, str]
        Hashmap of file paths and their contents.
    """

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
    """
    Returns the name of a repository from its URL or local path.

    Parameters
    ----------
    path : Union[str, Path]
        The URL or local path of the repository.

    Returns
    -------
    str
        The name of the repository.
    """

    parsed_url = urlparse(str(path))

    if parsed_url.hostname in ALLOWED_HOSTS:
        repo_path = parsed_url.path
        repo_name = repo_path.split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
    else:
        repo_name = Path(path).name

    return repo_name
