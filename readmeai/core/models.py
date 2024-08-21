"""
Abstract base class for the large language model (LLM) API handlers.
"""

import asyncio
from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager
from typing import Any

import aiohttp

from readmeai.config.settings import ConfigLoader, ModelOptions
from readmeai.core.logger import Logger
from readmeai.models.prompts import (
    get_prompt_context,
    set_additional_contexts,
    set_summary_context,
)
from readmeai.models.tokens import update_max_tokens


class BaseModelHandler(ABC):
    """
    Abstract base class for Large Language Model (LLM) API handlers.
    """

    def __init__(self, config_loader: ConfigLoader) -> None:
        """
        Initializes the LLM handler with configuration and logging.
        """
        self._logger = Logger(__name__)
        self._session: aiohttp.ClientSession = None
        self.config = config_loader.config
        self.prompts = config_loader.prompts
        self.system_message = self.config.api.system_message
        self.rate_limit = self.config.api.rate_limit
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)

    @abstractmethod
    async def _model_settings(self) -> None:
        """
        Initializes the LLM settings for the specific API implementation.
        """
        ...

    @abstractmethod
    async def _build_payload(self, prompt: str, tokens: int) -> dict[str, Any]:
        """
        Builds the payload for the POST request to the LLM API.
        """
        ...

    @abstractmethod
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        raw_files: list[tuple[str, str]] | None,
    ) -> list[tuple[str, str]]:
        """
        Handles LLM API response and returns the generated text.
        """
        ...

    @asynccontextmanager
    async def use_api(self) -> AsyncGenerator[Any, None]:
        """Async context manager for managing the lifecycle of the HTTP client."""
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=None),
        ) as session:
            self._session = session
            try:
                yield self
            finally:
                await self.close()

    async def close(self) -> None:
        """Closes the HTTP client session."""
        if self._session:
            await self._session.close()
            self._logger.debug("HTTP client closed.")
        else:
            self._logger.debug("HTTP client already closed.")

    async def batch_request(
        self,
        dependencies: list[str],
        raw_files: list[tuple[str, str]],
    ) -> list[tuple[str, str]]:
        """
        Generates a batch of prompts and processes the responses.
        """
        if self.config.llm.api == ModelOptions.OFFLINE.name:
            return await self._make_request(
                index=None,
                prompt=None,
                tokens=None,
                raw_files=raw_files,
            )
        else:
            raw_files = [
                file for file in raw_files if not file[0].endswith(".lock")
            ]
        summaries_prompts = await set_summary_context(
            self.config,
            dependencies,
            raw_files,
        )
        summaries_responses = await self._batch_prompts(summaries_prompts)

        additional_prompts = await set_additional_contexts(
            self.config,
            dependencies,
            summaries_responses,
        )
        additional_responses = await self._batch_prompts(additional_prompts)

        return summaries_responses + additional_responses

    async def _batch_prompts(
        self,
        prompts: list[str | tuple[str, str]],
        batch_size: int = 10,
    ) -> list[tuple[str, str]]:
        """
        Processes a batch of prompts and returns the generated text.
        """
        responses = []

        for batch in self._generate_batches(prompts, batch_size):
            batch_responses = await asyncio.gather(
                *[self._process_batch(prompt) for prompt in batch],
                return_exceptions=True,
            )
            responses.extend(batch_responses)

        return responses

    def _generate_batches(
        self,
        items: list[Any],
        batch_size: int,
    ) -> Generator[list[Any], None, None]:
        """
        Generates batches of items to be processed.
        """
        for i in range(0, len(items), batch_size):
            yield items[i : i + batch_size]

    async def _process_batch(self, prompt: dict[str, Any]) -> Any:
        """
        Processes a single prompt and returns the generated text.
        """
        if prompt["type"] == "file_summary":
            return await self._make_request_code_summary(prompt["context"])
        else:
            formatted_prompt = get_prompt_context(
                self.prompts,
                prompt["type"],
                prompt["context"],
            )
            tokens = update_max_tokens(
                self.config.llm.tokens,
                formatted_prompt,
            )
            _, summary = await self._make_request(
                prompt["type"],
                formatted_prompt,
                tokens,
                None,
            )
            return summary

    async def _make_request_code_summary(
        self,
        file_context: list[tuple[str, str]],
    ) -> list[tuple[str, str]]:
        """
        Generates code summaries for each file in the project.
        """
        summary_text = []

        for file_path, file_content in file_context["file_summary"]:
            prompt = self.prompts["prompts"]["file_summary"].format(
                self.config.md.tree,
                file_path,
                file_content,
            )
            tokens = update_max_tokens(
                self.config.llm.tokens,
                prompt,
            )
            _, summary_or_error = await self._make_request(
                file_path,
                prompt,
                tokens,
                None,
            )
            summary_text.append((file_path, summary_or_error))

        return summary_text
