"""Utilities for managing color schemes used to style the README."""

import colorsys
from random import randint

from readmeai.core.logger import get_logger

_logger = get_logger(__name__)


def generate_base_color() -> tuple:
    """Generate a random base color in HSV."""
    # Random hue value between 0 and 1
    hue = randint(0, 360) / 360.0
    # Keep saturation constant for related colors
    saturation = 0.8
    # Keep brightness constant
    value = 0.9
    return hue, saturation, value


def generate_gradient_colors() -> list:
    """Generate a list of related colors to form a gradient."""
    base_hue, saturation, value = generate_base_color()
    # Generate 3 related colors
    gradient_colors = [
        generate_related_color(base_hue, shift / 10) for shift in range(3)
    ]
    _logger.info(f"Generated gradient colors: {gradient_colors}")
    return gradient_colors


def generate_random_color() -> str:
    """Generate a random hex color."""
    color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
    _logger.info(f"Generated random color: {color}")
    return color


def generate_related_color(base_hue: float, shift: float) -> str:
    """Generate a related color by shifting the hue of the base color."""
    # Wrap around if the hue exceeds 1.0
    hue = (base_hue + shift) % 1.0
    r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 0.9)
    color = f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"
    _logger.info(f"Generated related color: {color}")
    return color
