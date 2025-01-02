import re
from typing import Any, Dict, Literal
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import pytest
from pydantic import ValidationError
from readmeai.core.errors import FileReadError
from readmeai.generators.banners.svg import SVGBannerGenerator, SVGBannerSettings


@pytest.fixture
def mock_file_handler():
    """Mock the file handler to avoid actual file operations"""
    with patch("readmeai.utilities.file_handler.FileHandler") as mock:
        handler = mock.return_value
        handler.read.side_effect = FileReadError(
            "File not found: config/settings/templates/banners.toml"
        )
        yield mock


@pytest.fixture
def valid_settings_dict():
    """Real settings from banners.toml"""
    return {
        "border_radius": 5.0,
        "font_color": "#FFFFFF",
        "font_family": "Arial, sans-serif",
        "font_size": 24,
        "height": 200,
        "pattern_opacity": 0.2,
        "pattern_size": 20.0,
        "shadow_blur": 4.0,
        "shadow_dx": 2.0,
        "shadow_dy": 2.0,
        "shadow_opacity": 0.5,
        "shape_opacity": 0.8,
        "subtitle_size": 18,
        "width": 800,
    }


@pytest.fixture
def valid_config_dict(valid_settings_dict: Dict[str, Dict[str, float]]):
    """Real template from banners.toml"""
    return {
        "banners": {
            "svg": {
                "template": """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
    <defs>
        <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
            <stop offset="50%" style="stop-color:{color2};stop-opacity:1" />
            <stop offset="100%" style="stop-color:{color3};stop-opacity:1" />
        </linearGradient>
        <filter id="shadow">
            <feDropShadow dx="{shadow_dx}" dy="{shadow_dy}" stdDeviation="{shadow_blur}" flood-opacity="{shadow_opacity}" />
        </filter>
        <pattern id="dots" width="{pattern_size}" height="{pattern_size}" patternUnits="userSpaceOnUse">
            <circle cx="3" cy="3" r="1.5" fill="rgba(255,255,255,{pattern_opacity})" />
        </pattern>
    </defs>
    <rect width="100%" height="100%" fill="url(#bg)" rx="{border_radius}" />
    <rect width="100%" height="100%" fill="url(#dots)" />
    <circle cx="{width_08}" cy="{height_025}" r="{height_015}" fill="rgba(255,255,255,{shape_opacity})" />
    <circle cx="{width_92}" cy="{height_075}" r="{height_02}" fill="rgba(255,255,255,{shape_opacity})" />
    <path d="M {width_2} {height_0125}
             L {width_2_plus_height_025} {height_0375}
             L {width_2_minus_height_025} {height_0375} Z" fill="rgba(255,255,255,{shape_opacity})" />
    <text x="{width_2}" y="{height_2}" font-family="{font_family}" font-size="{font_size}" font-weight="bold" text-anchor="middle" fill="{font_color}" filter="url(#shadow)">
        {title}
    </text>
    <text x="{width_2}" y="{height_0625}" font-family="{font_family}" font-size="{subtitle_size}" text-anchor="middle" fill="rgba(255,255,255,0.9)">
"""
            }
        },
        "settings": valid_settings_dict,
    }


class TestSVGBannerSettings:
    """Test cases for SVGBannerSettings validation"""

    def test_valid_settings(self, valid_settings_dict: Dict[str, Any]):
        """Test actual settings from banners.toml"""
        settings = SVGBannerSettings(**valid_settings_dict)
        assert settings.border_radius == 5.0
        assert settings.font_color == "#FFFFFF"
        assert settings.font_family == "Arial, sans-serif"
        assert settings.font_size == 24
        assert settings.height == 200
        assert settings.pattern_opacity == 0.2
        assert settings.pattern_size == 20.0
        assert settings.shadow_blur == 4.0
        assert settings.shadow_dx == 2.0
        assert settings.shadow_dy == 2.0
        assert settings.shadow_opacity == 0.5
        assert settings.shape_opacity == 0.8
        assert settings.subtitle_size == 18
        assert settings.width == 800

    @pytest.mark.parametrize(
        "field,invalid_value,error_type",
        [
            ("pattern_opacity", 1.5, "less_than_equal"),
            ("shadow_opacity", -0.1, "greater_than_equal"),
            ("font_size", 0, "greater_than"),
            ("border_radius", -1.0, "greater_than_equal"),
        ],
    )
    def test_invalid_field_values(
        self,
        valid_settings_dict: Dict[str, Any],
        field: Literal["pattern_opacity"]
        | Literal["shadow_opacity"]
        | Literal["font_size"]
        | Literal["border_radius"],
        invalid_value,
        error_type,
    ):
        valid_settings_dict[field] = invalid_value
        with pytest.raises(ValidationError) as exc_info:
            SVGBannerSettings(**valid_settings_dict)
        assert error_type in str(exc_info.value)

    def test_invalid_font_color(self, valid_settings_dict: Dict[str, Any]):
        valid_settings_dict["font_color"] = "rgb(255,255,255)"  # Invalid format
        with pytest.raises(ValidationError, match="pattern"):
            SVGBannerSettings(**valid_settings_dict)

    def test_invalid_width_height_ratio(self, valid_settings_dict: Dict[str, Any]):
        valid_settings_dict["width"] = 150
        valid_settings_dict["height"] = 200
        with pytest.raises(
            ValidationError, match="Width must be greater than or equal to height"
        ):
            SVGBannerSettings(**valid_settings_dict)


