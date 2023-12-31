"""Unit tests for the CLI commands module."""

from click.testing import CliRunner

from readmeai.cli.commands import commands


def test_commands(config):
    """Test that the CLI command runs."""
    runner = CliRunner()
    result = runner.invoke(
        commands,
        [
            "--repository",
            config.git.repository,
            "--api-key",
            "dummy-key",
        ],
    )
    assert result.exit_code == 0


def test_commands_with_options():
    """Test that the CLI command runs with options."""
    runner = CliRunner()
    result = runner.invoke(
        commands,
        [
            "--repository",
            "https://github.com/example/repo",
            "--api-key",
            "your-api-key",
            "--model",
            "gpt-4",
            "--temperature",
            "0.8",
        ],
    )
    assert result.exit_code == 1


def test_commands_missing_repository():
    """Test that the CLI command fails when repository option is missing."""
    runner = CliRunner()
    result = runner.invoke(commands, ["--badges", "flat"])
    assert result.exit_code != 0
    assert "Usage: commands" in result.output


if __name__ == "__main__":
    test_commands()
    test_commands_with_options()
    test_commands_missing_repository()
