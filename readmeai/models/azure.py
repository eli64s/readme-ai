"""Azure OpenAI model handler for ReadmeAI."""
import os
from typing import Any

import aiohttp
import openai
from openai import AsyncAzureOpenAI

from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.openai_ import OpenAIHandler
from readmeai.models.tokens import token_handler


class AzureOpenAIHandler(OpenAIHandler):
    """Handler for Azure OpenAI models."""

    def __init__(self, config_loader: ConfigLoader, context: RepositoryContext) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        self.host_name = os.getenv("AZURE_ENDPOINT")
        self.max_tokens = self.config.llm.tokens
        self.model = os.getenv("AZURE_MODEL")
        self.top_p = self.config.llm.top_p

        self.client = AsyncAzureOpenAI(
            azure_endpoint=self.host_name,
            api_key=os.getenv("AZURE_API_KEY"),
            api_version=os.getenv("AZURE_API_VERSION"),
        )

    async def _make_request(
            self,
            index: str | None,
            prompt: str | None,
            tokens: int | None,
            repo_files: Any,
    ):
        """Process requests to OpenAI API, with retries and error handling."""

        try:
            if prompt is None:
                raise ValueError("Prompt cannot be None")

            prompt = await token_handler(
                config=self.config,
                index=index,
                prompt=prompt,
                tokens=tokens,
            )
            if not prompt:
                raise ValueError("Token handler returned empty prompt")

            if index == "file_summary":
                self.max_tokens = 100

            parameters = await self._build_payload(prompt)

            # Just await the create call directly
            response = await self.client.chat.completions.create(**parameters)
            content = response.choices[0].message.content

            if not content:
                raise ValueError("Empty response from API")

            self._logger.info(
                f"Response from {self.config.llm.api.capitalize()} for '{index}': {content}",
            )
            return index, content

        except (
                aiohttp.ClientError,
                aiohttp.ClientResponseError,
                aiohttp.ClientConnectorError,
                openai.OpenAIError,
        ) as e:
            self._logger.error(f"Error processing request for '{index}': {e!r}")
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
