"""Tests for Python dependency and package manager file parsers."""

from readmeai.parsers.python import RequirementsParser, TomlParser, YamlParser


def test_requirements_parser():
    """Tests the requirements.txt parser."""
    content = """
    # This is a comment
    aiohttp==3.8.6
    aiosignal==1.3.1
    gitpython==3.1.40 ; python_full_version >= "3.8.1" and python_full_version < "4.0.0"
    """
    parser = RequirementsParser()
    expected_dependencies = ["aiohttp", "aiosignal", "gitpython"]
    assert parser.parse(content) == expected_dependencies


def test_pipfile_parser():
    """Tests the Pipfile parser."""
    content = """
    [[source]]
    url = "https://pypi.org/simple"
    verify_ssl = true
    name = "pypi"

    [packages]
    aiohttp = "==3.8.6"
    aiosignal = "==1.3.1"

    [dev-packages]
    pytest = "==6.2.5"

    [requires]
    python_version = "3.11"
    """
    parser = TomlParser()
    expected_dependencies = ["aiohttp", "aiosignal", "pytest"]
    assert parser.parse(content).sort() == expected_dependencies.sort()


def test_pyproject_poetry_parser():
    """Tests the pyproject.toml parser."""
    content = """
    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"

    [tool.poetry.dependencies]
    python = "^3.8.1"
    click = "^8.1.7"

    [tool.poetry.dev-dependencies]
    black = "*"
    flake8 = "*"
    isort = "*"
    pytest = "*"
    pytest-cov = "*"
    pre-commit = "*"
    """
    parser = TomlParser()
    expected_dependencies = [
        "python",
        "click",
        "black",
        "flake8",
        "isort",
        "pytest",
        "pytest-cov",
        "pre-commit",
    ]
    assert parser.parse(content).sort() == expected_dependencies.sort()


def test_pyproject_flit_parser():
    """Tests the pyproject.toml parser for Flit."""
    content = """
    [build-system]
    requires = ["flit_core >=3,<4"]
    build-backend = "flit_core.buildapi"

    [project]
    dependencies = [
        "requests >=2.6",
        "configparser; python_version == '2.7'",
    ]

    [project.optional-dependencies]
    test = [
        "pytest >=2.7.3",
        "pytest-cov",
    ]
    doc = ["sphinx"]
    """
    parser = TomlParser()
    expected_dependencies = [
        "requests",
        "configparser",
        "pytest",
        "pytest-cov",
        "sphinx",
    ]
    assert parser.parse(content).sort() == expected_dependencies.sort()


def test_conda_env_yaml_parser():
    """Tests the conda environment.yml parser."""
    content = """
    name: readmeai
    channels:
    - conda-forge
    - defaults
    dependencies:
    - python>=3.9
    - pip
    - pip:
        - pandas==1.3.3
        - snowflake-connector-python==2.4.6
    """
    parser = YamlParser()
    expected_dependencies = [
        "python",
        "pip",
        "pandas",
        "snowflake-connector-python",
    ]
    assert parser.parse(content) == expected_dependencies


def test_requirements_parser_success():
    content = "package1\npackage2==1.0\n# Comment"
    parser = RequirementsParser()
    assert parser.parse(content) == ["package1", "package2"]


def test_requirements_parser_regex_error():
    content = "[Invalid Regex"
    parser = RequirementsParser()
    data = parser.parse(content)
    assert data == []


def test_toml_parser_toml_decode_error():
    content = "[Invalid TOML"
    parser = TomlParser()
    data = parser.parse(content)
    assert data == []


def test_yaml_parser_success():
    content = "dependencies:\n  - package1\n  - package2=1.0"
    parser = YamlParser()
    assert parser.parse(content) == ["package1", "package2"]


def test_yaml_parser_yaml_error():
    content = "{Invalid YAML"
    parser = YamlParser()
    data = parser.parse(content)
    assert data == []
