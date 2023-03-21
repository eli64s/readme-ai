"""
src/processor.py
"""
import os
import re
from pathlib import Path

import requests

import file_parser
from logger import Logger

LOGGER = Logger("readme_ai_logger")
ACCESS_TOKEN = os.environ["GITHUB_TOKEN"]
IGNORE_FILE_TYPES = [".gitignore", "png"]
IGNORE_FILE_NAMES = ["__init__.py", "badges", "LICENSE", "Makefile", "README.md"]
IGNORE_FOLDER_NAMES = ["conf", "docs", "file_handlers", "imgs", "notebooks", "tests"]
TOOLS_LIST = {
    "bash": "GNU Bash",
    "conda": "Anaconda",
    "json": "JSON",
    "python": "Python",
}


def add_space_between_sentences(text):
    pattern = r"([.!?])(\S)"
    return re.sub(pattern, r"\1 \2", text)


def check_keys_in_string(repo_dict: dict):
    repo_code_str = "\n".join(repo_dict.values())
    badge_list = []
    for key in TOOLS_LIST.keys():
        if key in repo_code_str:
            badge_list.append(TOOLS_LIST[key])
    return list(set(badge_list))


def create_dependency_list(file_names: list, repo_dict: dict):
    all_badges = []
    all_badges.extend(check_keys_in_string(repo_dict))
    dependency_path_map = get_dependency_paths(file_names, repo_dict)

    cwd_path = Path.cwd()
    for file, path in dependency_path_map.items():
        file_path = cwd_path / path

        if "requirements" in file:
            all_badges.extend(file_parser.parse_requirements_file(file_path))

        elif "environment.yaml" in path:
            all_badges.extend(file_parser.parse_conda_env_file(file_path))

    return all_badges


def fetch_github_repo_files_recursive(repo_url):
    repo_api_url = repo_url.replace("github.com", "api.github.com/repos")
    files_dict = {}
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    def fetch_files_in_directory(directory_path):
        contents_url = f"{repo_api_url}/contents/{directory_path}"
        if ACCESS_TOKEN:
            response = requests.get(contents_url, headers=headers)
        else:
            response = requests.get(contents_url)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return

        contents = response.json()

        # Check if the response is a list (as expected)
        if not isinstance(contents, list):
            print(f"Unexpected response format: {contents}")
            return

        for item in contents:
            if item["type"] == "file":
                file_path = item["path"]
                if (
                    any(file_path.endswith(ext) for ext in IGNORE_FILE_TYPES)
                    or file_path in IGNORE_FILE_NAMES
                ):
                    continue

                file_url = item["download_url"]
                if ACCESS_TOKEN:
                    response = requests.get(file_url, headers=headers)
                else:
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

                files_dict[file_path] = file_content

            elif item["type"] == "dir":
                if item["name"] in IGNORE_FOLDER_NAMES:
                    continue

                fetch_files_in_directory(f"{directory_path}/{item['name']}")

    fetch_files_in_directory("")

    return files_dict


def get_dependency_paths(file_names: list, repo_dict: dict):
    dependency_paths = {}
    for path, _ in repo_dict.items():
        file_name = get_file_name(path)
        if file_name in file_names:
            dependency_paths[str(file_name)] = str(path)
    return dependency_paths


def get_file_name(dir_str_path):
    path = Path(dir_str_path)
    return path.name


def get_repo_name(url):
    pattern = r"github.com/([^/]+)/([^/]+)"
    match = re.search(pattern, url)
    if match:
        user, repo = match.groups()
        return f"{user}/{repo}", repo
    else:
        raise ValueError("Invalid GitHub URL.")
