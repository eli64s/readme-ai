"""Google Gemini LLM API service implementation."""

import os
from typing import Any, Optional

import aiohttp
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

try:
    import google.generativeai as genai

    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    GENAI_AVAILABLE = False


class GeminiHandler(BaseModelHandler):
    """
    Google Gemini LLM API service implementation.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)
        self.model: Optional[Any] = None
        self.model_name: str = "gemini-1.5-flash"
        self.top_p: float = (
            0.8  # Default value, override from config if available
        )
        if GENAI_AVAILABLE:
            self._model_settings()
        else:
            self._logger.warning(
                "Google Generative AI library is not available. Some features will be disabled."
            )

    def _model_settings(self):
        if not GENAI_AVAILABLE:
            self._logger.error(
                "Attempted to configure Gemini model without the required library."
            )
            return

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            self._logger.error(
                "GOOGLE_API_KEY environment variable is not set."
            )
            return

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(self.model_name)

        # Safely get top_p from config, use default if not available
        self.top_p = getattr(self.config.llm, "top_p", self.top_p)

    async def _build_payload(self, prompt: str, tokens: int) -> Any:
        """Build payload for POST request to the Gemini API."""
        if not GENAI_AVAILABLE:
            raise RuntimeError(
                "Google Generative AI library is not available."
            )

        return genai.types.GenerationConfig(
            max_output_tokens=tokens,
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
            )
            if GENAI_AVAILABLE
            else tuple()
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
        if not GENAI_AVAILABLE:
            self._logger.error(
                "Cannot make request: Google Generative AI library is not available."
            )
            return index, self.placeholder

        if self.model is None:
            self._logger.error("Gemini model is not properly initialized.")
            return index, self.placeholder

        try:
            prompt = await token_handler(self.config, index, prompt, tokens)
            parameters = await self._build_payload(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.model.generate_content_async(
                    prompt,
                    generation_config=parameters,
                )
                data = (
                    response.text
                    if hasattr(response, "text")
                    else str(response)
                )
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
