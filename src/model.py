"""OpenAI API handler for generating text for the README.md file."""

import asyncio
from typing import Dict, List, Tuple

import httpx
import openai
from cachetools import TTLCache
from tenacity import retry, stop_after_attempt, wait_exponential

import conf
import utils
from logger import Logger


class OpenAIHandler:
    """OpenAI API handler for generating text for the README.md file."""

    LOGGER = Logger("readmeai_logger")
    MAX_TOKENS = 4096
    RATE_LIMIT = 5

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
            timeout=60,
            limits=httpx.Limits(
                max_keepalive_connections=10, max_connections=100
            ),
        )
        self.cache = TTLCache(maxsize=500, ttl=600)
        self.rate_limit_semaphore = asyncio.Semaphore(self.RATE_LIMIT)
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
        ignore_files
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
                    self.fetch_summary(self.http_client, path, prompt_code)
                )
            )

        results = await asyncio.gather(*tasks, return_exceptions=True)

        return results

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
    )
    async def fetch_summary(
        self, client: httpx.AsyncClient, file: str, prompt: str
    ) -> Tuple[str, str]:
        """Generate a summary for a file using the OpenAI API."""
        if prompt in self.cache:
            self.LOGGER.warning(f"Using cached summary for {file}")
            return (file, self.cache[prompt])

        try:
            async with self.rate_limit_semaphore:
                response = await client.post(
                    self.endpoint,
                    headers={"Authorization": f"Bearer {openai.api_key}"},
                    json={
                        "messages": [
                            {
                                "role": "user",
                                "content": prompt,
                            }
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

                self.LOGGER.info(f"Processing request: {file}")
                self.LOGGER.info(f"Response: {summary}")
                self.cache[prompt] = summary

                return (file, summary)

        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in [400, 429, 500, 502, 503, 504]:
                retry_after = exc.response.headers.get("Retry-After", 10)
                await asyncio.sleep(int(retry_after))
            self.LOGGER.error(
                f"HTTP {exc.response.status_code} error for {file}."
            )
            return await self.null_summary(
                file,
                f"HTTP {exc.response.status_code} error when fetching summary.",
            )
        except Exception as exc:
            self.LOGGER.error(f"Error fetching summary for {file}: {str(exc)}")
            return await self.null_summary(
                file, f"Error generating file summary. Exception: {str(exc)}"
            )

    async def summary_text_gen(self, prompts: List[str]) -> List[str]:
        """Generate text using prompts and OpenAI's GPT-3.

        Parameters
        ----------
        prompts
            The prompts to use for the OpenAI API calls.

        Returns
        -------
        A list of generated text.
        """
        response_list = []

        if self.http_client.is_closed:
            self.http_client = httpx.AsyncClient()

        tasks = []
        for idx, prompt in enumerate(prompts):
            tasks.append(
                asyncio.create_task(self.generate_summary(prompt, idx + 1))
            )

        results = await asyncio.gather(*tasks)
        response_list = [summary for _, summary in sorted(results)]

        return response_list

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
    )
    async def generate_summary(
        self, prompt: str, index: int
    ) -> Tuple[int, str]:
        """Generate a summary for a single prompt using the OpenAI API."""
        try:
            async with self.rate_limit_semaphore:
                response = await self.http_client.post(
                    self.endpoint,
                    headers={"Authorization": f"Bearer {openai.api_key}"},
                    json={
                        "messages": [
                            {
                                "role": "user",
                                "content": prompt,
                            }
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

                self.LOGGER.info(f"Processing request: {prompt}")
                self.LOGGER.info(f"Response: {summary}")

                return (index, summary)

        except httpx.HTTPStatusError as exc:
            if exc.response.status_code in [400, 429, 500, 502, 503, 504]:
                retry_after = exc.response.headers.get("Retry-After", 10)
                await asyncio.sleep(int(retry_after))
            self.LOGGER.error(
                f"HTTP {exc.response.status_code} error for {index}."
            )
            return await self.null_summary(
                index,
                f"HTTP {exc.response.status_code} error when fetching summary.",
            )
        except Exception as exc:
            self.LOGGER.error(
                f"Error fetching summary for {index}: {str(exc)}"
            )
            return await self.null_summary(
                index, f"Error generating file summary. Exception: {str(exc)}"
            )

    @staticmethod
    async def null_summary(file: str, summary: str) -> Tuple[str, str]:
        """Placeholder summary for files that exceed the max token limit."""
        return (file, summary)

    async def close(self):
        """Close the HTTP client when it's no longer needed."""
        await self.http_client.aclose()
