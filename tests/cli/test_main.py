"""
Tests for the entry point of the CLI.
"""

from unittest.mock import patch

import pytest
from click.testing import CliRunner

from readmeai.cli.main import main


@pytest.fixture
def runner():
    """Create a Click CLI runner."""
    return CliRunner()


@patch("readmeai.__main__.retrieve_repository")
def test_commands_with_defaults(mock_clone, runner, temp_dir, tmp_path):
    """Test the commands function with default options."""
    mock_clone.return_value = temp_dir / "repo-dir"
    result = runner.invoke(
        main,
        [
            "--repository",
            "https://github.com/eli64s/readme-ai-streamlit",
            "--align",
            "left",
            "--api",
            "offline",
        ],
    )
    assert result.exit_code == 0


def test_commands_with_invalid_option(runner):
    """Test the commands function with an invalid option."""
    result = runner.invoke(
        main,
        [
            "--align",
            "right",
            "--repository",
            None,
            "--api",
            "OpenAI-AGI-v0",
        ],
    )
    assert result.exit_code != 0


if __name__ == "__main__":
    test_commands_with_defaults()
    test_commands_with_invalid_option()