class TestSVGBannerGenerator:
    """Test cases for SVGBannerGenerator"""

    @pytest.fixture
    def mock_gradient_colors(self):
        """Mock gradient colors with a passthrough to allow any valid hex colors"""
        with patch(
            "readmeai.generators.colors.gradients.generate_gradient_colors"
        ) as mock:
            # Don't specify colors, let the actual implementation provide them
            yield mock

    def test_svg_generation_with_real_template(
        self,
        mock_file_handler: MagicMock | AsyncMock,
        mock_gradient_colors: MagicMock | AsyncMock,
        valid_config_dict: Dict[str, Any],
    ):
        """Test SVG generation with the actual template from banners.toml"""
        file_handler_instance = Mock()
        file_handler_instance.read.return_value = valid_config_dict
        mock_file_handler.return_value = file_handler_instance

        generator = SVGBannerGenerator("config/settings/templates/banners.toml")
        svg = generator.generate_svg("readme-ai")

        # Verify SVG structure
        assert 'viewBox="0 0 800 200"' in svg
        assert 'linearGradient id="bg"' in svg
        assert 'pattern id="dots"' in svg
        assert 'filter id="shadow"' in svg

        # Verify gradient color format without checking specific colors
        hex_color_pattern = r"stop-color:#[0-9A-Fa-f]{6};stop-opacity:1"
        gradient_colors = re.findall(hex_color_pattern, svg)
        assert len(gradient_colors) == 3  # Should have exactly 3 gradient stops

        # Verify settings application
        assert 'font-family="Arial, sans-serif"' in svg
        assert 'font-size="24"' in svg
        assert 'fill="#FFFFFF"' in svg
        assert "readme-ai" in svg

    @pytest.mark.parametrize(
        "title",
        [
            "readme-ai",
            "Project with <special> chars",
            "Very " * 10 + "long project name",
            "Project with 数字 and ñ",
            "",  # Empty title
        ],
    )
    def test_title_handling(
        self,
        mock_file_handler: MagicMock | AsyncMock,
        mock_gradient_colors: MagicMock | AsyncMock,
        valid_config_dict: Dict[str, Any],
        title: str,
    ):
        file_handler_instance = Mock()
        file_handler_instance.read.return_value = valid_config_dict
        mock_file_handler.return_value = file_handler_instance

        generator = SVGBannerGenerator("config/settings/templates/banners.toml")
        svg = generator.generate_svg(title)

        assert title in svg
        assert 'text-anchor="middle"' in svg
        assert 'font-weight="bold"' in svg

    def test_missing_config_file(self, mock_file_handler: MagicMock | AsyncMock):
        """Test handling of missing config file"""
        with pytest.raises(FileReadError) as e:
            SVGBannerGenerator("config/settings/templates/missing.toml")
        assert isinstance(e.value, FileReadError)

    def test_calculated_dimensions(
        self,
        mock_file_handler: MagicMock | AsyncMock,
        valid_config_dict: Dict[str, Any],
    ):
        """Test the calculated dimension values used in the SVG"""
        file_handler_instance = Mock()
        file_handler_instance.read.return_value = valid_config_dict
        mock_file_handler.return_value = file_handler_instance

        generator = SVGBannerGenerator("config/settings/templates/banners.toml")
        svg = generator.generate_svg("Test")

        # Verify calculated values are present
        width = valid_config_dict["settings"]["width"]
        height = valid_config_dict["settings"]["height"]

        assert f'cx="{width * 0.08}"' in svg  # width_08
        assert f'cy="{height * 0.25}"' in svg  # height_025
        assert f'r="{height * 0.15}"' in svg  # height_015
        assert f'cx="{width * 0.92}"' in svg  # width_92
        assert f'cy="{height * 0.75}"' in svg  # height_075
        assert f'r="{height * 0.20}"' in svg  # height_02
