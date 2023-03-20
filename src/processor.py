"""
src/processor.py
"""
import collections
import os
import re
import shutil
import subprocess
import tempfile
from collections import defaultdict
from contextlib import contextmanager
from pathlib import Path

import requests
import toml

config = toml.load(Path("conf/file_extensions_map.toml").resolve())
extension_map = config["extensions"]


def add_space_between_sentences(text):
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


@contextmanager
def clone_repository(repo_url: str):
    _, repo_name = get_repo_name(repo_url)
    if not repo_name:
        print("Invalid GitHub repo URL.")
        return ""

    temp_dir = tempfile.mkdtemp()
    cloned_repo_path = os.path.join(temp_dir, repo_name)

    try:
        subprocess.run(["git", "clone", repo_url, repo_name], cwd=temp_dir, check=True)
        yield cloned_repo_path
    except Exception as e:
        print(f"Error: {e}")
    finally:
        shutil.rmtree(temp_dir)


def detect_primary_language(repo_path: str) -> str:
    # Get the output of the "git ls-files" command
    try:
        git_ls_files_output = subprocess.check_output(
            ["git", "ls-files"], stderr=subprocess.DEVNULL, cwd=repo_path
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""

    # Convert the output to a list of file paths
    file_paths = git_ls_files_output.decode("utf-8").strip().split("\n")

    # Count the number of files for each extension
    extensions_counts = collections.defaultdict(int)
    for file_path in file_paths:
        extension = os.path.splitext(file_path)[1]
        extensions_counts[extension] += 1

    # Count the number of files for each programming language
    language_counts = collections.defaultdict(int)
    for extension, count in extensions_counts.items():
        if extension in extension_map:
            language = extension_map[extension]
            language_counts[language] += count

    # Get the most common programming language based on the number of files
    top_language = max(language_counts.items(), key=lambda x: x[1])[0]
    return top_language


def extract_dependencies(file_contents):
    if "requirements.txt" in file_contents:
        requirements = file_contents["requirements.txt"].split("\n")
        return requirements
    return []


def fetch_github_folder_contents(repo_name):
    ignore_file_types = ["csv", "git", "gitignore", "md", "png", "txt"]
    ignore_file_names = ["LICENSE", "Makefile", "setup.py", "pyproject.toml"]
    ignore_folder_names = ["conf", "docs", "setup", "tests"]
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


def generate_user_instructions(md: str, name: str, url: str, language: str) -> str:
    config = toml.load(Path("conf/language_instructions.toml").resolve())
    instructions = config["language_instructions"]

    if not name:
        print("Invalid GitHub repo URL.")
        return ""

    language_instructions = instructions.get(language)
    if not language_instructions:
        # logger.info(f"Instructions for {language} not found.")
        return ""

    install = language_instructions[0]
    running = language_instructions[1]
    markdown = md.format(name=name, url=url, install=install, running=running)
    return markdown


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
            ext_name = extension_map.get(ext.lower(), None)
            extensions[ext_name] += 1
    return extensions


def get_repo_language(repo_url: str) -> str:
    with clone_repository(repo_url) as repo_path:
        if repo_path:
            primary_language = detect_primary_language(repo_path)
        return primary_language


def get_repo_name(url):
    pattern = r"github.com/([^/]+)/([^/]+)"
    match = re.search(pattern, url)
    if match:
        user, repo = match.groups()
        return f"{user}/{repo}", repo
    else:
        raise ValueError("Invalid GitHub URL.")


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
        raise (f"Error fetching repo contents: {e}")
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


def dependencies_helper(repo_url):
    dependencies, file_extensions = list_dependencies_and_file_extensions(repo_url)
    for ext, _ in file_extensions.items():
        if ext:
            dependencies.append(ext.lower().strip("."))
    return [s.split("=")[0] for s in dependencies if "=" in s]


def clone_repository_helper(md: str, repo_name: str, repo_url: str) -> str:
    with clone_repository(repo_url) as repo_path:
        if repo_path:
            primary_language = detect_primary_language(repo_path)
            md_instructions = generate_user_instructions(
                md, repo_name, repo_url, primary_language
            )
        else:
            print("Error cloning the repository.")
        return md_instructions
