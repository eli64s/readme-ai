"""Methods to parse and extract dependency file metadata."""

import json
import re
from typing import List

import toml
import yaml

from . import logger

logger = logger.Logger(__name__)


def parse_docker_compose(content: str) -> List[str]:
    """Extracts services from a docker-compose.yaml file."""
    try:
        data = yaml.safe_load(content)
        if isinstance(data, dict) and "services" in data:
            return list(data["services"].keys())
        else:
            logger.error("Invalid docker-compose.yaml file format")
    except yaml.YAMLError as excinfo:
        logger.error(f"Error parsing docker-compose.yaml: {str(excinfo)}")
    return []


def parse_conda_env_file(content: str) -> List[str]:
    """Extracts dependencies from a conda environment file."""
    try:
        data = yaml.safe_load(content)
        if isinstance(data, dict) and "dependencies" in data:
            dependencies = []
            for package in data["dependencies"]:
                if isinstance(package, str):
                    dependencies.append(package.split("=")[0])
                elif isinstance(package, dict):
                    dependencies.extend(package.keys())
            return dependencies
    except yaml.YAMLError as excinfo:
        logger.error(f"Error parsing conda environment file: {str(excinfo)}")
    return []


def parse_pipfile(content: str) -> List[str]:
    """Extracts dependencies from a Pipfile."""
    try:
        data = toml.loads(content)
        packages = data.get("packages", {})
        dev_packages = data.get("dev-packages", {})
        return list(packages.keys()) + list(dev_packages.keys())
    except toml.TomlDecodeError as excinfo:
        logger.error(f"Error parsing Pipfile: {str(excinfo)}")
    return []


def parse_pipfile_lock(content: str) -> List[str]:
    """Extracts dependencies from a Pipfile.lock."""
    try:
        data = json.loads(content)
        default_packages = data.get("default", {})
        develop_packages = data.get("develop", {})
        return list(default_packages.keys()) + list(develop_packages.keys())
    except json.JSONDecodeError as excinfo:
        logger.error(f"Error parsing Pipfile.lock: {str(excinfo)}")
    return []


def parse_poetry_lock(content: str) -> List[str]:
    """Extracts dependencies from a poetry.lock file."""
    try:
        sections = content.split("[[package]]")
        # Skip 1st section as it contains metadata not relevant to packages
        packages = []
        for section in sections[1:]:
            lines = section.strip().splitlines()
            for line in lines:
                if line.startswith("name = "):
                    package_name = line.split('"')[1]
                    packages.append(package_name)
                    break
        return packages
    except Exception as excinfo:
        logger.error(f"Error parsing poetry.lock: {str(excinfo)}")
        return []


def parse_pyproject_toml(content: str) -> List[str]:
    """Extracts dependencies from a pyproject.toml file."""
    try:
        parsed_content = toml.loads(content)
        tool_section = parsed_content.get("tool", {})
        poetry_section = tool_section.get("poetry", {})
        dependencies = poetry_section.get("dependencies", {})
        optional_dependencies = poetry_section.get("optional-dependencies", {})
        return list(dependencies.keys()) + [
            dep_name
            for dep_list in optional_dependencies.values()
            for dep_name in dep_list
        ]
    except Exception as excinfo:
        logger.error(f"Error parsing pyproject.toml: {str(excinfo)}")
        return []


def parse_requirements_file(content: str) -> List[str]:
    """Extracts dependencies from a requirements.txt file."""
    lines = content.splitlines()
    package_names = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.match(r"^\s*([a-zA-Z0-9._-]+)", line)
        if match:
            package_names.append(match.group(1))
    return package_names


def parse_cargo_toml(content: str) -> List[str]:
    """Extracts dependencies from a Cargo.toml file."""
    try:
        dependencies = re.findall(r"\[dependencies\.(.*?)\]", content)
        return dependencies
    except re.error as excinfo:
        logger.error(f"Error parsing Cargo.toml: {str(excinfo)}")
    return []


def parse_cargo_lock(content: str) -> List[str]:
    """Extracts dependencies from a Cargo.lock file."""
    try:
        data = toml.loads(content)
        packages = data.get("package", [])
        return [package.get("name") for package in packages]
    except toml.TomlDecodeError as excinfo:
        logger.error(f"Error parsing Cargo.lock: {str(excinfo)}")
    return []


def parse_package_json(content: str) -> List[str]:
    """Extracts dependencies from a package.json file."""
    try:
        data = json.loads(content)
        package_names = []
        for section in ["dependencies", "devDependencies", "peerDependencies"]:
            if section in data:
                package_names.extend(data[section].keys())
        return package_names
    except json.JSONDecodeError as excinfo:
        logger.error(f"Error parsing package.json: {str(excinfo)}")
    return []


def parse_yarn_lock(content: str) -> List[str]:
    """Extracts dependencies from a yarn.lock file."""
    try:
        return re.findall(r"(\S+)(?=@)", content)
    except re.error as excinfo:
        logger.error(f"Error parsing yarn.lock: {str(excinfo)}")
    return []


def parse_package_lock_json(content: str) -> List[str]:
    """Extracts dependencies from a package-lock.json file."""
    try:
        data = json.loads(content)
        dependencies = data.get("dependencies", {})
        return [
            package[7:]
            for package in dependencies.keys()
            if package.startswith("@types/")
        ]
    except json.JSONDecodeError as excinfo:
        logger.error(f"Error parsing package-lock.json: {str(excinfo)}")
    return []


def parse_go_mod(content: str) -> List[str]:
    """Extracts dependencies from a go.mod file."""
    lines = content.split("\n")
    pattern = r"^\s*([\w\.\-_/]+)\s+v[\w\.\-_/]+"
    regex = re.compile(pattern)
    return [
        regex.match(line.strip()).group(1).split("/")[-1]
        for line in lines
        if regex.match(line.strip())
    ]


def parse_gradle(content: str) -> List[str]:
    """Extracts dependencies from a build.gradle file."""
    dependencies_pattern = r'implementation\([\'"]([^\'"]+):[^\'"]+[\'"]\)'
    return [
        match.split(":")[-2].split(".")[-1]
        for match in re.findall(dependencies_pattern, content)
    ]


def parse_maven(content: str) -> List[str]:
    """Extracts dependencies from a pom.xml file."""
    regex = re.compile(
        r"<dependency>\s*<groupId>([^<]+)</groupId>\s*<artifactId>([^<]+)</artifactId>\s*<version>([^<]+)</version>"
    )
    matches = regex.findall(content)
    return [
        f"{group_id}:{artifact_id}:{version}"
        for group_id, artifact_id, version in matches
    ]


def parse_cmake(content: str) -> List[str]:
    """Extracts dependencies from a CMakeLists.txt file."""
    regex = re.compile(r"add_executable\([^)]+\s+([^)]+)\)")
    package_names = regex.findall(content)
    return package_names


def parse_configure_ac(content: str) -> List[str]:
    """Extracts dependencies from a configure.ac file."""
    regex = re.compile(r"AC_CHECK_LIB\([^)]+\s+([^)]+)\)")
    package_names = regex.findall(content)
    return package_names


def parse_makefile_am(content: str) -> List[str]:
    """Extracts dependencies from a Makefile.am file."""
    regex = re.compile(r"bin_PROGRAMS\s*=\s*(.+)")
    package_names = []
    matches = regex.findall(content)
    for match in matches:
        deps = filter(None, match.split())
        package_names.extend(deps)
    return package_names
