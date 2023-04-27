"""Unit tests for conf.py"""

import pytest

from src.conf import AppConf, AppConfHelper, load_conf_helper


def test_appconf():
    conf = AppConf()
    assert conf.api.api_key == ""
    assert (
        conf.api.prompt_intro
        == """Generate a short summary that describes the capabilities of the GitHub project {}."""
    )
    assert conf.api.prompt_slogan == """Generate a slogan for the GitHub project {}."""
    assert conf.github.local == ""
    assert conf.github.name == ""
    assert conf.github.path == ""
    assert conf.github.remote == "https://github.com/eli64s/readme-ai"
    assert conf.paths.file_extensions == "file_extensions.toml"
    assert conf.paths.file_names == "file_names.toml"
    assert conf.paths.ignore_files == "ignore_files.toml"
    assert conf.paths.setup_guide == "setup_guide.toml"
    assert conf.paths.badges == "conf/badges.json"
    assert conf.paths.docs == "docs/raw_data.csv"
    assert conf.paths.md == "docs/README.md"


def test_appconfhelper():
    conf = AppConfHelper()
    helper = load_conf_helper(conf)
    assert isinstance(helper.file_names, list)
    assert isinstance(helper.file_extensions, dict)
    assert isinstance(helper.ignore_files, list)
    assert isinstance(helper.setup, dict)
