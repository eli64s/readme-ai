"""Dependency parsing functions for different programming languages."""

import json
import re
from typing import List

import toml
import yaml

from factory import FileHandler

FILE_HANDLER = FileHandler()

# Docker


def parse_docker_compose(content: str) -> List[str]:
    """Extracts services from a docker-compose.yaml file."""
    data = yaml.safe_load(content)
    try:
        return list(data["services"].keys())
    except KeyError as exc:
        LOGGER.error(f"Error: {str(exc)}")
        return []


# Python


def parse_conda_env_file(file_content: str) -> List[str]:
    """Extracts dependencies from a conda environment file."""
    data = yaml.safe_load(file_content)
    dependencies = []

    if not isinstance(data, dict):
        raise ValueError(f"Invalid content in repository file")

    for package in data.get("dependencies", []):
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            for name, _ in package.items():
                dependencies.append(name)
    return dependencies


def parse_pipfile(file_content: str) -> List[str]:
    """Extracts dependencies from a Pipfile."""
    data = toml.loads(file_content)
    packages = list(data["packages"].keys())
    dev_packages = list(data["dev-packages"].keys())
    return packages + dev_packages


def parse_pipfile_lock(file_content: str) -> List[str]:
    """Extracts dependencies from a Pipfile.lock."""
    data = json.loads(file_content)
    packages = list(data.get("default", {}).keys())
    dev_packages = list(data.get("develop", {}).keys())
    return packages + dev_packages


def parse_pyproject_toml(toml_content: str) -> List[str]:
    """Extracts dependencies from a pyproject.toml file."""
    data = toml.loads(toml_content)
    dependencies = []
    if "dependencies" in data:
        dependencies = data["dependencies"]
    if "optional-dependencies" in data:
        optional_dependencies = data["optional-dependencies"]
        for _, dep_list in optional_dependencies.items():
            dependencies.extend(dep_list)
    return dependencies


def parse_requirements_file(file_content: str) -> List[str]:
    """Extracts dependencies from a requirements.txt file."""
    lines = file_content.splitlines()

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


def parse_cargo_toml(content: str) -> List[str]:
    """Extracts dependencies from a Cargo.toml file."""
    dependencies = re.findall(r"\[dependencies\.(.*?)\]", content)
    return dependencies


def parse_cargo_lock(content: str) -> List[str]:
    data = toml.loads(content)
    packages = data.get("package", [])
    return [package.get("name") for package in packages]


# Javascript & TypeScript


def parse_package_json(content: str) -> List[str]:
    data = json.loads(content)
    package_names = []
    for section in ["dependencies", "devDependencies", "peerDependencies"]:
        if section in data:
            for package, _ in data[section].items():
                if section == "peerDependencies" and package.startswith("@types/"):
                    package_names.append(package[7:])  # Remove '@types/' prefix
                else:
                    package_names.append(package)
    return package_names


def parse_yarn_lock(content: str) -> List[str]:
    return re.findall(r"(\S+)(?=@)", content)


def parse_package_lock_json(content: str) -> List[str]:
    data = json.loads(content)
    return [
        package[7:]
        for package, _ in data.get("dependencies", {}).items()
        if package.startswith("@types/")
    ]


# Go


def parse_go_mod(content: str) -> List[str]:
    lines = content.split("\n")
    pattern = r"^\s*([\w\.\-_/]+)\s+v[\w\.\-_/]+"
    regex = re.compile(pattern)
    return [
        regex.match(line.strip()).group(1).split("/")[-1]
        for line in lines
        if regex.match(line.strip())
    ]


# Java


def parse_gradle(content: str) -> List[str]:
    dependencies_pattern = r'implementation\([\'"]([^\'"]+):[^\'"]+[\'"]\)'
    return [
        match.split(":")[-2].split(".")[-1]
        for match in re.findall(dependencies_pattern, content)
    ]


def parse_maven(content: str) -> List[str]:
    regex = re.compile(
        r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>"
    )
    matches = regex.findall(content)
    return [
        f"{group_id}:{artifact_id}:{version}"
        for group_id, artifact_id, version in matches
    ]


# C/C++


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
