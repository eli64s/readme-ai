"""Anthropic LLM API service implementation."""

from typing import Any

import aiohttp
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.enums import AnthropicModels
from readmeai.models.tokens import token_handler
from readmeai.utilities.importer import is_available
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

if is_available("anthropic"):
    import anthropic

    ANTHROPIC_AVAILABLE = True
    ANTHROPIC_EXCEPTIONS = (
        anthropic.APIError,
        anthropic.APIConnectionError,
        anthropic.RateLimitError,
    )
else:
    anthropic = None
    ANTHROPIC_AVAILABLE = False
    ANTHROPIC_EXCEPTIONS: tuple[type[Exception], ...] = tuple()


class AnthropicHandler(BaseModelHandler):
    """
    Anthropic LLM API service implementation.
    """

    def __init__(self, config_loader: ConfigLoader, context: RepositoryContext) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        self.client = anthropic.AsyncAnthropic()
        self.model = AnthropicModels.CLAUDE35_SONNET.value

    async def _build_payload(self, prompt: str) -> dict[str, Any]:
        """Build request body for making text generation requests."""

        return {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "messages": [{"role": "user", "content": prompt}],
            "system": self.system_message,
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type((
            *ANTHROPIC_EXCEPTIONS,
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
        repo_files: list[tuple[str, str]] | None,
    ) -> Any:
        """Processes Anthropic API responses and returns generated text."""
        try:
            prompt = await token_handler(
                config=self.config,
                index=index,
                prompt=prompt,
                tokens=tokens,
            )
            parameters = await self._build_payload(prompt)

            async with self.rate_limit_semaphore:
                response = await self.client.messages.create(**parameters)
                content = (
                    response.content[0].text
                    if hasattr(response, "content")
                    else str(response)
                )
                self._logger.info(f"Response from Anthropic for '{index}': {content}")
                return index, content

        except (
            *ANTHROPIC_EXCEPTIONS,
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
        ) as e:
            self._logger.error(f"Anthropic API error for '{index}': {e!r}")
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
