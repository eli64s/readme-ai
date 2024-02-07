"""Tests for the readmeai package main module."""

from unittest.mock import Mock, patch

import pytest

from readmeai.app import readme_agent, readme_generator
from readmeai.exceptions import ReadmeGeneratorError


@pytest.fixture
def mock_output_file(tmp_path):
    """Fixture for a mock output file."""
    return tmp_path / "test_readme.md"


@patch("readmeai.app.clone_repository")
@patch("readmeai.app.process_repository")
@patch("readmeai.app.model_handler")
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
    mock_output_file,
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
        {"dependency1": "command1", "dependency2": "command2"},
    )
    mock_config.git.repository = tmp_path
    mock_model_handler.return_value.use_api.return_value.__aenter__.return_value.batch_request.return_value = (
        "summaries_response",
        "features_response",
        "overview_response",
        "slogan_response",
    )
    mock_build_readme_md.return_value = "test_readme_md"

    await readme_generator(mock_config, mock_config_helper, mock_output_file)

    mock_clone_repository.assert_called_once()
    mock_process_repository.assert_called_once()
    mock_model_handler.assert_called_once()
    mock_build_readme_md.assert_called_once()


@pytest.mark.asyncio
def test_readme_agent_exception_handling():
    """Test the readme_agent function exception handling."""
    with patch(
        "readmeai.app.load_config", side_effect=Exception("Test exception")
    ), pytest.raises(ReadmeGeneratorError) as exc:
        readme_agent(
            align=None,
            api="test_api",
            badges=None,
            badge_color=None,
            emojis=None,
            image=None,
            max_tokens=None,
            model=None,
            output=None,
            repository=None,
            temperature=None,
            tree_depth=None,
        )
    assert "Test exception" in str(exc.value)
    assert isinstance(exc.value.__cause__, Exception)


@patch("readmeai.app.clone_repository")
@pytest.mark.asyncio
async def test_readme_generator_exception_handling(
    mock_clone_repository,
    mock_config,
    mock_config_helper,
    mock_output_file,
):
    """Test the readme_generator function exception handling."""
    mock_clone_repository.side_effect = Exception("Test Exception")
    with pytest.raises(ReadmeGeneratorError):
        await readme_generator(
            mock_config, mock_config_helper, mock_output_file
        )
    assert mock_clone_repository.call_count == 1
