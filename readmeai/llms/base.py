"""Abstract base class for all LLM implementations."""

from abc import ABC, abstractmethod
from typing import Tuple

from readmeai.config.settings import AppConfig
from readmeai.core.logger import Logger
from readmeai.llms.cache import ResponseCache
from readmeai.llms.tokenize import count_tokens, truncate_tokens


class LLMHandler(ABC):
    """Abstract base class for LLM handlers."""

    def __init__(self, config: AppConfig) -> None:
        """Initializes the LLMHandler class."""
        self.config = config
        self.llm_cache = ResponseCache()
        self.logger = Logger(__name__)
        self.encoding = self.config.llm.encoding
        self.max_tokens = self.config.llm.max_tokens

    async def generate_text(self, prompt: str, tokens: int) -> Tuple[str, str]:
        """Generates text using the LLM."""
        token_count = count_tokens(prompt, self.encoding)
        if token_count > self.max_tokens:
            self.logger.warning(
                f"Truncating tokens for {prompt}: {token_count} > {self.max_tokens} max"
            )
            prompt = truncate_tokens(self.encoding, prompt, tokens)

        cache_key = self.llm_cache.generate_cache_key(
            self.service, prompt, tokens
        )
        cached_response = self.llm_cache.get_cached_response(cache_key)
        if cached_response:
            return cached_response

        response = await self._handle_response(prompt, tokens)
        self.llm_cache.update_cache(cache_key, response)
        return response

    @abstractmethod
    async def _handle_response(
        self, index: str, prompt: str, tokens: int
    ) -> Tuple[str, str]:
        """Abstract method to handle the LLM response."""
        ...
