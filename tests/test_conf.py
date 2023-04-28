"""Unit tests for the configuration module."""

from pathlib import Path
from unittest.mock import MagicMock

import pytest

from src.conf import (AppConf, AppConfHelper, GitHub, Markdown, OpenAI, Paths,
                      load_conf_helper, read_config_file)


@pytest.fixture
def config_file(tmp_path: Path):
    config_file_path = tmp_path / "config.toml"
    config_file_path.write_text(
        """
        [api]
        api_key = "SECRET_API_KEY"
        prompt_intro = "intro"
        prompt_slogan = "slogan"

        [github]
        local = "local"
        name = "name"
        path = "path"
        remote = "remote"

        [md]
        close = "close"
        head = "head"
        intro = "intro"
        dropdown = "dropdown"
        modules = "modules"
        setup = "setup"
        toc = "toc"
        tree = "tree"

        [paths]
        file_extensions = "extensions.toml"
        file_names = "names.toml"
        ignore_files = "ignore.toml"
        setup_guide = "setup.toml"
        badges = "badges"
        docs = "docs"
        md = "md"
        """
    )
    yield config_file_path


@pytest.fixture
def conf_helper_files(tmp_path: Path):
    names_file = tmp_path / "names.toml"
    extensions_file = tmp_path / "extensions.toml"
    ignore_file = tmp_path / "ignore.toml"
    setup_file = tmp_path / "setup.toml"

    names_file.write_text(
        """
        [file_names]
        name = ["file1.py", "file2.py"]
        """
    )
    extensions_file.write_text(
        """
        [py]
        py = "python"
        """
    )
    ignore_file.write_text(
        """
        [ignore_files]
        ignore = ["file3.py", "file4.py"]
        """
    )
    setup_file.write_text(
        """
        [setup]
        key = "value"
        """
    )
    yield [names_file, extensions_file, ignore_file, setup_file]


def test_read_config_file(config_file):
    conf_dict = read_config_file(config_file)
    assert isinstance(conf_dict, dict)
    assert conf_dict["api"]["api_key"] == "SECRET_API_KEY"


def test_load_conf_helper(config_file, conf_helper_files):
    # Replace `read_config_file` with a MagicMock so we can control what it returns
    read_config_file_mock = MagicMock()
    read_config_file_mock.side_effect = [
        {"file_names": {"name": ["file1.py", "file2.py"]}},
        {"py": "python"},
        {"ignore_files": {"ignore": ["file3.py", "file4.py"]}},
        {"setup": {"key": "value"}},
    ]
    AppConf.paths.file_names = "names.toml"
    AppConf.paths.file_extensions = "extensions.toml"
    AppConf.paths.ignore_files = "ignore.toml"
    AppConf.paths.setup_guide = "setup.toml"
    conf = AppConf(
        api=OpenAI(api_key="", prompt_intro="", prompt_slogan=""),
        github=GitHub(local="", name="", path="", remote=""),
        md=Markdown(
            close="",
            head="",
            intro="",
            dropdown="",
            modules="",
            setup="",
            toc="",
            tree="",
        ),
        paths=Paths(
            file_extensions="",
            file_names="",
            ignore_files="",
            setup_guide="",
            badges="",
            docs="",
            md="",
        ),
    )

    # Call the function we're testing
    conf_helper = load_conf_helper(conf)
    assert isinstance(conf_helper, AppConfHelper)
    assert conf_helper.file_names == ["file1.py", "file2.py"]
    assert conf_helper.file_extensions == {"py": "python"}
    assert conf_helper.ignore_files == ["file3.py", "file4.py"]
    assert conf_helper.setup == {"key": "value"}

    # Ensure that `read_config_file` is called 4 times with the correct arguments
    expected_calls = [
        ((Path("conf/names.toml")),),
        ((Path("conf/extensions.toml")),),
        ((Path("conf/ignore.toml")),),
        ((Path("conf/setup.toml")),),
    ]
    assert read_config_file_mock.call_args_list == expected_calls


def test_load_conf_helper(config_file, conf_helper_files):
    # Replace `read_config_file` with a MagicMock so we can control what it returns
    read_config_file_mock = MagicMock()
    read_config_file_mock.side_effect = [
        {"file_names": {"name": ["file1.py", "file2.py"]}},
        {"py": "python"},
        {"ignore_files": {"ignore": ["file3.py", "file4.py"]}},
        {"setup": {"key": "value"}},
    ]
    AppConf.paths.file_names = "names.toml"
    AppConf.paths.file_extensions = "extensions.toml"
    AppConf.paths.ignore_files = "ignore.toml"
    AppConf.paths.setup_guide = "setup.toml"
    conf = AppConf(
        api=OpenAI(api_key="", prompt_intro="", prompt_slogan=""),
        github=GitHub(local="", name="", path="", remote=""),
        md=Markdown(
            close="",
            head="",
            intro="",
            dropdown="",
            modules="",
            setup="",
            toc="",
            tree="",
        ),
        paths=Paths(
            file_extensions="",
            file_names="",
            ignore_files="",
            setup_guide="",
            badges="",
            docs="",
            md="",
        ),
    )

    # Call the function we're testing
    conf_helper = load_conf_helper(conf)

    # Check that the function returns the expected values
    assert conf_helper.file_names == ["file1.py", "file2.py"]
    assert conf_helper.file_extensions == {"py": "python"}
    assert conf_helper.ignore_files == ["file3.py", "file4.py"]
    assert conf_helper.setup == {"key": "value"}


def test_load_conf_helper_file_not_found(config_file):
    # Remove the file that is supposed to be read
    (config_file.parent / "names.toml").unlink()

    # Call the function we're testing
    with pytest.raises(FileNotFoundError) as excinfo:
        conf_helper = load_conf_helper(
            AppConf(
                api=OpenAI(api_key="", prompt_intro="", prompt_slogan=""),
                github=GitHub(local="", name="", path="", remote=""),
                md=Markdown(
                    close="",
                    head="",
                    intro="",
                    dropdown="",
                    modules="",
                    setup="",
                    toc="",
                    tree="",
                ),
                paths=Paths(
                    file_extensions="",
                    file_names="",
                    ignore_files="",
                    setup_guide="",
                    badges="",
                    docs="",
                    md="",
                ),
            )
        )
    assert excinfo.type == FileNotFoundError
    assert "No such file or directory" in str(excinfo.value)
