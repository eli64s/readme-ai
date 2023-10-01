"""Token-related utility functions."""

from tiktoken import get_encoding

from readmeai.core import logger

logger = logger.Logger(__name__)


def adjust_max_tokens(
    max_tokens: int, prompt: str, target: str = "Hello!"
) -> int:
    """Adjust the maximum number of tokens based on the specific prompt."""
    is_valid_prompt = prompt.strip().startswith(target.strip())
    adjusted_max_tokens = max_tokens if is_valid_prompt else max_tokens // 3
    return adjusted_max_tokens


def get_token_count(text: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = get_encoding(encoding_name)
    num_tokens = len(encoding.encode(text))
    return num_tokens


def truncate_tokens(text: str, encoding_name: str, max_tokens: int) -> str:
    """Truncate a text string to a maximum number of tokens."""
    encoding = get_encoding(encoding_name)
    encoded_text = encoding.encode(text)[:max_tokens]
    truncated_text = encoding.decode(encoded_text)
    return truncated_text
