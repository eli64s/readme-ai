"""Tests for the readmeai package main module."""

from unittest.mock import AsyncMock, Mock, patch

import pytest

from readmeai.main import readme_agent


@patch("readmeai.main.clone_repo_to_temp_dir")
@patch("readmeai.main.process_repository")
@patch("readmeai.main.ModelHandler")
@patch("readmeai.main.build_readme_md")
@pytest.mark.asyncio
async def test_readme_agent_normal_flow(
    mock_build_readme_md,
    mock_model_handler,
    mock_process_repository,
    mock_clone_repo_to_temp_dir,
    mock_config,
    mock_config_helper,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    """Test the readme_agent function."""
    mock_clone_repo_to_temp_dir.return_value = tmp_path
    mock_process_repository.return_value = (
        [Mock(), Mock(), Mock()],
        mock_dependencies,
        mock_summaries,
        "test_tree",
    )
    mock_config.cli.offline = True
    mock_model_handler.return_value.use_api.return_value.__aenter__.return_value = (
        AsyncMock()
    )
    mock_build_readme_md.return_value = "test_readme_md"

    await readme_agent(mock_config, mock_config_helper)

    mock_clone_repo_to_temp_dir.assert_called_once()
    mock_process_repository.assert_called_once()
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
