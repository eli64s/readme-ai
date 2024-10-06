from readmeai.generators.emojis import remove_emojis


def test_remove_emojis_from_headers_with_emojis():
    """Tests the remove_emojis static method with emojis."""
    content_with_emojis = ["# Header 🚀", "## Another Header 😃"]
    expected_output = ["# Header ", "## Another Header "]
    result = remove_emojis(content_with_emojis)
    assert result == expected_output


def test_remove_emojis_from_headers_without_emojis():
    """Tests the remove_emojis static method without emojis."""
    content_without_emojis = ["# Header", "## Another Header"]
    result = remove_emojis(content_without_emojis)
    assert result == content_without_emojis
