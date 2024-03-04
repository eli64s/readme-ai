"""
Abstract base class for the large language model (LLM) API handlers.
"""

import asyncio
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import Any, Dict, Generator, List, Tuple, Union

import aiohttp

from readmeai.cli.options import ModelOptions as llms
from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import Logger
from readmeai.models.prompts import (
    get_prompt_context,
    set_additional_contexts,
    set_summary_context,
)
from readmeai.models.tokens import update_max_tokens


class BaseModelHandler(ABC):
    """Abstract base class for Large Language Model (LLM) API handlers."""

    def __init__(self, config_loader: ConfigLoader) -> None:
        """Initializes the LLM handler with configuration and logging."""
        self._logger = Logger(__name__)
        self._session: aiohttp.ClientSession = None
        self.config = config_loader.config
        self.prompts = config_loader.prompts
        self.sys_content = self.config.api.content
        self.rate_limit = self.config.api.rate_limit
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)

    @abstractmethod
    async def _model_settings(self):
        """Initializes the LLM settings for the specific API implementation."""
        ...

    @abstractmethod
    async def _build_payload(self, prompt: str, tokens: int) -> Dict[str, Any]:
        """Builds the payload for the POST request to the LLM API."""
        ...

    @abstractmethod
    async def _make_request(
        self,
        index: str,
        prompt: str,
        tokens: int,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Handles LLM API response and returns the generated text."""
        ...

    @asynccontextmanager
    async def use_api(self) -> Generator:
        """Async context manager for managing the lifecycle of the HTTP client."""
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=None)
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
            self._session = None
        else:
            self._logger.debug("HTTP client already closed.")

    async def batch_request(
        self,
        dependencies: List[str],
        raw_files: List[Tuple[str, str]],
    ) -> List[str]:
        """Generates a batch of prompts and processes the responses.

        Parameters
        ----------
        dependencies
            List of dependencies for the project.
        raw_files
            List of tuples containing all file paths and file contents.

        Returns
        -------
            List of generated text responses from the LLM API.
        """
        if self.config.llm.api == llms.OFFLINE.name:
            return await self._make_request(
                index=None, prompt=None, tokens=None, raw_files=raw_files
            )
        else:
            raw_files = [
                file for file in raw_files if not file[0].endswith(".lock")
            ]
        summaries_prompts = await set_summary_context(
            self.config, dependencies, raw_files
        )
        summaries_responses = await self._batch_prompts(summaries_prompts)

        additional_prompts = await set_additional_contexts(
            self.config, dependencies, summaries_responses
        )
        additional_responses = await self._batch_prompts(additional_prompts)

        return summaries_responses + additional_responses

    async def _batch_prompts(
        self, prompts: List[Union[str, Tuple[str, str]]], batch_size: int = 10
    ) -> List[str]:
        """Processes a batch of prompts and returns the generated text.

        Parameters
        ----------
        prompts
            List of prompts to be processed.
        batch_size, optional
            Max number of prompts to process in a single batch. Defaults to 10.

        Returns
        -------
            List of generated text responses from the LLM API.
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
        self, items: List[Any], batch_size: int
    ) -> Generator[List[Any], None, None]:
        """Generates batches of items to be processed.

        Parameters
        ----------
        items
            List of items to be processed.
        batch_size
            Maximum number of items to process in a single batch.

        Returns
        -------
            List of batches of items to be processed.

        Yields
        ------
            List of items to be processed.
        """
        for i in range(0, len(items), batch_size):
            yield items[i : i + batch_size]

    async def _process_batch(self, prompt: Dict[str, Any]) -> str:
        """Processes a single prompt and returns the generated text.

        Parameters
        ----------
        prompt
            Prompt to be processed by the LLM API.

        Returns
        -------
            Generated text response from the LLM API.
        """
        if prompt["type"] == "file_summary":
            return await self._make_request_code_summary(prompt["context"])
        else:
            formatted_prompt = get_prompt_context(
                self.prompts, prompt["type"], prompt["context"]
            )
            tokens = update_max_tokens(self.tokens, formatted_prompt)
            _, summary = await self._make_request(
                prompt["type"], formatted_prompt, tokens
            )
            return summary

    async def _make_request_code_summary(
        self, file_context: List[Tuple[str, str]]
    ) -> List[Tuple[str, str]]:
        """Generates code summaries for each file in the project.

        Parameters
        ----------
        file_context
            List of tuples containing all file paths and file contents.

        Returns
        -------
            List of generated code summaries for each file in the project.
        """
        summary_text = []

        for file_path, file_content in file_context["file_summary"]:
            prompt = self.prompts["prompts"]["file_summary"].format(
                self.config.md.tree, file_path, file_content
            )
            tokens = update_max_tokens(self.tokens, prompt)
            _, summary_or_error = await self._make_request(
                file_path, prompt, tokens
            )
            summary_text.append((file_path, summary_or_error))

        return summary_text
