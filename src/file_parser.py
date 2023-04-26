"""File parser module."""
import os
import re
from typing import List

import toml
import yaml

from logger import Logger

LOGGER = Logger("readme_ai_logger")


def list_files(directory: str) -> List[str]:
    file_list = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            file_list.append(os.path.join(root, f))
    return file_list


def parse_conda_env_file(file_path):
    with open(file_path, "r") as f:
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
    with open(file_path, "r") as file:
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


"""
def find_dependencies(file_names, directory_path):
    # Dictionary to store dependency parsers
    parsers = {
        "requirements.txt": parse_requirements_files,
        "requirements-dev.txt": parse_requirements_files,
        "requirements.in": parse_requirements_files,
        "requirements-prod.txt": parse_requirements_files,
        "requirements.test.txt": parse_requirements_files,
        "requirements.txt": parse_requirements_files,
        "Pipfile": parse_pipfile,
        "Gemfile": parse_gemfile,
        "Cargo.lock": parse_cargo_lock,
        "Cargo.toml": parse_cargo_toml,
        "build.gradle": parse_build_gradle,
        "build.sbt": parse_build_sbt,
        "composer.json": parse_composer_json,
        "composer.lock": parse_composer_lock,
        "conda.yml": parse_conda_yaml,
        "dependencies.yml": parse_conda_yaml,
        "environment.yml": parse_conda_yaml,
        "snapcraft.yaml": parse_snapcraft_yaml,
        "snap/snapcraft.yaml": parse_snapcraft_yaml,
        "snapcraft-deps.yaml": parse_snapcraft_deps_yaml,
        "snap/snapcraft-deps.yaml": parse_snapcraft_deps_yaml,
        "snapcraft-deps-lock.yaml": parse_snapcraft_deps_lock_yaml,
        "snap/snapcraft-deps-lock.yaml": parse_snapcraft_deps_lock_yaml,
        "pyproject.toml": parse_pyproject_toml,
        "mix.exs": parse_mixfile,
        "mix.lock": parse_mixfile,
        "shadow-cljs.edn": parse_shadow_cljs,
        "build.boot": parse_boot_clj,
        "build.boot.repl": parse_boot_clj,
        "deps.clj.edn": parse_deps_clj,
        "deps.edn": parse_deps_edn,
        "deps.json": parse_deps_json,
        "deps.kts": parse_deps_kts,
        "deps.cljs.edn": parse_deps_cljs_edn,
        "yarn.lock": parse_yarn_lock_file,
        "package.json": parse_package_json_file,
    }

    # List to store dependencies
    dependencies = []

    # Loop through the file names
    for file_name in file_names:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            # Get the parser function for this file type
            parser = parsers.get(file_name)

            if parser:
                with open(file_path, "r") as f:
                    # Parse the dependencies using the appropriate parser
                    file_dependencies = parser(f)
                    dependencies.extend(file_dependencies)

    for short_name, _ in PACKAGE_MAP.items():
        if short_name in dependencies:
            dependencies.append(PACKAGE_MAP[short_name])

    return dependencies


def parse_requirements_files(directory_path):
    requirement_files = [
        "requirements-dev.txt",
        "requirements.in",
        "requirements-prod.txt",
        "requirements.test.txt",
        "requirements.txt",
    ]

    dependencies = []

    for file_name in requirement_files:
        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                lines = [line.strip() for line in f.readlines()]

            for line in lines:
                # Ignore comments and blank lines
                if re.match(r"^\s*(#|$)", line):
                    continue

                # Parse package name and version range
                match = re.match(r"^([a-zA-Z0-9._-]+)\s*(?:([!=<>]+).+)?$", line)

                if match:
                    package_name = match.group(1)
                    dependencies.append(package_name)

    return dependencies


def parse_conda_yaml(file):
    data = yaml.safe_load(file)
    dependencies = []
    for package in data.get("dependencies", []):
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            for name, version in package.items():
                dependencies.append(name)
    return dependencies





def parse_gemfile(file):
    lines = [line.strip() for line in file.readlines()]
    dependencies = []
    for line in lines:
        if line.startswith("gem "):
            package = line.split()[1].strip("'\"")
            dependencies.append(package)
    return dependencies


def parse_cargo_lock(file):
    data = toml.load(file)
    dependencies = []
    for package in data.get("package", []):
        dependencies.append(package["name"])
    return dependencies


def parse_cargo_toml(file):
    data = toml.load(file)
    dependencies = []
    for package in data.get("dependencies", []):
        dependencies.append(package)
    for package in data.get("dev-dependencies", []):
        dependencies.append(package)
    return dependencies


def parse_build_gradle(file):
    lines = [line.strip() for line in file.readlines()]
    dependencies = []
    for line in lines:
        if line.startswith("implementation ") or line.startswith("compile "):
            package = line.split()[-1].strip("'")
            dependencies.append(package)
    return dependencies


def parse_build_sbt(file):
    lines = [line.strip() for line in file.readlines()]
    dependencies = []
    for line in lines:
        if line.startswith("libraryDependencies += "):
            package = line.split()[-1].strip('"')
            dependencies.append(package)
    return dependencies


def parse_composer_json(file):
    data = json.load(file)
    dependencies = []
    for package, version in data.get("require", {}).items():
        dependencies.append(package)
    for package, version in data.get("require-dev", {}).items():
        dependencies.append(package)
    return dependencies


def parse_composer_lock(file):
    data = json.load(file)
    dependencies = []
    for package, version in data.get("packages", {}).items():
        dependencies.append(package)
    return dependencies


def parse_conda_env_file(file):
    data = yaml.safe_load(file)
    dependencies = []
    for package in data.get("dependencies", []):
        if isinstance(package, str):
            dependencies.append(package.split("=")[0])
        elif isinstance(package, dict):
            for name, version in package.items():
                dependencies.append(name)
    return dependencies


def parse_snapcraft_yaml(file):
    data = yaml.safe_load(file)
    dependencies = []
    for app in data.get("apps", {}).values():
        for package in app.get("stage-packages", []):
            dependencies.append(package)
        for package in app.get("build-packages", []):
            dependencies.append(package)
    return dependencies


def parse_snapcraft_deps_yaml(file):
    data = yaml.safe_load(file)
    dependencies = []
    for package in data.get("packages", []):
        dependencies.append(package)
    return dependencies


def parse_snapcraft_deps_lock_yaml(file):
    data = yaml.safe_load(file)
    dependencies = []
    for package in data.get("snapcraft-packages", []):
        dependencies.append(package)
    return dependencies




def parse_mixfile(file):
    data = toml.load(file)
    dependencies = []
    for package, version in data.get("dependencies", {}).items():
        dependencies.append(package)
    for package, version in data.get("dev_dependencies", {}).items():
        dependencies.append(package)
    return dependencies


def parse_shadow_cljs(file):
    data = edn.loads(file.read())
    dependencies = []
    for package in data.get(":dependencies", []):
        dependencies.append(package)
    return dependencies


def parse_boot_clj(file):
    data = edn.loads(file.read())
    dependencies = []
    for package in data.get(":dependencies", []):
        dependencies.append(package)
    for package in data.get(":extra-deps", []):
        dependencies.append(package)
    return dependencies


def parse_deps_clj(file):
    data = edn.loads(file.read())
    dependencies = []
    for package, version in data.get(":deps", {}).items():
        dependencies.append(package)
    return dependencies


def parse_deps_edn(file):
    data = edn.loads(file.read())
    dependencies = []
    for package, version in data.get(
        ":deps",
    ).items():
        dependencies.append(package)
    return dependencies


def parse_deps_json(file):
    data = json.load(file)
    dependencies = []
    for package, version in data.items():
        dependencies.append(package)
    return dependencies


def parse_deps_kts(file):
    lines = [line.strip() for line in file.readlines()]
    dependencies = []
    for line in lines:
        if line.startswith("dependencies {") or line.startswith("implementation "):
            continue
        if line == "}":
            break
        package = line.split(":")[-1].strip("'")
        dependencies.append(package)
    return dependencies


def parse_deps_cljs_edn(file):
    data = edn.loads(file.read())
    dependencies = []
    for package, version in data.get(":deps", {}).items():
        dependencies.append(package)
    for package, version in data.get(":extra-deps", {}).items():
        dependencies.append(package)
    return dependencies


def parse_yarn_lock(file):
    lines = [line.strip() for line in file.readlines()]
    dependencies = []
    for i, line in enumerate(lines):
        if line.startswith("#"):
            continue
        if line.startswith("http"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            dependencies.append(lines[i - 1].split("@")[0])
    return dependencies


def parse_package_json(file):
    data = json.load(file)
    dependencies = []
    for package, version in data.get("dependencies", {}).items():
        dependencies.append(package)
    for package, version in data.get("devDependencies", {}).items():
        dependencies.append(package)
    return dependencies


def parse_requirements_file(directory_path):
    requirement_files = [
        "requirements-dev.txt",
        "requirements.in",
        "requirements-prod.txt",
        "requirements.test.txt",
        "requirements.txt",
    ]

    dependencies = []

    for file_name in requirement_files:
        file_path = os.path.join(directory_path, file_name)

        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                lines = [line.strip() for line in f.readlines()]

            for line in lines:
                # Ignore comments and blank lines
                if re.match(r"^\s*(#|$)", line):
                    continue

                # Parse package name and version range
                match = re.match(r"^([a-zA-Z0-9._-]+)\s*(?:([!=<>]+).+)?$", line)

                if match:
                    package_name = match.group(1)
                    dependencies.append(package_name)

    return dependencies


def parse_yarn_lock_file(file):
    lines = [line.strip() for line in file.readlines()]
    dependencies = []
    for i, line in enumerate(lines):
        if line.startswith("#"):
            continue
        if line.startswith("http"):
            continue
        if line.startswith(" ") or line.startswith("\t"):
            dependencies.append(lines[i - 1].split("@")[0])
    return dependencies


def parse_package_json_file(file):
    data = json.load(file)
    dependencies = []
    for package, version in data.get("dependencies", {}).items():
        dependencies.append(package)
    for package, version in data.get("devDependencies", {}).items():
        dependencies.append(package)
    return dependencies
"""
