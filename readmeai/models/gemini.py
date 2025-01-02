"""Google Gemini LLM API service implementation."""

from typing import Any

import aiohttp
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.enums import GeminiModels
from readmeai.models.tokens import token_handler
from readmeai.utilities.importer import is_available
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)


class GeminiHandler(BaseModelHandler):
    """
    Google Gemini LLM API service implementation.
    """

    def __init__(self, config_loader: ConfigLoader, context: RepositoryContext) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        if is_available("google.generativeai"):
            import google.generativeai as genai

            self.model_name = GeminiModels.GEMINI_FLASH.value
            genai.configure()
            self.model = genai.GenerativeModel(self.model_name)
            self.generation_config = genai.types.GenerationConfig(
                max_output_tokens=self.max_tokens,
                temperature=self.temperature,
                top_p=self.top_p,
            )
        else:
            self._logger.error(
                "Google Generative AI library is not installed in current environment."
            )
            raise RuntimeError(
                """Install the optional dependencies for Gemini:
                pip install 'readmeai[google-generativeai]'"""
            )

    async def _build_payload(self, prompt: str) -> Any:
        """Build request body for making text generation requests."""
        return self.generation_config

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        )),
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
            prompt = await token_handler(
                config=self.config,
                index=index,
                prompt=prompt,
                tokens=tokens,
            )

            parameters = await self._build_payload(prompt)

            async with self.rate_limit_semaphore:
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=parameters,
                )
                content = response.text if hasattr(response, "text") else str(response)
                self._logger.info(f"Response from Gemini for '{index}': {content}")
                return index, content

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        ) as e:
            self._logger.error(f"Gemini API error for '{index}': {e!r}")
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
