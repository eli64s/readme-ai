from enum import Enum


class Section(str, Enum):
    """README section types."""

    OVERVIEW = "overview"
    FEATURES = "features"
    INSTALLATION = "installation"
    USAGE = "usage"
    ARCHITECTURE = "architecture"


class Style(str, Enum):
    """README style types."""

    MINIMAL = "minimal"
    TECHNICAL = "technical"
    DETAILED = "detailed"
    BUSINESS = "business"
