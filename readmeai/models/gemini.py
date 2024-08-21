"""
Google Cloud's Gemini API handler implementation.
"""

import os

import aiohttp
import google.generativeai as genai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import Logger
from readmeai.core.models import BaseModelHandler
from readmeai.models.tokens import token_handler
from readmeai.utils.text_cleaner import clean_response


class GeminiHandler(BaseModelHandler):
    """Google Gemini API LLM implementation."""

    def __init__(self, config_loader: ConfigLoader) -> None:
        """Initializes the Gemini API handler."""
        super().__init__(config_loader)
        self._logger = Logger(__name__)
        self._model_settings()

    def _model_settings(self):
        """Initializes the Gemini API LLM settings."""
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(self.config.llm.model)
        self.temperature = self.config.llm.temperature
        self.tokens = self.config.llm.tokens
        self.top_p = self.config.llm.top_p

    async def _build_payload(self, prompt: str, tokens: int) -> dict:
        """Build payload for POST request to the Gemini API."""
        return genai.types.GenerationConfig(
            max_output_tokens=self.tokens,
            temperature=self.temperature,
            top_p=self.top_p,
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(
            (
                aiohttp.ClientError,
                aiohttp.ClientResponseError,
                aiohttp.ClientConnectorError,
            ),
        ),
    )
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        raw_files: list[tuple[str, str]] | None,
    ) -> list[tuple[str, str]]:
        """
        Processes Gemini API responses and returns generated text.
        """
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            parameters = await self._build_payload(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=parameters,
                )
                response_text = response.text

                self._logger.info(f"Response for '{index}':\n{response_text}")

                return index, clean_response(index, response_text)

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        ):
            self._logger.error(
                f"Error processing request for prompt: {index}",
                exc_info=True,
            )
            return index, self.config.md.placeholder
