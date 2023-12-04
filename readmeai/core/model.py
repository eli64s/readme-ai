"""OpenAI API handler, generates text for the README.md file."""

import asyncio
import time
from typing import Dict, List, Tuple

import httpx
import openai
from cachetools import TTLCache
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


class OpenAIHandler:
    """OpenAI API handler for generating text for the README.md file."""

    logger = logger.Logger(__name__)

    def __init__(self, config: settings.AppConfig):
        """Initialize the OpenAI API handler.

        Parameters
        ----------
        config : conf.AppConfig
            Configuration constant values.
        """
        self.endpoint = config.api.endpoint
        self.encoding = config.api.encoding
        self.model = config.api.model
        self.tokens = config.api.tokens
        self.tokens_max = config.api.tokens_max
        self.temperature = config.api.temperature
        self.rate_limit = config.api.rate_limit
        self.cache = TTLCache(maxsize=500, ttl=600)
        self.http_client = httpx.AsyncClient(
            http2=True,
            timeout=30,
            limits=httpx.Limits(
                max_keepalive_connections=10, max_connections=100
            ),
        )
        self.last_request_time = time.monotonic()
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)

    async def code_to_text(
        self,
        files: Dict[str, str],
        ignore: Dict[str, List[str]],
        prompt: str,
        tree: str,
    ) -> Dict[str, str]:
        """Converts code to natural language text using large language models.

        Parameters
        ----------
        files : Dict[str, str]
            The repository files to convert to text.
        ignore : Dict[str, List[str]]
            Files, directories, or file extensions to ignore.
        prompt : str
            The prompt to use for the OpenAI API calls.

        Returns
        -------
        Dict[str, str]
            Dictionary of file paths and their corresponding summaries.
        """
        tasks = []
        for path, contents in files.items():
            if not (
                all(
                    idir not in path.parts
                    for idir in ignore.get("directories", [])
                )
                and path.name not in ignore.get("files", [])
                and path.suffix[1:] not in ignore.get("extensions", [])
            ):
                self.logger.warning(f"Ignoring file: {path}")
                continue

            prompt_code = prompt.format(tree, str(path), contents)
            tasks.append(
                asyncio.create_task(
                    self.generate_text(path, prompt_code, self.tokens)
                )
            )

        results = await asyncio.gather(*tasks, return_exceptions=True)

        filter_results = []

        for result in results:
            if isinstance(result, Exception):
                self.logger.error(f"Task failed with exception: {result}")
            else:
                filter_results.append(result)

        return filter_results

    async def chat_to_text(self, prompts: List[str]) -> List[str]:
        """Generate text using prompts and OpenAI's GPT-3.

        Parameters
        ----------
        prompts : List[str]
            The prompts to use for the OpenAI API calls.

        Returns
        -------
        List[str]
            A list of generated text.
        """
        if self.http_client.is_closed:
            self.http_client = httpx.AsyncClient()

        tasks = []
        for idx, prompt in enumerate(prompts):
            tokens = adjust_max_tokens(self.tokens, prompt)
            tasks.append(
                asyncio.create_task(
                    self.generate_text(idx + 1, prompt, tokens)
                )
            )

        results = []
        while tasks:
            done, pending = await asyncio.wait(
                tasks, return_when=asyncio.FIRST_COMPLETED
            )
            for task in done:
                result = await task
                results.append(result)
            tasks = pending

        response_list = [summary for _, summary in sorted(results)]
        return response_list

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=(
            retry_if_exception_type(Exception)
            | retry_if_exception_type(httpx.HTTPStatusError)
        ),
    )
    async def generate_text(
        self, index: str, prompt: str, tokens: int
    ) -> Tuple[str, str]:
        """Handles the request to the OpenAI API to generate text."""
        try:
            token_count = get_token_count(prompt, self.encoding)

            if token_count > self.tokens_max:
                self.logger.warning(
                    f"Truncating tokens: {token_count} > {self.tokens_max}"
                )
                prompt = truncate_tokens(prompt, tokens)

            async with self.rate_limit_semaphore:
                response = await self.http_client.post(
                    self.endpoint,
                    headers={"Authorization": f"Bearer {openai.api_key}"},
                    json={
                        "messages": [
                            {
                                "role": "system",
                                "content": "You're a brilliant Tech Lead.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                        "model": self.model,
                        "temperature": self.temperature,
                        "max_tokens": tokens,
                    },
                )
                response.raise_for_status()
                data = response.json()
                summary = data["choices"][0]["message"]["content"]
                summary = format_sentence(summary) if index != 3 else summary

                self.logger.info(
                    f"\nProcessing prompt: {index}\nResponse: {summary}"
                )
                self.cache[prompt] = summary
                return index, summary

        except openai.error.OpenAIError as excinfo:
            self.logger.error(f"OpenAI Exception:\n{str(excinfo)}")
            return await self.null_summary(
                index, f"OpenAI Exception: {excinfo.response.status_code}"
            )

        except httpx.HTTPStatusError as excinfo:
            self.logger.error(f"HTTPStatus Exception:\n{str(excinfo)}")
            return await self.null_summary(
                index, f"HTTPStatus Exception: {excinfo.response.status_code}"
            )
        except RetryError as excinfo:
            self.logger.error(f"RetryError Exception:\n{str(excinfo)}")
            return await self.null_summary(
                index, f"RetryError Exception: {excinfo}"
            )

        except Exception as excinfo:
            self.logger.error(f"Exception:\n{str(excinfo)}")
            return await self.null_summary(index, f"Exception: {excinfo}")

        finally:
            self.last_request_time = time.monotonic()

    @staticmethod
    async def null_summary(index: str, summary: str) -> Tuple[str, str]:
        """Handles any exceptions raised while requesting the API."""
        return index, summary

    async def close(self):
        """Close the HTTP client."""
        await self.http_client.aclose()
