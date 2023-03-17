"""
src/processor.py
"""
import contextlib
import os
import re
import shutil
import subprocess
import tempfile
from collections import defaultdict
from pathlib import Path

import git
import requests


def add_space_between_sentences(text):
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


@contextlib.contextmanager
def clone_in_temp_directory():
    """Create a temporary directory.

    Yields:
        str: The path to the temporary directory.
    """
    temp_dir = tempfile.mkdtemp()
    try:
        yield temp_dir
    finally:
        shutil.rmtree(temp_dir)


def clone_repository(repo_url):
    """_summary_

    Parameters
    ----------
    repo_url
        _description_
    """
    cwd_dir = Path.cwd()
    with clone_in_temp_directory() as temp_dir:
        git.Repo.clone_from(repo_url, temp_dir)
        create_environ_file(cwd_dir, temp_dir)


def create_environ_file(repo_path, temp_dir):
    """Create a conda environment file.

    Args:
        repo_path (str): The path to the repository.
    """
    file_name = "environment.yaml"
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


def extract_user_repo_from_url(url):
    pattern = r"github.com/([^/]+)/([^/]+)"
    match = re.search(pattern, url)
    if match:
        user, repo = match.groups()
        return f"{user}/{repo}", repo
    else:
        raise ValueError("Invalid GitHub URL.")


def fetch_github_folder_contents(repo_name):
    ignore_file_types = ["png", "md", "gitignore", "git", "txt", "csv"]
    ignore_file_names = ["LICENSE", "Makefile", "setup.py", "pyproject.toml"]
    ignore_folder_names = ["docs", "setup", "tests", "conf"]

    base_url = f"https://api.github.com/repos/{repo_name}"
    folder_contents = {}

    def should_ignore_file(file_path):
        extension = file_path.split(".")[-1]
        file_name = file_path.split("/")[-1]
        return extension in ignore_file_types or file_name in ignore_file_names

    def should_ignore_folder(folder_path):
        folder_name = folder_path.split("/")[-1]
        return folder_name in ignore_folder_names

    def recurse_contents(path):
        url = f"{base_url}/contents/{path}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return

        contents = response.json()
        if not isinstance(contents, list):
            print(f"Unexpected response: {contents}")
            return

        for item in contents:
            if item["type"] == "dir":
                if should_ignore_folder(item["path"]):
                    continue
                recurse_contents(item["path"])
            else:
                if should_ignore_file(item["path"]):
                    continue

                file_url = item["download_url"]
                response = requests.get(file_url)

                if response.status_code == 200:
                    try:
                        file_content = response.text
                    except UnicodeDecodeError:
                        file_content = (
                            "Could not decode content: non-text or non-UTF-8 file"
                        )
                else:
                    file_content = "Unsupported encoding or empty file"

                folder_contents[item["path"]] = file_content

    recurse_contents("")

    return folder_contents


def extract_dependencies(file_contents):
    if "requirements.txt" in file_contents:
        requirements = file_contents["requirements.txt"].split("\n")
        return requirements
    return []


def get_file_contents(url, file_name):
    file_contents = ""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_contents = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {file_name}: {e}")
    return file_contents


def get_file_extensions(files):
    extensions = defaultdict(int)
    for file in files:
        _, ext = os.path.splitext(file["name"])
        if ext:
            extensions[ext] += 1
    return extensions


def list_files_recursive(url):
    files = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            contents = response.json()
            for item in contents:
                if item["type"] == "file":
                    files.append(item)
                elif item["type"] == "dir":
                    files.extend(list_files_recursive(item["url"]))
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repo contents: {e}")
    return files


def list_dependencies_and_file_extensions(repo_url):
    if not repo_url.startswith("https://github.com/"):
        raise ValueError(
            "Invalid GitHub URL. Please make sure it starts with 'https://github.com/'"
        )

    repo_url = repo_url.rstrip("/")

    repo_api_url = (
        repo_url.replace("https://github.com", "https://api.github.com/repos")
        + "/contents"
    )

    repo_files = list_files_recursive(repo_api_url)

    file_contents = {}
    for file in repo_files:
        if file["name"] == "requirements.txt":
            file_contents["requirements.txt"] = get_file_contents(
                file["download_url"], "requirements.txt"
            )

    dependencies = extract_dependencies(file_contents)
    file_extensions = get_file_extensions(repo_files)
    return dependencies, file_extensions


def get_file_extension_full_name(extension):
    extension_map = {
        ".py": "Python",
        ".js": "JavaScript",
        ".html": "HTML",
        ".css": "CSS",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".rb": "Ruby",
        ".php": "PHP",
        ".go": "Go",
        ".swift": "Swift",
        ".rs": "Rust",
        ".ts": "TypeScript",
        ".kt": "Kotlin",
        ".m": "Objective-C",
        ".scala": "Scala",
        ".dart": "Dart",
        ".groovy": "Groovy",
        ".lua": "Lua",
        ".sh": "Shell",
        ".r": "R",
        ".pl": "Perl",
        ".hs": "Haskell",
        ".coffee": "CoffeeScript",
        ".sql": "SQL",
        ".xml": "XML",
        ".json": "JSON",
        ".yaml": "YAML",
        ".yml": "YAML",
        ".md": "Markdown",
        ".txt": "Text",
    }
    return extension_map.get(extension.lower(), None)


def dependencies_helper(repo_url):
    dependencies, file_extensions = list_dependencies_and_file_extensions(repo_url)
    for ext, _ in file_extensions.items():
        dependencies.append(ext.strip("."))
        full_ext = get_file_extension_full_name(ext)
        if full_ext:
            dependencies.append(full_ext)
    clone_repository(repo_url)
    return dependencies
