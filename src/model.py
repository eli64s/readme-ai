"""OpenAI API handler for generating text for the README.md file."""

import asyncio
import time
from typing import Dict, List, Tuple

import httpx
import openai
from cachetools import TTLCache
from httpx import HTTPStatusError
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

import conf
import utils
from logger import Logger


class OpenAIHandler:
    """OpenAI API handler for generating text for the README.md file."""

    LOGGER = Logger("readmeai_logger")
    MAX_TOKENS = 4096
    RATE_LIMIT = 5

    class RetryAfter(HTTPStatusError):
        """Custom exception for HTTP errors."""

        pass

    class OpenAIError(Exception):
        """Custom exception for OpenAI API errors."""

        pass

    def __init__(self, conf: conf.AppConfig):
        """Initialize the OpenAI API handler.

        Parameters
        ----------
        conf
            Configuration constant values.
        """
        self.http_client = httpx.AsyncClient(
            http2=True,
            timeout=30,
            limits=httpx.Limits(
                max_keepalive_connections=10, max_connections=100
            ),
        )
        self.cache = TTLCache(maxsize=500, ttl=600)
        self.rate_limit_semaphore = asyncio.Semaphore(self.RATE_LIMIT)
        self.last_request_time = time.monotonic()
        self.endpoint = conf.api.endpoint
        self.engine = conf.api.engine
        self.tokens = conf.api.tokens
        self.temperature = conf.api.temperature

    async def code_to_text(
        self, ignore: dict, files: Dict[str, str], prompt: str
    ) -> Dict[str, str]:
        """Converts code to natural language text using large language models.

        Parameters
        ----------
        ignore
            Files, directories, or file extensions to ignore.
        files
            The repository files to convert to text.
        prompt
            The prompt to use for the OpenAI API calls.

        Returns
        -------
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
                and path.suffix not in ignore.get("extensions", [])
            ):
                self.LOGGER.warning(f"Ignoring file: {path}")
                continue

            prompt_code = prompt.format(contents)
            prompt_len = len(prompt_code.split())
            if prompt_len > self.MAX_TOKENS:
                err = "Prompt exceeds max token limit: {}"
                tasks.append(
                    asyncio.create_task(
                        self.null_summary(path, err.format(prompt_len))
                    )
                )
                self.LOGGER.debug(err.format(prompt_code))
                continue

            tasks.append(
                asyncio.create_task(
                    self.generate_text(path, prompt_code, "file")
                )
            )
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

    async def chat_to_text(self, prompts: List[str]) -> List[str]:
        """Generate text using prompts and OpenAI's GPT-3.

        Parameters
        ----------
        prompts
            The prompts to use for the OpenAI API calls.

        Returns
        -------
        A list of generated text.
        """
        if self.http_client.is_closed:
            self.http_client = httpx.AsyncClient()

        tasks = []
        for idx, prompt in enumerate(prompts):
            tasks.append(
                asyncio.create_task(
                    self.generate_text(idx + 1, prompt, "prompt")
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
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=(
            retry_if_exception_type(Exception)
            | retry_if_exception_type(RetryAfter)
            | retry_if_exception_type(httpx.StreamClosed)
        ),
    )
    async def generate_text(
        self, identifier: str, prompt: str, type: str
    ) -> Tuple[str, str]:
        """Generate a summary for a file using the OpenAI API."""
        if prompt in self.cache:
            self.LOGGER.warning(f"Using cached summary for {identifier}")
            return (identifier, self.cache[prompt])

        # Rate limit
        current_time = time.monotonic()
        elapsed_time = current_time - self.last_request_time
        if elapsed_time < 1 / self.RATE_LIMIT:
            await asyncio.sleep(1 / self.RATE_LIMIT - elapsed_time)

        try:
            async with self.rate_limit_semaphore:  # Keep the semaphore, it's not bad to have it
                response = await self.http_client.post(
                    self.endpoint,
                    headers={"Authorization": f"Bearer {openai.api_key}"},
                    json={
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are a helpful assistant.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                        "model": self.engine,
                        "temperature": self.temperature,
                        "max_tokens": self.tokens,
                    },
                )
                response.raise_for_status()
                data = response.json()
                summary = data["choices"][0]["message"]["content"]
                summary = utils.format_sentence(summary)

                self.LOGGER.info(
                    f"Processing...\n\tRequest: {identifier}\n\tSummary: {summary}"
                )
                self.cache[prompt] = summary

                return (identifier, summary)

        except Exception as exc:
            return await self.handle_exception(identifier, prompt, type, exc)

        finally:
            self.last_request_time = time.monotonic()

    async def handle_exception(
        self, identifier: str, prompt: str, type: str, exc
    ):
        self.LOGGER.error(
            f"Error fetching summary for {identifier}: {str(exc)}"
        )
        if isinstance(exc, httpx.HTTPStatusError):
            if exc.response.status_code in [429, 500, 503, 504]:
                retry_after = exc.response.headers.get("Retry-After", 10)
                retry_after = int(retry_after)
                await asyncio.sleep(retry_after)
                return await self.generate_text(identifier, prompt, type)
            else:
                self.LOGGER.error(
                    f"HTTP {exc.response.status_code} error for {identifier}."
                )
        elif isinstance(exc, httpx.StreamClosed):
            self.LOGGER.error(
                f"Stream was reset while fetching summary for {identifier}: {str(exc)}"
            )
        return await self.null_summary(
            identifier, f"Error generating file summary. Exception: {str(exc)}"
        )

    @staticmethod
    async def null_summary(identifier: str, summary: str) -> Tuple[str, str]:
        """Placeholder summary for files that exceed the max token limit."""
        return (identifier, summary)

    async def close(self):
        """Close the HTTP client when it's no longer needed."""
        await self.http_client.aclose()
