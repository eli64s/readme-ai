"""Tests for the readmeai package main module."""

from unittest.mock import Mock, patch

import pytest

from readmeai.app import readme_generator
from readmeai.exceptions import ReadmeGeneratorError


@patch("readmeai.app.clone_repository")
@patch("readmeai.app.process_repository")
@patch("readmeai.app.ModelHandler")
@patch("readmeai.app.build_readme_md")
@pytest.mark.asyncio
async def test_readme_generator_online(
    mock_build_readme_md,
    mock_model_handler,
    mock_process_repository,
    mock_clone_repository,
    mock_config,
    mock_config_helper,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    """Test the readme_generator function."""
    mock_config.llm.offline = False
    mock_clone_repository.return_value = tmp_path
    mock_process_repository.return_value = (
        [Mock(), Mock(), Mock()],
        mock_dependencies,
        mock_summaries,
        "test_tree",
    )
    mock_config.git.repository = tmp_path
    mock_model_handler.return_value.use_api.return_value.__aenter__.return_value.batch_request.return_value = (
        "summaries_response",
        "features_response",
        "overview_response",
        "slogan_response",
    )
    mock_build_readme_md.return_value = "test_readme_md"

    await readme_generator(mock_config, mock_config_helper)

    mock_clone_repository.assert_called_once()
    mock_process_repository.assert_called_once()
    mock_model_handler.assert_called_once()
    mock_build_readme_md.assert_called_once()


@patch("readmeai.app.clone_repository")
@patch("readmeai.app.process_repository")
@patch("readmeai.app.ModelHandler")
@patch("readmeai.app.build_readme_md")
@pytest.mark.asyncio
async def test_readme_generator_offline(
    mock_build_readme_md,
    mock_model_handler,
    mock_process_repository,
    mock_clone_repository,
    mock_config,
    mock_config_helper,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    """Test the readme_generator function."""
    mock_config.llm.offline = True
    mock_clone_repository.return_value = tmp_path
    mock_process_repository.return_value = (
        [Mock(), Mock(), Mock()],
        mock_dependencies,
        mock_summaries,
        "test_tree",
    )
    mock_config.git.repository = tmp_path
    mock_build_readme_md.return_value = "test_readme_md"

    await readme_generator(mock_config, mock_config_helper)

    mock_clone_repository.assert_called_once()
    mock_process_repository.assert_called_once()
    mock_model_handler.assert_not_called()
    mock_build_readme_md.assert_called_once()


@patch("readmeai.app.clone_repository")
@pytest.mark.asyncio
async def test_readme_generator_exception_handling(
    mock_clone_repository,
    mock_config,
    mock_config_helper,
):
    """Test the readme_generator function exception handling."""
    mock_clone_repository.side_effect = Exception("Test Exception")
    with pytest.raises(ReadmeGeneratorError):
        await readme_generator(mock_config, mock_config_helper)
    assert mock_clone_repository.call_count == 1


@pytest.mark.asyncio
async def test_readme_generator_error_handling():
    """Test the readme_generator function."""
    with patch("readmeai.services.git_utils.clone_repository") as clone_mock:
        clone_mock.side_effect = Exception("Failed to clone repo")
        conf = Mock()
        conf_helper = Mock()
        with pytest.raises(Exception) as exc:
            await readme_generator(conf, conf_helper)
            assert "Failed to clone repo" in str(exc.value)
