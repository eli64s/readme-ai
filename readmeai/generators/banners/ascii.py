def generate_banner(title: str) -> str:
    """Generate an ASCII banner for the project name."""
    lines = [""] * 5
    for char in title:
        letter = _create_letter(char)
        for i in range(5):
            lines[i] += f"{letter[i]} "

    return _wrap_with_pre_tag("\n".join(lines))


def generate_box_banner(title: str, tagline: str = "") -> str:
    """Generate an ASCII banner for the project name and tagline."""
    lines = [""] * 5
    for char in title:
        letter = _create_letter(char)
        for i in range(5):
            lines[i] += f"{letter[i]} "

    max_width = max(len(line) for line in lines)
    box_width = max(max_width, len(tagline)) + 4

    banner = [
        "╔" + "═" * box_width + "╗",
        "║" + " " * box_width + "║",
    ]
    banner.extend(f"║  {line.ljust(box_width - 2)}║" for line in lines)
    banner.extend([
        "║" + " " * box_width + "║",
        # f"║  {tagline.center(box_width - 4)}  ║",
        "║" + " " * box_width + "║",
        "╚" + "═" * box_width + "╝",
    ])
    return _wrap_with_pre_tag("\n".join(banner))


def generate_console_banner(title: str) -> str:
    """Generate an ASCII banner for the project name and tagline."""
    lines = [""] * 5
    for char in title:
        letter = _create_letter(char)
        for i in range(5):
            lines[i] += f"{letter[i]} "
    return _wrap_with_console_tag("\n".join(lines))


def _create_letter(char) -> list[str]:
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
        ".": ["      ", "      ", "  ██  ", "  ██  ", "      "],
        " ": ["    ", "    ", "    ", "    ", "    "],
    }
    return letters.get(char.upper(), ["?????"] * 5)


def _wrap_with_pre_tag(text: str) -> str:
    """Wrap the text content with a <pre> tag."""
    return f"<pre>\n{text}\n</pre>"


def _wrap_with_console_tag(text: str) -> str:
    """Wrap the text content with a console code block."""
    return f"""```console\n{text}"""
