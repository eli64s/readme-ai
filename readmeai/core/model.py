"""GPT language model API handler for document generation."""

import asyncio
import time
import traceback
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Tuple, Union

import openai
from cachetools import TTLCache
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

import readmeai.config.settings as settings
from readmeai.core.logger import Logger
from readmeai.core.tokens import (
    adjust_max_tokens,
    get_token_count,
    truncate_tokens,
)
from readmeai.core.utils import format_sentence


class ModelHandler:
    """LLM API handler that generates text for the README.md file."""

    @asynccontextmanager
    async def use_api(self) -> None:
        """Context manager for managing HTTP client resources used by the the LLM API."""
        try:
            yield self
        finally:
            await self.close()

    async def close(self) -> None:
        """Closes the HTTP client."""
        await self.http_client.aclose()

    def __init__(self, config: settings.AppConfig) -> None:
        """Initializes the GPT language model API handler."""
        self.logger = Logger(__name__)
        self.config = config
        self.prompts = config.prompts
        self.tokens = config.llm.tokens
        self.tokens_max = config.llm.tokens_max
        self.cache = TTLCache(maxsize=100, ttl=360)
        self.http_client = AsyncClient(
            http2=True,
            timeout=20,
            limits=Limits(max_keepalive_connections=100, max_connections=200),
        )
        self.last_request_time = time.monotonic()
        self.rate_limit_semaphore = asyncio.Semaphore(config.llm.rate_limit)

    async def batch_text_generator(
        self, prompts: List[Union[str, Tuple[str, str]]]
    ) -> List[str]:
        """Generates text for the README.md file using GPT language models.

        Parameters
        ----------
        prompts
            A list of prompts to generate text from.

        Returns
        -------
        List[str]
            A list of generated text.
        """
        responses = []
        for batch in self._batch_prompts(prompts):
            batch_responses = await asyncio.gather(
                *[self._process_prompt(prompt) for prompt in batch]
            )
            responses.extend(batch_responses)
        return responses

    def _batch_prompts(
        self, prompts: List[Union[str, Tuple[str, str]]], batch_size: int = 5
    ) -> List[List[Union[str, Tuple[str, str]]]]:
        """Batches prompts for the LLM API.

        Parameters
        ----------
        prompts
            A list of prompts to batch.
        batch_size, optional
            The number of prompts to batch, by default 5

        Returns
        -------
        List[List[Union[str, Tuple[str, str]]]]
            A list of batches of prompts.

        Yields
        ------
        List[Union[str, Tuple[str, str]]]
            A batch of prompts.
        """
        for i in range(0, len(prompts), batch_size):
            yield prompts[i : i + batch_size]

    def build_prompt(self, prompt_type, context) -> str:
        """Generates a prompt for the LLM API.

        Parameters
        ----------
        prompt_type
            The type of prompt to generate i.e. features, overview, slogan.
        context
            A dictionary containing the context for the prompt.

        Returns
        -------
        str
            The generated prompt.
        """
        prompt_templates = {
            "features": self.prompts.features,
            "overview": self.prompts.overview,
            "slogan": self.prompts.slogan,
        }
        prompt_template = prompt_templates.get(prompt_type)

        if prompt_template:
            return prompt_template.format(*[context[key] for key in context])
        else:
            self.logger.error(f"Unknown prompt type: {prompt_type}")
            return ""

    async def _process_prompt(self, prompt: Dict[str, Any]) -> str:
        """Processes a prompt and returns the generated text.

        Parameters
        ----------
        prompt
            A dictionary containing the prompt type and context.

        Returns
        -------
        str
            The generated text from the LLM API.
        """
        if prompt["type"] == "summaries":
            return await self._generate_summaries(prompt["context"])
        else:
            formatted_prompt = self.build_prompt(
                prompt["type"], prompt["context"]
            )
            tokens = adjust_max_tokens(self.tokens, formatted_prompt)
            _, summary = await self.generate_text(
                prompt["type"], formatted_prompt, tokens
            )
            return summary

    async def _generate_summaries(
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
            List of tuples containing the file path and the generated summary or error message.
        """
        code_summaries = []

        for context in file_context["summaries"]:
            file_path, file_content = context
            prompt = self.prompts.summaries.format(
                self.config.md.tree, file_path, file_content
            )
            tokens = adjust_max_tokens(self.tokens, prompt)
            _, summary_or_error = await self.generate_text(
                file_path, prompt, tokens
            )
            code_summaries.append((file_path, summary_or_error))

        return code_summaries

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, min=2, max=6),
        retry=retry_if_exception_type(
            (
                openai.error.OpenAIError,
                HTTPStatusError,
                NetworkError,
                TimeoutException,
            )
        ),
    )
    async def generate_text(
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
        token_count = get_token_count(prompt, self.config.llm.encoding)
        if token_count > self.tokens_max:
            self.logger.warning(
                f"Truncating tokens: {token_count} > {self.tokens_max} max"
            )
            prompt = truncate_tokens(prompt, tokens)

        try:
            async with self.rate_limit_semaphore:
                response = await self.http_client.post(
                    self.config.llm.endpoint,
                    headers={"Authorization": f"Bearer {openai.api_key}"},
                    json={
                        "messages": [
                            {
                                "role": "system",
                                "content": self.config.llm.content,
                            },
                            {"role": "user", "content": prompt},
                        ],
                        "model": self.config.llm.model,
                        "temperature": self.config.llm.temperature,
                        "max_tokens": tokens,
                    },
                )
                response.raise_for_status()
                llm_text = response.json()
                summary = llm_text["choices"][0]["message"]["content"]
                summary = (
                    format_sentence(summary)
                    if index != "features"
                    else summary
                )
                self.cache[prompt] = summary
                self.logger.info(f"Response: {index} - {summary}")
                return index, summary

        except Exception as exc_info:
            error_message = f"Error generating summary: {exc_info.__class__.__name__} occurred. See logs for details."
            self.logger.error(
                f"Exception making request: {exc_info}\n{traceback.format_exc()}"
            )
            return index, error_message
