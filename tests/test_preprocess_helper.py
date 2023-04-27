"""Unit tests for preprocess_helper.py."""

from src import logger
from src import preprocess_helper as helper


def test_parse_conda_env_file():
    file_path = "test_data/conda_env.yaml"
    expected_output = ["numpy", "pandas", "matplotlib"]
    assert helper.parse_conda_env_file(file_path) == expected_output


def test_parse_pipfile():
    file_path = "test_data/Pipfile"
    expected_output = ["requests", "flask", "flask-restful"]
    with open(file_path) as f:
        assert helper.parse_pipfile(f) == expected_output


def test_parse_pyproject_toml():
    file_path = "test_data/pyproject.toml"
    expected_output = ["numpy", "pandas", "matplotlib"]
    with open(file_path) as f:
        assert helper.parse_pyproject_toml(f) == expected_output


def test_parse_requirements_file():
    file_path = "test_data/requirements.txt"
    expected_output = ["numpy", "pandas", "matplotlib"]
    assert helper.parse_requirements_file(file_path) == expected_output


def test_parse_cargo_toml():
    file_path = "test_data/Cargo.toml"
    expected_output = ["serde", "tokio", "log"]
    with open(file_path) as f:
        assert helper.parse_cargo_toml(f) == expected_output


def test_parse_cargo_lock():
    file_path = "test_data/Cargo.lock"
    expected_output = ["serde", "tokio", "log"]
    with open(file_path) as f:
        assert helper.parse_cargo_lock(f) == expected_output


def test_parse_package_json():
    file_path = "test_data/package.json"
    expected_output = ["express", "lodash", "debug"]
    with open(file_path) as f:
        assert helper.parse_package_json(f) == expected_output


def test_parse_yarn_lock():
    file_path = "test_data/yarn.lock"
    expected_output = ["express", "lodash", "debug"]
    with open(file_path) as f:
        assert helper.parse_yarn_lock(f) == expected_output
