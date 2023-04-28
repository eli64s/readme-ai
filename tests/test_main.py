"""Unit tests for main module."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src import main
from src.file_factory import FileHandler
from src.model import code_to_text, generate_summary_text
from tests.test_data import mock_repo_contents

pytestmark = pytest.mark.asyncio


@pytest.fixture
def config_file(tmp_path):
    config = {
        "api": {
            "api_key": "",
            "prompt_intro": "Project {0} documentation",
            "prompt_slogan": "Codebase summaries for {0}",
        },
        "github": {
            "local": "",
            "name": "",
            "path": "",
            "remote": "",
        },
        "md": {
            "close": "",
            "head": "",
            "intro": "## {0}\n",
            "dropdown": "",
            "modules": "",
            "setup": "",
            "toc": "",
            "tree": "",
        },
        "paths": {
            "file_extensions": "",
            "file_names": "",
            "ignore_files": "",
            "setup_guide": "",
            "badges": "",
            "docs": "",
            "md": "",
        },
    }
    config_file_path = tmp_path / "conf" / "conf.toml"
    config_file_path.parent.mkdir(parents=True)
    FileHandler().write(config, config_file_path)
    return config_file_path


@patch("openai.api_key", new="")
@patch("preprocess.get_codebase_local", MagicMock(return_value=mock_repo_contents))
async def test_generate_readme_with_local(config_file, tmp_path):
    # Set command line arguments
    api_key = "test_api_key"
    local = str(tmp_path / "repo")
    output = str(tmp_path / "docs" / "README.md")

    # Generate README
    await main.generate_readme(api_key, local, output, None)

    # Check that the README file is created
    assert Path(output).exists()

    # Check that the generated documentation matches the expected output
    codebase_docs = await code_to_text([], mock_repo_contents)
    intro_text = generate_summary_text("Project TestRepo documentation")
    slogan_text = generate_summary_text("Codebase summaries for TestRepo")
    expected_df = pd.DataFrame(
        {
            "Module": ["main", "preprocess"],
            "Summary": ["This is the main module", "This is the preprocess module"],
        }
    )
    expected_df.set_index("Module", inplace=True)
    expected_intro = "## TestRepo\n"
    expected_intro += intro_text + "\n\n" + slogan_text + "\n\n"
    expected_docs = expected_df.to_csv(index=False)
    with open(output) as f:
        actual_text = f.read()

    assert expected_intro in actual_text
    assert expected_docs in actual_text
    assert isinstance(codebase_docs, list)


@patch("openai.api_key", new="")
@patch("preprocess.get_codebase_remote", MagicMock(return_value=mock_repo_contents))
async def test_generate_readme_with_remote(config_file, tmp_path):
    # Set command line arguments
    api_key = "test_api_key"
    remote = "https://github.com/testuser/testrepo"
    output = str(tmp_path / "docs" / "README.md")

    # Generate README
    await main.generate_readme(api_key, None, output, remote)

    # Check that the README file is created
    assert Path(output).exists()

    # Check that the generated documentation matches the expected output
    codebase_docs = await code_to_text([], mock_repo_contents)
    intro_text = generate_summary_text("Project TestRepo documentation")
    slogan_text = generate_summary_text("Codebase summaries for TestRepo")
    expected_df = pd.DataFrame(
        {
            "Module": ["main", "preprocess"],
            "Summary": ["This is the main module", "This is the preprocess module"],
        }
    )
    expected_df.set_index("Module", inplace=True)
    expected_intro = "## TestRepo\n"
    expected_intro += intro_text + "\n\n" + slogan_text + "\n\n"
    expected_docs = expected_df.to_csv(index=False)
    with open(output) as f:
        actual_text = f.read()

    assert expected_intro in actual_text
    assert expected_docs in actual_text
    assert isinstance(codebase_docs, list)
