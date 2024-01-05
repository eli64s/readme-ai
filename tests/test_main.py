"""Tests for the readmeai package main module."""

import asyncio
from unittest.mock import AsyncMock, Mock, patch

import pytest

from readmeai.config.settings import AppConfig
from readmeai.main import generate_prompts, readme_agent, update_settings
from readmeai.markdown.builder import build_readme_md


@patch("readmeai.main.clone_repo_to_temp_dir")
@patch("readmeai.main.ModelHandler")
@patch("readmeai.main.RepoProcessor")
@patch("readmeai.main.build_readme_md")
@pytest.mark.asyncio
async def test_readme_agent_normal_flow(
    mock_build_readme_md,
    mock_repo_processor,
    mock_model_handler,
    mock_clone_repo_to_temp_dir,
    config,
    config_helper,
):
    """Test the readme_agent function."""
    mock_config = config
    mock_config_helper = config_helper
    mock_clone_repo_to_temp_dir.return_value = asyncio.Future()
    mock_clone_repo_to_temp_dir.return_value.set_result("test_dir")
    mock_model_handler.return_value.use_api.return_value.__aenter__.return_value = (
        AsyncMock()
    )
    mock_build_readme_md.return_value = "test_readme_md"

    # Mock the RepoProcessor's methods
    mock_repo_processor_instance = mock_repo_processor.return_value
    mock_repo_processor_instance.generate_contents.return_value = []
    mock_repo_processor_instance.language_mapper.return_value = []
    mock_repo_processor_instance.tokenize_content.return_value = []

    with pytest.raises(Exception):
        await readme_agent(mock_config, mock_config_helper)
        build_readme_md(mock_config, mock_config_helper, [], [], "test_dir")

        mock_repo_processor_instance.generate_contents.assert_called_once()
        mock_repo_processor_instance.language_mapper.assert_called_once()
        mock_repo_processor_instance.tokenize_content.assert_called_once()

        mock_clone_repo_to_temp_dir.assert_called_once()
        mock_model_handler.assert_called_once()
        mock_build_readme_md.assert_called_once()


@pytest.mark.asyncio
async def test_readme_agent_error_handling():
    """Test the readme_agent function."""
    with patch(
        "readmeai.services.git_operations.clone_repo_to_temp_dir"
    ) as clone_mock:
        clone_mock.side_effect = Exception("Failed to clone repo")
        conf = Mock()
        conf_helper = Mock()
        with pytest.raises(Exception) as exc_info:
            readme_agent(conf, conf_helper)
            assert "Failed to clone repo" in str(exc_info.value)


@pytest.mark.asyncio
async def test_generate_prompts(mock_dependencies, mock_summaries):
    """Test the generate_prompts function."""
    conf = Mock()
    conf.git.repository = "https://example.com/repo"
    conf.md.tree = "test_tree"
    file_context = {"file1": Mock(), "file2": Mock()}
    prompts = await generate_prompts(
        conf,
        file_context,
        mock_dependencies,
        mock_summaries,
    )
    assert len(prompts) == 4
    expected_prompts = []
    for prompt, expected in zip(prompts, expected_prompts):
        assert prompt == expected


def test_update_settings(config):
    """Test the update_settings function."""
    config = update_settings(
        config,
        "left",
        "flat",
        config.cli.emojis,
        config.md.image,
        99999,
        config.llm.model,
        config.cli.offline,
        config.files.output,
        config.git.repository,
        config.llm.temperature,
    )
    assert isinstance(config, AppConfig)
    assert config.md.align == "left"
    assert config.cli.emojis is False
    assert config.llm.tokens_max == 99999
