"""Preprocesses the codebase to extract the README.md file and the code files."""

import os
import re
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Union
from urllib.parse import urlparse

import git

import preprocess_helper as helper
from logger import Logger

LOGGER = Logger("readmeai_logger")


def add_space_between_sentences(text: str) -> str:
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


def clone_codebase(url: str) -> Dict[str, str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        git.Repo.clone_from(url, temp_dir)
        files = get_file_contents(temp_dir)
    return files


def get_file_contents(directory: str, exclude: List[str] = []) -> Dict[str, str]:
    contents = {}
    for path in Path(directory).rglob("*"):
        if path.is_file() and not any(p.match(str(path)) for p in exclude):
            try:
                with open(path, encoding="utf-8") as f:
                    lines = f.readlines()
                    if path.suffix == ".py":
                        lines = remove_comments(lines)
                    contents[path.relative_to(directory)] = "".join(lines)
            except UnicodeDecodeError:
                contents[
                    path.relative_to(directory)
                ] = "Could not decode content: non-text or non-UTF-8 file"
    return contents


def get_local_codebase(local_directory: str) -> Dict[str, str]:
    return get_file_contents(local_directory)


def get_project_dependencies(
    repo: str, file_ext: List[str], file_names: List[str]
) -> List[str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        if "github.com" in repo:
            git.Repo.clone_from(repo, temp_dir)
        elif os.path.isdir(repo):
            shutil.copytree(repo, temp_dir)
        else:
            raise ValueError("Repository link is not valid.")

        # Get list of files from the remote or local repository
        all_files = helper.list_files(temp_dir)
        dependency_files = [f for f in all_files if Path(f).name in file_names]

        file_parsers = {
            "cargo.toml": helper.parse_cargo_toml,
            "cargo.lock": helper.parse_cargo_lock,
            "requirements.txt": helper.parse_requirements_file,
            "environment.yaml": helper.parse_conda_env_file,
            "environment.yml": helper.parse_conda_env_file,
            "Pipfile": helper.parse_pipfile,
            "pyproject.toml": helper.parse_pyproject_toml,
            "package.json": helper.parse_package_json,
            "yarn.lock": helper.parse_yarn_lock,
        }

        dependencies = []

        for f in dependency_files:
            parse_fn = file_parsers.get(Path(f).name)

            if parse_fn:
                packages = parse_fn(f)
                dependencies.append(packages)

        # Get a set of file extensions from the repository
        ext_list = list({Path(f).suffix[1:] for f in all_files})
        file_extensions = ext_list + [
            file_ext[key] for key in ext_list if key in file_ext
        ]
        dependencies.append(file_extensions)

        packages = sum(dependencies, [])
        packages = [p.lower() for p in packages]
        return list(set(packages))


def get_repo_name(path: Union[str, os.PathLike]) -> str:
    if "github.com" in str(path):
        # GitHub URL
        repo_path = urlparse(str(path)).path
        repo_name = repo_path.split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
    else:
        # Local path
        repo_name = os.path.basename(os.path.normpath(str(path)))

    return repo_name


def remove_comments(lines):
    return (line for line in lines if not line.strip().startswith("#"))
