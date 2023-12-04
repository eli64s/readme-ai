"""Pytest configuration file."""

import pytest

from readmeai.config.settings import AppConfigModel, ConfigHelper, load_config


@pytest.fixture(scope="session")
def config():
    config_dict = load_config()
    config_model = AppConfigModel(app=config_dict)
    return config_model


@pytest.fixture(scope="session")
def config_helper(config):
    return ConfigHelper(config)
