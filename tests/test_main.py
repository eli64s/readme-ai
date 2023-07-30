import argparse
import asyncio
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

import readmeai.main

sys.path.append("readmeai")


@pytest.fixture
def api_key():
    return "OPENAI_API_KEY"


@pytest.fixture
def output():
    return "readme_ai.md"


@pytest.fixture
def repository():
    return "https://github.com/user/repo.git"


@pytest.fixture
def mock_openaihandler():
    return MagicMock()


# Tests


def test_validate_api_key(api_key):
    os.environ["OPENAI_API_KEY"] = ""
    with pytest.raises(argparse.ArgumentTypeError):
        readmeai.main.validate_api_key(api_key)


def test_validate_repository(repository):
    # Test with a valid repository
    readmeai.main.validate_repository(repository)

    # Test with an invalid repository
    with pytest.raises(argparse.ArgumentTypeError):
        readmeai.main.validate_repository("")


@patch("src.main.OpenAIHandler")
@patch("src.main.validate_api_key")
@patch("src.main.validate_repository")
@patch("src.main.generate_readme")
def test_main(
    mock_generate_readme,
    mock_validate_repository,
    mock_validate_api_key,
    mock_openaihandler,
    api_key,
    output,
    repository,
):
    # This will test if the functions are called as expected
    asyncio.run(readmeai.main.main(api_key, output, repository))
    mock_validate_api_key.assert_called_once_with(api_key)
    mock_validate_repository.assert_called_once_with(repository)
    mock_generate_readme.assert_called_once()


@patch("src.main.generate_code_to_text")
@patch("src.main.generate_markdown_text")
def test_generate_readme(
    mock_generate_markdown_text, mock_generate_code_to_text, mock_openaihandler
):
    # This will test if the functions are called as expected
    asyncio.run(readmeai.main.generate_readme(mock_openaihandler))
    mock_generate_code_to_text.assert_called_once()
    mock_generate_markdown_text.assert_called_once()
