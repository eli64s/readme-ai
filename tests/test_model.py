"""Unit tests for the model.py module."""

from unittest.mock import MagicMock, patch

import pytest

from src.model import code_to_text, fetch_summary


@pytest.fixture
def mock_http_client():
    with patch("openai_handler.http_client") as mock_client:
        yield mock_client


@pytest.fixture
def mock_response():
    response = MagicMock()
    response.status_code = 200
    response.json.return_value = {"choices": [{"text": "generated text"}]}
    return response


@pytest.mark.asyncio
async def test_fetch_summary(mock_http_client, mock_response):
    mock_http_client.post.return_value = mock_response
    file_path = "tests/sample_code.py"
    prompt = "Create a summary description for this code: def test(): pass"
    result = await fetch_summary(file_path, prompt)
    assert result == (file_path, "generated text")


@pytest.mark.asyncio
async def test_code_to_text_ignore_files():
    ignore_files = ["test.py"]
    files = {"tests/sample_code.py": "def test(): pass"}
    result = await code_to_text(ignore_files, files)
    assert result == {}


@pytest.mark.asyncio
async def test_code_to_text_max_length(mock_http_client):
    ignore_files = []
    files = {"tests/sample_code.py": "a" * 5000}
    result = await code_to_text(ignore_files, files)
    assert result == {"tests/sample_code.py": "Prompt too long to generate summary."}


@pytest.mark.asyncio
async def test_code_to_text(mock_http_client, mock_response):
    mock_http_client.post.return_value = mock_response
    ignore_files = []
    files = {"tests/sample_code.py": "def test(): pass"}
    result = await code_to_text(ignore_files, files)
    assert result == {"tests/sample_code.py": "generated text"}
