"""Unit tests for file_factory.py"""

import os
import tempfile
import unittest

from src.factory import FileHandler, ReadFileError, WriteFileError


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.file_handler = FileHandler()

    def test_read_write_markdown(self):
        content = "# Markdown File\nThis is a test markdown file."
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".md") as temp:
            self.file_handler.write(temp.name, content)
            read_content = self.file_handler.read(temp.name)
            self.assertEqual(content, read_content)
            os.remove(temp.name)

    def test_read_write_toml(self):
        content = {"title": "TOML Example", "owner": {"name": "John Doe"}}
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".toml"
        ) as temp:
            self.file_handler.write(temp.name, content)
            read_content = self.file_handler.read(temp.name)
            self.assertEqual(content, read_content)
            os.remove(temp.name)

    def test_read_write_json(self):
        content = {"title": "JSON Example", "owner": {"name": "John Doe"}}
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".json"
        ) as temp:
            self.file_handler.write(temp.name, content)
            read_content = self.file_handler.read(temp.name)
            self.assertEqual(content, read_content)
            os.remove(temp.name)

    def test_cache(self):
        content = "# Markdown File\nThis is a test markdown file."
        with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".md") as temp:
            self.file_handler.write(temp.name, content)
            _ = self.file_handler.read(temp.name)
            self.assertIn(temp.name, self.file_handler.cache)
            os.remove(temp.name)

    def test_unsupported_file_type(self):
        with tempfile.NamedTemporaryFile(
            mode="w+", delete=False, suffix=".txt"
        ) as temp:
            with self.assertRaises(ReadFileError):
                self.file_handler.read(temp.name)
            os.remove(temp.name)

    def test_unsupported_action_type(self):
        with self.assertRaises(ValueError):
            self.file_handler.get_action("md", "invalid_action_type")

    def test_read_failure(self):
        with self.assertRaises(ReadFileError):
            self.file_handler.read("nonexistent_file.txt")

    def test_write_failure(self):
        with self.assertRaises(WriteFileError):
            self.file_handler.write("/path/does/not/exist/test.txt", "Content")
