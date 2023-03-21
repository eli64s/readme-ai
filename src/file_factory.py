"""File factory module."""
import json

import toml


class FileHandler:
    def read(self, file_path):
        file_extension = str(file_path).split(".")[-1]
        reader = self.get_reader(file_extension)
        return reader(file_path)

    def write(self, file_path, content):
        file_extension = str(file_path).split(".")[-1]
        writer = self.get_writer(file_extension)
        writer(file_path, content)

    def get_reader(self, file_extension):
        readers = {
            "md": self.read_markdown,
            "toml": self.read_toml,
            "json": self.read_json,
        }
        reader = readers.get(file_extension)
        if not reader:
            raise ValueError(f"Unsupported file type: {file_extension}")
        return reader

    def get_writer(self, file_extension):
        writers = {
            "md": self.write_markdown,
            "toml": self.write_toml,
            "json": self.write_json,
        }
        writer = writers.get(file_extension)
        if not writer:
            raise ValueError(f"Unsupported file type: {file_extension}")
        return writer

    @staticmethod
    def read_markdown(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def read_toml(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = toml.load(file)
        data_cleaned = {key.lower(): value for key, value in data.items()}
        return data_cleaned

    @staticmethod
    def read_json(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_markdown(file_path, content):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    @staticmethod
    def write_toml(file_path, content):
        with open(file_path, "w", encoding="utf-8") as file:
            toml.dump(content, file)

    @staticmethod
    def write_json(file_path, content):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(content, file, ensure_ascii=False, indent=4)
