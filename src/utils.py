"""
src/utils.py
"""
import json


class FileHandler:
    def __init__(self, conf: object) -> None:
        self.json_path = conf.paths.pkgs
        self.html_path = conf.paths.html
        self.md_path = conf.paths.mrkd

    def read_json(self):
        with open(self.json_path, "r", encoding="utf8") as j:
            contents = json.load(j)
        return contents

    def write_html(self, html):
        with open(self.html_path, "w", encoding="utf-8") as file:
            file.write(html)

    def write_md(self, html):
        with open(self.md, "w", encoding="utf-8") as file:
            file.write(html)
