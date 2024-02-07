"""Google Vertex AI LLM API implementation."""

import os
from typing import List, Tuple

import httpx
import vertexai
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)
from vertexai.preview.generative_models import GenerativeModel

from readmeai.config.settings import AppConfig
from readmeai.core.logger import Logger
from readmeai.core.model import ModelHandler
from readmeai.core.utils import format_response
from readmeai.llms.tokens import count_tokens, truncate_tokens

logger = Logger(__name__)


class VertexAIHandler(ModelHandler):
    """Vertex AI Generative Models API LLM implementation."""

    def __init__(self, config: AppConfig) -> None:
        """Initialize Vertex AI Generative Models API LLM."""
        self.config = config
        self._llm_settings()
        super().__init__(config)
        vertexai.init(project=self.project_id, location=self.location)

    def _llm_settings(self):
        """Initializes basic attributes for the class."""
        self.location = os.getenv("VERTEXAI_LOCATION", None)
        self.project_id = os.getenv("VERTEXAI_PROJECT", None)

        self.content = self.config.llm.content
        self.encoder = self.config.llm.encoding
        self.model = self.config.llm.model
        self.prompts = self.config.prompts
        self.tokens = self.config.llm.tokens
        self.tokens_max = self.config.llm.tokens_max
        self.temperature = self.config.llm.temperature

    @retry(
        stop=stop_after_attempt(4),
        wait=wait_exponential(multiplier=1, min=2, max=6),
        retry=retry_if_exception_type(
            (
                httpx.HTTPStatusError,
                httpx.NetworkError,
                httpx.TimeoutException,
            )
        ),
    )
    async def _handle_response(
        self,
        index: str,
        prompt: str,
        tokens: int,
        raw_files: List[Tuple[str, str]] = None,
    ) -> Tuple[str, str]:
        """Handles Vertex AI LLM API responses and returns the generated text."""
        token_cnt = count_tokens(prompt, self.encoder)
        if token_cnt > self.tokens_max:
            self.logger.debug(
                f"Truncating '{index}' prompt: {token_cnt} > {self.tokens_max}"
            )
            prompt = truncate_tokens(self.encoder, prompt, tokens)

        try:
            async with self.rate_limit_semaphore:
                model = GenerativeModel(self.model)
                response = await model.generate_content_async(
                    prompt,
                )
                response_text = response.text
                formatted_text = format_response(index, response_text)
                self.logger.info(f"Response for '{index}':\n{formatted_text}")
                return index, formatted_text

        except (
            httpx.HTTPStatusError,
            httpx.NetworkError,
            httpx.TimeoutException,
        ) as exc:
            logger.error(f"Error generating response for {index}: {exc}")
            return index, self.config.md.default
