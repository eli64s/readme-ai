"""Unit tests for generating the 'Quick Start' section of the README."""

from readmeai.generators.quickstart import (
    QuickStart,
    count_languages,
    get_setup_data,
    get_top_language,
    get_top_language_setup,
)


def test_count_languages(mock_summaries, mock_configs):
    """Tests the count_languages method."""
    language_counts = count_languages(mock_summaries, mock_configs)
    assert language_counts == {"py": 2, "yml": 1}


def test_get_top_language():
    """Tests the get_top_language method."""
    language_counts = {"Python": 5, "JavaScript": 3}
    top_language = get_top_language(language_counts)
    assert top_language == "Python"


def test_get_top_language_setup(mock_configs):
    """Tests the get_top_language_setup method."""
    language_counts = {"py": 5, "js": 3}
    setup = get_top_language_setup(language_counts, mock_configs)
    assert isinstance(setup, QuickStart)
    assert setup.install_command == "pip install -r requirements.txt"


def test_get_setup_data(mock_configs, mock_summaries):
    """Tests the get_setup_data method."""
    setup = get_setup_data(mock_configs, mock_summaries)
    assert isinstance(setup, QuickStart)
