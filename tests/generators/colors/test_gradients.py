import re
from unittest.mock import patch

import pytest
from readmeai.generators.colors.gradients import (
    generate_base_color,
    generate_gradient_colors,
    generate_random_color,
    generate_related_color,
)


class TestColorUtils:
    """Test suite for color utility functions."""

    @pytest.fixture
    def hex_color_pattern(self):
        """Regex pattern for validating hex color codes."""
        return re.compile(r"^#[0-9a-fA-F]{6}$")

    def test_generate_base_color(self):
        """Test base color generation."""
        # Test multiple generations to ensure consistency
        for _ in range(10):
            hue, saturation, value = generate_base_color()

            # Check value ranges
            assert 0 <= hue <= 1, "Hue should be between 0 and 1"
            assert saturation == 0.8, "Saturation should be 0.8"
            assert value == 0.9, "Value should be 0.9"

            # Check types
            assert isinstance(hue, float)
            assert isinstance(saturation, float)
            assert isinstance(value, float)

    def test_generate_random_color_format(self, hex_color_pattern):
        """Test random color generation format."""
        # Test multiple generations
        for _ in range(10):
            color = generate_random_color()
            assert hex_color_pattern.match(color), f"Invalid hex color format: {color}"
            assert len(color) == 7, (
                f"Color should be 7 characters (including #): {color}"
            )

    def test_generate_related_color_format(self, hex_color_pattern):
        """Test related color generation format."""
        base_hue = 0.5
        shifts = [0.1, 0.2, 0.3]

        for shift in shifts:
            color = generate_related_color(base_hue, shift)
            assert hex_color_pattern.match(color), f"Invalid hex color format: {color}"
            assert len(color) == 7, (
                f"Color should be 7 characters (including #): {color}"
            )

    def test_generate_related_color_hue_wrapping(self):
        """Test hue wrapping for related colors."""
        base_hue = 0.9
        shift = 0.2
        color = generate_related_color(base_hue, shift)

        # The result should still be a valid hex color
        assert color.startswith("#")
        assert len(color) == 7

        # Test with hue > 1.0
        base_hue = 0.9
        shift = 0.5
        color = generate_related_color(base_hue, shift)
        assert color.startswith("#")
        assert len(color) == 7

    def test_generate_gradient_colors_length(self):
        """Test gradient colors list length."""
        colors = generate_gradient_colors()
        assert len(colors) == 3, "Should generate exactly 3 colors"

    def test_generate_gradient_colors_format(self, hex_color_pattern):
        """Test format of all gradient colors."""
        colors = generate_gradient_colors()
        for color in colors:
            assert hex_color_pattern.match(color), f"Invalid hex color format: {color}"
            assert len(color) == 7, (
                f"Color should be 7 characters (including #): {color}"
            )

    @patch("readmeai.generators.colors.gradients.randint")
    def test_random_color_deterministic(self, mock_randint):
        """Test random color generation with fixed random values."""
        mock_randint.side_effect = [255, 128, 0]  # RGB values
        color = generate_random_color()
        assert color == "#ff8000", f"Expected #ff8000, got {color}"

    def test_related_colors_consistency(self):
        """Test that related colors are consistently generated."""
        base_hue = 0.5
        color1 = generate_related_color(base_hue, 0.1)
        color2 = generate_related_color(base_hue, 0.1)
        assert color1 == color2, "Same inputs should generate same color"

    def test_gradient_colors_relationships(self):
        """Test relationships between gradient colors."""
        with patch(
            "readmeai.generators.colors.gradients.generate_base_color"
        ) as mock_base:
            mock_base.return_value = (0.5, 0.8, 0.9)  # Fixed base color
            colors = generate_gradient_colors()

            # Should have 3 different colors
            assert len(set(colors)) == 3, "All gradient colors should be different"

            # Colors should be in sequential order based on hue shift
            for i in range(len(colors) - 1):
                assert colors[i] != colors[i + 1], "Adjacent colors should be different"

    @pytest.mark.parametrize(
        "base_hue,shift",
        [
            (0.0, 0.1),  # Start of spectrum
            (0.5, 0.1),  # Middle of spectrum
            (0.9, 0.1),  # End of spectrum
            (1.0, 0.1),  # Edge case
            (0.5, 0.0),  # No shift
            (0.5, 1.0),  # Full shift
        ],
    )
    def test_related_color_various_inputs(self, base_hue, shift, hex_color_pattern):
        """Test related color generation with various inputs."""
        color = generate_related_color(base_hue, shift)
        assert hex_color_pattern.match(color), f"Invalid hex color format: {color}"

    def test_color_values_in_valid_range(self):
        """Test that generated colors have valid RGB values."""

        def is_valid_rgb(color: str) -> bool:
            """Check if color has valid RGB values."""
            # Remove '#' and convert to RGB integers
            rgb = tuple(int(color[i : i + 2], 16) for i in (1, 3, 5))
            return all(0 <= v <= 255 for v in rgb)

        # Test random colors
        for _ in range(10):
            color = generate_random_color()
            assert is_valid_rgb(color), f"Invalid RGB values in color: {color}"

        # Test gradient colors
        colors = generate_gradient_colors()
        for color in colors:
            assert is_valid_rgb(color), f"Invalid RGB values in color: {color}"
