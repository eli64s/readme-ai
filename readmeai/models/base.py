"""Base class for handling LLM API requests."""

import asyncio
from abc import ABC, abstractmethod
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager
from typing import Any, List, Tuple

import aiohttp
from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import get_logger
from readmeai.extractors.models import RepositoryContext
from readmeai.models.enums import LLMProviders
from readmeai.models.prompts import (
    get_prompt_context,
    set_additional_contexts,
    set_summary_context,
)
from readmeai.models.tokens import update_max_tokens

_logger = get_logger(__name__)


class BaseModelHandler(ABC):
    """
    Interface for LLM API handler implementations.
    """

    def __init__(self, config_loader: ConfigLoader, context: RepositoryContext) -> None:
        self._logger = get_logger(__name__)
        self._session: aiohttp.ClientSession | None = None
        self.config = config_loader.config
        self.prompts = config_loader.prompts
        self.placeholder = self.config.md.placeholder
        self.max_tokens = self.config.llm.tokens
        self.rate_limit = self.config.llm.rate_limit
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)
        self.system_message = self.config.llm.system_message
        self.temperature = self.config.llm.temperature
        self.top_p = self.config.llm.top_p
        self.repo_context = context
        self.dependencies = context.dependencies
        self.documents = [
            (file.path, file.content)
            for file in context.files
            if ".lock" not in file.name
        ]

    @asynccontextmanager
    async def use_api(self) -> AsyncGenerator[Any, None]:
        """Async context manager for managing HTTP client lifecycle."""
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
            self._logger.debug("HTTP client is already closed.")

    @abstractmethod
    async def _model_settings(self) -> None:
        """Initializes LLM API settings for a given service."""
        ...

    @abstractmethod
    async def _build_payload(self, prompt: str) -> dict[str, Any]:
        """Build request body for making text generation requests."""
        ...

    @abstractmethod
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: list[tuple[str, str]] | None,
    ) -> Any:
        """Makes a POST request to the LLM API and returns the response."""
        ...

    async def batch_request(
        self,
    ) -> Tuple[List[Any], str, str, str]:
        """Generates a batch of prompts and processes the responses."""
        if self.config.llm.api == LLMProviders.OFFLINE.value:
            file_summaries = await self._make_request(
                index=None,
                prompt=None,
                tokens=None,
                repo_files=self.documents,
            )
            return (
                file_summaries,
                self.placeholder,
                self.placeholder,
                self.placeholder,
            )
        summaries_prompts = set_summary_context(
            self.config,
            self.documents,
        )
        summaries_responses = await self._batch_prompts(summaries_prompts)
        additional_prompts = set_additional_contexts(
            self.config,
            self.repo_context,
            summaries_responses,
        )
        additional_responses = await self._batch_prompts(additional_prompts)

        return summaries_responses + additional_responses

    async def _batch_prompts(
        self,
        prompts: Any,
        batch_size: int = 10,
    ) -> list[tuple[str, str]]:
        """Processes a batch of prompts and returns the generated text."""
        responses = []

        for batch in self._generate_batches(prompts, batch_size):
            batch_responses = await asyncio.gather(
                *[self._process_batch(prompt) for prompt in batch],
                return_exceptions=False,
            )
            responses.extend(batch_responses)

        return responses

    def _generate_batches(
        self,
        items: list[Any],
        batch_size: int,
    ) -> Generator[list[Any], None, None]:
        """Generates batches of items to be processed."""
        for i in range(0, len(items), batch_size):
            yield items[i : i + batch_size]

    async def _process_batch(self, prompt: dict[str, Any]) -> Any:
        """Processes a single prompt and returns the generated text."""
        if prompt["type"] == "file_summary":
            return await self._make_request_code_summary(
                prompt["context"],
            )
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
        file_context: dict[str, list[tuple[str, str]]],
    ) -> Any:
        """Generates code summaries for each file in the project."""
        if not file_context or "repo_files" not in file_context:
            return await self._make_request(
                index=None,
                prompt=None,
                tokens=None,
                repo_files=file_context["repo_files"],
            )
        else:
            file_summaries = []
            for file_path, file_content in file_context["repo_files"]:
                prompt = self.prompts["prompts"]["file_summary"].format(
                    self.config.md.directory_structure,
                    file_path,
                    file_content,
                )
                tokens = update_max_tokens(self.config.llm.tokens, prompt)
                _, summary_or_error = await self._make_request(
                    file_path,
                    prompt,
                    tokens,
                    None,
                )
                file_summaries.append((file_path, summary_or_error))

            return file_summaries
