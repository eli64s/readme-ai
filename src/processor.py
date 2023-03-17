"""
src/processor.py
"""
import contextlib
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import git


def add_space_between_sentences(text):
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


def clone_codebase(cwd_path, file_type, url):
    """Clones a Git repository and retrieves its contents.

    Args:
        cwd_path (str): The path to the current working directory.
        file_type (str): The file type to parse.
        url (str): The URL of the Git repository.

    Returns:
        Dict: A map of the repository contents.
    """
    with make_temp_directory() as temp_dir:
        repo = git.Repo.clone_from(url, temp_dir)
        files = parse_codebase(file_type, temp_dir)
        files["packages"] = get_packages(temp_dir)
        files["extensions"] = get_extensions(temp_dir)
        create_environ_file(cwd_path, temp_dir)

    repo.close()
    return files


def create_environ_file(repo_path, temp_dir):
    """Create a conda environment file.

    Args:
        repo_path (str): The path to the repository.
    """
    file_name = "environment.yml"
    env_file = os.path.join(temp_dir, file_name)
    if os.path.exists(env_file):
        print(f"{env_file} already exists")
        return

    env_file = os.path.join(temp_dir, file_name)
    if os.path.exists(env_file):
        print(f"{env_file} already exists")
        return

    setup_dir = os.path.join(repo_path, "setup")
    os.makedirs(setup_dir, exist_ok=True)
    env_file = os.path.join(setup_dir, file_name)

    try:
        subprocess.run(
            f"conda env export > {env_file}", shell=True, check=True, cwd=repo_path
        )
        print(f"Created {env_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error creating {env_file}: {e}")


def extract_repo_name(repo_url):
    repo_name = repo_url.rstrip("/").split("/")[-1]
    repo_name = re.sub(r"[-_]", " ", repo_name)
    return repo_name


def get_extensions(temp_dir):
    """Get file extensions in the repository.

    Args:
        temp_dir (str): The path to the repository.

    Returns:
        List: A list of file extensions.
    """
    file_types = set()
    for _, _, files in os.walk(temp_dir):
        for file in files:
            file_types.add(file.split(".")[-1])
    return list(file_types)


def get_packages(temp_dir):
    """Get package names in the repository.

    Args:
        temp_dir (str): The path to the repository.

    Returns:
        List: A list of package names.
    """
    subprocess.run(["pipreqs", temp_dir], check=True)
    with open(f"{temp_dir}/requirements.txt") as f:
        pkgs = [line.split("=")[0] for line in f.read().splitlines()]
    return pkgs


@contextlib.contextmanager
def make_temp_directory():
    """Create a temporary directory.

    Yields:
        str: The path to the temporary directory.
    """
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def parse_codebase(file_type, directory):
    """Get the contents of each file with a specific file type.

    Args:
        file_type (str): The file type to retrieve.
        directory (str): The path to the directory to search.

    Returns:
        dict: A map of the file contents.
    """
    artifacts = {}
    for path in Path(directory).rglob(file_type):
        with open(path) as f:
            contents = f.read()
            key = "/".join(path.relative_to(directory).parts[-2:])
            artifacts[key] = contents
    return artifacts
