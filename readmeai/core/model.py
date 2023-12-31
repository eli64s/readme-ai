"""LLM API handler that generates various text for the README.md file."""

import asyncio
import time
import traceback
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Tuple

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
import readmeai.core.logger as logger
from readmeai.core.tokens import (
    adjust_max_tokens,
    get_token_count,
    truncate_tokens,
)
from readmeai.utils.utils import format_sentence


class LlmApiHandler:
    """LLM API handler that generates text for the README.md file."""

    @asynccontextmanager
    async def use_api(self) -> None:
        """Context manager for manage resources used by the HTTP client."""
        try:
            yield
        finally:
            await self.close()

    async def close(self) -> None:
        """Closes the HTTP client."""
        await self.http_client.aclose()

    def __init__(self, config: settings.AppConfig) -> None:
        """Initializes the GPT language model API handler."""
        self.config = config
        self.logger = logger.Logger(__name__)
        self.prompts = config.prompts
        self.tokens = config.llm.tokens
        self.tokens_max = config.llm.tokens_max
        self.cache = TTLCache(maxsize=1000, ttl=1200)
        self.http_client = AsyncClient(
            http2=True,
            timeout=20,
            limits=Limits(max_keepalive_connections=20, max_connections=200),
        )
        self.last_request_time = time.monotonic()
        self.rate_limit_semaphore = asyncio.Semaphore(config.llm.rate_limit)

    async def prompt_processor(
        self, prompt_type: str, context: Dict[str, Any]
    ) -> Dict[str, str]:
        """Processes a prompt and returns the generated text.

        Parameters
        ----------
        prompt_type
            The type of prompt to generate i.e. features, overview, slogan.
        context
            A dictionary containing the context for the prompt.

        Returns
        -------
        Dict[str, str]
            A dictionary containing the prompt type and the generated text.
        """
        self.logger.info(f"Processing prompt: {prompt_type}")

        if prompt_type == "summaries":
            return await self._generate_summaries(context)

        formatted_prompt = self.generate_prompt(prompt_type, context)
        tokens = adjust_max_tokens(self.tokens, formatted_prompt)
        _, summary = await self.generate_text(
            prompt_type, formatted_prompt, tokens
        )
        return {prompt_type: summary}

    def generate_prompt(self, prompt_type, context) -> str:
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
        return prompt_templates[prompt_type].format(
            *[context[key] for key in sorted(context.keys())]
        )

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
            List of tuples containing the file path and the generated summary.
        """
        code_summaries = []

        for context in file_context["summaries"]:
            file_path, file_content = context
            prompt = self.prompts.summaries.format(
                self.config.md.tree, file_path, file_content
            )
            tokens = adjust_max_tokens(self.tokens, prompt)
            _, summary = await self.generate_text(file_path, prompt, tokens)
            code_summaries.append((file_path, summary))

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
            A tuple containing the prompt type and the generated text.
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
            self.logger.error(f"Exception making request: {exc_info}")
            return index, f"{exc_info}: {traceback.format_exc()}"
