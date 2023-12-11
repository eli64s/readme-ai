"""Pytest configuration file."""

import pytest

from readmeai.config.settings import (
    AppConfigModel,
    load_config,
    load_config_helper,
)


@pytest.fixture(scope="session")
def config():
    """Returns the default configuration."""
    return load_config()


@pytest.fixture(scope="session")
def config_helper(config):
    """Returns the default configuration helper."""
    conf_model = AppConfigModel(app=config)
    return load_config_helper(conf_model)
