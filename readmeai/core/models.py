"""Abstract base class for the Large Language Model (LLM) API handlers."""

import asyncio
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import Any, Dict, Generator, List, Tuple, Union

import aiohttp

from readmeai.config.settings import ConfigLoader, Settings
from readmeai.models.prompts import (
    get_prompt_context,
    set_additional_contexts,
    set_feature_context,
    set_summary_context,
)
from readmeai.models.tokens import (
    count_tokens,
    truncate_tokens,
    update_max_tokens,
)
from readmeai.utils.logger import Logger


class BaseModelHandler(ABC):
    """Base class for the Large Language Model (LLM) API handlers.

    Parameters
    ----------
    ABC
        Abstract base class for the LLM API handler implementations.
    """

    def __init__(self, config: Settings, config_loader: ConfigLoader) -> None:
        """Initializes the LLM handler.

        Parameters
        ----------
        config
            Base configuration settings for the application.
        config_loader
            Application configuration loader with all loaded TOML files.
        """
        self._logger = Logger(__name__)
        self._session = None
        self.config = config
        self.prompts = config_loader.prompts
        self.rate_limit_semaphore = asyncio.Semaphore(
            self.config.llm.rate_limit
        )

    async def _http_client(self) -> aiohttp.ClientSession:
        """Initializes the HTTP client for the LLM API.

        Returns
        -------
            HTTP client session for the LLM API.
        """
        return aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=None))

    @abstractmethod
    async def _llm_settings(self):
        """
        Initializes the LLM settings for the specific API implementation.
        """
        ...

    @abstractmethod
    async def _handle_response(
        self,
        index: str,
        prompt: str,
        tokens: int,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Handles LLM API response and returns the generated text.

        Parameters
        ----------
        index
            Prompt type or index for the LLM API.
        prompt
            Prompt to be processed by the LLM API.
        tokens
            Maximum number of tokens to process in the prompt.
        raw_files, optional
            List of tuples containing all file paths and file contents.

        Returns
        -------
            Tuple containing the prompt index and the generated text response.
        """
        ...

    @asynccontextmanager
    async def use_api(self) -> Any:
        """
        Manages lifecycle of the HTTP client in an async context.
        """
        try:
            self._session = await self._http_client()
            yield self
        finally:
            await self.close()

    async def close(self) -> None:
        """
        Closes the HTTP client session.
        """
        if self._session:
            await self._session.close()
            self._session = None
        else:
            self._logger.debug("HTTP client session is already closed.")

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
        if self.config.llm.offline is True:
            return await self._handle_response(
                index=None, prompt=None, tokens=None, raw_files=raw_files
            )
        else:
            raw_files = [
                file for file in raw_files if not file[0].endswith(".lock")
            ]

        file_summary_prompts = await set_summary_context(
            self.config, dependencies, raw_files
        )
        file_summary_responses = await self._batch_prompts(
            file_summary_prompts
        )

        additional_prompts = await set_additional_contexts(
            self.config, dependencies, file_summary_responses
        )
        additional_responses = await self._batch_prompts(additional_prompts)

        synthesize_features_table_prompt = await set_feature_context(
            additional_responses[0]
        )
        synthesize_features_table_response = await self._batch_prompts(
            synthesize_features_table_prompt
        )

        return (
            file_summary_responses
            + additional_responses
            + synthesize_features_table_response
        )

    async def _batch_prompts(
        self, prompts: List[Union[str, Tuple[str, str]]], batch_size: int = 10
    ) -> List[str]:
        """Processes a batch of prompts and returns the generated text.

        Parameters
        ----------
        prompts
            List of prompts to be processed.
        batch_size, optional
            Maximum number of prompts to process in a single batch. By default 10.

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
            return await self._handle_response_code_summary(prompt["context"])
        else:
            formatted_prompt = get_prompt_context(
                self.prompts, prompt["type"], prompt["context"]
            )
            tokens = update_max_tokens(self.tokens, formatted_prompt)
            _, summary = await self._handle_response(
                prompt["type"], formatted_prompt, tokens
            )
            return summary

    async def _handle_response_code_summary(
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
            _, summary_or_error = await self._handle_response(
                file_path, prompt, tokens
            )
            summary_text.append((file_path, summary_or_error))

        return summary_text

    async def _token_handler(
        self, index: str, prompt: str, tokens: int
    ) -> str:
        """Handle token count for the prompt."""
        token_cnt = count_tokens(prompt, self.encoding)

        if token_cnt > self.tokens_max:
            self._logger.debug(
                f"Truncating '{index}' prompt: {token_cnt} > {self.tokens_max}"
            )
            prompt = truncate_tokens(self.encoding, prompt, tokens)

        return prompt
