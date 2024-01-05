"""Unit tests for the README Markdown file builder."""

from unittest.mock import patch

import pytest

from readmeai.markdown.builder import ReadmeBuilder, build_readme_md


@pytest.fixture
def readme_builder(
    config, config_helper, mock_dependencies, mock_summaries, mock_temp_dir
):
    return ReadmeBuilder(
        config, config_helper, mock_dependencies, mock_summaries, mock_temp_dir
    )


def test_md_header(readme_builder):
    """Tests if md_header property returns a string."""
    header = readme_builder.md_header
    assert isinstance(header, str)


def test_md_summaries(readme_builder):
    """Tests if md_summaries property returns a string."""
    summaries = readme_builder.md_summaries
    assert isinstance(summaries, str)


def test_md_tree(readme_builder):
    """Tests if md_tree property returns a string."""
    tree = readme_builder.md_tree
    assert isinstance(tree, str)


def test_md_quickstart(readme_builder):
    """Tests if md_quick_start property returns a string."""
    quickstart = readme_builder.md_quickstart
    assert isinstance(quickstart, str)


@patch("readmeai.markdown.builder.ReadmeBuilder.remove_emojis")
def test_build_with_emojis(mock_remove_emojis, config, readme_builder):
    """Tests if emojis are removed when the config is set."""
    config.cli.emojis = False
    readme_builder.build()
    mock_remove_emojis.assert_called_once()


@patch("readmeai.markdown.builder.factory.FileHandler.write")
def test_build_readme_md(
    mock_write,
    config,
    config_helper,
    mock_dependencies,
    mock_summaries,
    mock_temp_dir,
):
    """Tests the build_readme_md function."""
    build_readme_md(
        config, config_helper, mock_dependencies, mock_summaries, mock_temp_dir
    )
    mock_write.assert_called_once()


def test_remove_emojis_from_headers_with_emojis():
    """Tests the remove_emojis static method with emojis."""
    content_with_emojis = ["# Header 🚀", "## Another Header 😃"]
    expected_output = ["# Header ", "## Another Header "]
    result = ReadmeBuilder.remove_emojis(content_with_emojis)
    assert result == expected_output


def test_remove_emojis_from_headers_without_emojis():
    """Tests the remove_emojis static method without emojis."""
    content_without_emojis = ["# Header", "## Another Header"]
    result = ReadmeBuilder.remove_emojis(content_without_emojis)
    assert result == content_without_emojis
