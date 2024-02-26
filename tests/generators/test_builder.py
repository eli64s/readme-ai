"""Unit tests for the README Markdown file builder."""

import pytest

from readmeai.generators.builder import ReadmeBuilder, build_markdown


@pytest.fixture
def readme_builder(
    mock_configs,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    return ReadmeBuilder(
        mock_configs,
        mock_dependencies,
        mock_summaries,
        tmp_path,
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


def test_build_markdown(
    mock_configs,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    """Tests the build_markdown function."""
    build_markdown(
        mock_configs,
        mock_dependencies,
        mock_summaries,
        tmp_path,
    )
