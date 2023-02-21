"""
src/utils.py
"""
import csv
import json
import os

import toml


class FileFactory:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_handler(self):
        file_readers = {
            ".csv": CSVFileHandler,
            ".json": JSONFileHandler,
            ".html": HTMLFileHandler,
            ".md": MDFileHandler,
            ".toml": TOMLFileHandler,
        }
        file_type = os.path.splitext(self.file_path)[1]
        file_reader_class = file_readers.get(file_type)
        if file_reader_class:
            return file_reader_class(self.file_path)
        else:
            raise ValueError("Unsupported file type")


class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        pass

    def write_file(self, data):
        self.data = data


class CSVFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            data = [row for row in reader]
        return data

    def write_file(self, data):
        with open(self.file_path, "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["module", "summary"])
            for row in data:
                writer.writerow(row)


class JSONFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r") as json_file:
            data = json.load(json_file)
        return data

    def write_file(self, data):
        with open(self.file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)


class HTMLFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r") as html_file:
            data = html_file.read()
        return data

    def write_file(self, data):
        with open(self.file_path, "w") as html_file:
            html_file.write(data)


class MDFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r") as md_file:
            data = md_file.read()
        return data

    def write_file(self, data):
        with open(self.file_path, "w") as md_file:
            md_file.write(data)


class TOMLFileHandler(FileHandler):
    def read_file(self):
        with open(self.file_path, "r") as toml_file:
            data = toml.load(toml_file)
        return data

    def write_file(self, data):
        with open(self.file_path, "w") as toml_file:
            toml.dump(data, toml_file)
