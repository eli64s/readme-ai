"""Unit tests for generating the 'Quick Start' section of the README."""

import pytest

from readmeai.markdown.quickstart import getting_started


def test_getting_started_with_default_config(config, config_helper):
    """Tests the getting_started method with default config."""
    deps = ["pytest", "tensorflow", "python"]
    summaries = [("module.pyc", "summary")]
    result = getting_started(config, config_helper, deps, summaries)
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
def test_getting_started_with_language_setup(
    language, setup_commands, config, config_helper
):
    """Tests the getting_started method with language setup."""
    deps = ["pytest", "tensorflow", "python"]
    summaries = [(f"module.{language}", "summary")]
    result = getting_started(config, config_helper, deps, summaries)
    assert result == tuple(setup_commands)


def test_getting_started_with_multiple_languages(config, config_helper):
    """Tests the getting_started method with multiple languages."""
    deps = ["pytest", "tensorflow", "python"]
    summaries = [
        ("module.py", "summary"),
        ("module.js", "summary"),
        ("module.py", "summary"),
    ]
    result = getting_started(config, config_helper, deps, summaries)
    assert result == (
        "pip install -r requirements.txt",
        "python main.py",
        "pytest",
    )
