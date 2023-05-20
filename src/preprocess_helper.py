"""Dependency parsing helper functions for README-AI."""

import json
import re
from typing import List

import toml
import yaml

from logger import Logger

LOGGER = Logger("readmeai_logger")


# Python
def parse_conda_env_file(file):
    with open(file) as f:
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
    with open(file) as f:
        data = toml.load(f)

    packages = data.get("packages", {})
    dev_packages = data.get("dev-packages", {})

    dependencies = []
    for package, version in packages.items():
        dependencies.append(package)

    for package, version in dev_packages.items():
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


def parse_requirements_file(file):
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
        # Split the line by spaces and filter out empty strings
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
        # Split the line by spaces and filter out empty strings
        deps = filter(None, match.split())
        dependencies.extend(deps)

    return dependencies
