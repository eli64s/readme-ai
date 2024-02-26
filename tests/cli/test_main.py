"""Unit tests for the CLI commands module."""


import pytest
from click.testing import CliRunner

from readmeai.cli.main import main


@pytest.fixture
def runner():
    """Create a Click CLI runner."""
    return CliRunner()


def test_commands_with_defaults(runner, tmp_path):
    """Test the commands function with default options."""
    test_dir = tmp_path / "repo-dir"
    test_dir.mkdir()
    (test_dir / "test_app.py").touch()
    (tmp_path / "test_src").mkdir()
    (tmp_path / "test_src" / "test_readme.md").touch()
    result = runner.invoke(
        main,
        [
            "--repository",
            "https://github.com/eli64s/readme-ai-streamlit",
            "--api",
            "offline",
        ],
    )
    assert result.exit_code == 0

    """Test the commands function with an invalid option."""
    result = runner.invoke(
        main,
        [
            "--alignment",
            "right",
            "--repository",
            "https://github.com/test/repo",
            "--api",
            "offline",
        ],
    )
    assert result.exit_code != 0


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
