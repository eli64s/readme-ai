"""
tests/test_conf.py
"""
from src.conf import AppConfig, GitHub, Markdown, OpenAI, Paths

# Test data for dataclass instances
openai_data = {
    "api_key": "test_key",
    "engine": "test_engine",
    "prompt_features": "test_features",
}
github_data = {"url": "https://github.com/test"}
markdown_data = {
    "body": "test_body",
    "head": "test_head",
    "dropdown": "test_dropdown",
    "modules": "test_modules",
    "toc": "test_toc",
    "tree": "test_tree",
    "usage": "test_usage",
}
paths_data = {"badges": "test_badges", "docs": "test_docs", "md": "test_md"}


def test_openai_dataclass():
    openai = OpenAI(**openai_data)
    for key, value in openai_data.items():
        assert getattr(openai, key) == value


def test_github_dataclass():
    github = GitHub(**github_data)
    for key, value in github_data.items():
        assert getattr(github, key) == value


def test_markdown_dataclass():
    markdown = Markdown(**markdown_data)
    for key, value in markdown_data.items():
        assert getattr(markdown, key) == value


def test_paths_dataclass():
    paths = Paths(**paths_data)
    for key, value in paths_data.items():
        assert getattr(paths, key) == value


def test_appconfig_dataclass():
    app_config = AppConfig(
        api=OpenAI(**openai_data),
        github=GitHub(**github_data),
        md=Markdown(**markdown_data),
        paths=Paths(**paths_data),
    )

    assert app_config.api == OpenAI(**openai_data)
    assert app_config.github == GitHub(**github_data)
    assert app_config.md == Markdown(**markdown_data)
    assert app_config.paths == Paths(**paths_data)
