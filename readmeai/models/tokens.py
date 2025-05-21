"""Utilities for handling tokens in the LLM model."""

import structlog
from readmeai.config.settings import Settings
from readmeai.core.logger import get_logger
from tiktoken import Encoding, get_encoding

_encoding_cache = {}

_logger = get_logger(__name__)


def _set_encoding_cache(encoding_name: str) -> Encoding:
    """Set the encoding cache for a specific encoding."""
    if encoding_name not in _encoding_cache:
        _encoding_cache[encoding_name] = get_encoding(encoding_name)
    return _encoding_cache[encoding_name]


async def token_handler(
    config: Settings,
    index: str,
    prompt: str,
    tokens: int,
) -> str:
    """Handle token count for the prompt."""
    encoder = config.llm.encoder
    max_count = config.llm.context_window
    token_count = count_tokens(prompt, encoder)

    structlog.contextvars.bind_contextvars(
        token_count=token_count,
        max_count=max_count,
        index=index,
    )

    if token_count > max_count:
        _logger.debug(
            f"Truncating '{index}' prompt: {token_count} > {max_count} tokens!",
        )
        prompt = truncate_tokens(encoder, prompt, tokens)

    return prompt


def count_tokens(text: str, encoder: str) -> int:
    """Return the number of tokens in a text string."""
    try:
        encoding = _set_encoding_cache(encoder)
        token_count = len(encoding.encode(text, disallowed_special=()))

    except (UnicodeEncodeError, ValueError) as exc:
        _logger.error(
            f"Error counting tokens for '{text}' with {encoder}: {exc}",
        )
        token_count = 0

    return token_count


def truncate_tokens(encoding: str, text: str, max_count: int) -> str:
    """Truncate a text string to a maximum number of tokens."""
    if not text:
        return text
    try:
        encoder = _set_encoding_cache(encoding)
        token_count = len(encoder.encode(text))
        if token_count <= max_count:
            return text
        char_total = len(text)
        chars_per_token = char_total / token_count
        truncated_total = int(chars_per_token * max_count)
        return text[:truncated_total]

    except Exception as exc:
        _logger.error(f"Error truncating tokens for '{text}': {exc}")
        return text


def update_max_tokens(
    max_tokens: int,
    prompt: str,
    target: str = "Hello!",
) -> int:
    """Adjust the maximum number of tokens based on the specific prompt."""
    is_valid_prompt = prompt.strip().startswith(target.strip())
    return max_tokens if is_valid_prompt else max_tokens // 2
