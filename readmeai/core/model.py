"""Abstract base class for all LLM implementations."""

import asyncio
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Tuple, Union

import httpx

from readmeai.config.settings import AppConfig
from readmeai.core.logger import Logger
from readmeai.llms.prompts import (
    get_prompt_context,
    set_additional_prompt_contexts,
    set_summary_prompt_context,
)
from readmeai.llms.tokens import update_max_tokens

logger = Logger(__name__)


class ModelHandler(ABC):
    """Abstract base class for LLM API implementations."""

    def __init__(self, config: AppConfig) -> None:
        """Initializes the GPT language model API handler."""
        self.config = config
        self.logger = Logger(__name__)
        self._http_client()
        self._llm_settings()

    @abstractmethod
    def _llm_settings(self):
        """Initializes basic attributes for the class."""
        ...

    @abstractmethod
    async def _handle_response(
        self,
        index: str,
        prompt: str,
        tokens: int,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Handles LLM API response and returns the generated text."""
        ...

    @asynccontextmanager
    async def use_api(self) -> None:
        """Context manager for HTTP client used by the LLM API."""
        try:
            yield self
        finally:
            await self.close()

    async def close(self) -> None:
        """Closes the HTTP client."""
        await self.http_client.aclose()

    def _http_client(self):
        """Configures the HTTP client for the class."""
        self.http_client = httpx.AsyncClient(
            http2=True,
            timeout=20,
            limits=httpx.Limits(
                max_keepalive_connections=100, max_connections=200
            ),
        )
        self.rate_limit_semaphore = asyncio.Semaphore(
            self.config.llm.rate_limit
        )

    async def batch_request(
        self,
        dependencies: List[str],
        raw_files: List[Tuple[str, str]],
    ) -> List[str]:
        """Generates text for the README.md file using LLM API."""
        if self.config.llm.offline is True:
            return await self._handle_response(
                index=None, prompt=None, tokens=None, raw_files=raw_files
            )

        prompts = await set_summary_prompt_context(
            self.config, dependencies, raw_files
        )
        file_summaries_resp = await self._batch_prompts(prompts)

        additional_prompts = await set_additional_prompt_contexts(
            self.config, dependencies, file_summaries_resp
        )
        additional_resp = await self._batch_prompts(additional_prompts)

        return file_summaries_resp + additional_resp

    async def _batch_prompts(
        self, prompts: List[Union[str, Tuple[str, str]]], batch_size: int = 10
    ):
        """Processes prompts in batches and returns the generated text."""
        responses = []

        for batch in self._generate_batches(prompts, batch_size):
            batch_responses = await asyncio.gather(
                *[self._process_batch(prompt) for prompt in batch],
                return_exceptions=True,
            )
            responses.extend(batch_responses)

        return responses

    def _generate_batches(self, items: List[Any], batch_size: int):
        """Generator to create batches from a list of items."""
        for i in range(0, len(items), batch_size):
            yield items[i : i + batch_size]

    async def _process_batch(self, prompt: Dict[str, Any]) -> str:
        """Processes a prompt and returns the generated text."""
        if prompt["type"] == "summaries":
            return await self._handle_response_code_summary(prompt["context"])
        else:
            formatted_prompt = get_prompt_context(
                self.config, prompt["type"], prompt["context"]
            )
            tokens = update_max_tokens(self.tokens, formatted_prompt)
            _, summary = await self._handle_response(
                prompt["type"], formatted_prompt, tokens
            )
            return summary

    async def _handle_response_code_summary(
        self, file_context: List[Tuple[str, str]]
    ) -> List[Tuple[str, str]]:
        """Generates code summaries for the README.md file."""
        summary_text = []
        for context in file_context["summaries"]:
            file_path, file_content = context
            prompt = self.prompts.summaries.format(
                self.config.md.tree, file_path, file_content
            )
            tokens = update_max_tokens(self.tokens, prompt)
            _, summary_or_error = await self._handle_response(
                file_path, prompt, tokens
            )
            summary_text.append((file_path, summary_or_error))

        return summary_text
