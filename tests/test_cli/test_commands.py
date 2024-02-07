"""Unit tests for the CLI commands module."""

import pytest
from click.testing import CliRunner

from readmeai.cli.commands import commands


@pytest.fixture
def runner():
    """Create a Click CLI runner."""
    return CliRunner()


def test_commands_with_defaults(runner):
    """Test the commands function with default options."""
    with runner.isolated_filesystem():
        result = runner.invoke(
            commands,
            [
                "--repository",
                "https://github.com/eli64s/readme-ai-streamlit",
                "--api",
                "offline",
            ],
        )
        assert result.exit_code == 0


def test_commands_with_invalid_option(runner):
    """Test the commands function with an invalid option."""
    result = runner.invoke(
        commands,
        [
            "--align",
            "right",
            "--repository",
            "https://github.com/test/repo",
            "--api",
            "offline",
        ],
    )
    assert result.exit_code != 0


if __name__ == "__main__":
    test_commands_with_defaults()
    test_commands_with_invalid_option()
