"""LiteLLM AI gateway handler implementation."""

from typing import Any

from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.tokens import token_handler
from readmeai.utils.importer import is_available
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

if is_available("litellm"):
    import litellm

    LITELLM_AVAILABLE = True
else:
    litellm = None
    LITELLM_AVAILABLE = False


def _is_transient_litellm_error(exc: BaseException) -> bool:
    """Check if an exception is a transient LiteLLM error worth retrying."""
    qualname = f"{type(exc).__module__}.{type(exc).__name__}"
    return qualname in {
        "litellm.exceptions.APIConnectionError",
        "litellm.exceptions.Timeout",
        "litellm.exceptions.RateLimitError",
        "litellm.exceptions.InternalServerError",
        "litellm.exceptions.ServiceUnavailableError",
    }


class LiteLLMHandler(BaseModelHandler):
    """
    LiteLLM AI gateway handler supporting 100+ LLM providers.
    """

    def __init__(self, config_loader: ConfigLoader, context: RepositoryContext) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        if not LITELLM_AVAILABLE:
            raise ImportError(
                "LiteLLM is not installed. "
                "Install it with: pip install 'readmeai[litellm]'"
            )
        self.model = self.config.llm.model

    async def _build_payload(self, prompt: str) -> dict[str, Any]:
        """Build request body for LiteLLM completion requests."""
        return {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_message,
                },
                {"role": "user", "content": prompt},
            ],
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
            "drop_params": True,
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception(_is_transient_litellm_error),
    )
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: Any,  # noqa: ARG002
    ):
        """Process requests via LiteLLM, with retries and error handling."""
        try:
            if prompt is None:
                raise ValueError("Prompt cannot be None")

            prompt = await token_handler(
                config=self.config,
                index=index,
                prompt=prompt,
                tokens=tokens,
            )
            if not prompt:
                raise ValueError("Token handler returned empty prompt")

            if index == "file_summary":
                self.max_tokens = 100

            parameters = await self._build_payload(prompt)

            async with self.rate_limit_semaphore:
                response = await litellm.acompletion(**parameters)
                content = response.choices[0].message.content

                if not content:
                    raise ValueError("Empty response from API")

                self._logger.info(
                    f"Response from LiteLLM for '{index}': {content}",
                )
                return index, content

        except Exception as e:
            if _is_transient_litellm_error(e):
                self._logger.error(f"LiteLLM API error for '{index}': {e!r}")
                raise
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
