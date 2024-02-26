"""Test cases for the file_parser module."""

from readmeai.parsers.factory import parser_handler
from readmeai.parsers.language.python import RequirementsParser, TomlParser


def test_parser_handler():
    """Test cases for the get_file_parsers method."""
    parsers = parser_handler()
    assert "requirements.txt" in parsers
    assert isinstance(parsers["requirements.txt"], RequirementsParser)

    assert "pyproject.toml" in parsers
    assert isinstance(parsers["pyproject.toml"], TomlParser)

    assert "Pipfile" in parsers
    assert isinstance(parsers["Pipfile"], TomlParser)
