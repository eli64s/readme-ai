"""Unit tests for readmeai utility methods."""

from pathlib import Path

from readmeai.config.settings import ConfigHelper
from readmeai.core.utils import (
    extract_markdown_table,
    flatten_list,
    format_sentence,
    get_resource_path,
    is_valid_url,
    should_ignore,
)


def test_extract_markdown_table():
    """Test that the markdown table is extracted from the input string."""
    test_string = """<remove this>
    | Column 1 | Column 2 | Column 3 |
    | -------- | -------- | -------- |
    | Content  | Content  | Content  |
    | Content  | Content  | Content  |
    | Content  | Content  | Content  |
    and this
    """
    result = extract_markdown_table(test_string)
    assert isinstance(result, str)
    assert "<remove this>" not in result
    assert "and this" not in result


def test_format_sentence():
    text = "'hello world'"
    formatted_sentence = format_sentence(text)
    assert formatted_sentence == "hello world"


def test_is_valid_url():
    assert is_valid_url("https://www.example.com") is True
    assert is_valid_url("http://www.example.com") is True
    assert is_valid_url("www.example.com") is False
    assert is_valid_url("example.com") is False


def test_flatten_list():
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = flatten_list(nested_list)
    assert flattened_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_should_ignore(mock_config_helper: ConfigHelper):
    """Test that the file is ignored."""
    file_path_ignored = Path("README.md")
    file_path_not_ignored = Path("readmeai/main.py")
    assert should_ignore(mock_config_helper, file_path_ignored) is True
    assert should_ignore(mock_config_helper, file_path_not_ignored) is False


def test_get_resource_path_from_resources(monkeypatch):
    def mock_resources_files(package):
        return Path("/fake/path")

    monkeypatch.setattr("importlib.resources.files", mock_resources_files)

    package = "readmeai"
    resource_name = "data.txt"
    expected = Path("/fake/path") / resource_name
    actual = get_resource_path(package, resource_name)
    assert actual == expected


def test_get_resource_path_from_pkg_resources(monkeypatch):
    def mock_resource_filename(package, resource_name):
        return f"/fake/path/{resource_name}"

    monkeypatch.setattr(
        "pkg_resources.resource_filename", mock_resource_filename
    )

    package = "readmeai"
    resource_name = "settings/ignore_files.toml"
    expected = Path().cwd() / "readmeai/settings/ignore_files.toml"
    actual = get_resource_path(package, resource_name)
    assert actual == expected


def test_get_resource_path_handles_importerror(monkeypatch):
    def raise_typeerror():
        raise TypeError

    monkeypatch.setattr("importlib.resources.files", raise_typeerror)

    package = "readmeai"
    resource_name = "settings/ignore_files.toml"
    expected = str(Path().cwd() / "readmeai/settings/ignore_files.toml")
    actual = get_resource_path(package, resource_name)
    assert actual == expected
