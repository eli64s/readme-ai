"""LLM API handler that generates various text for the README.md file."""

import asyncio
import time
from typing import Any, Dict, List, Tuple

import openai
from cachetools import TTLCache
from httpx import AsyncClient, HTTPStatusError, Limits
from tenacity import (
    RetryError,
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
    """LLM API handler that generates various text for the README.md file."""

    logger = logger.Logger(__name__)

    def __init__(self, config: settings.AppConfig):
        """Initializes the LLM API handler.

        Parameters
        ----------
        config
            The application configuration data class object.
        """
        self.config = config
        self.endpoint = config.llm.endpoint
        self.encoding = config.llm.encoding
        self.model = config.llm.model
        self.prompts = config.prompts
        self.rate_limit = config.llm.rate_limit
        self.temperature = config.llm.temperature
        self.tokens = config.llm.tokens
        self.tokens_max = config.llm.tokens_max
        self.cache = TTLCache(maxsize=500, ttl=600)
        self.http_client = AsyncClient(
            http2=True,
            timeout=30,
            limits=Limits(max_keepalive_connections=10, max_connections=100),
        )
        self.last_request_time = time.monotonic()
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)

    async def prompt_processor(
        self, prompt_type: str, context: Dict[str, Any]
    ) -> Dict[str, str]:
        """
        Generates a response for a given prompt type using the OpenAI API.

        Parameters
        ----------
        prompt_type : str
            Type of prompt (i.e. features, overview, slogan, summaries).
        context : Dict[str, Any]
            The context information needed for the prompt.

        Returns
        -------
        Dict[str, str]
            A dictionary mapping file paths to their generated summaries.
        """
        self.logger.info(f"Processing prompt: {prompt_type}")

        if prompt_type == "summaries":
            return await self._generate_summaries(context)

        prompt_templates = {
            "features": self.prompts.features,
            "overview": self.prompts.overview,
            "slogan": self.prompts.slogan,
        }
        formatted_prompt = prompt_templates[prompt_type].format(
            *[context[key] for key in sorted(context.keys())]
        )
        tokens = adjust_max_tokens(self.tokens, formatted_prompt)
        _, summary = await self.generate_text(
            prompt_type, formatted_prompt, tokens
        )
        return {prompt_type: summary}

    async def _generate_summaries(
        self, file_context: List[Tuple[str, str]]
    ) -> List[Tuple[str, str]]:
        """
        Generates summaries for a list of files and updates their placeholders.

        Parameters
        ----------
        files_with_placeholders : List[Tuple[str, str]]
            A list of tuples where each tuple contains a file path and
            placeholder text where the generated summary will be inserted.

        Returns
        -------
        List[Tuple[str, str]]
            List of tuples updated with the generated summaries for each file.
        """
        updated_files = []
        for context in file_context["summaries"]:
            file_path, file_content = context
            prompt = self.prompts.summaries.format(
                self.config.md.tree, file_path, file_content
            )
            tokens = adjust_max_tokens(self.tokens, prompt)
            _, summary = await self.generate_text(file_path, prompt, tokens)
            updated_files.append((file_path, summary))

        return updated_files

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=(
            retry_if_exception_type(Exception)
            | retry_if_exception_type(HTTPStatusError)
        ),
    )
    async def generate_text(
        self, index: str, prompt: str, tokens: int
    ) -> Tuple[str, str]:
        """Generates text using a LLM API endpoint.

        Parameters
        ----------
        index
            The prompt type (i.e. features, overview, slogan, summaries).
        prompt
            The prompt used to generate the text.
        tokens
            The number of tokens to generate.

        Returns
        -------
            The generated text response from the LLM API.
        """
        try:
            token_count = get_token_count(prompt, self.encoding)
            if token_count > self.tokens_max:
                self.logger.warning(
                    f"Truncating tokens: {token_count} > {self.tokens_max} max"
                )
                prompt = truncate_tokens(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.http_client.post(
                    self.endpoint,
                    headers={
                        "Authorization": f"Bearer {openai.api_key}",
                    },
                    json={
                        "messages": [
                            {
                                "role": "system",
                                "content": "You're a brilliant Tech Lead at OpenAI.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                        "model": self.model,
                        "temperature": self.temperature,
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
                self.logger.info(f"Response: {index}\n{summary}")
                self.cache[prompt] = summary
                return index, summary

        except openai.error.OpenAIError as exc_info:
            self.logger.error(f"OpenAI Exception:\n{str(exc_info)}")
            return await self.null_summary(
                index, f"OpenAI Exception: {exc_info.response.status_code}"
            )

        except HTTPStatusError as exc_info:
            self.logger.error(f"HTTPStatus Exception:\n{str(exc_info)}")
            return await self.null_summary(
                index, f"HTTPStatus Exception: {exc_info.response.status_code}"
            )
        except RetryError as exc_info:
            self.logger.error(f"RetryError Exception:\n{str(exc_info)}")
            return await self.null_summary(
                index, f"RetryError Exception: {exc_info}"
            )

        except Exception as exc_info:
            self.logger.error(f"Exception:\n{str(exc_info)}")
            return await self.null_summary(index, f"Exception: {exc_info}")

        finally:
            self.last_request_time = time.monotonic()

    @staticmethod
    async def null_summary(index: str, summary: str) -> Tuple[str, str]:
        """Returns a null summary for a given prompt.

        Parameters
        ----------
        index
            The index of the prompt (i.e. 0, 1, 2, 3).
        summary
            The summary to return.

        Returns
        -------
            The null summary.
        """
        return index, summary

    async def close(self):
        """Closes the HTTP client."""
        await self.http_client.aclose()
