"""Tests for creating LLM prompts."""

from unittest.mock import Mock, patch

import pytest

from readmeai.llms.prompts import (
    get_prompt_context,
    get_prompt_template,
    inject_prompt_context,
    set_prompt_context,
)


@pytest.mark.skip
def test_get_prompt_template_valid():
    prompts = {
        "features": "template1",
        "overview": "template2",
        "slogan": "template3",
    }
    assert get_prompt_template(prompts, "features") == "template1"
    assert get_prompt_template(prompts, "overview") == "template2"
    assert get_prompt_template(prompts, "slogan") == "template3"


@pytest.mark.skip
def test_get_prompt_template_invalid():
    prompts = {
        "features": "template1",
        "overview": "template2",
        "slogan": "template3",
    }
    assert get_prompt_template(prompts, "nonexistent") == ""


def test_inject_prompt_context_correct():
    template = "This is a {} template."
    context = {"test": "sample"}
    assert (
        inject_prompt_context(template, context)
        == "This is a sample template."
    )


def test_inject_prompt_context_missing_key():
    template = "This is a {test} template."
    context = {}
    assert inject_prompt_context(template, context) == ""


@pytest.mark.skip
def test_get_prompt_context_valid(mock_config):
    patch(
        "readmeai.prompts.get_prompt_template",
        return_value="This is a sample template.",
    )
    patch(
        "readmeai.prompts.inject_prompt_context",
        return_value="This is a sample template.",
    )
    config = Mock()
    config.prompts = Mock()
    assert get_prompt_context(config, "overview", {"test": "sample"}) == (
        "This is a sample template."
    )


def test_get_prompt_context_invalid():
    patch("readmeai.prompts.get_prompt_template", return_value="")
    config = Mock()
    config.prompts = Mock()
    assert get_prompt_context(config, "nonexistent", {"test": "sample"}) == ""


@pytest.mark.asyncio
async def test_set_prompt_context_valid():
    config = Mock()
    config.git.repository = "repo"
    config.git.name = "name"
    config.md.tree = "tree"
    file_context = [Mock()]
    dependencies = ["dep1", "dep2"]
    summaries = ["summary1", "summary2"]

    result = await set_prompt_context(
        config, file_context, dependencies, summaries
    )
    assert isinstance(result, list)
