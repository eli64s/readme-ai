"""Unit tests for the model.py module."""

import sys

sys.path.append("src")

import json
import os
import unittest
from unittest.mock import patch

import httpx
import pytest
import redis
import responses

import src.model as ai
from src.model import OpenAIError, cache, fetch_summary

# Configure Redis client
redis_client = redis.Redis(
    host="localhost", port=6379, db=0, decode_responses=True
)


class TestOpenAIHandler(unittest.IsolatedAsyncioTestCase):
    @responses.activate
    async def test_fetch_summary(self):
        os.environ["OPENAI_API_KEY"] = "dummy_key"
        file = "test_file.py"
        prompt = 'Summarize this code: print("Hello, World!")'

        # Mocking the OpenAI API response
        responses.add(
            responses.POST,
            ai.ENDPOINT,
            json={
                "choices": [
                    {"text": "This script prints a hello world message."}
                ]
            },
            status=200,
        )

        # Actual test
        result = await ai.fetch_summary(file, prompt)
        self.assertEqual(
            result,
            (
                file,
                'This code prints the phrase " Hello, World! " to the console.',
            ),
        )

    @responses.activate
    async def test_null_summary(self):
        file = "test_file.py"
        summary = "Null summary."
        result = await ai.null_summary(file, summary)
        self.assertEqual(result, (file, summary))

    def test_spacy_text_processor(self):
        text = "Hello, World!"
        result = ai.spacy_text_processor(text)
        self.assertEqual(result, "Hello , World !")


@pytest.mark.asyncio
async def test_fetch_summary_cache_hit():
    file = "test_file.py"
    prompt = 'Summarize this code: print("Hello, World!")'
    cache[prompt] = "Cached summary"

    result = await fetch_summary(file, prompt)

    assert result == (file, "Cached summary")


@pytest.mark.asyncio
@responses.activate
async def test_fetch_summary_success():
    file = "test_file.py"
    prompt = 'Summarize this code: print("Hello, World!")'
    expected_summary = "This is a generated summary."

    responses.add(
        responses.POST,
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        json={"choices": [{"text": expected_summary}]},
        status=200,
    )

    result = await fetch_summary(file, prompt)

    assert result != (file, expected_summary)
    assert prompt in cache
    assert cache[prompt] != expected_summary


@pytest.mark.asyncio
@responses.activate
async def test_fetch_summary_failure():
    file = "test_file.py"
    prompt = 'Summarize this code: print("Hello, World!")'
    error_message = "Error generating file summary."

    responses.add(
        responses.POST,
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        status=500,
    )

    with patch.object(httpx.AsyncClient, "post") as mock_post:
        response = httpx.Response(status_code=500)
        mock_post.side_effect = httpx.HTTPStatusError(
            error_message,
            request=httpx.Request("POST", "url"),
            response=response,
        )

        result = await fetch_summary(file, prompt)

        assert result != (file, error_message)


if __name__ == "__main__":
    unittest.main()
