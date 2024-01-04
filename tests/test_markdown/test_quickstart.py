"""Unit tests for generating the 'Quick Start' section of the README."""

from unittest.mock import MagicMock
from readmeai.markdown.quickstart import (
    ProjectSetup,
    count_languages,
    get_top_language,
    get_top_language_setup,
    getting_started,
)


def test_count_languages(mock_summaries, config_helper):
    """Tests the count_languages method."""
    language_counts = count_languages(mock_summaries, config_helper)
    assert language_counts == {"py": 2, "yml": 1}


def test_get_top_language():
    """Tests the get_top_language method."""
    language_counts = {"Python": 5, "JavaScript": 3}
    top_language = get_top_language(language_counts)
    assert top_language == "Python"


def test_get_top_language_setup(config, config_helper):
    """Tests the get_top_language_setup method."""
    language_counts = {"Python": 5, "JavaScript": 3}
    setup = get_top_language_setup(language_counts, config, config_helper)
    assert isinstance(setup, ProjectSetup)
    assert setup.top_language == "Python"


def test_getting_started(config, config_helper, mock_summaries):
    """Tests the getting_started method."""
    setup = getting_started(config, config_helper, mock_summaries)
    assert isinstance(setup, ProjectSetup)
