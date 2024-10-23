import pytest
from pydantic import ValidationError

from readmeai.config.constants import (
    BadgeStyleOptions,
    HeaderStyleOptions,
    ImageOptions,
    TocStyleOptions,
)
from readmeai.config.settings import GitSettings, MarkdownSettings, Settings
from readmeai.errors import GitValidationError


@pytest.fixture
def valid_settings_dict():
    return {
        "api": {"rate_limit": 10, "system_message": "Test message"},
        "files": {
            "ignore_list": "ignore.txt",
            "languages": "languages.json",
            "parsers": "parsers.json",
            "prompts": "prompts.toml",
            "tool_config": "tool_config.json",
            "tooling": "tooling.json",
            "shieldsio_icons": "shieldsio_icons.json",
            "skill_icons": "skill_icons.json",
        },
        "git": {"repository": "https://github.com/user/repo"},
        "llm": {
            "api": "openai",
            "base_url": "https://api.openai.com",
            "context_window": 4096,
            "encoder": "cl100k_base",
            "host_name": "https://api.openai.com",
            "localhost": "http://localhost:1234",
            "model": "gpt-3.5-turbo",
            "path": "/v1",
            "temperature": 0.7,
            "tokens": 1000,
            "top_p": 1.0,
        },
        "md": {
            "align": "center",
            "badge_color": "blue",
            "badge_style": BadgeStyleOptions.DEFAULT,
            "badges_tech_stack": "",
            "badges_tech_stack_text": "",
            "contribute": "",
            "emojis": False,
            "features": "Test features",
            "header_style": HeaderStyleOptions.CLASSIC,
            "image": ImageOptions.BLUE,
            "image_width": "20%",
            "project_index": "\n## Project Index\n",
            "overview": "Test overview",
            "placeholder": "<code>Test placeholder</code>",
            "quickstart": "",
            "shieldsio_icons": "",
            "skill_icons": "",
            "slogan": "Test slogan",
            "tables": "",
            "toc_style": TocStyleOptions.BULLET,
            "tree": "",
            "tree_depth": 2,
        },
    }


@pytest.mark.parametrize(
    "repository, expected_host_domain, expected_host, expected_name",
    [
        ("https://github.com/user/repo", "github.com", "github", "repo"),
        ("https://gitlab.com/user/repo", "gitlab.com", "gitlab", "repo"),
    ],
)
def test_git_settings_validation(
    repository, expected_host_domain, expected_host, expected_name
):
    git_settings = GitSettings(repository=repository)
    assert git_settings.host_domain == expected_host_domain
    assert git_settings.host == expected_host
    assert git_settings.name == expected_name


def test_git_settings_invalid_repository():
    with pytest.raises(GitValidationError):
        GitSettings(repository="invalid_url")


@pytest.mark.parametrize(
    "image, expected_width",
    [
        (ImageOptions.LLM, "30%"),
        (ImageOptions.BLUE, "30%"),
    ],
)
def test_markdown_settings_image_width(
    valid_settings_dict, image, expected_width
):
    valid_settings_dict["md"]["image"] = image
    settings = Settings(**valid_settings_dict)
    assert settings.md.image_width == expected_width


@pytest.mark.parametrize(
    "header_style, expected_align",
    [
        (HeaderStyleOptions.CLASSIC, "center"),
        (HeaderStyleOptions.COMPACT, "center"),
        (HeaderStyleOptions.MODERN, "center"),
    ],
)
def test_markdown_settings_header_style(
    valid_settings_dict, header_style, expected_align
):
    valid_settings_dict["md"]["header_style"] = header_style
    settings = Settings(**valid_settings_dict)
    assert settings.md.align == expected_align


def test_markdown_settings_badge_color_validation(valid_settings_dict):
    valid_settings_dict["md"]["badge_color"] = "invalid_color"
    with pytest.raises(ValidationError):
        Settings(**valid_settings_dict)


@pytest.mark.parametrize("tree_depth", [0, 6])
def test_markdown_settings_tree_depth_validation(
    valid_settings_dict, tree_depth
):
    valid_settings_dict["md"]["tree_depth"] = tree_depth
    with pytest.raises(ValidationError):
        Settings(**valid_settings_dict)


def test_api_settings_rate_limit_validation(valid_settings_dict):
    valid_settings_dict["api"]["rate_limit"] = 30
    with pytest.raises(ValidationError):
        Settings(**valid_settings_dict)


def test_full_settings_validation(valid_settings_dict):
    settings = Settings(**valid_settings_dict)
    assert isinstance(settings, Settings)
    assert isinstance(settings.git, GitSettings)
    assert isinstance(settings.md, MarkdownSettings)


def test_settings_immutability(valid_settings_dict):
    settings = Settings(**valid_settings_dict)
    with pytest.raises(ValidationError):
        settings.api = None


if __name__ == "__main__":
    pytest.main(["-v", __file__])
