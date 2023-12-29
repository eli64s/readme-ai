"""Unit tests for readmeai utility methods."""

from pathlib import Path

from readmeai.config.settings import ConfigHelper
from readmeai.utils.utils import (
    flatten_list,
    format_sentence,
    get_relative_path,
    get_resource_path,
    is_valid_url,
    remove_substring,
    should_ignore,
)


def test_is_valid_url():
    assert is_valid_url("https://www.example.com") is True
    assert is_valid_url("http://www.example.com") is True
    assert is_valid_url("www.example.com") is False
    assert is_valid_url("example.com") is False


def test_flatten_list():
    nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened_list = flatten_list(nested_list)
    assert flattened_list == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_format_sentence():
    text = "'hello world'"
    formatted_sentence = format_sentence(text)
    assert formatted_sentence == "hello world"


def test_get_relative_path():
    """Test that the relative path is correct."""
    absolute_path = "readmeai/utils/utils.py"
    base_path = Path().parent
    relative_path = get_relative_path(absolute_path, base_path)
    assert str(relative_path) == "readmeai/utils/utils.py"


def test_remove_substring():
    """Test that the substring is removed from the input string."""
    test_string = """
    <div>
        <p>Paragraph 1 content.</p>
        Some content that should remain.
        <p>Paragraph 2 content with <div> nested tag.</p></div>
        This content is outside of the div tags.
        <p>Another paragraph.</p>
        <div>Content to be removed.</div>
        <p>Final paragraph.</p>
        <div>
            <p>Paragraph inside div.</p>
            Content inside div that should be removed.
        </div>
    </div>
    """
    result = remove_substring(test_string)
    assert isinstance(result, str)


def test_should_ignore(config_helper: ConfigHelper):
    """Test that the file is ignored."""
    file_path_ignored = Path("README.md")
    file_path_not_ignored = Path("readmeai/main.py")
    assert should_ignore(config_helper, file_path_ignored) is True
    assert should_ignore(config_helper, file_path_not_ignored) is False


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
