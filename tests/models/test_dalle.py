"""
Tests for multi-modal models and image generation.
"""

from unittest.mock import MagicMock, patch

from readmeai.cli.options import ImageOptions
from readmeai.models.dalle import DalleHandler


@patch("readmeai.models.dalle.Client")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
def test_image_generator(mock_client):
    """Test image generation."""
    # Given
    config = MagicMock()
    image_generator = DalleHandler(config)
    image_generator._build_prompt = MagicMock(return_value="prompt")
    image_generator.client.images.run = MagicMock(
        return_value=MagicMock(data=[MagicMock(url="url")])
    )
    # When
    result = image_generator.run()
    # Then
    assert result is not None


@patch("readmeai.models.dalle.get")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
def test_image_download(mock_get):
    """Test image download."""
    # Given
    config = MagicMock()
    image_generator = DalleHandler(config)
    image_generator._logger = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b"image"
    mock_get.return_value = mock_response
    # When
    result = image_generator.download("url")
    # Then
    assert isinstance(result, str)
    image_generator._logger.error.assert_not_called()


@patch("readmeai.models.dalle.get")
@patch.dict("os.environ", {"OPENAI_API_KEY": "sk-test-key"}, clear=True)
def test_image_download_failure(mock_get):
    """Test image download failure."""
    # Given
    config = MagicMock()
    image_generator = DalleHandler(config)
    image_generator._logger = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    mock_get.side_effect = Exception("404")

    # When
    result = image_generator.download("url")

    # Then
    with patch("builtins.open", MagicMock()) as mock_open:
        assert result == ImageOptions.BLUE.value
        image_generator._logger.error.assert_called_once_with(
            "Failed to download image: 404"
        )
        mock_open.assert_not_called()
        mock_response.content = b"image"
        mock_response.status_code = 200
        result = image_generator.download("url")
        assert result == ImageOptions.BLUE.value
