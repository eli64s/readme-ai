"""Dependency parsing functions for different programming languages."""

import re
from typing import List

from factory import FileHandler
from logger import Logger

FILE_HANDLER = FileHandler()
LOGGER = Logger("readmeai_logger")


# Python


def parse_conda_env_file(file_path: str) -> List[str]:
    """Extracts dependencies from a conda environment file."""
    data = FILE_HANDLER.read_yaml(file_path)
    dependencies = []

    if not isinstance(data, dict):
        raise ValueError(f"Invalid content in repository file: {file_path}")

    for package in data.get("dependencies", []):
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            for name, _ in package.items():
                dependencies.append(name)
    return dependencies


def parse_pipfile(file_path: str) -> List[str]:
    """Extracts dependencies from a Pipfile."""
    data = FILE_HANDLER.read_toml(file_path)
    packages = list(data["packages"].keys())
    dev_packages = list(data["dev-packages"].keys())
    return packages + dev_packages


def parse_pipfile_lock(file_path: str) -> List[str]:
    """Extracts dependencies from a Pipfile.lock."""
    data = FILE_HANDLER.read_json(file_path)
    packages = list(data.get("default", {}).keys())
    dev_packages = list(data.get("develop", {}).keys())
    return packages + dev_packages


def parse_pyproject_toml(file_path: str) -> List[str]:
    """Extracts dependencies from a pyproject.toml file."""
    data = FILE_HANDLER.read_toml(file_path)
    package_names = []
    for package in (
        data.get("tool", {}).get("poetry", {}).get("dependencies", [])
    ):
        package_names.append(package)
    for package in (
        data.get("tool", {}).get("poetry", {}).get("dev-dependencies", [])
    ):
        package_names.append(package)
    return package_names


def parse_requirements_file(file_path: str) -> List[str]:
    """Extracts dependencies from a requirements.txt file."""
    with open(file_path) as f:
        lines = f.readlines()

    package_names = []
    for line in lines:
        line = line.strip()
        if re.match(r"^\s*(#|$)", line):
            continue

        match = re.match(r"^([a-zA-Z0-9._-]+)", line)
        if match:
            module_name = match.group(1)
            package_names.append(module_name)
    return package_names


# Rust


def parse_cargo_toml(file_path: str) -> List[str]:
    """Extracts dependencies from a Cargo.toml file."""
    data = FILE_HANDLER.read_toml(file_path)
    dependencies = list(data.get("dependencies", {}).keys())
    dev_dependencies = list(data.get("dev-dependencies", {}).keys())
    package_names = dependencies + dev_dependencies
    return package_names


def parse_cargo_lock(file_path: str) -> List[str]:
    """Extracts package names from a Cargo.lock file."""
    data = FILE_HANDLER.read_toml(file_path)
    packages = data.get("package", [])
    package_names = [package.get("name") for package in packages]
    return package_names


# Javascript & TypeScript


def parse_package_json(file_path: str) -> List[str]:
    """
    Extracts dependencies from a package.json
    file for both JavaScript and TypeScript.
    """
    data = FILE_HANDLER.read_json(file_path)
    package_names = []
    for section in ["dependencies", "devDependencies", "peerDependencies"]:
        if section in data:
            for package, _ in data[section].items():
                # For TypeScript, only keep packages that start with '@types/',
                # and remove the '@types/' prefix from the package name
                if section == "peerDependencies" and package.startswith(
                    "@types/"
                ):
                    package_names.append(package[7:])
                else:
                    package_names.append(package)
    return package_names


def parse_yarn_lock(file_path: str) -> List[str]:
    """Extracts package names from a yarn.lock file."""
    with open(file_path, "r") as f:
        content = f.read()

    package_names = re.findall(r"(\S+)(?=@)", content)
    return package_names


def parse_package_lock_json(file_path: str) -> List[str]:
    """Extracts TypeScript dependencies from a package-lock.json file."""
    data = FILE_HANDLER.read_json(file_path)
    package_names = []
    for package, _ in data.get("dependencies", {}).items():
        if package.startswith("@types/"):
            package_names.append(package[7:])  # Remove '@types/' prefix
    return package_names


# Go


def parse_go_mod(file_path: str) -> List[str]:
    """
    Extracts dependencies from a Go module file.

    Parameters:
        file_path (str): The path to the Go module file.

    Returns:
        str: A list of the extracted dependencies.
    """
    with open(file_path, "r") as f:
        content = f.readlines()

    pattern = r"^\s*([\w\.\-_/]+)\s+v[\w\.\-_/]+"
    regex = re.compile(pattern)

    package_names = []
    for line in content:
        match = regex.match(line.strip())
        if match:
            last_segment = match.group(1).split("/")[-1]
            package_names.append(last_segment)

    return package_names


# Java


def parse_gradle(file_path: str) -> List[str]:
    """Extracts dependencies from a Gradle file."""
    with open(file_path) as file:
        content = file.read()

    package_names = []
    dependencies_pattern = r'implementation\([\'"]([^\'"]+):[^\'"]+[\'"]\)'
    matches = re.findall(dependencies_pattern, content)

    for match in matches:
        package_name = match.split(":")[-2]
        package_name = package_name.split(".")[-1]
        package_names.append(package_name)

    return package_names


def parse_maven(file_path: str) -> List[str]:
    """Extracts dependencies from a Maven file."""
    with open(file_path) as file:
        content = file.read()

    package_names = []

    regex = re.compile(
        r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>"
    )

    matches = regex.findall(content)
    for match in matches:
        group_id, artifact_id, version = match
        dependency = f"{group_id}:{artifact_id}:{version}"
        package_names.append(dependency)

    return package_names


# C/C++

# Makefile
def parse_makefile(file_path: str) -> List[str]:
    with open(file_path) as f:
        content = f.read()

    regex = re.compile(r"^\w+\s*[:+]?=\s*(.+)$", re.MULTILINE)
    package_names = []
    matches = regex.findall(content)
    for match in matches:
        deps = filter(None, match.split())
        package_names.extend(deps)

    return package_names


# CMakeLists.txt
def parse_cmake(file_path: str) -> List[str]:
    with open(file_path) as f:
        content = f.read()

    regex = re.compile(r"add_executable\([^)]+\s+([^)]+)\)")
    package_names = regex.findall(content)

    return package_names


# configure.ac
def parse_configure_ac(file_path: str) -> List[str]:
    with open(file_path) as f:
        content = f.read()

    regex = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
    package_names = regex.findall(content)

    return package_names


# Makefile.am
def parse_makefile_am(file_path: str) -> List[str]:
    with open(file_path) as f:
        content = f.read()

    regex = re.compile(r"bin_PROGRAMS\s*=\s*(.+)")
    package_names = []
    matches = regex.findall(content)
    for match in matches:
        deps = filter(None, match.split())
        package_names.extend(deps)

    return package_names


# Docker


def parse_docker_compose(file_path: str) -> List[str]:
    """Extracts dependencies from a Docker Compose file."""
    data = FILE_HANDLER.read_yaml(file_path)
    try:
        return data["services"]["app"]["depends_on"]
    except KeyError:
        return []
