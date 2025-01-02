"""Pytest fixtures to reuse across readmeai.generators submodule."""

import pytest
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import QuickStart
from readmeai.generators.quickstart import QuickStartGenerator

# -- generators.quickstart.py -------------------------------------------------------


@pytest.fixture
def quickstart_fixture():
    return QuickStart(
        primary_language="Python",
        language_counts={"py": 10, "sh": 2},
        package_managers={"pip": "requirements.txt"},
        containers={},
        install_commands="",
        usage_commands="",
        test_commands="",
    )


@pytest.fixture
def quickstart_generator(mock_config_loader: ConfigLoader):
    return QuickStartGenerator(mock_config_loader)
