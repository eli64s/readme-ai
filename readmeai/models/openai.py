"""OpenAI API model handler implementation, with Ollama support."""

import os
from typing import Any

import aiohttp
import openai
from readmeai.auth import get_openai_bearer_token, load_openai_codex_credentials
from readmeai.oauth_openai_codex import get_openai_codex_session_headers
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.models.base import BaseModelHandler
from readmeai.models.enums import BaseURLs, LLMProviders
from readmeai.models.tokens import token_handler
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)


class OpenAIHandler(BaseModelHandler):
    """
    OpenAI API model handler implementation, with Ollama support.
    """

    def __init__(self, config_loader: ConfigLoader, context: RepositoryContext) -> None:
        super().__init__(config_loader, context)
        self._model_settings()

    def _model_settings(self):
        """Handles both OpenAI API and Ollama local deployments."""
        self.host_name = BaseURLs["OPENAI"].value
        self.localhost = BaseURLs["OLLAMA"].value
        self.max_tokens = self.config.llm.tokens
        self.model = self.config.llm.model
        self.resource = self.config.llm.resource
        self.top_p = self.config.llm.top_p

        if self.config.llm.api == LLMProviders.OPENAI.value:
            self.standard_url = str(self.config.llm.base_url or f"{self.host_name}{self.resource}")
            self.url = self.standard_url
            token = get_openai_bearer_token()
            if token is None:
                raise ValueError(
                    "OpenAI credentials not found. Set OPENAI_API_KEY or login with `readmeai --login-openai-codex`."
                )
            self.client = openai.OpenAI(api_key=token)
            mode = self.config.llm.openai_auth_mode
            has_oauth = bool(load_openai_codex_credentials())
            has_api = bool(os.getenv('OPENAI_API_KEY'))
            self.using_oauth_codex = (mode == 'codex' and has_oauth) or (mode == 'auto' and has_oauth and not has_api)
            if self.using_oauth_codex:
                self.codex_url = 'https://chatgpt.com/backend-api/codex/responses'
                if not self.config.llm.base_url or 'api.openai.com' in str(self.config.llm.base_url):
                    self.url = self.codex_url

        elif self.config.llm.api == LLMProviders.OLLAMA.value:
            self.standard_url = f"{self.localhost}{self.resource}"
            self.url = self.standard_url
            self.client = openai.OpenAI(
                base_url=f"{self.localhost}v1",
                api_key=LLMProviders.OLLAMA.name,
            )

        self.headers = {"Authorization": f"Bearer {self.client.api_key}"}
        if getattr(self, 'using_oauth_codex', False):
            creds = load_openai_codex_credentials() or {}
            self.headers = get_openai_codex_session_headers(self.client.api_key, creds.get('accountId'))

    def _effective_model(self) -> str:
        if not getattr(self, 'using_oauth_codex', False):
            return self.model
        preferred = self.model
        if preferred in {'gpt-5.4', 'gpt-5.4-mini', 'gpt-5.2', 'gpt-5.1', 'gpt-5.1-codex-mini'}:
            return preferred
        return 'gpt-5.4'

    async def _build_payload(self, prompt: str) -> dict[str, Any]:
        """Build request body for making text generation requests."""
        if getattr(self, 'using_oauth_codex', False):
            reasoning_effort = 'low'
            text_verbosity = 'medium'
            return {
                'model': self._effective_model(),
                'instructions': self.system_message,
                'input': [
                    {'role': 'user', 'content': [{'type': 'input_text', 'text': prompt}]},
                ],
                'store': False,
                'stream': True,
                'tool_choice': 'auto',
                'parallel_tool_calls': True,
                'text': {'verbosity': text_verbosity},
                'reasoning': {'effort': reasoning_effort, 'summary': 'auto'},
            }
        return {
            "messages": [
                {
                    "role": "system",
                    "content": self.system_message,
                },
                {"role": "user", "content": prompt},
            ],
            "model": self.model,
            "max_tokens": self.max_tokens,
            "temperature": self.temperature,
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(
            (
                aiohttp.ClientError,
                aiohttp.ClientResponseError,
                aiohttp.ClientConnectorError,
                openai.OpenAIError,
            ),
        ),
    )
    async def _make_request(
        self,
        index: str | None,
        prompt: str | None,
        tokens: int | None,
        repo_files: Any,
    ):
        """Process requests to OpenAI API, with retries and error handling."""
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

            async with self._session.post(
                self.url,
                headers=self.headers,
                json=parameters,
            ) as response:
                if response.status >= 400 and getattr(self, 'using_oauth_codex', False) and self.url.startswith('https://chatgpt.com/backend-api/codex/responses'):
                    err_raw = await response.text()
                    raise ValueError(f"Codex backend error {response.status}: {err_raw[:2000]}")
                response.raise_for_status()
                if getattr(self, 'using_oauth_codex', False) and self.url.startswith('https://chatgpt.com/backend-api/codex/responses'):
                    raw = await response.text()
                    content = None
                    for line in raw.splitlines():
                        if line.startswith('data: '):
                            import json as _json
                            try:
                                evt = _json.loads(line[6:])
                            except Exception:
                                continue
                            if evt.get('type') == 'response.output_text.delta':
                                delta = evt.get('delta')
                                if isinstance(delta, str):
                                    content = (content or '') + delta
                            elif evt.get('type') == 'response.completed':
                                resp = evt.get('response', {})
                                output = resp.get('output', [])
                                chunks = []
                                for item in output:
                                    for c in item.get('content', []):
                                        txt = c.get('text')
                                        if isinstance(txt, str):
                                            chunks.append(txt)
                                if chunks and not content:
                                    content = ''.join(chunks)
                    if not content:
                        raise ValueError(f'Empty Codex response. Raw: {raw[:1000]}')
                else:
                    response = await response.json()
                    content = response["choices"][0]["message"]["content"]

                    if not content:
                        raise ValueError("Empty response from API")

                self._logger.info(
                    f"Response from {self.config.llm.api.capitalize()} for '{index}': {content}",
                )
                return index, content

        except (
            aiohttp.ClientError,
            aiohttp.ClientResponseError,
            aiohttp.ClientConnectorError,
            openai.OpenAIError,
        ) as e:
            self._logger.error(f"Error processing request for '{index}': {e!r}")
            raise  # Re-raise for retry decorator

        except Exception as e:
            self._logger.error(f"Unexpected error for '{index}': {e!r}")
            return index, self.placeholder
