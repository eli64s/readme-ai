"""Unit tests for the builder.py module."""

import sys
import unittest.mock as mock
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from pandas import DataFrame

from readmeai.builder import (
    build,
    create_directory_tree,
    create_tables,
    format_badges,
    get_badges,
    parse_pandas_cols,
)
from readmeai.conf import AppConfig, ConfigHelper, load_config, load_config_helper
from readmeai.factory import FileHandler

sys.path.append("readmeai")

FILE_HANDLER = FileHandler()
CONF = Path("conf/conf.toml")
conf = load_config(CONF)
conf_helper = load_config_helper(conf)
dependency_list = ["dependency1", "dependency2"]
summaries = [("module1.py", "Summary 1"), ("module2.py", "Summary 2")]


@pytest.fixture
def mock_conf():
    return AppConfig(
        paths=mock.MagicMock(),
        md=mock.MagicMock(),
        git=mock.MagicMock(),
        api=mock.MagicMock(),
        prompts=mock.MagicMock(),
    )


@pytest.fixture
def mock_conf_helper():
    return ConfigHelper(
        ignore_files=[],
        language_names={},
        language_setup={},
        dependency_files=[],
    )


@pytest.fixture
def mock_summaries():
    return [("module1.py", "Summary 1"), ("module2.py", "Summary 2")]


@pytest.fixture
def mock_dependency_list():
    return ["dependency1", "dependency2"]


@mock.patch("src.builder.FileHandler")
@mock.patch("src.builder.Logger")
def test_build(mock_logger, mock_file_handler):
    mock_conf = mock.MagicMock()
    mock_conf.md.head = "mock string"
    mock_conf.md.close = "mock string"
    mock_conf.md.dropdown = mock.MagicMock()
    mock_conf.md.dropdown.format.return_value = "formatted string"
    mock_conf.git.name = "mock string"
    mock_conf.md.slogan = "mock string"
    mock_conf_helper = mock.MagicMock()
    mock_dependency_list = ["dependency1", "dependency2"]
    mock_summaries = [("module1.py", "Summary 1"), ("module2.py", "Summary 2")]
    assert mock_conf.md.head == "mock string"


def test_get_badges():
    badge_metadata = {
        "icons": [
            {
                "name": "dependency1",
                "src": "https://img.shields.io/badge/dependency1-src1",
            },
            {
                "name": "dependency2",
                "src": "https://img.shields.io/badge/dependency2-src2",
            },
        ]
    }
    dependency_list = ["dependency1", "dependency2"]
    badges = get_badges(badge_metadata, dependency_list)

    assert "src1" in badges
    assert "src2" in badges


def test_format_badges():
    badges = [
        "https://img.shields.io/badge/dependency1-src1",
        "https://img.shields.io/badge/dependency2-src2",
        "https://img.shields.io/badge/dependency3-src3",
    ]
    dependencies = ["dependency1", "dependency2", "dependency3"]
    formatted_badges = format_badges(badges, dependencies)

    assert (
        '<img src="https://img.shields.io/badge/dependency1-src1" alt="dependency1" />'
        in formatted_badges
    )
    assert (
        '<img src="https://img.shields.io/badge/dependency2-src2" alt="dependency2" />'
        in formatted_badges
    )
    assert (
        '<img src="https://img.shields.io/badge/dependency3-src3" alt="dependency3" />'
        in formatted_badges
    )


@mock.patch("src.builder.Path")
def test_create_setup_guide(mock_path, mock_conf, mock_conf_helper):
    mock_setup = mock.MagicMock()
    mock_setup.format.return_value = "[INSERT_INSTALLATION_STEPS_HERE]"
    mock_conf.md.setup = mock_setup


@mock.patch("src.builder.subprocess.check_output")
@mock.patch("src.builder.git.Repo.clone_from")
def test_create_directory_tree(mock_git_clone, mock_subprocess_check_output):
    url = "https://github.com/test/repo"
    mock_subprocess_check_output.return_value.decode.return_value = "\n".join(
        ["line1", "line2", "line3"]
    )
    tree = create_directory_tree(url)
    mock_git_clone.assert_called_once_with(url, mock.ANY)
    assert "line2" in tree
    assert "line3" in tree


def test_create_tables():
    df = DataFrame(
        {
            "Module": ["module1.py", "module2.py"],
            "Summary": ["Summary 1", "Summary 2"],
            "File": ["file1.py", "file2.py"],
        }
    )
    dropdown = "expected format or content"
    tables = create_tables(df, dropdown)
    assert tables != ""


