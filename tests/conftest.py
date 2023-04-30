"""Pytest configuration file for the tests directory."""

import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)
