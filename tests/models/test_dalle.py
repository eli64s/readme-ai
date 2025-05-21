import re
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from readmeai.generators.enums import DefaultLogos
from readmeai.models.dalle import DalleHandler


def cleanup_mock_png_files(directory="."):
    """Cleanup mock png files."""
    pattern = re.compile(
        r"<MagicMock name='mock\.config\.git\.name' id='\d+'>\.png",
    )
    for filename in Path(directory).glob("*.png"):
        if pattern.match(filename.name) and filename.exists():
            filename.unlink()


@pytest.mark.asyncio
@patch("readmeai.models.dalle.openai.AsyncOpenAI")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_image_generator(mock_openai):
    """Test image generator."""
    # Given
    config = MagicMock()
    mock_client = AsyncMock()
    mock_openai.return_value = mock_client
    mock_response = MagicMock()
    mock_response.data = [MagicMock(url="test_url")]
    mock_client.images.generate.return_value = mock_response

    async with DalleHandler(config) as image_generator:
        # When
        result = await image_generator._make_request()

        # Then
        assert result == "test_url"
        mock_client.images.generate.assert_called_once()

    # Cleanup
    cleanup_mock_png_files()


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_image_download(mock_get):
    """Test image download."""
    # Given
    config = MagicMock()
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.read.return_value = b"logo"
    mock_get.return_value.__aenter__.return_value = mock_response

    async with DalleHandler(config) as image_generator:
        image_generator._logger = MagicMock()

        # When
        result = await image_generator.download("url")

        # Then
        assert isinstance(result, str)
        assert result == image_generator.filename
        image_generator._logger.error.assert_not_called()

    # Cleanup
    cleanup_mock_png_files()


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.get")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_image_download_failure(mock_get):
    """Test image download failure."""
    # Given
    config = MagicMock()
    mock_response = AsyncMock()
    mock_response.status = 404
    mock_get.return_value.__aenter__.return_value = mock_response

    async with DalleHandler(config) as image_generator:
        image_generator._logger = MagicMock()

        # When
        result = await image_generator.download("url")

        # Then
        assert result == DefaultLogos.PURPLE.value
        image_generator._logger.error.assert_called_once_with(
            "Failed to download image: 404"
        )

    # Cleanup
    cleanup_mock_png_files()


@pytest.mark.asyncio
@patch("readmeai.models.dalle.openai.AsyncOpenAI")
@patch("aiohttp.ClientSession.get")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
async def test_generate_and_download(mock_get, mock_openai):
    """Test generate and download process."""
    # Given
    config = MagicMock()
    mock_client = AsyncMock()
    mock_openai.return_value = mock_client
    mock_response = MagicMock()
    mock_response.data = [MagicMock(url="test_url")]
    mock_client.images.generate.return_value = mock_response

    mock_download_response = AsyncMock()
    mock_download_response.status = 200
    mock_download_response.read.return_value = b"logo"
    mock_get.return_value.__aenter__.return_value = mock_download_response

    async with DalleHandler(config) as image_generator:
        # When
        result = await image_generator.generate_and_download()

        # Then
        assert result == image_generator.filename
        mock_client.images.generate.assert_called_once()
        mock_get.assert_called_once_with("test_url")

    # Cleanup
    cleanup_mock_png_files()
