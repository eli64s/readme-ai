"""Utility functions cleaning and formatting LLM API responses."""

import re


def fix_markdown_table_rows(md_table: str) -> str:
    """Format a Markdown table with feature and description columns."""
    lines = md_table.split("||")

    formatted_md_table = "| Feature | Description |\n|---------|-------------|\n"

    for line in lines[2:]:
        clean_line = line.strip("|")
        parts = clean_line.split("|")

        if len(parts) >= 3:
            feature = parts[1].strip()
            description = parts[2].strip()
            formatted_row = f"| {feature} | {description} |\n"
            formatted_md_table += formatted_row

    return formatted_md_table


def format_markdown_table(text: str) -> str:
    """
    Pattern to match a Markdown table. Looks for a
    header row with at least two columns, followed by
    a separator row, and then one or more data rows.
    This version is designed to be more robust in removing
    text around the markdown table.
    """
    if "REPLACE-ME</code>" in text:
        return text

    pattern = r"(?:.*\n)*(\|.*\|.*\n\|[-: ]+\|[-: ]+\|.*\n(?:\|.*\|.*\n)*)(?:.*\n)*"
    match = re.search(pattern, text, re.DOTALL)
    return match[1].strip() if match else ""


def process_markdown(text):
    """Remove uneven Markdown syntax while preserving valid formatting."""
    # Remove extra asterisks at the end of lines
    text = re.sub(r"\*+$", "", text, flags=re.MULTILINE)

    # Remove unmatched bullets or hyphens at the beginning of lines
    text = re.sub(r"^[\s]*[-*]\s+", "", text, flags=re.MULTILINE)

    # Preserve valid bold and italic formatting
    # This regex handles nested bold and italic formatting
    text = re.sub(
        r"\*{1,2}(?P<content>[^*\n]+(?:\*{1,2}[^*\n]+\*{1,2}[^*\n]+)*)\*{1,2}",
        lambda m: m.group(0) if m.group(0).count("*") % 2 == 0 else m.group(0)[1:-1],
        text,
    )

    # Remove standalone asterisks or underscores
    text = re.sub(r"(?<!\*)\*(?!\*)|(?<!_)_(?!_)", "", text)

    return text.strip()


def process_text(text: str) -> str:
    """Format and clean generated text from the LLM."""
    # Dynamically remove all text before and including the first colon if any exist
    text = re.sub(r"^[^:]*:\s*", "", text)

    # Remove any text before and including "**:"
    text = re.sub(r"\*\*:\s*", "", text, flags=re.DOTALL)

    # Remove single and double quotes that are missing their closing counterpart
    text = re.sub(r"['\"](.*?)$", r"\1", text)
    text = re.sub(r"^(.*?)['\"]", r"\1", text)

    # Remove specific pattern and rephrase
    text = re.sub(
        r"\*\*Code Summary:\*\*\s*(.*?)\s*provides functions to",
        r"Provides functions to",
        text,
        flags=re.DOTALL,
    )
    # Remove single and double quotes around any text
    text = re.sub(r"(?<!\w)['\"](.*?)['\"](?!\w)", r"\1", text)

    # Remove newlines and tabs
    text = text.replace("\n", "").replace("\t", "")

    # Remove non-letter characters from the beginning of the string
    text = re.sub(r"^[^a-zA-Z]*", "", text)

    # Remove extra white space around punctuation except for '('
    text = re.sub(r"\s*([)'.!,?;:])(?!\.\s*\w)", r"\1", text)

    # Remove extra white space before opening parentheses
    text = re.sub(r"(\()\s*", r"\1", text)

    # Replace multiple consecutive spaces with a single space
    text = re.sub(r" +", " ", text)

    # Remove extra white space around hyphens
    text = re.sub(r"\s*-\s*", "-", text)

    # Specifically target and remove trailing special characters like asterisks
    text = re.sub(r"\*+$", "", text)

    text = text.strip()

    # Ensure the first letter is capitalized if it's alphabetic
    if text and not text[0].isupper() and text[0].isalpha():
        text = text[0].upper() + text[1:]

    return text


def extract_text_between_tags(input_string: str, start_tag: str, end_tag: str) -> str:
    """Extract text between <overview/intro> tags in a string."""
    match = re.search(
        rf"{start_tag}(.*){end_tag}",
        input_string,
        re.DOTALL | re.IGNORECASE,
    )
    return match.group(1).strip() if match else ""


def remove_quotes(text: str) -> str:
    """Remove quotes from a string if they exist."""
    if not text or len(text) < 2:
        return text
    quote_chars = ("'", '"', "`")
    return text[1:-1] if text[0] == text[-1] and text[0] in quote_chars else text
