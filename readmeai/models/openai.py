"""OpenAI API LLM handler implementation."""

import os
from typing import List, Tuple

import aiohttp
from openai import OpenAI, OpenAIError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.settings import ConfigLoader, Settings
from readmeai.core.models import BaseModelHandler
from readmeai.utils.formatter import format_response


class OpenAIHandler(BaseModelHandler):
    """OpenAI API LLM implementation."""

    def __init__(self, config: Settings, config_loader: ConfigLoader) -> None:
        """Initialize OpenAI API LLM handler."""
        super().__init__(config, config_loader)
        self._llm_settings()
        self._openai_client()

    def _llm_settings(self):
        self.content = self.config.llm.content
        self.encoding = self.config.llm.encoding
        self.endpoint = self.config.llm.endpoint
        self.model = self.config.llm.model
        self.tokens = self.config.llm.tokens
        self.tokens_max = self.config.llm.tokens_max
        self.temperature = self.config.llm.temperature

    def _openai_client(self) -> OpenAI:
        """Set up the OpenAI API client using OpenAI API key or Ollama."""
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(
            (
                aiohttp.ClientError,
                aiohttp.ClientResponseError,
                aiohttp.ClientConnectorError,
                OpenAIError,
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
        """Processes OpenAI API LLM responses and returns generated text."""
        try:
            prompt = await self._token_handler(index, prompt, tokens)

            async with self._session.post(
                self.endpoint,
                headers={"Authorization": f"Bearer {self.client.api_key}"},
                json={
                    "messages": [
                        {
                            "role": "system",
                            "content": self.content,
                        },
                        {"role": "user", "content": prompt},
                    ],
                    "model": self.model,
                    "temperature": self.temperature,
                    "max_tokens": tokens,
                },
            ) as response:
                response.raise_for_status()
                response_json = await response.json()
                response_text = response_json["choices"][0]["message"][
                    "content"
                ]
                formatted_text = format_response(index, response_text)
                self._logger.info(f"Response for '{index}':\n{formatted_text}")
                return index, formatted_text

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
            OpenAIError,
        ) as exc:
            self._logger.error(
                f"Error making LLM API request for `{index}`: {exc}"
            )
            return index, self.config.md.placeholder

    async def close(self) -> None:
        """Ensure the HTTP client is closed properly."""
        if self._session:
            await self._session.close()

    async def __aenter__(self) -> "OpenAIHandler":
        """Initialize the HTTP client for OpenAI."""
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self) -> None:
        """Close the HTTP client for OpenAI."""
        await self.close()
