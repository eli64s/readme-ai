"""Unit tests for generating the 'Quick Start' section of the README."""

import pytest

from readmeai.markdown.quickstart import create_instructions


def test_create_instructions_with_default_config(config, config_helper):
    """Tests the create_instructions method with default config."""
    summaries = [("module.pyc", "summary")]
    result = create_instructions(config, config_helper, summaries)
    assert result == ("► INSERT-TEXT", "► INSERT-TEXT", "► INSERT-TEXT")


@pytest.mark.parametrize(
    "language, setup_commands",
    [
        (
            "py",
            ["pip install -r requirements.txt", "python main.py", "pytest"],
        ),
        ("js", ["npm install", "node app.js", "npm test"]),
    ],
)
def test_create_instructions_with_language_setup(
    language, setup_commands, config, config_helper
):
    """Tests the create_instructions method with language setup."""
    summaries = [(f"module.{language}", "summary")]
    result = create_instructions(config, config_helper, summaries)
    assert result == tuple(setup_commands)


def test_create_instructions_with_multiple_languages(config, config_helper):
    """Tests the create_instructions method with multiple languages."""
    summaries = [
        ("module.py", "summary"),
        ("module.js", "summary"),
        ("module.py", "summary"),
    ]
    result = create_instructions(config, config_helper, summaries)
    assert result == (
        "pip install -r requirements.txt",
        "python main.py",
        "pytest",
    )
