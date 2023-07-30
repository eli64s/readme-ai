"""Unit tests for the configuration module."""

import sys
from unittest.mock import Mock

import dacite
import pytest

from readmeai.conf import (
    ApiConfig,
    AppConfig,
    GitConfig,
    MarkdownConfig,
    PathsConfig,
    PromptsConfig,
    load_config,
    load_config_helper,
)

sys.path.append("readmeai")


@pytest.fixture
def git_config(config):
    return GitConfig(name=config["git"]["name"], repository=config["git"]["repository"])


@pytest.fixture
def api_config():
    return ApiConfig(
        endpoint="https://api.openai.com",
        engine="gpt-4",
        encoding="utf-8",
        rate_limit=10,
        tokens=50,
        tokens_max=60,
        temperature=0.8,
    )


@pytest.fixture
def markdown_config():
    return MarkdownConfig(
        badges="",
        default="",
        dropdown="",
        ending="",
        header="",
        intro="",
        modules="",
        setup="",
        toc="",
        tree="",
    )


@pytest.fixture
def paths_config():
    return PathsConfig(
        badges="",
        dependency_files="",
        ignore_files="",
        language_names="",
        language_setup="",
        readme="",
    )


@pytest.fixture
def prompts_config():
    return PromptsConfig(code_summary="", features="", overview="", slogan="")


@pytest.fixture
def handler(mocker):
    return mocker.Mock()


@pytest.fixture
def config_data(api_config, git_config, markdown_config, paths_config, prompts_config):
    return {
        "api": api_config,
        "git": git_config,
        "md": markdown_config,
        "paths": paths_config,
        "prompts": prompts_config,
    }


def test_get_repository_name(config, git_config):
    url = config["git"]["repository"]
    name = git_config.get_repository_name(url)
    assert name == config["git"]["name"]


def test_get_repository_name_with_unsupported_host(git_config):
    url = "https://bitbucket.org/username/yourproject"
    with pytest.raises(ValueError):
        git_config.get_repository_name("not a url")


def test_get_repository_name_with_invalid_url(git_config):
    with pytest.raises(ValueError):
        git_config.get_repository_name("not a url")


def test_load_config(mocker, config_data):
    get_config_dict_mock = mocker.patch(
        "src.conf._get_config_dict", return_value=config_data
    )
    dacite_from_dict_mock = mocker.patch(
        "src.conf.dacite.from_dict", return_value=Mock(spec=AppConfig)
    )
    config = load_config("conf.toml")
    get_config_dict_mock.assert_called_once_with(mocker.ANY, "conf.toml")
    dacite_from_dict_mock.assert_called_once_with(AppConfig, config_data)


def test_load_config_with_non_existent_file(mocker):
    mocker.patch("src.conf._get_config_dict", side_effect=FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        load_config("non_existent.toml")


def test_load_config_with_invalid_data(mocker):
    mocker.patch(
        "src.conf._get_config_dict", return_value={"invalid": "data", "api": {}}
    )
    with pytest.raises(dacite.exceptions.MissingValueError):
        load_config("invalid.toml")


def test_load_config_helper(
    mocker, api_config, git_config, markdown_config, paths_config, prompts_config
):
    app_config = AppConfig(
        api=api_config,
        git=git_config,
        md=markdown_config,
        paths=paths_config,
        prompts=prompts_config,
    )
    config_helper_mock = mocker.patch("src.conf.ConfigHelper", return_value=Mock())
    config_helper = load_config_helper(app_config)
    config_helper_mock.assert_called_once_with(conf=app_config)
