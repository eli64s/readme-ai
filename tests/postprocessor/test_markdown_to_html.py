from collections.abc import Callable

import pytest
from readmeai.postprocessor.markdown_to_html import convert


@pytest.fixture
def converter() -> Callable[[str], str]:
    return convert


@pytest.mark.parametrize(
    "markdown, expected_html",
    [
        ("**bold text**", "<strong>bold text</strong>"),
        ("*italic text*", "<em>italic text</em>"),
        ("`inline code`", "<code>inline code</code>"),
        (
            "[link text](https://example.com)",
            '<a href="https://example.com">link text</a>',
        ),
        ("# Header 1", "<h1>Header 1</h1>"),
        ("## Header 2", "<h2>Header 2</h2>"),
        ("### Header 3", "<h3>Header 3</h3>"),
        ("#### Header 4", "<h4>Header 4</h4>"),
        ("##### Header 5", "<h5>Header 5</h5>"),
        ("###### Header 6", "<h6>Header 6</h6>"),
    ],
)
def test_basic_markdown_conversion(
    converter: Callable[[str], str], markdown: str, expected_html: str
):
    assert converter(markdown) == expected_html


def test_unordered_list(converter: Callable[[str], str]):
    markdown = """
    - Item 1
    - Item 2
    - Item 3
    """
    expected_html = """
    <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
    </ul>
    """
    assert converter(markdown).strip() == expected_html.strip()
    assert converter(markdown).strip() == expected_html.strip()


def test_ordered_list(converter: Callable[[str], str]):
    markdown = """
1. First item
2. Second item
3. Third item
"""
    expected_html = """
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
</ol>
"""
    assert converter(markdown).strip() == expected_html.strip()


def test_mixed_formatting(converter: Callable[[str], str]):
    markdown = "This is **bold** and *italic* text with a [link](https://example.com) and `inline code`."
    expected_html = 'This is <strong>bold</strong> and <em>italic</em> text with a <a href="https://example.com">link</a> and <code>inline code</code>.'
    assert converter(markdown) == expected_html


def test_nested_formatting(converter: Callable[[str], str]):
    markdown = "**Bold text with *italic* inside**"
    expected_html = "<strong>Bold text with <em>italic</em> inside</strong>"
    assert converter(markdown) == expected_html


def test_multiple_paragraphs(converter: Callable[[str], str]):
    markdown = """
First paragraph with **bold** text.

Second paragraph with *italic* text.

### Header in between

Last paragraph with a [link](https://example.com).
"""
    expected_html = """
First paragraph with <strong>bold</strong> text.

Second paragraph with <em>italic</em> text.

<h3>Header in between</h3>

Last paragraph with a <a href="https://example.com">link</a>.
"""
    assert converter(markdown).strip() == expected_html.strip()


def test_edge_cases(converter: Callable[[str], str]):
    assert converter("") == ""
    assert converter("Plain text without markdown") == "Plain text without markdown"
    assert converter("**") == "**"
    assert converter("*") == "*"
    assert converter("[]()") == "[]()"


if __name__ == "__main__":
    pytest.main([__file__])
