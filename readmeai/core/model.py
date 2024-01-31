"""LLM API handler for README.md file generation."""

import asyncio
import functools
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Tuple, Union

import openai
from httpx import (
    AsyncClient,
    HTTPStatusError,
    Limits,
    NetworkError,
    TimeoutException,
)
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from readmeai.config.settings import AppConfig
from readmeai.core.logger import Logger
from readmeai.core.utils import format_response
from readmeai.llms.cache import CacheManager
from readmeai.llms.prompts import (
    get_prompt_context,
    set_other_prompt_context,
    set_prompt_context,
)
from readmeai.llms.tokenize import (
    count_tokens,
    truncate_tokens,
    update_max_tokens,
)


class ModelHandler:
    """LLM API handler that generates text for the README.md file."""

    def __init__(self, config: AppConfig) -> None:
        """Initializes the GPT language model API handler."""
        self.config = config
        self.cache = CacheManager()
        self.logger = Logger(__name__)
        self._llm_settings()
        self._http_client()
        self._handle_response = functools.lru_cache(maxsize=100)(
            self._handle_response
        )

    def _http_client(self):
        """Configures the HTTP client for the class."""
        self.http_client = AsyncClient(
            http2=True,
            timeout=20,
            limits=Limits(max_keepalive_connections=100, max_connections=20),
        )
        self.rate_limit = self.config.llm.rate_limit
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)

    def _llm_settings(self):
        """Initializes basic attributes for the class."""
        self.content = self.config.llm.content
        self.encoder = self.config.llm.encoding
        self.model = self.config.llm.model
        self.prompts = self.config.prompts
        self.tokens = self.config.llm.tokens
        self.tokens_max = self.config.llm.tokens_max
        self.temperature = self.config.llm.temperature

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

    async def batch_request(
        self,
        dependencies: List[str],
        summaries: List[str],
    ) -> List[str]:
        """Generates text for the README.md file using LLM API."""
        prompts = await set_prompt_context(
            self.config, dependencies, summaries
        )
        summaries_response = await self._batch_prompts(prompts)

        other_prompts = await set_other_prompt_context(
            self.config, dependencies, summaries_response
        )
        other_responses = await self._batch_prompts(other_prompts)

        return summaries_response + other_responses

    async def _batch_prompts(
        self, prompts: List[Union[str, Tuple[str, str]]], batch_size: int = 5
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

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, min=2, max=6),
        retry=retry_if_exception_type(
            (
                HTTPStatusError,
                NetworkError,
                TimeoutException,
                openai.error.OpenAIError,
            )
        ),
    )
    async def _handle_response(
        self, index: str, prompt: str, tokens: int
    ) -> Tuple[str, str]:
        """Generates text for the README.md file using GPT language models.

        Parameters
        ----------
        index
            Type of prompt i.e. features, overview, slogan, or code summary.
        prompt
            The prompt to generate text from.
        tokens
            The number of tokens to generate.

        Returns
        -------
        Tuple[str, str]
            Tuple containing the prompt type and generated response.
        """
        cache_key = self.cache._hash_key((index, prompt, tokens))
        cached_response = self.cache.get(cache_key)
        if cached_response:
            return cached_response

        token_cnt = count_tokens(prompt, self.encoder)
        if token_cnt > self.tokens_max:
            self.logger.debug(
                f"Truncating '{index}' prompt: {token_cnt} > {self.tokens_max}"
            )
            prompt = truncate_tokens(self.encoder, prompt, tokens)

        try:
            async with self.rate_limit_semaphore:
                response = await self.http_client.post(
                    self.config.llm.endpoint,
                    headers={"Authorization": f"Bearer {openai.api_key}"},
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
                )
                response.raise_for_status()
                response_json = response.json()
                response_text = response_json["choices"][0]["message"][
                    "content"
                ]
                formatted_text = format_response(index, response_text)

                self.logger.info(f"Response for {index}:\n{response_json}")
                self.cache.set(index, prompt, tokens, formatted_text)

                return index, formatted_text

        except (
            HTTPStatusError,
            NetworkError,
            TimeoutException,
            openai.error.OpenAIError,
        ) as exc:
            if isinstance(exc, HTTPStatusError):
                status_code = exc.response.status_code
                message = f"HTTP error {status_code} for prompt `{index}`"
            else:
                message = f"Error generating text for prompt `{index}`: {exc}"
            self.logger.error(message)
            return index, message

    async def _handle_response_code_summary(
        self, file_context: List[Tuple[str, str]]
    ) -> List[Tuple[str, str]]:
        """Generates code summaries for the README.md file.

        Parameters
        ----------
        file_context
            A list of tuples containing the file path and file content.

        Returns
        -------
        List[Tuple[str, str]]
            List of tuples containing the file path and the generated response.
        """
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
