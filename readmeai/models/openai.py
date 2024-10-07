"""OpenAI API model handler implementation, with Ollama support."""

import os
from typing import Any

import aiohttp
import openai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.constants import LLMService
from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler


class OpenAIHandler(BaseModelHandler):
    """
    OpenAI API LLM implementation, with Ollama support.
    """

    def __init__(
        self, config_loader: ConfigLoader, context: RepositoryContext
    ) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        self.host_name = self.config.llm.host_name
        self.localhost = self.config.llm.localhost
        self.model = self.config.llm.model
        self.path = self.config.llm.path
        self.tokens = self.config.llm.tokens
        self.top_p = self.config.llm.top_p

        if self.config.llm.api == LLMService.OPENAI.name:
            self.url = f"{self.host_name}{self.path}"
            self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        elif self.config.llm.api == LLMService.OLLAMA.name:
            self.url = f"{self.localhost}{self.path}"
            self.client = openai.OpenAI(
                base_url=f"{self.localhost}v1",
                api_key=LLMService.OLLAMA.name,
            )

        self.headers = {"Authorization": f"Bearer {self.client.api_key}"}

    async def _build_payload(self, prompt: str, tokens: int) -> dict:
        """Build payload for POST request to OpenAI API."""
        return {
            "messages": [
                {
                    "role": "system",
                    "content": self.system_message,
                },
                {"role": "user", "content": prompt},
            ],
            "model": self.model,
            "max_tokens": tokens,
            "temperature": self.temperature,
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(
            (
                aiohttp.ClientError,
                aiohttp.ClientResponseError,
                aiohttp.ClientConnectorError,
                openai.OpenAIError,
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
        """Processes OpenAI API LLM responses and returns generated text."""
        try:
            prompt = await token_handler(self.config, index, prompt, tokens)

            parameters = await self._build_payload(prompt, tokens)

            async with self._session.post(
                self.url,
                headers=self.headers,
                json=parameters,
            ) as response:
                response.raise_for_status()
                data = await response.json()
                data = data["choices"][0]["message"]["content"]
                self._logger.info(
                    f"Response from OpenAI for '{index}': {data}"
                )
                return index, data

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
            openai.OpenAIError,
        ) as e:
            self._logger.error(
                f"Error processing request for '{index}': {e!r}"
            )
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
