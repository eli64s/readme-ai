"""Tests for the readmeai module."""

from unittest.mock import patch

import pytest

from readmeai.exceptions import ReadmeGeneratorError
from readmeai.readmeai import readme_agent, readme_generator


@patch("readmeai.readmeai.clone_repository")
@patch("readmeai.readmeai.preprocessor")
@patch("readmeai.readmeai.model_handler")
@patch("readmeai.readmeai.build_markdown")
@pytest.mark.asyncio
async def test_readme_generator(
    mock_build_markdown,
    mock_model_handler,
    mock_preprocessor,
    mock_clone_repository,
    mock_config,
    mock_configs,
    mock_dependencies,
    mock_summaries,
    tmp_path,
):
    """Test the readme_generator function."""
    mock_config.llm.offline = False
    mock_clone_repository.return_value = tmp_path
    mock_preprocessor.return_value = (
        mock_dependencies,
        mock_summaries,
        {"dependency1": "command1", "dependency2": "command2"},
    )
    mock_config.git.repository = tmp_path
    mock_model_handler.return_value.use_api.return_value.__aenter__.return_value.batch_request.return_value = (
        "summaries_response",
        "features_response",
        "overview_response",
        "slogan_response",
        "synthesized_features",
    )
    mock_build_markdown.return_value = str(tmp_path / "test_readme.md")
    await readme_generator(mock_configs)
    mock_clone_repository.assert_called_once()
    mock_preprocessor.assert_called_once()
    mock_model_handler.assert_called_once()
    mock_build_markdown.assert_called_once()


@pytest.mark.asyncio
async def test_readme_agent_exception_handling():
    """Test the readme_agent function exception handling."""
    with patch(
        "readmeai.readmeai.readme_generator",
        side_effect=Exception("Test exception"),
    ), pytest.raises(ReadmeGeneratorError) as exc:
        readme_agent(
            alignment=None,
            api="invalid_api_provider",
            badge_style=None,
            badge_color=None,
            emojis=None,
            image=None,
            max_tokens=None,
            model=None,
            output=None,
            repository="https:///invalid_url",
            temperature=None,
            tree_depth=None,
        )
    assert isinstance(exc.value, ReadmeGeneratorError)


@pytest.mark.asyncio
async def test_readme_generator_exception_handling(mock_configs):
    """Test the readme_generator function exception handling."""
    with pytest.raises(ReadmeGeneratorError) as exc:
        await readme_generator(mock_configs)
    assert isinstance(exc.value, ReadmeGeneratorError)
