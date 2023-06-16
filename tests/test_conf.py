"""Unit tests for the configuration module."""

import sys

from src.conf import (
    AppConfig,
    ConfigHelper,
    GitConfig,
    MarkdownConfig,
    OpenAIConfig,
    PathsConfig,
    PromptsConfig,
)

sys.path.append("src")

pass


def test_openai_config(config):
    assert len(config["api"]["api_key"]) == 0
    assert config["api"]["engine"] == "text-davinci-003"
    assert isinstance(config["api"]["temperature"], float)
    assert isinstance(config["api"]["tokens"], int)


def test_git_config(config):
    assert len(config["git"]["hosts"]) == 2
    assert config["git"]["name"] == "README-AI"
    assert config["git"]["repository"] is not None


def test_markdown_config(config):
    assert isinstance(config["md"]["close"], str)


def test_paths_config(config):
    assert isinstance(config["paths"]["dependency_files"], str)


def test_app_config():
    openai_config = OpenAIConfig(
        api_key="test_key",
        engine="test_engine",
        temperature=0.5,
        tokens=1024,
    )
    git_config = GitConfig(
        hosts=["github.com", "gitlab.com"],
        name="git_name",
        repository="repo",
    )
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
        badges="badges",
        dependency_files="deps",
        ignore_files="ignore",
        language_names="lang",
        language_setup="setup",
        readme="md",
    )
    prompt_config = PromptsConfig(
        code_to_text="code_to_text",
        features="features",
        intro="intro",
        slogan="slogan",
    )
    app_config = AppConfig(
        api=openai_config,
        git=git_config,
        md=markdown_config,
        paths=paths_config,
        prompts=prompt_config,
    )

    assert app_config.api == openai_config
    assert app_config.git == git_config
    assert app_config.md == markdown_config
    assert app_config.paths == paths_config


def test_config_helper():
    config_helper = ConfigHelper(
        dependency_files=["file1", "file2"],
        ignore_files=["ignore1", "ignore2"],
        language_names={
            "lang1": "name1",
            "lang2": "name2"
        },
        language_setup={
            "lang1": "setup1",
            "lang2": "setup2"
        },
    )
    assert config_helper.dependency_files == ["file1", "file2"]
    assert config_helper.ignore_files == ["ignore1", "ignore2"]
    assert config_helper.language_names == {"lang1": "name1", "lang2": "name2"}
    assert config_helper.language_setup == {
        "lang1": "setup1",
        "lang2": "setup2",
    }
