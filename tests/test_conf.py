"""Unit tests for the configuration module."""

import sys

sys.path.append("src")

from pathlib import Path
from unittest.mock import MagicMock

from src.conf import (
    AppConfig,
    ConfigHelper,
    GitConfig,
    MarkdownConfig,
    OpenAIConfig,
    PathsConfig,
    load_configuration_helper,
    read_config_file,
    read_helper_configurations,
    update_helper_configurations,
)


def test_openai_config():
    config = OpenAIConfig(
        api_key="test_key",
        prompt_intro="intro",
        prompt_slogan="slogan",
        prompt_code_to_text="code_to_text",
    )
    assert config.api_key == "test_key"
    assert config.prompt_intro == "intro"
    assert config.prompt_slogan == "slogan"
    assert config.prompt_code_to_text == "code_to_text"


def test_git_config():
    config = GitConfig(name="git_name", repository="repo")
    assert config.name == "git_name"
    assert config.repository == "repo"


def test_markdown_config():
    config = MarkdownConfig(
        close="close",
        head="head",
        intro="intro",
        dropdown="dropdown",
        modules="modules",
        setup="setup",
        slogan="slogan",
        toc="toc",
        tree="tree",
    )
    assert config.close == "close"
    assert config.head == "head"
    assert config.intro == "intro"
    assert config.dropdown == "dropdown"
    assert config.modules == "modules"
    assert config.setup == "setup"
    assert config.slogan == "slogan"
    assert config.toc == "toc"
    assert config.tree == "tree"


def test_paths_config():
    config = PathsConfig(
        dependency_files="deps",
        ignore_files="ignore",
        language_names="lang",
        language_setup="setup",
        badges="badges",
        docs="docs",
        md="md",
    )
    assert config.dependency_files == "deps"
    assert config.ignore_files == "ignore"
    assert config.language_names == "lang"
    assert config.language_setup == "setup"
    assert config.badges == "badges"
    assert config.docs == "docs"
    assert config.md == "md"


def test_app_config():
    openai_config = OpenAIConfig(
        api_key="test_key",
        prompt_intro="intro",
        prompt_slogan="slogan",
        prompt_code_to_text="code_to_text",
    )
    git_config = GitConfig(name="git_name", repository="repo")
    markdown_config = MarkdownConfig(
        close="close",
        head="head",
        intro="intro",
        dropdown="dropdown",
        modules="modules",
        setup="setup",
        slogan="slogan",
        toc="toc",
        tree="tree",
    )
    paths_config = PathsConfig(
        dependency_files="deps",
        ignore_files="ignore",
        language_names="lang",
        language_setup="setup",
        badges="badges",
        docs="docs",
        md="md",
    )

    app_config = AppConfig(
        api=openai_config,
        git=git_config,
        md=markdown_config,
        paths=paths_config,
    )

    assert app_config.api == openai_config
    assert app_config.git == git_config
    assert app_config.md == markdown_config
    assert app_config.paths == paths_config


def test_config_helper():
    config_helper = ConfigHelper(
        dependency_files=["file1", "file2"],
        ignore_files=["ignore1", "ignore2"],
        language_names={"lang1": "name1", "lang2": "name2"},
        language_setup={"lang1": "setup1", "lang2": "setup2"},
    )
    assert config_helper.dependency_files == ["file1", "file2"]
    assert config_helper.ignore_files == ["ignore1", "ignore2"]
    assert config_helper.language_names == {"lang1": "name1", "lang2": "name2"}
    assert config_helper.language_setup == {
        "lang1": "setup1",
        "lang2": "setup2",
    }


def test_read_config_file(mocker):
    mock_handler = mocker.patch("file_factory.FileHandler", autospec=True)
    mock_handler.return_value.read.return_value = {"key": "value"}
    config = read_config_file(Path("path"))
    assert config == {"key": "value"}


def test_load_configuration_helper(mocker):
    mock_handler = mocker.patch("file_factory.FileHandler", autospec=True)
    mock_handler.return_value.read.return_value = {"key": "value"}
    mock_conf = MagicMock()
    mock_conf.paths.dependency_files = "path1"
    mock_conf.paths.ignore_files = "path2"
    mock_conf.paths.language_names = "path3"
    mock_conf.paths.language_setup = "path4"
    config_helper = load_configuration_helper(mock_conf)
    assert isinstance(config_helper, ConfigHelper)


def test_read_helper_configurations(mocker):
    mock_handler = mocker.patch("file_factory.FileHandler", autospec=True)
    mock_handler.return_value.read.return_value = {"key": "value"}
    mock_conf = MagicMock()
    mock_conf.paths.dependency_files = "path1"
    mock_conf.paths.ignore_files = "path2"
    mock_conf.paths.language_names = "path3"
    mock_conf.paths.language_setup = "path4"
    dependencies, ignores, names, setups = read_helper_configurations(
        mock_handler.return_value, mock_conf
    )
    assert dependencies == []
    assert ignores == []
    assert names == {}
    assert setups == {}


def test_update_helper_configurations():
    dependency_files = []
    ignore_files = []
    language_names = {}
    language_setup = {}
    conf_dict = {
        "dependency_files": {"dependency_files": ["file1", "file2"]},
        "ignore_files": {"ignore_files": ["ignore1", "ignore2"]},
        "language_names": {"lang1": "name1", "lang2": "name2"},
        "language_setup": {"lang1": "setup1", "lang2": "setup2"},
    }
    update_helper_configurations(
        dependency_files,
        ignore_files,
        language_names,
        language_setup,
        conf_dict,
    )
    assert dependency_files == ["file1", "file2"]
    assert ignore_files == ["ignore1", "ignore2"]
    assert language_names == {"lang1": "name1", "lang2": "name2"}
    assert language_setup == {"lang1": "setup1", "lang2": "setup2"}
