"""Test cases for the file_parser module."""

from readmeai.parsers.base_parser import FileParser
from readmeai.parsers.factory import parser_factory
from readmeai.parsers.python import RequirementsParser, TomlParser


def test_parser_factory():
    """Test cases for the get_file_parsers method."""
    parsers = parser_factory()
    assert "requirements.txt" in parsers
    assert isinstance(parsers["requirements.txt"], RequirementsParser)

    assert "pyproject.toml" in parsers
    assert isinstance(parsers["pyproject.toml"], TomlParser)

    assert "Pipfile" in parsers
    assert isinstance(parsers["Pipfile"], TomlParser)

    for parser in parsers.values():
        assert isinstance(parser, FileParser)