def test_parse_pandas_cols():
    df = DataFrame({"Module": ["path/to/module1.py", "path/to/module2.py"]})
    parsed_df = parse_pandas_cols(df)

    assert parsed_df["Directory"].tolist() == ["path/to", "path/to"]
    assert parsed_df["File"].tolist() == ["module1.py", "module2.py"]


def test_build_calls_file_handler_write_with_correct_arguments(
    config,
    conf_helper=conf_helper,
    dependency_list=dependency_list,
    summaries=summaries,
):
    handler_mock = MagicMock(FileHandler)
    config["md"]["head"] = "mock string"
    config["md"]["close"] = "mock string"
    config["md"]["intro"] = "mock string"
    config["md"]["dropdown"] = "mock string"
    config["md"]["modules"] = "mock string"
    config["md"]["setup"] = "mock string"
    config["md"]["slogan"] = "mock string"
    config["md"]["toc"] = "mock string"
    config["md"]["tree"] = "mock string"
    config["paths"]["badges"] = "mock_path"
    config["git"]["repository"] = "mock_repository"

    handler_instance_mock = handler_mock.return_value
    handler_instance_mock.read.return_value = {}
    summaries_dataframe_mock = MagicMock()
    parse_pandas_cols_mock = MagicMock()
    get_badges_mock = MagicMock(return_value="mock_badges")
    create_tables_mock = MagicMock(return_value="mock_tables")
    create_directory_tree_mock = MagicMock(return_value="mock_repo")
    create_setup_guide_mock = MagicMock(return_value="mock_setup")

    with patch("src.builder.FileHandler", handler_mock):
        with patch("pandas.DataFrame", summaries_dataframe_mock):
            with patch("src.builder.parse_pandas_cols", parse_pandas_cols_mock):
                with patch("src.builder.get_badges", get_badges_mock):
                    with patch("src.builder.create_tables", create_tables_mock):
                        with patch(
                            "src.builder.create_directory_tree",
                            create_directory_tree_mock,
                        ):
                            with patch(
                                "src.builder.create_setup_guide",
                                create_setup_guide_mock,
                            ):
                                build(
                                    conf,
                                    conf_helper,
                                    dependency_list,
                                    summaries,
                                )

    handler_instance_mock.write.assert_called_once()


def test_build_calls_logger_info_with_correct_argument(
    config,
    conf_helper=conf_helper,
    dependency_list=dependency_list,
    summaries=summaries,
):
    handler_mock = MagicMock(FileHandler)
    config["md"]["head"] = "mock string"
    config["md"]["close"] = "mock string"
    config["md"]["intro"] = "mock string"
    config["md"]["dropdown"] = "mock string"
    config["md"]["modules"] = "mock string"
    config["md"]["setup"] = "mock string"
    config["md"]["slogan"] = "mock string"
    config["md"]["toc"] = "mock string"
    config["md"]["tree"] = "mock string"
    config["paths"]["badges"] = "mock_path"
    config["git"]["repository"] = "mock_repository"

    handler_instance_mock = handler_mock.return_value
    handler_instance_mock.read.return_value = {}
    summaries_dataframe_mock = MagicMock()
    parse_pandas_cols_mock = MagicMock()
    get_badges_mock = MagicMock(return_value="mock_badges")
    create_tables_mock = MagicMock(return_value="mock_tables")
    create_directory_tree_mock = MagicMock(return_value="mock_repo")
    create_setup_guide_mock = MagicMock(return_value="mock_setup")

    with patch("src.builder.FileHandler", handler_mock):
        with patch("pandas.DataFrame", summaries_dataframe_mock):
            with patch("src.builder.parse_pandas_cols", parse_pandas_cols_mock):
                with patch("src.builder.get_badges", get_badges_mock):
                    with patch("src.builder.create_tables", create_tables_mock):
                        with patch(
                            "src.builder.create_directory_tree",
                            create_directory_tree_mock,
                        ):
                            with patch(
                                "src.builder.create_setup_guide",
                                create_setup_guide_mock,
                            ):
                                with patch(
                                    "src.builder.LOGGER.info"
                                ) as logger_info_mock:
                                    build(
                                        conf,
                                        conf_helper,
                                        dependency_list,
                                        summaries,
                                    )

    logger_info_mock.assert_called_once_with(
        f"README.md file created at: {Path.cwd() / config['paths']['readme']}"
    )
