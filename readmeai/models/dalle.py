"""Text-to-Image generation using OpenAI's DALL-E model.

Notes:
------
    - Generated image is saved locally as a PNG file.
    - This feature is only available OpenAI API users.
"""

from typing import Any

import aiohttp
import openai
from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import get_logger
from readmeai.generators.enums import DefaultLogos


class DalleHandler:
    """
    Generate and download an image using OpenAI's DALL-E model.
    """

    def __init__(self, config: ConfigLoader) -> None:
        self.config = config
        self.default_image = DefaultLogos.PURPLE.value
        self.filename = f"{config.config.git.name}.png"
        self._logger = get_logger(__name__)
        self._model_settings()

    def _model_settings(self) -> None:
        self.client = openai.AsyncOpenAI()
        self.model = "dall-e-3"
        self.size = "1792x1024"
        self.quality = "standard"
        self.n = 1

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
        self._logger.debug(f"Closed {self.model.upper()} API session...")

    def _build_payload(self) -> dict[str, Any]:
        """Formats the prompt string using configuration data."""
        return {
            "prompt": self.config.prompts["prompts"]["logo"].format(
                project_name=self.config.config.git.name,
                project_tagline=self.config.config.md.tagline,
                project_overview=self.config.config.md.overview,
            ),
            "model": self.model,
            "size": self.size,
            "quality": self.quality,
            "n": self.n,
        }

    async def _make_request(self) -> str:
        """Generate an image using the DALL-E model, and return its URL."""
        try:
            payload = self._build_payload()
            response = await self.client.images.generate(**payload)
            if response and response.data and response.data[0].url:
                return response.data[0].url
            else:
                self._logger.error(f"Failed to generate project logo image: {response}")
                return self.default_image

        except (Exception, openai.OpenAIError) as e:
            self._logger.error(f"Error generating project logo image: {e!r}")
            return self.default_image

    async def download(self, image_url) -> str:
        """Download the generated image from the provided URL."""
        try:
            async with self.session.get(image_url) as response:
                if response.status == 200:
                    content = await response.read()
                    with open(self.filename, "wb") as f:
                        f.write(content)

                    self._logger.info(
                        f"{self.model.upper()} image successfully downloaded."
                    )
                    return self.filename
                else:
                    self._logger.error(f"Failed to download image: {response.status}")

        except Exception as e:
            self._logger.error(f"Error downloading image: {e!r}")

        return self.default_image

    async def generate_and_download(self) -> str:
        """Generate and download the image."""
        image_url = await self._make_request()
        return await self.download(image_url)
