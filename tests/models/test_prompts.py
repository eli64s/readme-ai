from unittest.mock import patch

import pytest

from readmeai.config.settings import Settings
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.prompts import (get_prompt_context, get_prompt_template,
                                     inject_prompt_context,
                                     set_additional_contexts,
                                     set_summary_context)


def test_get_prompt_context_found(config_fixture: Settings):
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
            config_fixture.prompts,
            "greeting",
            {"name": "World"},
        )
        assert result == "Hello, World!"


def test_get_prompt_context_not_found(config_fixture: Settings):
    """Test the retrieval of a prompt context."""
    with patch("readmeai.models.prompts.get_prompt_template", return_value=""):
        result = get_prompt_context(
            config_fixture.prompts, "unknown", {}
        )
        assert result == ""


def test_get_prompt_template(config_fixture: Settings):
    """Test the retrieval of a prompt template."""
    assert "Hello!" in get_prompt_template(
        config_fixture.prompts, "features_table"
    )


def test_inject_prompt_context_success(
    config_fixture: Settings,
    config_fixture: Settings,
    dependencies_fixture: list[str],
    repository_context_fixture: RepositoryContext,
    file_summaries_fixture: list[tuple[str, str]],
):
    """Test the injection of a prompt context."""
    context = get_prompt_context(
        config_fixture.prompts,
        "features_table",
        {
            "name": config_fixture.git.name,
            "dependencies": dependencies_fixture,
            "quickstart": repository_context_fixture.quickstart,
            "file_summary": file_summaries_fixture,
        },
    )
    assert config_fixture.git.name in context


def test_inject_prompt_context_missing_key(caplog: pytest.LogCaptureFixture):
    template = "This is {a} and {b}."
    context = {"a": "A"}
    assert inject_prompt_context(template, context) == ""


@pytest.mark.asyncio
async def test_set_summary_context(
    config_fixture: Settings,
    file_summaries_fixture: list[tuple[str, str]],
):
    """Test the generation of summary prompts."""
    config_fixture.md.tree = "mock_tree"

    # Test with non-empty dependencies and summaries
    result = await set_summary_context(config_fixture, file_summaries_fixture)
    assert len(result) == 1
    assert result[0]["type"] == "file_summary"
    assert result[0]["context"]["tree"] == "mock_tree"
    assert result[0]["context"]["repo_files"] == [
        ("/path/to/file1.py", "This is summary for file1.py"),
        ("/path/to/file2.py", "This is summary for file2.py"),
        (".github/workflows/ci.yml", "This is summary for ci.yml"),
    ]

    # Test with empty dependencies and summaries
    result_empty = await set_summary_context(config_fixture, [])
    assert len(result_empty) == 1
    assert result_empty[0]["type"] == "file_summary"
    assert result_empty[0]["context"]["tree"] == "mock_tree"
    assert result_empty[0]["context"]["repo_files"] == []


@pytest.mark.asyncio
async def test_set_additional_contexts(
    config_fixture: Settings,
    repository_context_fixture: RepositoryContext,
    file_summaries_fixture: list[tuple[str]],
):
    """Test the generation of additional prompts."""
    result = await set_additional_contexts(
        config_fixture, repository_context_fixture, file_summaries_fixture
    )
    assert len(result) == 3
    assert result[0]["type"] == "features_table"
    assert result[1]["type"] == "overview"
    assert result[2]["type"] == "tagline"
    assert result[0]["context"]["file_summary"] == file_summaries_fixture
