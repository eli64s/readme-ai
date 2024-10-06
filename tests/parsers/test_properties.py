import pytest

from readmeai.parsers.properties import PropertiesParser


@pytest.fixture
def parser(properties_parser: PropertiesParser):
    return properties_parser


def test_parser_initialization(parser: PropertiesParser):
    assert isinstance(parser, PropertiesParser)


def test_parse_properties_content(
    parser: PropertiesParser, properties_content: str
):
    result = parser.parse(properties_content)
    assert isinstance(result, list)
    assert len(result) > 0


def test_extracted_dependencies(
    parser: PropertiesParser, properties_content: str
):
    result = parser.parse(properties_content)
    assert "spring" in result
    assert "kotlin" in result
    assert "java" in result
    assert "junit" in result
    assert "kotlin" in result
    assert "tomcat" in result


def test_version_extraction(parser: PropertiesParser):
    content = "javaVersion=1.2.3\notherToolVersion=4.5.6"
    result = parser.parse(content)
    assert "java" in result


def test_camelcase_splitting(parser: PropertiesParser):
    content = "camelCaseProperty=someValue"
    result = parser.parse(content)
    assert "camelcaseproperty" in result


def test_snake_case_splitting(parser: PropertiesParser):
    content = "snake_case_property=some_value"
    result = parser.parse(content)
    assert "snake_case_property" in result
    assert "some_value" in result


def test_common_prefix_removal(parser: PropertiesParser):
    content = "org.myproject.core.MainClass"
    result = parser.parse(content)
    assert "mainclass" in result
    assert "myproject" in result


def test_common_suffix_removal(parser: PropertiesParser):
    content = "myAwesomeLibrary=1.0.0\ncoolFrameworkVersion=2.0.0"
    result = parser.parse(content)
    assert "myawesomelibrary" in result


def test_short_word_filtering(parser: PropertiesParser):
    content = "a=1\nbb=2\nccc=3"
    result = parser.parse(content)
    assert "a" in result
    assert "ccc" in result


def test_common_tech_keywords(parser: PropertiesParser):
    content = "using=java,python,react"
    result = parser.parse(content)
    assert "java" in result
    assert "python" in result
    assert "react" in result


def test_empty_content(parser: PropertiesParser):
    result = parser.parse("")
    assert result == []


def test_comment_handling(parser: PropertiesParser):
    content = "# This is a comment\nrealProperty=value"
    result = parser.parse(content)
    assert "realproperty" in result


def test_multiple_occurrences(parser: PropertiesParser):
    content = "spring.version=5.0\nspring.boot.version=2.5"
    result = parser.parse(content)
    assert result.count("spring") == 1  # Should only appear once


def test_case_insensitivity(parser: PropertiesParser):
    content = "JavaVersion=11\nkotlinVERSION=1.5"
    result = parser.parse(content)
    assert "java" in result
    assert "kotlin" in result
