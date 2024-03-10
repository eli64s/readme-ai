"""
Utility functions cleaning and formatting LLM API responses.
"""

import re


def clean_response(prompt_type: str, response_text: str) -> str:
    """Post-processes the response from the LLM."""
    if prompt_type == "features":
        return format_md_table(response_text)
    elif prompt_type != "features":
        return clean_text(response_text)
    else:
        return response_text


def clean_text(text: str) -> str:
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


def fix_md_table_rows(md_table: str) -> str:
    """Format a Markdown table with feature and description columns."""
    lines = md_table.split("||")

    formatted_md_table = (
        "| Feature | Description |\n|---------|-------------|\n"
    )

    for line in lines[2:]:
        clean_line = line.strip("|")
        parts = clean_line.split("|")

        if len(parts) >= 3:
            feature = parts[1].strip()
            description = parts[2].strip()
            formatted_row = f"| {feature} | {description} |\n"
            formatted_md_table += formatted_row

    return formatted_md_table


def format_md_table(text: str) -> str:
    """
    Pattern to match a Markdown table. Looks for a
    header row with at least two columns, followed by
    a separator row, and then one or more data rows.
    This version is designed to be more robust in removing
    text around the markdown table.
    """
    pattern = (
        r"(?:.*\n)*(\|.*\|.*\n\|[-: ]+\|[-: ]+\|.*\n(?:\|.*\|.*\n)*)(?:.*\n)*"
    )
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""
