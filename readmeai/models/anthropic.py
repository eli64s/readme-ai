"""Anthropic API service implementation."""

import os
from typing import Any, Optional

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.settings import Settings
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler

try:
    import anthropic

    ANTHROPIC_AVAILABLE = True
    ANTHROPIC_EXCEPTIONS = (
        anthropic.APIError,
        anthropic.APIConnectionError,
        anthropic.RateLimitError,
    )
except ImportError:
    anthropic = None
    ANTHROPIC_AVAILABLE = False
    ANTHROPIC_EXCEPTIONS = tuple()


class AnthropicHandler(BaseModelHandler):
    """
    Anthropic Claude LLM API service implementation.
    """

    def __init__(self, config: Settings, context: RepositoryContext) -> None:
        super().__init__(config, context)
        self.client: Optional[Any] = None
        self.model: str = "claude-3-opus-20240229"
        if ANTHROPIC_AVAILABLE:
            self._model_settings()
        else:
            self._logger.warning(
                "Anthropic library is not available. Some features will be disabled."
            )

    def _model_settings(self):
        if not ANTHROPIC_AVAILABLE:
            self._logger.error(
                "Attempted to configure Anthropic model without the required library."
            )
            return

        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            self._logger.error(
                "ANTHROPIC_API_KEY environment variable is not set."
            )
            return

        self.client = anthropic.AsyncAnthropic(api_key=api_key)

    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """Build payload for POST request to the Anthropic API."""
        if not ANTHROPIC_AVAILABLE:
            raise RuntimeError("Anthropic library is not available.")

        return {
            "model": self.model,
            "max_tokens": tokens,
            "temperature": self.temperature,
            "messages": [{"role": "user", "content": prompt}],
            "system": self.system_message,
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(ANTHROPIC_EXCEPTIONS),
    )
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: list[tuple[str, str]] | None,
    ) -> Any:
        """Processes Anthropic API responses and returns generated text."""
        if not ANTHROPIC_AVAILABLE:
            self._logger.error(
                "Anthropic SDK is not installed. Install with: "
                "pip install 'readmeai[anthropic]'"
            )
            return index, self.placeholder

        if self.client is None:
            self._logger.error("Anthropic client is not initialized.")
            return index, self.placeholder

        try:
            token_count = self.client.beta.messages.count_tokens(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
            self._logger.info(
                f"Pre request token count: {token_count}/{tokens}"
            )

            prompt = await token_handler(self.config, index, prompt, tokens)
            parameters = await self._build_payload(prompt, tokens)

            async with self.rate_limit_semaphore:
                self._logger.info(f"Making request to Anthropic for '{index}'")
                response = await self.client.messages.create(**parameters)
                data = (
                    response.content[0].text
                    if hasattr(response, "content")
                    else str(response)
                )
                self._logger.info(
                    f"Response from Anthropic for '{index}': {data}"
                )
                return index, data

        except ANTHROPIC_EXCEPTIONS as e:
            self._logger.error(
                f"API Error processing request for '{index}': {e!r}"
            )
            # Re-raise for retry decorator
            raise

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
