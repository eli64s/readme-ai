"""Unit tests for file_factory.py"""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import toml

from src import file_factory

# Test data
test_data = {"key": "value"}

# Test files
test_md = "test.md"
test_toml = "test.toml"
test_json = "test.json"


@pytest.fixture
def TestFileHandler():
    return file_factory.FileHandler()


def test_read_markdown(file_handler):
    with patch("file_factory.FileHandler.read_markdown", return_value="content"):
        content = file_handler.read(test_md)
        assert content == "content"


def test_read_toml(file_handler):
    with patch("file_factory.FileHandler.read_toml", return_value=test_data):
        content = file_handler.read(test_toml)
        assert content == test_data


def test_read_json(file_handler):
    with patch("file_factory.FileHandler.read_json", return_value=test_data):
        content = file_handler.read(test_json)
        assert content == test_data


def test_write_markdown(file_handler):
    with patch("file_factory.FileHandler.write_markdown") as mock_write_markdown:
        file_handler.write(test_md, "content")
        mock_write_markdown.assert_called_once_with(test_md, "content")


def test_write_toml(file_handler):
    with patch("file_factory.FileHandler.write_toml") as mock_write_toml:
        file_handler.write(test_toml, test_data)
        mock_write_toml.assert_called_once_with(test_toml, test_data)


def test_write_json(file_handler):
    with patch("file_factory.FileHandler.write_json") as mock_write_json:
        file_handler.write(test_json, test_data)
        mock_write_json.assert_called_once_with(test_json, test_data)
