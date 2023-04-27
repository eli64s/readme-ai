"""Dependency parsing helper functions for README-AI."""

import json
import re
from pathlib import Path
from typing import List

import toml
import yaml

from logger import Logger

LOGGER = Logger("readmeai_logger")


def list_files(directory: str) -> List[str]:
    try:
        path = Path(directory)
        if not path.exists():
            return []
        return [str(p) for p in path.glob("**/*") if p.is_file()]
    except (OSError, TypeError):
        return []


# Python
def parse_conda_env_file(file_path):
    with open(file_path) as f:
        data = yaml.safe_load(f)
    dependencies = []
    for package in data.get("dependencies", []):
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            for name, version in package.items():
                dependencies.append(name)
    return dependencies


def parse_pipfile(file):
    data = json.load(file)
    dependencies = []
    for section in ["packages", "dev-packages"]:
        if section in data:
            for package, version in data[section].items():
                dependencies.append(package)
    return dependencies


def parse_pyproject_toml(file):
    data = toml.load(file)
    dependencies = []
    for package in data.get("tool", {}).get("poetry", {}).get("dependencies", []):
        dependencies.append(package)
    for package in data.get("tool", {}).get("poetry", {}).get("dev-dependencies", []):
        dependencies.append(package)
    return dependencies


def parse_requirements_file(file_path):
    with open(file_path) as file:
        lines = file.readlines()

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
    data = toml.load(file)
    dependencies = []
    for package in data.get("dependencies", []):
        dependencies.append(package)
    for package in data.get("dev-dependencies", []):
        dependencies.append(package)
    return dependencies


def parse_cargo_lock(file):
    data = toml.load(file)
    dependencies = []
    for package in data.get("package", []):
        dependencies.append(package["name"])
    return dependencies


# Javascript
def parse_package_json(file):
    with open(file) as f:
        data = json.load(f)
    dependencies = []
    for section in ["dependencies", "devDependencies"]:
        if section in data:
            for package, version in data[section].items():
                dependencies.append(package)
    return dependencies


def parse_yarn_lock(file):
    with open(file) as f:
        content = f.read()
    regex = re.compile(r"^(\w[\w\-]*\w)@", re.MULTILINE)
    dependencies = regex.findall(content)
    return list(set(dependencies))


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

    # Find all lines starting with "require" and extract the module name
    regex = re.compile(r"^require (.+)$", re.MULTILINE)
    dependencies = regex.findall(content)

    return dependencies


def parse_go_sum(file_path: str) -> List[str]:
    """
    Extracts dependencies from a Go sum file.

    Parameters:
        file_path (str): The path to the Go sum file.

    Returns:
        List[str]: A list of the extracted dependencies.
    """
    with open(file_path, "r") as f:
        content = f.read()

    # Find all lines starting with the module name and extract the version
    regex = re.compile(r"^([^\s]+)\s([^@]+)", re.MULTILINE)
    dependencies = [match.group(1) for match in regex.finditer(content)]

    return dependencies
