from unittest.mock import patch

import pytest
from readmeai.config.settings import ConfigLoader, Settings
from readmeai.extractors.models import RepositoryContext
from readmeai.models.prompts import (
    get_prompt_context,
    get_prompt_template,
    inject_prompt_context,
    set_additional_contexts,
    set_summary_context,
)


def test_get_prompt_context_found(mock_config_loader: ConfigLoader):
    """Test the retrieval of a prompt context."""
    with (
        patch(
            "readmeai.models.prompts.get_prompt_template",
            return_value="Hello, {name}!",
        ),
        patch(
            "readmeai.models.prompts.inject_prompt_context",
            return_value="Hello, World!",
        ),
    ):
        result = get_prompt_context(
            mock_config_loader.prompts,
            "greeting",
            {"name": "World"},
        )
        assert result == "Hello, World!"


def test_get_prompt_context_not_found(mock_config_loader: ConfigLoader):
    """Test the retrieval of a prompt context."""
    with patch("readmeai.models.prompts.get_prompt_template", return_value=""):
        result = get_prompt_context(mock_config_loader.prompts, "unknown", {})
        assert result == ""


def test_get_prompt_template(mock_config_loader: ConfigLoader):
    """Test the retrieval of a prompt template."""
    assert "Hello!" in get_prompt_template(mock_config_loader.prompts, "features_table")


def test_inject_prompt_context_success(
    mock_config: Settings,
    mock_config_loader: ConfigLoader,
    caplog: pytest.LogCaptureFixture,
):
    """Test successful injection of prompt context."""
    template = "Project {0} is a {1} repository in {2}."
    context = {0: "ReadmeAI", 1: "documentation", 2: "Python"}
    result = inject_prompt_context(template, context)
    assert len(caplog.records) == 0
    assert result == "Project ReadmeAI is a documentation repository in Python."


def test_inject_prompt_context_missing_key(caplog: pytest.LogCaptureFixture):
    template = "This is {a} and {b}."
    context = {"a": "A"}
    assert inject_prompt_context(template, context) == ""


def test_set_summary_context(
    mock_config: Settings, mock_summaries: list[tuple[str, str]]
):
    """Test the generation of summary prompts."""
    mock_config.md.directory_structure = "mock_tree"
    result = set_summary_context(mock_config, mock_summaries)
    assert len(result) == 1
    assert result[0]["type"] == "file_summary"
    assert result[0]["context"]["tree"] == "mock_tree"
    assert result[0]["context"]["repo_files"] == mock_summaries
    result_empty = set_summary_context(mock_config, [])
    assert len(result_empty) == 1
    assert result_empty[0]["type"] == "file_summary"
    assert result_empty[0]["context"]["repo_files"] == []


def test_set_additional_contexts(
    mock_config: Settings,
    mock_repository_context: RepositoryContext,
    mock_summaries: list[tuple[str, str]],
):
    """Test the generation of additional prompts."""
    result = set_additional_contexts(
        mock_config, mock_repository_context, mock_summaries
    )
    assert len(result) == 3
    assert result[0]["type"] == "features_table"
    assert result[1]["type"] == "overview"
    assert result[2]["type"] == "tagline"
    assert result[0]["context"]["file_summaries"] == mock_summaries
