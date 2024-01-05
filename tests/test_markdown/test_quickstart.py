"""Unit tests for generating the 'Quick Start' section of the README."""

from readmeai.markdown.quickstart import (
    ProjectSetup,
    count_languages,
    get_top_language,
    get_top_language_setup,
    setup_guide,
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


def test_setup_guide(config, config_helper, mock_summaries):
    """Tests the setup_guide method."""
    setup = setup_guide(config, config_helper, mock_summaries)
    assert isinstance(setup, ProjectSetup)
