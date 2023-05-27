"""Dependency parsing helper functions for README-AI."""

import re
from typing import List

import toml
import yaml

from factory import FileHandler
from logger import Logger

FILE_HANDLER = FileHandler()
LOGGER = Logger("readmeai_logger")


# Python


def parse_conda_env_file(file):
    """Extracts dependencies from a conda environment file."""
    with open(file) as f:
        data = yaml.safe_load(f)
    dependencies = []
    for package in data.get("dependencies", []):
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            for name, _ in package.items():
                dependencies.append(name)
    return dependencies


def parse_pipfile(file):
    """Extracts dependencies from a Pipfile."""
    data = FILE_HANDLER.read_toml(file)

    packages = data.get("packages", {})
    dev_packages = data.get("dev-packages", {})

    dependencies = []
    for package, _ in packages.items():
        dependencies.append(package)

    for package, _ in dev_packages.items():
        dependencies.append(package)

    return dependencies


def parse_pyproject_toml(file):
    """Extracts dependencies from a pyproject.toml file."""
    data = FILE_HANDLER.read_toml(file)
    dependencies = []
    for package in (
        data.get("tool", {}).get("poetry", {}).get("dependencies", [])
    ):
        dependencies.append(package)
    for package in (
        data.get("tool", {}).get("poetry", {}).get("dev-dependencies", [])
    ):
        dependencies.append(package)
    return dependencies


def parse_requirements_file(file):
    """Extracts dependencies from a requirements.txt file."""
    with open(file) as f:
        lines = f.readlines()

    module_names = []
    for line in lines:
        line = line.strip()

        # Ignore comments and blank lines
        if re.match(r"^\s*(#|$)", line):
            continue

        # Extract the module name
        match = re.match(r"^([a-zA-Z0-9._-]+)", line)
        if match:
            module_name = match.group(1)
            module_names.append(module_name)
    return module_names


# Rust


def parse_cargo_toml(file):
    """Extracts dependencies from a Cargo.toml file."""
    data = FILE_HANDLER.read_toml(file)
    dependencies = []
    for package in data.get("dependencies", []):
        dependencies.append(package)
    for package in data.get("dev-dependencies", []):
        dependencies.append(package)
    return dependencies


def parse_cargo_lock(file):
    """Extracts dependencies from a Cargo.lock file."""
    data = FILE_HANDLER.read_toml(file)
    dependencies = []
    for package in data.get("package", []):
        dependencies.append(package["name"])
    return dependencies


# Javascript and TypeScript


def parse_package_json(file):
    """
    Extracts dependencies from a package.json
    file for both JavaScript and TypeScript.
    """
    data = FILE_HANDLER.read_json(file)
    dependencies = []
    for section in ["dependencies", "devDependencies", "peerDependencies"]:
        if section in data:
            for package, _ in data[section].items():
                # For TypeScript, only keep packages that start with '@types/',
                # and remove the '@types/' prefix from the package name
                if section == "peerDependencies" and package.startswith(
                    "@types/"
                ):
                    dependencies.append(package[7:])
                else:
                    dependencies.append(package)
    return dependencies


def parse_yarn_lock(file):
    """Extracts dependencies from a yarn.lock file."""
    data = FILE_HANDLER.read(file)
    regex = re.compile(r"^(\w[\w\-]*\w)@", re.MULTILINE)
    dependencies = regex.findall(data)
    return list(set(dependencies))


def parse_package_lock_json(file):
    """Extracts TypeScript dependencies from a package-lock.json file."""
    data = FILE_HANDLER.read_json(file)
    dependencies = []
    for package, details in data.get("dependencies", {}).items():
        if package.startswith("@types/"):
            dependencies.append(package[7:])  # Remove '@types/' prefix
    return dependencies


# Go


def parse_go_mod(file_path: str) -> List[str]:
    """
    Extracts dependencies from a Go module file.

    Parameters:
        file_path (str): The path to the Go module file.

    Returns:
        List[str]: A list of the extracted dependencies.
    """
    with open(file_path, "r") as f:
        content = f.read()

    regex = re.compile(r"^require (.+)$", re.MULTILINE)
    dependencies = regex.findall(content)

    return dependencies


def parse_go_sum(file_path: str) -> List[str]:
    """Extracts dependencies from a Go sum file."""
    with open(file_path, "r") as f:
        content = f.read()

    regex = re.compile(r"^([^\s]+)\s([^@]+)", re.MULTILINE)
    dependencies = [match.group(1) for match in regex.finditer(content)]

    return dependencies


# Java


def parse_gradle(file_path):
    with open(file_path) as file:
        content = file.read()

    regex = re.compile(r"implementation\s+['\"]([^'\"]+)['\"]")
    dependencies = regex.findall(content)

    return dependencies


def parse_maven(file_path):
    with open(file_path) as file:
        content = file.read()

    regex = re.compile(
        r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>"
    )
    dependencies = []
    matches = regex.findall(content)
    for match in matches:
        group_id, artifact_id, version = match
        dependency = f"{group_id}:{artifact_id}:{version}"
        dependencies.append(dependency)

    return dependencies


# C/C++

# Makefile
def parse_makefile(file):
    with open(file) as f:
        content = f.read()

    regex = re.compile(r"^\w+\s*[:+]?=\s*(.+)$", re.MULTILINE)
    dependencies = []
    matches = regex.findall(content)
    for match in matches:
        deps = filter(None, match.split())
        dependencies.extend(deps)

    return dependencies


# CMakeLists.txt
def parse_cmake(file):
    with open(file) as f:
        content = f.read()

    regex = re.compile(r"add_executable\([^)]+\s+([^)]+)\)")
    dependencies = regex.findall(content)

    return dependencies


# configure.ac
def parse_configure_ac(file):
    with open(file) as f:
        content = f.read()

    regex = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
    dependencies = regex.findall(content)

    return dependencies


# Makefile.am
def parse_makefile_am(file):
    with open(file) as f:
        content = f.read()

    regex = re.compile(r"bin_PROGRAMS\s*=\s*(.+)")
    dependencies = []
    matches = regex.findall(content)
    for match in matches:
        deps = filter(None, match.split())
        dependencies.extend(deps)

    return dependencies
