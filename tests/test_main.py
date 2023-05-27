"""Unit tests for main module."""

import sys

sys.path.append("src")

import asyncio

import openai
import pytest
import typer

from src.main import (
    generate_readme,
    generate_text,
    main,
    set_openai_api_key,
    validate_repository,
)


def test_set_openai_api_key(mocker):
    mocker.patch.object(openai, "api_key", None)

    # Test that function sets api_key correctly when valid api_key is passed
    set_openai_api_key("test_key")
    assert openai.api_key == "test_key"

    # Test that function sets api_key correctly when api_key is provided through environment variable
    mocker.patch.dict("os.environ", {"OPENAI_API_KEY": "env_key"}, clear=True)
    set_openai_api_key(None)
    assert openai.api_key == "env_key"

    # Test that function raises an exception when api_key is not provided
    mocker.patch.dict("os.environ", {}, clear=True)
    with pytest.raises(typer.Exit) as excinfo:
        set_openai_api_key(None)
    assert excinfo.typename == "Exit"


def test_validate_repository(config):
    # Test that function raises an exception when no repository is passed

    # Test that function raises an exception when non-url string is passed
    with pytest.raises(typer.Exit) as excinfo:
        validate_repository("not_a_url_or_path")
    assert excinfo.typename == "Exit"

    # Test that function raises an exception when non-existent local path is passed
    with pytest.raises(typer.Exit) as excinfo:
        validate_repository("/non/existent/path")
    assert excinfo.typename == "Exit"


def test_main(config, mocker):
    mocker.patch("main.set_openai_api_key")
    mocker.patch(
        "main.validate_repository", return_value=config["git"]["repository"]
    )
    mocker.patch("asyncio.run")
    with pytest.raises(typer.Exit) as excinfo:
        main()
    assert excinfo.typename == "Exit"


def test_generate_readme(mocker):
    mocker.patch(
        "main.preprocess.get_repository_name", return_value="repo_name"
    )
    mocker.patch(
        "main.preprocess.get_repository",
        return_value={"src/main.py": "def main():\nreturn 0"},
    )
    mocker.patch(
        "main.preprocess.extract_dependencies", return_value=["dep1", "dep2"]
    )
    mocker.patch("main.generate_text", return_value=["summary1", "summary2"])
    mocker.patch("main.builder.build")

    with pytest.raises(Exception) as excinfo:
        asyncio.run(generate_readme("http://valid.url"))
    assert excinfo.typename in ["AuthenticationError", "APIError"]


def test_generate_text(mocker):
    mocker.patch(
        "main.model.code_to_text",
        return_value={"src/main.py": "def main():\nreturn 0"},
    )
    mocker.patch("main.model.generate_summary_text", side_effect=lambda x: x)
    code_summaries = asyncio.run(
        generate_text(["src/main.py"], [".pyc", ".o"])
    )
    assert isinstance(code_summaries, dict)
