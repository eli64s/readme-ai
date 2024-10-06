from unittest.mock import MagicMock, patch

import pytest
from _pytest._py.path import LocalPath
from click.testing import CliRunner

from readmeai.cli.main import main
from readmeai.config.settings import ConfigLoader


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def mock_config():
    return MagicMock(spec=ConfigLoader)


@pytest.fixture
def mock_readme_agent():
    with patch("readmeai.__main__.readme_agent") as mock:
        yield mock


def test_main_command_basic(
    cli_runner: CliRunner,
    config_loader_fixture: ConfigLoader,
    output_file_path: str,
):
    with patch(
        "readmeai.config.settings.ConfigLoader",
        return_value=config_loader_fixture,
    ):
        result = cli_runner.invoke(
            main,
            [
                "-r",
                "https://github.com/eli64s/readme-ai-streamlit",
                "-o",
                output_file_path,
            ],
        )

    assert result.exit_code == 0


def test_main_command_all_options(
    cli_runner: CliRunner,
    config_loader_fixture: ConfigLoader,
    output_file_path: str,
):
    mock_config = config_loader_fixture
    mock_config.config.git.repository = (
        "https://github.com/eli64s/readme-ai-streamlit"
    )

    with patch(
        "readmeai.config.settings.ConfigLoader", return_value=mock_config
    ):
        result = cli_runner.invoke(
            main,
            [
                "--repository",
                "https://github.com/eli64s/readme-ai-streamlit",
                "--align",
                "center",
                "--api",
                "offline",
                "--badge-color",
                "blue",
                "--badge-style",
                "flat",
                "--context-window",
                "4000",
                "--emojis",
                "--header-style",
                "modern",
                "--image",
                "llm",
                "--output",
                output_file_path,
                "--rate-limit",
                "5",
                "--temperature",
                "0.7",
                "--toc-style",
                "number",
                "--top-p",
                "0.9",
                "--tree-depth",
                "3",
            ],
        )

    assert result.exit_code == 0


def test_main_command_missing_repository(cli_runner: CliRunner):
    result = cli_runner.invoke(main)
    assert result.exit_code != 0
    assert "Missing option '-r' / '--repository'" in result.output


def test_version_option(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "version" in result.output.lower()


@pytest.mark.parametrize(
    "option,value,expected",
    [
        ("--align", "invalid", "Invalid value for '-a' / '--align'"),
        (
            "--api",
            "invalid",
            "Usage: main [OPTIONS]\nTry 'main --help' for help.\n\nError: Invalid value for '--api': 'invalid' is not one of 'ANTHROPIC', 'GEMINI', 'OLLAMA', 'OPENAI', 'OFFLINE'.",
        ),
        # (
        #     "--badge-color",
        #     "invalid",
        #     "Invalid value for '-bc' / '--badge-color'",
        # ),
        (
            "--badge-style",
            "invalid",
            "Invalid value for '-bs' / '--badge-style'",
        ),
        (
            "--context-window",
            "invalid",
            "Invalid value for '-cw' / '--context-window'",
        ),
        (
            "--header-style",
            "invalid",
            "Invalid value for '-hs' / '--header-style'",
        ),
        ("--image", "invalid", "Invalid value for '-i' / '--image'"),
        # ("--model", "invalid", "Invalid value for '-m' / '--model'"),
        (
            "--rate-limit",
            "invalid",
            "Invalid value for '-rl' / '--rate-limit'",
        ),
        (
            "--temperature",
            "invalid",
            "Invalid value for '-t' / '--temperature'",
        ),
        ("--toc-style", "invalid", "Invalid value for '-ts' / '--toc-style'"),
        (
            "--top-p",
            "invalid",
            "Usage: main [OPTIONS]\nTry 'main --help' for help.\n\nError: Invalid value for '--top-p': 'invalid' is not a valid float range.\n",
        ),
        (
            "--tree-depth",
            "invalid",
            "Invalid value for '-td' / '--tree-depth'",
        ),
    ],
)
def test_invalid_option_values(
    temp_dir: LocalPath, cli_runner: CliRunner, option, value, expected
):
    result = cli_runner.invoke(
        main, ["--repository", str(temp_dir), option, value]
    )
    assert result.exit_code != 0
    assert expected in result.output


def test_main_command_exception_handling(
    cli_runner: CliRunner, mock_config: MagicMock
):
    with (
        patch(
            "readmeai.config.settings.ConfigLoader", return_value=mock_config
        ),
        patch(
            "readmeai.__main__.readme_agent",
            side_effect=Exception("Test error"),
        ),
    ):
        result = cli_runner.invoke(
            main, ["--repository", "https://github.com/user/repo"]
        )

    assert result.exit_code != 0
