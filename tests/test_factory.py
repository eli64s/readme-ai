"""Unit tests for the factory module."""

import json
import os
import tempfile
import unittest

from readmeai.factory import FileHandler, ReadFileException, WriteFileException


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_handler = FileHandler()

    def test_read_json(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
            f.write('{"name": "John", "age": 30}')
            f.flush()
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)

    def test_read_markdown(self):
        data = "# Heading\n\nThis is a paragraph."
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md") as f:
            f.write("# Heading\n\nThis is a paragraph.")
            f.flush()
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)

    def test_read_toml(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".toml") as f:
            f.write('name = "John"\nage = 30')
            f.flush()
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)

    def test_read_text(self):
        data = "This is a text file."
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as f:
            f.write("This is a text file.")
            f.flush()
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)

    def test_read_yaml(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml") as f:
            f.write("name: John\nage: 30")
            f.flush()
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)

    def test_read_nonexistent_file(self):
        with self.assertRaises(ReadFileException):
            self.file_handler.read("nonexistent.txt")

    def test_read_unsupported_file_type(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv") as f:
            with self.assertRaises(ValueError):
                self.assertEqual(self.file_handler.read(f.name), ValueError)

    def test_write_json(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
            self.file_handler.write(f.name, data)
            with open(f.name, "r") as f2:
                content = f2.read().replace("\n", "").strip()
                expected_content = json.dumps(data)
                self.assertEqual(content, expected_content)

    def test_write_markdown(self):
        data = "# Heading\n\nThis is a paragraph."
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md") as f:
            self.file_handler.write(f.name, data)
            with open(f.name, "r") as f2:
                content = f2.read()
                self.assertEqual(content, "# Heading\n\nThis is a paragraph.")

    def test_write_toml(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".toml") as f:
            self.file_handler.write(f.name, data)
            with open(f.name, "r") as f2:
                content = f2.read()
                self.assertEqual(content, 'name = "John"\nage = 30\n')

    def test_write_text(self):
        data = "This is a text file."
        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as f:
            self.file_handler.write(f.name, data)
            with open(f.name, "r") as f2:
                content = f2.read()
                self.assertEqual(content, "This is a text file.")

    def test_write_yaml(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml") as f:
            self.file_handler.write(f.name, data)
            with open(f.name, "r") as f2:
                content = f2.read()
                self.assertEqual(content, "age: 30\nname: John\n")

    def test_write_unsupported_file_type(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv") as f:
            with self.assertRaises(ValueError):
                self.file_handler.write(f.name, {})

    def test_write_read(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
            self.file_handler.write(f.name, data)
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)

    def test_write_read_cache(self):
        data = {"name": "John", "age": 30}
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
            self.file_handler.write(f.name, data)
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)
            os.remove(f.name)
            content = self.file_handler.read(f.name)
            self.assertEqual(content, data)


if __name__ == "__main__":
    unittest.main()
