"""Pytest fixtures for reuse across the test suite."""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import structlog
from _pytest._py.path import LocalPath
from structlog.testing import LogCapture

from readmeai.config.settings import Settings
from readmeai.ingestion.models import (
    FileContext,
    QuickStart,
    RepositoryContext,
)
from readmeai.models.gemini import GeminiHandler
from readmeai.models.offline import OfflineHandler
from readmeai.models.openai import OpenAIHandler
from readmeai.utils.file_handler import FileHandler

pytest_plugins = "pytester"

if sys.version_info < (3, 11):
    import tomli as toml
else:
    import tomllib as toml


# -- Logging -------------------------------------------------------


@pytest.fixture(name="log_output")
def fixture_log_output() -> LogCapture:
    return LogCapture()


@pytest.fixture(autouse=True)
def fixture_configure_structlog(log_output: LogCapture) -> None:
    structlog.configure(processors=[log_output])


# -- Paths -------------------------------------------------------


@pytest.fixture
def output_file_path(tmp_path: Path) -> str:
    return str(tmp_path / "test_readme_ai.md")


@pytest.fixture
def temp_dir(tmpdir: LocalPath) -> LocalPath:
    return tmpdir


# -- readmeai.config -------------------------------------------------------


@pytest.fixture(scope="session")
def config_fixture() -> Settings:
    return Settings().config


@pytest.fixture(scope="session")
def config_fixture() -> Settings:
    return Settings()


# -- readmeai.models -------------------------------------------------------


@pytest.fixture(scope="session")
def ollama_localhost() -> str:
    return "http://localhost:11434/"


@pytest.fixture
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
def openai_handler(config_fixture: Settings):
    config_fixture.config.llm.api = "OPENAI"
    config_fixture.config.llm.model = "gpt-3.5-turbo"
    return OpenAIHandler(config_fixture, MagicMock())


@pytest.fixture
def offline_handler(config_fixture: Settings):
    with patch.dict("os.environ", {}, clear=True):
        config_fixture.config.llm.api = "OFFLINE"
        config_fixture.config.llm.model = "offline"
        yield OfflineHandler(config_fixture, MagicMock())


@pytest.fixture
def gemini_handler(config_fixture: Settings):
    with patch.dict(
        "os.environ",
        {
            "GOOGLE_API_KEY": "sk-test-key",
        },
    ):
        config_fixture.config.llm.api = "GEMINI"
        config_fixture.config.llm.model = "gemini-pro"
        yield GeminiHandler(config_fixture, MagicMock())


# -- readmeai.utils.file_handler -------------------------------------------------------


@pytest.fixture
def file_handler():
    return FileHandler()


@pytest.fixture
def json_file_path_fixture():
    return Path("mock/path/file.json")


@pytest.fixture
def json_data_fixture():
    return json.dumps({"key": "value"})


@pytest.fixture
def toml_file_path_fixture():
    return Path("mock/path/file.toml")


@pytest.fixture
def toml_data_fixture():
    return toml.dumps({"key": "value"})


# -- readmeai.ingestion -------------------------------------------------------


@pytest.fixture(scope="session")
def dependencies_fixture():
    """
    Project dependencies fixture.
    """
    return ["python", "pytest", "pytest-cov", "black", "flake8", "mypy"]


@pytest.fixture(scope="session")
def file_summaries_fixture() -> list[tuple[str, str]]:
    """
    LLM generated file summaries.
    """
    return [
        ("/path/to/file1.py", "This is summary for file1.py"),
        ("/path/to/file2.py", "This is summary for file2.py"),
        (".github/workflows/ci.yml", "This is summary for ci.yml"),
    ]


@pytest.fixture(scope="session")
def repository_context_fixture() -> RepositoryContext:
    """
    Pytest fixture for the RepositoryContext model.
    """
    return RepositoryContext(
        files=[
            FileContext(
                path="requirements.txt",
                name="requirements.txt",
                ext="txt",
                content="pandas asyncio aiohttp aioresponses apache-flink apache-kafka pandas pyflink",
                language="requirements.txt",
                dependencies=[
                    "pandas",
                    "asyncio",
                    "aiohttp",
                    "aioresponses",
                    "apache-flink",
                    "apache-kafka",
                    "pandas",
                    "pyflink",
                ],
            ),
            FileContext(
                path="setup.py",
                name="setup.py",
                ext="py",
                content='''""" setup.py """
from pathlib import Path
from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

with open(Path(BASE_DIR, "requirements.txt"), "r") as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = ["mkdocs==1.3.0", "mkdocstrings==0.18.1"]
style_packages = ["black==22.3.0", "flake8==3.9.2", "isort==5.10.1"]
test_packages = ["pytest==7.1.2", "pytest-cov==2.10.1", "great-expectations==0.15.15"]

setup(
    name="STREAM-ON",
    version=0.1,
    description="",
    author="",
    author_email="",
    url="",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages + test_packages + ["pre-commit==2.19.0"],
        "test": test_packages,
    },
)
                ''',
                language="python",
                dependencies=[],
            ),
        ],
        dependencies=[
            "pip",
            "python",
            "conf.toml",
            "requirements.txt",
            "shell",
            "flink-config.yaml",
            "aiohttp",
            "pyflink",
            "apache-kafka",
            "asyncio",
            "pandas",
            "apache-flink",
            "aioresponses",
        ],
        languages=[
            "python",
            "conf.toml",
            "requirements.txt",
            "shell",
            "flink-config.yaml",
        ],
        language_counts={"txt": 1, "py": 4, "sh": 3, "yaml": 1, "toml": 1},
        metadata={
            "cicd": {},
            "containers": {},
            "documentation": {},
            "package_managers": {"pip": "requirements.txt"},
        },
        quickstart=QuickStart(
            primary_language="Python",
            language_counts={"txt": 1, "py": 4, "sh": 3, "yaml": 1, "toml": 1},
            package_managers={"pip": "requirements.txt"},
            containers={},
            install_commands="""
                **Using `pip`** &nbsp;
                [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

                ```sh
                ⨯ pip install -r requirements.txt
                ```
            """,
            usage_commands="""
                **Using `pip`** &nbsp;
                [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

                ```sh
                ⨯ python {entrypoint}
                ```
            """,
            test_commands="""
                **Using `pip`** &nbsp;
                [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

                ```sh
                ⨯ pytest
                ```
            """,
        ),
    )


# -- readmeai.templates -------------------------------------------------------
