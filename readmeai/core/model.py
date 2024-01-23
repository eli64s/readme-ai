"""GPT language model API handler for document generation."""

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

import readmeai.config.settings as settings
from readmeai.core.logger import Logger
from readmeai.core.preprocess import FileData
from readmeai.core.tokens import (
    adjust_max_tokens,
    token_counter,
    truncate_tokens,
)
from readmeai.core.utils import extract_markdown_table, format_sentence


class ModelHandler:
    """LLM API handler that generates text for the README.md file."""

    def __init__(self, config: settings.AppConfig) -> None:
        """Initializes the GPT language model API handler."""
        self.cache = {}
        self.config = config
        self.logger = Logger(__name__)
        self._llm_attributes()
        self._http_client()
        self._handle_response = functools.lru_cache(maxsize=100)(
            self._handle_response
        )

    def _llm_attributes(self):
        """Initializes basic attributes for the class."""
        self.encoder = self.config.llm.encoding
        self.prompts = self.config.prompts
        self.tokens = self.config.llm.tokens
        self.tokens_max = self.config.llm.tokens_max
        self.rate_limit = self.config.llm.rate_limit

    def _http_client(self):
        """Configures the HTTP client for the class."""
        self.http_client = AsyncClient(
            http2=True,
            timeout=20,
            limits=Limits(max_keepalive_connections=100, max_connections=20),
        )
        self.rate_limit_semaphore = asyncio.Semaphore(self.rate_limit)

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
        file_context: List[FileData],
        dependencies: List[str],
        summaries: List[str],
    ) -> List[str]:
        """Generates text for the README.md file using GPT language models."""
        prompts = await self._set_prompt_context(
            file_context, dependencies, summaries
        )
        responses = await self._batch_prompts(prompts)
        return responses

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
            return await self._handle_code_summary_response(prompt["context"])
        else:
            formatted_prompt = self._get_prompt_context(
                prompt["type"], prompt["context"]
            )
            tokens = adjust_max_tokens(self.tokens, formatted_prompt)
            _, summary = await self._handle_response(
                prompt["type"], formatted_prompt, tokens
            )
            return summary

    async def _set_prompt_context(
        self,
        file_context: list[FileData],
        dependencies: List[str],
        summaries: List[str],
    ) -> List[dict]:
        """Generates the prompts to be used by the LLM API."""
        return [
            {"type": prompt_type, "context": context}
            for prompt_type, context in [
                (
                    "summaries",
                    {
                        "repo": self.config.git.repository,
                        "tree": self.config.md.tree,
                        "dependencies": file_context,
                        "summaries": summaries,
                    },
                ),
                (
                    "features",
                    {
                        "repo": self.config.git.repository,
                        "dependencies": dependencies,
                        "summaries": summaries,
                    },
                ),
                (
                    "overview",
                    {
                        "name": self.config.git.name,
                        "repo": self.config.git.repository,
                        "summaries": summaries,
                    },
                ),
                (
                    "slogan",
                    {
                        "name": self.config.git.name,
                        "repo": self.config.git.repository,
                        "summaries": summaries,
                    },
                ),
            ]
        ]

    def _get_prompt_context(self, prompt_type, context) -> str:
        """Generates a prompt for the LLM API."""
        prompt_template = self._get_prompt_template(prompt_type)
        if not prompt_template:
            self.logger.error(f"Prompt type '{prompt_type}' not found.")
            return ""
        return self._inject_prompt_context(prompt_template, context)

    def _get_prompt_template(self, prompt_type: str) -> str:
        """Retrieves the template for the given prompt type."""
        prompt_templates = {
            "features": self.prompts.features,
            "overview": self.prompts.overview,
            "slogan": self.prompts.slogan,
        }
        return prompt_templates.get(prompt_type, "")

    def _inject_prompt_context(self, template: str, context: dict) -> str:
        """Formats the template with the provided context."""
        try:
            return template.format(*[context[key] for key in context])
        except KeyError as exc:
            self.logger.error(f"Missing context for prompt key: {exc}")
            return ""

    async def _handle_code_summary_response(
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
        code_summaries = []

        for context in file_context["summaries"]:
            file_path, file_content = context
            prompt = self.prompts.summaries.format(
                self.config.md.tree, file_path, file_content
            )
            tokens = adjust_max_tokens(self.tokens, prompt)
            _, summary_or_error = await self._handle_response(
                file_path, prompt, tokens
            )
            code_summaries.append((file_path, summary_or_error))

        return code_summaries

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
        key = (index, prompt, tokens)
        if key in self.cache:
            return self.cache[key]

        token_count = token_counter(prompt, self.encoder)
        if token_count > self.tokens_max:
            self.logger.warning(
                f"Truncating tokens for {index} prompt: {token_count} > {self.tokens_max} max"
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
                llm_response = response.json()
                llm_text = llm_response["choices"][0]["message"]["content"]
                llm_text = (
                    format_sentence(llm_text)
                    if index != "features"
                    else extract_markdown_table(llm_text)
                )
                self.logger.info(f"Response: {index} - {llm_text}")
                self.cache[key] = llm_text
                return index, llm_text

        except (
            HTTPStatusError,
            NetworkError,
            TimeoutException,
            openai.error.OpenAIError,
        ) as exc:
            error_msg = f"Error generating text for {index}: {exc}"
            self.logger.error(error_msg)
            return index, error_msg
