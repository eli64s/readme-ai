"""
src/utils.py
"""
import csv
import json
from pathlib import Path

import toml


class FileFactory:
    def __init__(self, base_path: str):
        self.base_path = base_path

    def read_json(self, file_name: str):
        with open(self._get_file_path(file_name), "r") as f:
            return json.load(f)

    def write_json(self, file_name: str, data):
        with open(self._get_file_path(file_name), "w") as f:
            json.dump(data, f, indent=2)

    def read_csv(self, file_name: str):
        with open(self._get_file_path(file_name), "r") as f:
            return list(csv.reader(f))

    def write_csv(self, file_name: str, data):
        with open(self._get_file_path(file_name), "w") as f:
            writer = csv.writer(f)
            for row in data:
                writer.writerow(row)

    def read_html(self, file_name: str):
        with open(self._get_file_path(file_name), "r") as f:
            return f.read()

    def write_html(self, file_name: str, data):
        with open(self._get_file_path(file_name), "w") as f:
            f.write(data)

    def read_md(self, file_name: str):
        with open(self._get_file_path(file_name), "r") as f:
            return f.read()

    def write_md(self, file_name: str, data):
        with open(self._get_file_path(file_name), "w") as f:
            f.write(data)

    def read_toml(self, file_name: str):
        return toml.load(file_name)

    def _get_file_path(self, file_name: str):
        return str(Path(self.base_path) / file_name)
