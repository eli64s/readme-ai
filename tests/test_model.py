"""Unit tests for the model.py module."""

import sys
from unittest.mock import AsyncMock, patch

import httpx
import pytest

from src.model import code_to_text, generate_summary_text, get_cache, get_http_client

sys.path.append("src")


def test_get_cache():
    cache = get_cache()
    # Initially, the cache should be empty
    assert len(cache) == 0


def test_get_http_client():
    with patch.object(httpx, "AsyncClient") as mock:
        get_http_client()
        mock.assert_called_once_with(
            http2=True,
            timeout=30,
            limits=httpx.Limits(max_keepalive_connections=10, max_connections=100),
        )


@patch("src.model.openai.Completion.create")
def test_generate_summary_text(mock_create):
    mock_create.return_value = type(
        "obj",
        (object,),
        {"choices": [type("obj", (object,), {"text": " Sample text"})]},
    )

    result = generate_summary_text("Test prompt")
    assert result == "Sample text"


@pytest.mark.asyncio
async def test_code_to_text():
    ignore_files = ["ignore.py"]
    files = {
        "ignore.py": "ignore this file",
        "file1.py": "print('Hello World')",
    }
    prompt = "Summarize the following code: {}"

    with patch("src.model.fetch_summary", new_callable=AsyncMock) as mock_fetch_summary:
        mock_fetch_summary.return_value = (
            "file1.py",
            "It prints 'Hello World'",
        )

        result = await code_to_text(ignore_files, files, prompt)

    assert len(result) == 1
    assert result[0] == ("file1.py", "It prints 'Hello World'")
