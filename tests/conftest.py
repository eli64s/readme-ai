"""Pytest configuration file."""

from pathlib import Path

import pytest
import toml


@pytest.fixture(scope="session")
def config():
    current_dir = Path(__file__).parent
    parent_dir = current_dir.parent
    config_path = parent_dir / "settings/config.toml"

    with open(config_path, "r") as file:
        config = toml.load(file)

    return config
