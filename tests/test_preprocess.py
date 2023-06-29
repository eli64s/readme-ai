"""Unit tests for preprocess.py."""

import sys
from typing import Any, Dict, List
from unittest.mock import Mock

import pytest

from src import conf, utils
from src.preprocess import RepositoryParser, RepositoryParserWrapper

sys.path.append("src")


class MockPaths:
    def __init__(self, config):
        self.dependency_files = config["paths"]["dependency_files"]
        self.ignore_files = config["paths"]["ignore_files"]
        self.language_names = config["paths"]["language_names"]
        self.language_setup = config["paths"]["language_setup"]


def fake_generate_file_info(code_root: utils.Path) -> List[Dict[str, Any]]:
    # replace with the actual data to mock the function
    return [("file1", code_root / "file1", "content1")]


def fake_clone_repository(repo_url: str, dest_dir: str):
    # You might want to copy some actual repository files into dest_dir to mock the function
    pass


def fake_analyze(root_path: str, is_remote: bool = False) -> List[Dict[str, Any]]:
    # replace with the actual data to mock the function
    return [
        {"name": "file1", "path": "path1", "content": "content1", "extension": "txt"}
    ]


@pytest.fixture
def setup_conf_and_helper(config):
    api_mock = Mock()  # initialize with suitable mock object or real object
    git_mock = Mock()  # initialize with suitable mock object or real object
    md_mock = Mock()  # initialize with suitable mock object or real object
    paths_mock = MockPaths(config)
    prompts_mock = Mock()  # initialize with suitable mock object or real object

    app_config = conf.AppConfig(
        api=api_mock, git=git_mock, md=md_mock, paths=paths_mock, prompts=prompts_mock
    )

    # pass app_config to ConfigHelper initializer
    config_helper = conf.ConfigHelper(conf=app_config)
    return app_config, config_helper


@pytest.fixture
def setup_repository_parser(setup_conf_and_helper, monkeypatch):
    monkeypatch.setattr(RepositoryParser, "generate_file_info", fake_generate_file_info)
    monkeypatch.setattr(utils, "clone_repository", fake_clone_repository)
    monkeypatch.setattr(RepositoryParser, "analyze", fake_analyze)

    app_config, config_helper = setup_conf_and_helper
    return RepositoryParser(
        app_config, config_helper.language_names, config_helper.language_setup
    )


@pytest.fixture
def setup_repository_parser(setup_conf_and_helper, monkeypatch):
    monkeypatch.setattr(RepositoryParser, "generate_file_info", fake_generate_file_info)
    monkeypatch.setattr(utils, "clone_repository", fake_clone_repository)
    monkeypatch.setattr(RepositoryParser, "analyze", fake_analyze)

    app_config, config_helper = setup_conf_and_helper
    return RepositoryParser(
        app_config, config_helper.language_names, config_helper.language_setup
    )


def test_repository_parser_analyze(setup_repository_parser):
    repository_parser = setup_repository_parser
    output = repository_parser.analyze("https://github.com/example/repo.git")
    assert output == [
        {"name": "file1", "path": "path1", "content": "content1", "extension": "txt"}
    ]


def test_repository_parser_generate_contents(setup_repository_parser, tmpdir):
    repository_parser = setup_repository_parser.analyze(tmpdir)
    assert repository_parser == [
        {"name": "file1", "path": "path1", "content": "content1", "extension": "txt"}
    ]


@pytest.fixture
def setup_repository_parser_wrapper(setup_conf_and_helper, mocker):
    app_config, config_helper = setup_conf_and_helper

    mocker.patch.object(RepositoryParser, "__init__", return_value=None)
    mocker.patch.object(RepositoryParser, "analyze", return_value=fake_analyze(""))

    return RepositoryParserWrapper(app_config, config_helper)


def test_repository_parser_wrapper_get_unique_contents(setup_repository_parser_wrapper):
    rp_wrapper = setup_repository_parser_wrapper
    contents = [
        {"extension": "txt", "language": "Python", "name": "file1"},
        {"extension": "py", "language": "Python", "name": "file2"},
    ]
    keys = ["extension", "language"]
    assert (
        rp_wrapper.get_unique_contents(contents, keys).sort()
        == ["txt", "py", "Python"].sort()
    )


def test_repository_parser_wrapper_get_file_contents(setup_repository_parser_wrapper):
    rp_wrapper = setup_repository_parser_wrapper
    contents = [
        {"path": "path1", "content": "content1"},
        {"path": "path2", "content": "content2"},
    ]
    assert rp_wrapper.get_file_contents(contents) == {
        "path1": "content1",
        "path2": "content2",
    }
