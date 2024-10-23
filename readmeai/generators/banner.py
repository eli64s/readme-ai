import xml.etree.ElementTree as ET
from base64 import b64encode
from typing import List

from readmeai.logger import get_logger

_logger = get_logger(__name__)


def convert_svg_to_html(title: str, output_svg_path: str) -> str:
    """Generate a stylish banner for the README file."""
    svg_content = f"""<?xml version="1.0" encoding="utf-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200">
        <defs>
            <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#4158D0;stop-opacity:1" />
                <stop offset="50%" style="stop-color:#C850C0;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#FFCC70;stop-opacity:1" />
            </linearGradient>
            <filter id="shadow">
                <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.25" />
            </filter>
        </defs>
        <rect width="800" height="200" fill="url(#bg-gradient)" rx="15" ry="15"/>
        <text x="400" y="100" font-family="Arial, sans-serif" font-size="48"
        font-weight="bold" text-anchor="middle" dominant-baseline="middle"
        fill="#FFFFFF" filter="url(#shadow)">{title.upper()}</text>
    </svg>"""

    # If output path is provided, save the SVG file
    if output_svg_path:
        root = ET.fromstring(svg_content)
        tree = ET.ElementTree(root)
        tree.write(output_svg_path, encoding="utf-8", xml_declaration=True)

    # Convert SVG to base64 for embedding
    svg_bytes = svg_content.encode("utf-8")
    svg_base64 = b64encode(svg_bytes).decode("utf-8")

    html_content = f"""<p align="center">\n\t<img src="data:image/svg+xml;base64,{svg_base64}" alt="{title.lower()}-banner" width="800">\n</p>"""

    _logger.info("Generated HTML content with embedded SVG for README.md")

    return html_content


def generate_ascii_banner(title: str) -> str:
    """Generate an ASCII banner for the project name."""
    lines = [""] * 5
    for char in title:
        letter = _create_letter(char)
        for i in range(5):
            lines[i] += f"{letter[i]} "

    return _wrap_with_pre_tag("\n".join(lines))


def generate_ascii_box_banner(title: str, slogan: str = "") -> str:
    """Generate an ASCII banner for the project name and slogan."""
    lines = [""] * 5
    for char in title:
        letter = _create_letter(char)
        for i in range(5):
            lines[i] += f"{letter[i]} "

    max_width = max(len(line) for line in lines)
    box_width = max(max_width, len(slogan)) + 4

    banner = [
        "╔" + "═" * box_width + "╗",
        "║" + " " * box_width + "║",
    ]

    banner.extend(f"║  {line.ljust(box_width - 2)}║" for line in lines)
    banner.extend(
        [
            "║" + " " * box_width + "║",
            # f"║  {slogan.center(box_width - 4)}  ║",
            "║" + " " * box_width + "║",
            "╚" + "═" * box_width + "╝",
        ]
    )

    return _wrap_with_pre_tag("\n".join(banner))


def _create_letter(char) -> List[str]:
    """Create an ASCII letter from a character."""
    letters = {
        "A": ["  ██  ", " ████ ", "██  ██", "██████", "██  ██"],
        "B": ["██████", "██   █", "██████", "██   █", "██████"],
        "C": [" ████ ", "██    ", "██    ", "██    ", " ████ "],
        "D": ["████  ", "██  ██", "██  ██", "██  ██", "████  "],
        "E": ["██████", "██    ", "████  ", "██    ", "██████"],
        "F": ["██████", "██    ", "████  ", "██    ", "██    "],
        "G": [" ████ ", "██    ", "██ ███", "██  ██", " ████ "],
        "H": ["██  ██", "██  ██", "██████", "██  ██", "██  ██"],
        "I": ["██████", "  ██  ", "  ██  ", "  ██  ", "██████"],
        "J": ["██████", "   ██ ", "   ██ ", "██ ██ ", " ███  "],
        "K": ["██  ██", "██ ██ ", "████  ", "██ ██ ", "██  ██"],
        "L": ["██    ", "██    ", "██    ", "██    ", "██████"],
        "M": ["██   ██", "███ ███", "██ █ ██", "██   ██", "██   ██"],
        "N": ["██   ██", "███  ██", "██ █ ██", "██  ███", "██   ██"],
        "O": [" ████ ", "██  ██", "██  ██", "██  ██", " ████ "],
        "P": ["██████", "██  ██", "██████", "██    ", "██    "],
        "Q": [" ████ ", "██  ██", "██  ██", "██ ███", " ██ ██"],
        "R": ["██████", "██  ██", "██████", "██ ██ ", "██  ██"],
        "S": [" ████ ", "██    ", " ████ ", "    ██", "█████ "],
        "T": ["██████", "  ██  ", "  ██  ", "  ██  ", "  ██  "],
        "U": ["██  ██", "██  ██", "██  ██", "██  ██", " ████ "],
        "V": ["██  ██", "██  ██", "██  ██", " ████ ", "  ██  "],
        "W": ["██   ██", "██   ██", "██ █ ██", "███ ███", "██   ██"],
        "X": ["██  ██", " ████ ", "  ██  ", " ████ ", "██  ██"],
        "Y": ["██  ██", " ████ ", "  ██  ", "  ██  ", "  ██  "],
        "Z": ["██████", "   ██ ", "  ██  ", " ██   ", "██████"],
        "-": ["      ", "      ", "██████", "      ", "      "],
        " ": ["    ", "    ", "    ", "    ", "    "],
    }
    return letters.get(char.upper(), ["?????"] * 5)


def _wrap_with_pre_tag(text: str) -> str:
    """Wrap the text content with a <pre> tag."""
    return f"<pre>\n{text}\n</pre>"
