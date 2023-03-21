"""Pytest configuration file."""
import tempfile

import pytest


@pytest.fixture
def config_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write("SOME_CONFIG_VALUE=42\n")
        f.flush()
        yield f.name
