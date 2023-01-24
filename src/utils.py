"""
src/utils.py
"""
import json

from markdownify import markdownify as md


def read_json(path):
    with open(path, "r", encoding="utf8") as j:
        contents = json.load(j)
    return contents


def write_file(html, html_path, md_path):
    with open(html_path, "w", encoding="utf-8") as file:
        file.write(html)
    with open(md_path, "w", encoding="utf-8") as file:
        file.write(md(html))
