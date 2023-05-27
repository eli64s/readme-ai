"""Unit tests for the builder.py module."""

import sys

sys.path.append("src")

import pandas as pd

from src.builder import create_tables, parse_pandas_cols


def test_parse_pandas_cols():
    data = {
        "Module": ["folder1/file1.py", "folder2/file2.py"],
        "Summary": ["summary1", "summary2"],
    }
    df = pd.DataFrame(data)

    parsed_df = parse_pandas_cols(df)

    assert parsed_df["Directory"].tolist() == ["folder1", "folder2"]
    assert parsed_df["File"].tolist() == ["file1.py", "file2.py"]


def test_create_tables():
    data = {
        "Module": ["folder1/file1.py", "folder2/file2.py"],
        "Summary": ["summary1", "summary2"],
        "Directory": ["folder1", "folder2"],
        "File": ["file1.py", "file2.py"],
    }
    df = pd.DataFrame(data)

    dropdown = "<details><summary>{}</summary>\n\n{}"
    result = create_tables(df, dropdown)
    assert "folder1" in result
    assert "folder2" in result
