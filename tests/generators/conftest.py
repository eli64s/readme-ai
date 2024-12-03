"""
Pytest fixtures to reuse across readmeai.generators submodule.
"""

import pytest

from readmeai.config.settings import Settings
from readmeai.generators.quickstart import QuickStartGenerator
from readmeai.ingestion.models import QuickStart

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
def quickstart_generator(config_fixture: Settings):
    return QuickStartGenerator(config_fixture)
