"""Unit tests for generating the badges for the README file."""

from unittest.mock import MagicMock, patch

import pytest

from readmeai.markdown.badges import (
    _read_badge_file,
    build_dependency_badges,
    build_metadata_badges,
    format_badges,
    shields_icons,
    skill_icons,
)


def test_read_badge_file_success(config, monkeypatch):
    """Tests the _read_badge_file method for successful file read."""
    badge_file_path = config.files.shields_icons
    mock_file_handler = MagicMock()
    mock_file_handler.read.return_value = {
        "icons": {"names": ["Python", "JavaScript"]},
        "url": {"base_url": "http://example.com/"},
    }
    monkeypatch.setattr("readmeai.core.factory.FileHandler", mock_file_handler)
    assert isinstance(_read_badge_file(badge_file_path), dict)


def test_read_badge_file_exception(config, monkeypatch):
    """Tests the _read_badge_file method for exception handling."""
    badge_file_path = "invalid_path"
    mock_file_handler = MagicMock()
    mock_file_handler.read.side_effect = Exception("File read error")
    monkeypatch.setattr("readmeai.core.factory.FileHandler", mock_file_handler)

    with pytest.raises(Exception) as exc_info:
        _read_badge_file(badge_file_path)
    assert isinstance(exc_info.value, Exception)


@pytest.mark.parametrize(
    "badges, expected",
    [
        ([], ""),
        (
            [
                "https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white"
            ],
            '<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">',
        ),
    ],
)
def test_format_badges(badges, expected):
    """Tests the format_html method."""
    assert format_badges(badges) == expected


@pytest.mark.parametrize(
    "dependencies, svg_icons, style, expected",
    [
        ([], {}, "skills", ""),
        (
            ["python"],
            {
                "python": [
                    "https://img.shields.io/badge/Python-3776AB.svg?style={0}&logo=Python&logoColor=white",
                    "3776AB",
                ],
            },
            "flat",
            '<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">',
        ),
    ],
)
def test_build_dependency_badges(dependencies, svg_icons, style, expected):
    """Tests the generate_html method."""
    assert build_dependency_badges(dependencies, svg_icons, style) == expected


def test_build_metadata_badges_success(config):
    """Tests build_metadata_badges with valid inputs."""
    mock_config = config
    mock_config.git.source = "github.com"
    mock_config.md.badges_shields = config.md.badges_shields
    mock_config.md.badges_style = "flat"
    badges = build_metadata_badges(mock_config, "github.com", "user/repo")
    assert isinstance(badges, str)
    assert "license" in badges


def test_shields_icons_success(config):
    """Tests shields_icons with valid inputs."""
    mock_config = config
    mock_config.git.source = "github.com"
    mock_config.files.shields_icons = config.files.shields_icons
    mock_config.md.badges_style = "flat"

    mock_helper = MagicMock()
    mock_helper.language_setup = {"Python": ["install", "run", "test"]}

    deps = ["Python", "JavaScript"]

    with patch("readmeai.markdown.badges._read_badge_file") as mock_read:
        mock_read.return_value = {
            "python": [
                "https://img.shields.io/badge/Python-3776AB.svg?style={0}&logo=Python&logoColor=white",
                "3776AB",
            ],
        }
        shields_badges, deps_badges = shields_icons(
            mock_config, deps, "full_name"
        )
        assert "license" in shields_badges
        assert "Python" in deps_badges
        assert "3776AB" in deps_badges
        assert "flat" in deps_badges


def test_skill_icons_success(config):
    """Tests skill_icons with valid inputs."""
    mock_config = config
    mock_config.files.skill_icons = config.files.skill_icons
    mock_config.md.badges_style = "skills-light"
    mock_icons = {
        "icons": {"names": ["fastapi", "py", "redis", "md", "github", "git"]},
        "url": {"base_url": "https://skillicons.dev/icons?i="},
    }
    deps = ["fastapi", "py", "redis", "github", "git"]

    with patch("readmeai.markdown.badges._read_badge_file") as mock_read:
        mock_read.return_value = mock_icons
        result = skill_icons(mock_config, deps)
        assert result.startswith("<a href=") is True
        assert result.endswith("\n\t</a>\n") is True
        assert "&theme=light" in result
        assert """<a href="https://skillicons.dev">""" in result
        assert (
            """\n\t\t<img src="https://skillicons.dev/icons?i=fastapi,py,redis,md,github,git&theme=light">\n\t</a>\n"""
            in result
        )
