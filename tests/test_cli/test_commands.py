"""Unit tests for the CLI commands."""

import pytest
from click.testing import CliRunner

from readmeai.cli import commands
from readmeai.main import main


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_missing_repository(runner: CliRunner):
    result = runner.invoke(commands.commands)
    assert result.exit_code == 2
    assert "Error: Missing option '-r' / '--repository'." in result.output


def test_with_repository(runner: CliRunner, mocker):
    mocker.patch("readmeai.main.main")
    result = runner.invoke(commands.commands, ["-r", "testrepo"])
    assert result.exit_code == 0
    main.assert_called_once_with(repository="testrepo")


def test_help_displayed(runner: CliRunner):
    result = runner.invoke(commands.commands, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_invalid_badge_choice(runner: CliRunner):
    result = runner.invoke(commands.commands, ["-r", "test", "-b", "invalid"])
    assert result.exit_code == 2
    assert "Invalid value for '--badges'." in result.output


def test_invalid_repository(runner: CliRunner):
    result = runner.invoke(commands.commands, ["-r", "invalid"])
    assert result.exit_code == 2
    assert "Error: Invalid value for '--repository'." in result.output
