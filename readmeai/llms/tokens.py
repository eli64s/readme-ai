"""Tokenization utilities for the readme-ai CLI application."""

from tiktoken import get_encoding

from readmeai.core.logger import Logger

logger = Logger(__name__)

_encoding_cache = {}


def _set_encoding_cache(encoding_name: str) -> str:
    """Set the encoding cache for a specific encoding."""
    if encoding_name not in _encoding_cache:
        _encoding_cache[encoding_name] = get_encoding(encoding_name)

    return _encoding_cache[encoding_name]


def count_tokens(text: str, encoding_name: str) -> int:
    """Return the number of tokens in a text string."""
    encoding = _set_encoding_cache(encoding_name)
    try:
        num_tokens = len(encoding.encode(text, disallowed_special=()))

    except Exception as exc:
        logger.error(f"Error in token encoding: {exc}")
        num_tokens = 0

    return num_tokens


def truncate_tokens(encoding_name: str, text: str, max_tokens: int) -> str:
    """Truncate a text string to a maximum number of tokens."""
    if not text:
        return text
    try:
        encoder = _set_encoding_cache(encoding_name)
        prompt_token_total = len(encoder.encode(text))
        if prompt_token_total <= max_tokens:
            return text

        char_total = len(text)
        chars_per_token = char_total / prompt_token_total
        truncated_total = int(chars_per_token * max_tokens)
        return text[:truncated_total]

    except Exception as exc:
        logger.error(f"Error truncating tokens: {exc}")
        return text


def update_max_tokens(
    max_tokens: int, prompt: str, target: str = "Hello!"
) -> int:
    """Adjust the maximum number of tokens based on the specific prompt."""
    is_valid_prompt = prompt.strip().startswith(target.strip())
    return max_tokens if is_valid_prompt else max_tokens // 2
