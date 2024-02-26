"""Unit tests for the CLI commands module."""


from unittest.mock import patch

import pytest
from click.testing import CliRunner

from readmeai.cli.main import main


@pytest.fixture
def runner():
    """Create a Click CLI runner."""
    return CliRunner()


@patch("readmeai.readmeai.clone_repository")
def test_commands_with_defaults(mock_clone, runner, temp_dir, tmp_path):
    """Test the commands function with default options."""
    mock_clone.return_value = temp_dir / "repo-dir"
    result = runner.invoke(
        main,
        [
            "--repository",
            temp_dir,
            "--api",
            "OFFLINE",
            "--alignment",
            "left",
            "--badge-style",
            "flat-square",
            "--output",
            tmp_path / "test_readme.md",
        ],
    )
    assert result.exit_code == 0


def test_commands_with_invalid_option(runner, tmp_path):
    """Test the commands function with an invalid option."""
    result = runner.invoke(
        main,
        [
            "--alignment",
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
