from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from readmeai.__main__ import (
    error_handler,
    generate_image,
    log_process_completion,
    log_repository_context,
    readme_agent,
    should_generate_image,
)
from readmeai.config.constants import ImageOptions, LLMService
from readmeai.config.settings import ConfigLoader
from readmeai.errors import ReadmeGeneratorError
from readmeai.ingestion.models import RepositoryContext


def test_error_handler_with_exception():
    """Test that ReadmeGeneratorError is raised when an error occurs."""
    with pytest.raises(ReadmeGeneratorError), error_handler():
        raise ValueError("Test error")


@patch("readmeai.__main__.asyncio.run")
def test_readme_agent(mock_asyncio_run, config_loader_fixture: ConfigLoader):
    """Test readme_agent calls asyncio.run."""
    readme_agent(config_loader_fixture, "readme-ai.md")
    mock_asyncio_run.assert_called_once()


@pytest.mark.asyncio
async def test_generate_image(config_loader_fixture: ConfigLoader):
    """Test generate_image generates an image using DalleHandler."""
    config_loader_fixture.config.md.image = ImageOptions.LLM.value
    with patch("readmeai.__main__.DalleHandler") as mock_dalle_handler_class:
        mock_dalle_handler = AsyncMock()
        mock_dalle_handler_class.return_value.__aenter__.return_value = (
            mock_dalle_handler
        )
        mock_dalle_handler._make_request.return_value = "image_url"
        mock_dalle_handler.download.return_value = "image_path"
        mock_config = config_loader_fixture
        await generate_image(mock_config)
        assert mock_config.config.md.image == "image_path"


def test_should_generate_image_true(config_loader_fixture: ConfigLoader):
    """Test should_generate_image returns True when conditions are met."""
    # Ensure the API is not set to offline
    mock_config = config_loader_fixture
    mock_config.config.llm.api = "valid_api"
    mock_config.config.md.image = ImageOptions.LLM.value
    result = should_generate_image(mock_config)
    assert result is True


def test_should_generate_image_false_due_to_image_option(
    config_loader_fixture: ConfigLoader,
):
    """Test should_generate_image returns False when image option is not LLM."""
    mock_config = config_loader_fixture
    mock_config.config.md.image = "not-llm"
    result = should_generate_image(mock_config)
    assert result is False


def test_should_generate_image_false_due_to_offline_mode(
    config_loader_fixture: ConfigLoader,
):
    """Test should_generate_image returns False when API is offline."""
    mock_config = config_loader_fixture
    mock_config.config.llm.api = LLMService.OFFLINE.value
    result = should_generate_image(mock_config)
    assert result is False


@patch("readmeai.__main__._logger")
def test_log_repository_context(mock_logger):
    """Test that log_repository_context logs repository context information."""
    context = MagicMock(spec=RepositoryContext)
    context.files = ["file1.py", "file2.py"]
    context.metadata = {"author": "John Doe"}
    context.dependencies = ["numpy", "pandas"]
    context.language_counts = {"Python": 2}

    log_repository_context(context)

    mock_logger.info.assert_any_call("Total files analyzed: 2")
    mock_logger.info.assert_any_call(f"Metadata extracted: {context.metadata}")
    mock_logger.info.assert_any_call(f"Dependencies: {context.dependencies}")
    mock_logger.info.assert_any_call(f"Languages: {context.language_counts}")


@patch("readmeai.__main__._logger")
def test_log_process_completion(mock_logger):
    """Test that log_process_completion logs README generation completion."""
    output_file = "README.md"
    log_process_completion(output_file)
    mock_logger.info.assert_any_call("README.md file generated successfully.")
    mock_logger.info.assert_any_call(f"Output file saved @ {output_file}")
    mock_logger.info.assert_any_call(
        "Share with us @ github.com/eli64s/readme-ai/discussions"
    )
