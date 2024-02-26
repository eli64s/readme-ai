"""Google Vertex AI LLM API implementation."""

import os
from typing import List, Tuple

import aiohttp
import vertexai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)
from vertexai.preview.generative_models import GenerativeModel

from readmeai.config.settings import ConfigLoader, Settings
from readmeai.core.models import BaseModelHandler
from readmeai.utils.formatter import format_response


class VertexAIHandler(BaseModelHandler):
    """Vertex AI Generative Models API LLM implementation."""

    def __init__(self, config: Settings, config_loader: ConfigLoader) -> None:
        """Initialize GCP Vertex AI API LLM handler."""
        super().__init__(config, config_loader)
        self._gcloud_auth()
        self._llm_settings()

    def _gcloud_auth(self) -> None:
        """Authenticate with Google Cloud."""
        self.location = os.getenv("VERTEXAI_LOCATION", None)
        self.project_id = os.getenv("VERTEXAI_PROJECT", None)
        vertexai.init(project=self.project_id, location=self.location)

    def _llm_settings(self):
        """Initializes basic attributes for the class."""
        self.content = self.config.llm.content
        self.encoding = self.config.llm.encoding
        self.model = "gemini-pro"
        self.tokens = self.config.llm.tokens
        self.tokens_max = self.config.llm.tokens_max
        self.temperature = self.config.llm.temperature

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(
            (
                aiohttp.ClientError,
                aiohttp.ClientResponseError,
                aiohttp.ClientConnectorError,
            )
        ),
    )
    async def _handle_response(
        self,
        index: str,
        prompt: str,
        tokens: int,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Processes Vertex AI LLM API responses and returns generated text."""
        try:
            prompt = await self._token_handler(index, prompt, tokens)

            async with self.rate_limit_semaphore:
                model = GenerativeModel(self.model)
                response = await model.generate_content_async(
                    prompt,
                )
                response_text = response.text
                formatted_text = format_response(index, response_text)
                self._logger.info(f"Response for '{index}':\n{formatted_text}")
                return index, formatted_text

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        ) as exc:
            self._logger.error(
                f"Error making API request for `{index}`: {exc}"
            )
            return index, self.config.md.placeholder

    async def close(self) -> None:
        """Ensure the HTTP client is closed properly."""
        if self._session:
            await self._session.close()

    async def __aenter__(self):
        """Initialize the HTTP client for Vertex AI."""
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *exc_info):
        """Close the HTTP client."""
        await self.close()
