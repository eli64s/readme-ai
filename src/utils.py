"""
src/utils.py
"""
import json


def read_json(path):
    with open(path, "r", encoding="utf8") as j:
        contents = json.load(j)
    return contents


def write_file(html, html_path):
    with open(html_path, "w") as file:
        file.write(html)
