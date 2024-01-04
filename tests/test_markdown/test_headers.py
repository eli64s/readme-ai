"""Unit tests for the markdown headers generator."""

from unittest.mock import patch

from readmeai.markdown.headers import (
    build_readme_md,
    format_readme_md,
    remove_emojis_from_headers,
)


def test_build_readme_md(
    config, config_helper, mock_dependencies, mock_summaries
):
    """Tests the build_readme_md method."""
    with patch("readmeai.core.factory.FileHandler.write") as mock_write:
        build_readme_md(
            config, config_helper, mock_dependencies, mock_summaries
        )
        mock_write.assert_called_once()
        written_content = mock_write.call_args[0][1]
        assert isinstance(written_content, str)
        assert len(written_content) > 0


def test_format_readme_md_local_source(
    config, config_helper, mock_dependencies, mock_summaries
):
    """Tests the format_readme_md method."""
    readme_md = format_readme_md(
        config, config_helper, mock_dependencies, mock_summaries
    )
    assert isinstance(readme_md, list)
    assert len(readme_md) == 9


def test_format_readme_md_nonlocal_source(
    config, config_helper, mock_dependencies, mock_summaries
):
    """Tests the format_readme_md method."""
    mock_config = config
    mock_config.cli.offline = True
    readme_md = format_readme_md(
        mock_config, config_helper, mock_dependencies, mock_summaries
    )
    assert isinstance(readme_md, list)


def test_remove_emojis_from_headers_with_emojis():
    """Tests the remove_emojis_from_headers method."""
    content_with_emojis = ["# Header 🚀", "## Another Header 😃"]
    expected_output = ["# Header ", "## Another Header "]
    assert remove_emojis_from_headers(content_with_emojis) == expected_output


def test_remove_emojis_from_headers_without_emojis():
    """Tests the remove_emojis_from_headers method."""
    content_without_emojis = ["# Header", "## Another Header"]
    assert (
        remove_emojis_from_headers(content_without_emojis)
        == content_without_emojis
    )
