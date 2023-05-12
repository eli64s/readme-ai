"""Handles preprocessing of the input codebase."""

import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlparse

import git

import preprocess_helper as helper
from logger import Logger

ALLOWED_HOSTS = ["github.com"]
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
        shutil.copytree(repo, temp_dir, dirs_exist_ok=True)
        return

    raise ValueError("Repository path or URL is not valid.")


def _get_codebase_remote(url: str) -> Dict[str, str]:
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
            files = _get_file_contents(temp_dir)
            return files
    except git.GitCommandError as e:
        print(f"Error cloning repository from {url}: {e}")
        return {}


def _get_file_contents(directory: str) -> Dict[str, str]:
    """
    Get the contents of all the files in a directory.

    Parameters
    ----------
    directory : str
        The path to the directory.

    Returns
    -------
    Dict[str, str]
        A dictionary where the keys are file paths and values are the contents of the files.
    """
    contents = {}
    for path in Path(directory).rglob("*"):
        if path.is_file():
            try:
                with open(path, encoding="utf-8") as f:
                    lines = f.readlines()
                    contents[path.relative_to(directory)] = "".join(lines)
            except UnicodeDecodeError:
                contents[
                    path.relative_to(directory)
                ] = "Could not decode content: non-text or non-UTF-8 file."
    return contents


def _get_file_extensions(all_files: List[str], file_ext: Dict[str, str]) -> List[str]:
    """
    Returns a list of unique file extensions present in the provided list
    of file paths, along with any additional file extensions defined in
    the file_ext dictionary.

    Parameters
    ----------
    all_files : List[str]
        A list of file paths.
    file_ext : Dict[str, str]
        A dictionary mapping file extensions to additional file extensions.

    Returns
    -------
    List[str]
        A list of unique file extensions present in the provided list of
        file paths, along with any additional file extensions defined in
        sthe file_ext dictionary.
    """

    ext_list = list({Path(f).suffix[1:] for f in all_files})
    file_extensions = ext_list + [file_ext[key] for key in ext_list if key in file_ext]
    return file_extensions


def _get_file_parsers() -> Dict[str, callable]:
    """
    Returns a dictionary containing file parsers for various file types.

    Returns
    -------
    Dict[str, callable]
        A dictionary containing file parsers for various file types.
    """
    return {
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
    }


def get_codebase(repo_path: str) -> Dict[str, str]:
    """
    Get the contents of all the files in a directory or a remote repository.

    Parameters
    ----------
    local : str
        The path to the local directory.
    remote: str, optional
        The URL of the remote repository, by default None.

    Returns
    -------
    Dict[str, str]
        A dictionary where the keys are file paths and
        values are the contents of the files.
    """

    if valid_url(repo_path):
        return _get_codebase_remote(repo_path)
    return _get_file_contents(repo_path)


def get_project_dependencies(
    repo: str, file_ext: List[str], file_names: List[str]
) -> List[str]:
    """
    Get the dependencies of a project.

    Parameters
    ----------
    repo : str
        The URL of the repository or the path to the local directory.
    file_ext : List[str]
        A list of file extensions to consider.
    file_names : List[str]
        A list of file names to consider.

    Returns
    -------
    List[str]
        A list of dependencies.
    """
    if not repo:
        return []

    with tempfile.TemporaryDirectory() as temp_dir:
        _clone_or_copy_repository(repo, temp_dir)

        all_files = helper.list_files(temp_dir)
        dependency_files = [f for f in all_files if Path(f).name in file_names]

        file_parsers = _get_file_parsers()
        dependencies = []

        for f in dependency_files:
            parse_fn = file_parsers.get(Path(f).name)

            if parse_fn:
                packages = parse_fn(f)
                dependencies.append(packages)

        file_extensions = _get_file_extensions(all_files, file_ext)
        dependencies.append(file_extensions)

        packages = sum(dependencies, [])
        packages = [p.lower() for p in packages]
        return list(set(packages))


def get_repo_name(path: Union[str, Path]) -> str:
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


def format_sentence(text: str) -> str:
    """
    Remove space between comma and period in a given string.

    Parameters
    ----------
    text : str
        The input string.

    Returns
    -------
    str
        The input string with spaces between comma and period removed.
    """
    return re.sub(r",\s*\.", ",.", text)


def valid_url(s: str) -> bool:
    """
    Check if a given string is a valid URL.

    Parameters
    ----------
    s : str
        The string to check.

    Returns
    -------
    bool
        Returns True if the string is a valid URL, False otherwise.

    Raises
    ------
    None

    Examples
    --------
    >>> is_url("https://www.google.com/")
    True
    >>> is_url("ftp://ftp.example.com/")
    True
    >>> is_url("www.example.com")
    False
    """
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https:// or ftp:// or ftps://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,63}|[A-Z]{2,63}\.[A-Z]{2,63}))"
        r"(?::\d+)?"  # optional port number
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return bool(regex.match(s))
