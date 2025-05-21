"""Enums that define settings for customizing the README file."""

from enum import Enum


class BadgeStyles(str, Enum):
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


class CustomLogos(str, Enum):
    """
    Options for custom/external project logo files.
    """

    CUSTOM = "CUSTOM"
    LLM = "LLM"


class DefaultLogos(str, Enum):
    """
    Predefined SVG project logo options.
    """

    ANIMATED = "readmeai/assets/logos/animated.svg"
    AURORA = "readmeai/assets/logos/aurora.svg"
    BLUE = "readmeai/assets/logos/blue.svg"
    GREEN = "readmeai/assets/logos/green.svg"
    ICE = "readmeai/assets/logos/ice.svg"
    METALLIC = "readmeai/assets/logos/metallic.svg"
    MIDNIGHT = "readmeai/assets/logos/midnight.svg"
    ORANGE = "readmeai/assets/logos/orange.svg"
    PURPLE = "readmeai/assets/logos/purple.svg"
    RAINBOW = "readmeai/assets/logos/rainbow.svg"
    TERMINAL = "readmeai/assets/logos/terminal.svg"


class EmojiThemes(str, Enum):
    """
    Emoji theme 'packs' for customizing header section titles.
    """

    # -- Core
    DEFAULT = "default"
    MINIMAL = "minimal"
    # OSS = "oss"

    # -- Development
    # API = "api"
    # GAME = "game"
    # MOBILE = "mobile"
    # WEB = "web"

    # -- Infrastructure
    # CLOUD = "cloud"
    # CYBER = "cyber"
    # IOT = "iot"

    # -- Data and AI
    # DATA = "data"
    # ML = "ml"

    # -- Geometric and Abstract
    ASCENSION = "ascension"
    FIBONACCI = "fibonacci"
    HARMONY = "harmony"
    PRISM = "prism"
    QUANTUM = "quantum"

    # -- Monochrome and Unicode
    MONOCHROME = "monochrome"
    UNICODE = "unicode"

    # -- Nature and Elements
    ATOMIC = "atomic"
    COSMIC = "cosmic"
    CRYSTAL = "crystal"
    EARTH = "earth"
    FIRE = "fire"
    FOREST = "forest"
    NATURE = "nature"
    RAINBOW = "rainbow"
    SOLAR = "solar"
    WATER = "water"

    # -- Miscellaneous
    FUN = "fun"
    VINTAGE = "vintage"
    ZEN = "zen"

    # -- Random
    RANDOM = "random"


class HeaderStyles(str, Enum):
    """
    Header style template options for the README file.
    """

    ASCII = "ascii"
    ASCII_BOX = "ascii_box"
    BANNER = "banner"
    CLASSIC = "classic"
    CLEAN = "clean"
    COMPACT = "compact"
    CONSOLE = "console"
    MODERN = "modern"


class NavigationStyles(str, Enum):
    """
    Navigation menu styles for the README file.
    """

    ACCORDION = "accordion"
    BULLET = "bullet"
    NUMBER = "number"
    ROMAN = "roman"
