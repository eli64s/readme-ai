"""Tests for the LLM prompt functions."""

from unittest.mock import patch

import pytest

from readmeai.llms.prompts import (
    get_prompt_context,
    get_prompt_template,
    inject_prompt_context,
    set_additional_prompt_contexts,
    set_summary_prompt_context,
)


def test_get_prompt_context_found(mock_config):
    """Test the retrieval of a prompt context."""
    with patch(
        "readmeai.llms.prompts.get_prompt_template",
        return_value="Hello, {name}!",
    ), patch(
        "readmeai.llms.prompts.inject_prompt_context",
        return_value="Hello, World!",
    ):
        result = get_prompt_context(mock_config, "greeting", {"name": "World"})
        assert result == "Hello, World!"


def test_get_prompt_context_not_found(mock_config):
    """Test the retrieval of a prompt context."""
    with patch("readmeai.llms.prompts.get_prompt_template", return_value=""):
        result = get_prompt_context(mock_config, "unknown", {})
        assert result == ""


def test_get_prompt_template(mock_config):
    """Test the retrieval of a prompt template."""
    assert "Hello!" in get_prompt_template(mock_config.prompts, "features")


def test_inject_prompt_context_success(
    mock_config, mock_dependencies, mock_summaries
):
    """Test the injection of a prompt context."""
    context = get_prompt_context(
        mock_config,
        "features",
        {
            "repo_name": mock_config.git.name,
            "dependencies": mock_dependencies,
            "summaries": mock_summaries,
            "tree": mock_config.md.tree,
        },
    )
    assert mock_config.git.name in context


def test_inject_prompt_context_missing_key(caplog):
    template = "This is {a} and {b}."
    context = {"a": "A"}
    assert inject_prompt_context(template, context) == ""
    assert "Missing context for prompt key" in caplog.text


@pytest.mark.asyncio
async def test_set_summary_prompt_context(mock_config):
    """Test the generation of summary prompts."""
    mock_config.md.tree = "mock_tree"
    # Similar setup for config.git as needed
    result = await set_summary_prompt_context(
        mock_config, ["dep1"], ["summary1"]
    )
    assert len(result) == 1
    assert result[0]["type"] == "summaries"
    assert result[0]["context"]["tree"] == "mock_tree"
    assert result[0]["context"]["dependencies"] == ["dep1"]
    assert result[0]["context"]["summaries"] == ["summary1"]


@pytest.mark.asyncio
async def test_set_additional_prompt_contexts(mock_config):
    """Test the generation of additional prompts."""
    result = await set_additional_prompt_contexts(
        mock_config, ["dep1"], ["summary1"]
    )
    assert len(result) == 3
    assert result[0]["type"] == "features"
    assert result[1]["type"] == "overview"
    assert result[2]["type"] == "slogan"
    assert result[0]["context"]["dependencies"] == ["dep1"]
    assert result[0]["context"]["summaries"] == ["summary1"]
