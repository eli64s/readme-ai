"""Google Gemini LLM API service implementation."""

import os
from typing import Any

import aiohttp
import google.generativeai as genai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler


class GeminiHandler(BaseModelHandler):
    """
    Google Gemini LLM API service implementation.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=api_key)
        self.model_name = "gemini-1.5-flash"
        self.model = genai.GenerativeModel(self.model_name)
        self.top_p = self.config.llm.top_p

    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """Build payload for POST request to the Gemini API."""
        return genai.types.GenerationConfig(
            max_output_tokens=self.max_tokens,
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
        repo_files: Any,
    ) -> Any:
        """Processes Gemini API responses and returns generated text."""
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            parameters = await self._build_payload(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=parameters,
                )
                data = response.text
                self._logger.info(
                    f"Response from Gemini for '{index}': {data}"
                )
                return index, data

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        ) as e:
            self._logger.error(
                f"Error processing request for '{index}': {e!r}"
            )
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
