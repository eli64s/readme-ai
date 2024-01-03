"""Unit tests for generating the 'Quick Start' section of the README."""

from pathlib import Path
from unittest.mock import Mock

from readmeai.markdown.quickstart import (
    ProjectSetup,
    count_languages,
    get_top_language,
    get_top_language_setup,
    getting_started,
)

mock_app_config = Mock()
mock_config_helper = Mock()
mock_summaries = [
    ("/path/to/file1.py", ""),
    ("/path/to/file2.js", ""),
]


def test_count_languages(config_helper):
    language_counts = count_languages(
        [
            ("/path/to/file1.py", ""),
            ("/path/to/file2.js", ""),
        ],
        config_helper,
    )
    assert language_counts == {"py": 1, "js": 1}


def test_get_top_language():
    language_counts = {"Python": 5, "JavaScript": 3}
    top_language = get_top_language(language_counts)
    assert top_language == "Python"


def test_get_top_language_setup(config):
    mock_config_helper.language_names.get.return_value = "Python"
    mock_config_helper.language_setup.get.return_value = [
        "pip install",
        "python app.py",
        "pytest",
    ]
    language_counts = {"Python": 5, "JavaScript": 3}

    setup = get_top_language_setup(language_counts, config, mock_config_helper)
    assert isinstance(setup, ProjectSetup)
    assert setup.top_language == "Python"


def test_getting_started():
    setup = getting_started(
        mock_app_config, mock_config_helper, mock_summaries
    )
    assert isinstance(setup, ProjectSetup)
