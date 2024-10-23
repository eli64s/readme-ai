"""
Enum classes that store information settings for the LLM
API service providers, badge styles, and image options.
"""

import enum


class BadgeStyleOptions(str, enum.Enum):
    """
    Badge icon styles for the project README.
    """

    DEFAULT = "default"
    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    FOR_THE_BADGE = "for-the-badge"
    PLASTIC = "plastic"
    SKILLS = "skills"
    SKILLS_LIGHT = "skills-light"
    SOCIAL = "social"


class HeaderStyleOptions(str, enum.Enum):
    """
    Enum of supported 'Header' template styles for the README file.
    """

    ASCII = "ascii"
    ASCII_BOX = "ascii_box"
    CLASSIC = "classic"
    COMPACT = "compact"
    MODERN = "modern"
    SVG = "svg"


class ImageOptions(str, enum.Enum):
    """
    Default image options for the project logo.
    """

    CUSTOM = "CUSTOM"
    LLM = "LLM"
    BLACK = "https://img.icons8.com/external-tal-revivo-regular-tal-revivo/96/external-readme-is-a-easy-to-build-a-developer-hub-that-adapts-to-the-user-logo-regular-tal-revivo.png"
    BLUE = "https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg"
    CLOUD = "https://cdn-icons-png.flaticon.com/512/6295/6295417.png"
    GRADIENT = "https://img.icons8.com/?size=512&id=55494&format=png"
    GREY = "https://img.icons8.com/external-tal-revivo-filled-tal-revivo/96/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-filled-tal-revivo.png"
    PURPLE = "https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png"


class TocStyleOptions(str, enum.Enum):
    """
    Enum of supported 'Table of Contents' templates for the README file.
    """

    BULLET = "bullet"
    FOLD = "fold"
    LINKS = "links"
    NUMBER = "number"
    ROMAN = "roman"


class LLMService(str, enum.Enum):
    """
    LLM API service providers.
    """

    ANTHROPIC = "ANTHROPIC"
    GEMINI = "GEMINI"
    OLLAMA = "OLLAMA"
    OPENAI = "OPENAI"
    OFFLINE = "OFFLINE"


class ServiceAuthKeys(str, enum.Enum):
    """
    Environment variable names associated with a LLM API key.
    """

    ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"
    GOOGLE_API_KEY = "GOOGLE_API_KEY"
    OLLAMA_HOST = "OLLAMA_HOST"
    OPENAI_API_KEY = "OPENAI_API_KEY"
