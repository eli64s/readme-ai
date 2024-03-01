"""
Google Cloud's Vertex AI LLM API implementation.
"""

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

from readmeai.config.settings import ConfigLoader
from readmeai.core.models import BaseModelHandler
from readmeai.models.tokens import token_handler
from readmeai.utils.text_cleaner import clean_response


class VertexAIHandler(BaseModelHandler):
    """Google Cloud Vertex AI LLM API implementation."""

    def __init__(self, config_loader: ConfigLoader) -> None:
        """Initialize GCP Vertex AI API LLM handler."""
        super().__init__(config_loader)
        self._model_settings()

    def _model_settings(self):
        """Initializes the Vertex AI LLM settings."""
        self.location = os.environ.get("VERTEXAI_LOCATION")
        self.project_id = os.environ.get("VERTEXAI_PROJECT")
        self.temperature = self.config.llm.temperature
        self.tokens = self.config.llm.tokens
        self.top_p = self.config.llm.top_p
        vertexai.init(location=self.location, project=self.project_id)
        self.model = GenerativeModel(self.config.llm.model)

    async def _build_payload(self, prompt: str, tokens: int) -> dict:
        """Build payload for POST request to Vertex AI API."""
        return {
            "max_output_tokens": tokens,
            "temperature": self.temperature,
            "top_p": self.top_p,
        }

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
    async def _make_request(
        self,
        index: str,
        prompt: str,
        tokens: int,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Processes Vertex AI LLM API responses and returns generated text."""
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            data = await self._build_payload(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=data,
                )
                content = response.text if response.text else response
                self._logger.info(f"Response for '{index}':\n{content}")
                return index, clean_response(index, content)

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        ) as exc:
            self._logger.error(
                f"Error making request to Vertex AI for `{index}`: {exc}"
            )
            return index, self.config.md.placeholder
