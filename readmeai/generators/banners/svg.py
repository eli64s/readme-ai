from pathlib import Path
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator
from readmeai.generators.colors.gradients import generate_gradient_colors
from readmeai.utilities.file_handler import FileHandler


class SVGBannerSettings(BaseModel):
    """
    Pydantic model for SVG configuration settings.
    """

    border_radius: float = Field(
        ..., ge=0, description="Border radius for the SVG container."
    )
    font_color: Annotated[
        str,
        StringConstraints(
            pattern=r"^#[0-9A-Fa-f]{6}$",
        ),
    ]
    font_family: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=1,
        ),
    ]
    font_size: int = Field(..., gt=0, description="Font size for the title.")
    height: int = Field(..., gt=0, description="Height of the SVG banner.")
    pattern_opacity: float = Field(
        ..., ge=0, le=1, description="Opacity of the pattern (0-1)."
    )
    pattern_size: float = Field(
        ..., gt=0, description="Pattern size for background elements."
    )
    shadow_blur: float = Field(..., description="Blur radius for the shadow.")
    shadow_dx: float = Field(..., description="Horizontal shadow offset.")
    shadow_dy: float = Field(..., description="Vertical shadow offset.")
    shadow_opacity: float = Field(
        ..., ge=0, le=1, description="Opacity of the shadow (0-1)."
    )
    shape_opacity: float = Field(
        ..., ge=0, le=1, description="Opacity for additional shapes."
    )
    subtitle_size: int = Field(..., gt=0, description="Font size for the subtitle.")
    width: int = Field(..., gt=0, description="Width of the SVG banner.")

    model_config = ConfigDict(strict=True, extra="forbid", validate_assignment=True)

    @model_validator(mode="after")
    def validate_sizes(self) -> "SVGBannerSettings":
        """
        Ensures that the width is greater than or equal to the height.
        """
        if self.width < self.height:
            raise ValueError("Width must be greater than or equal to height.")
        return self


class SVGBannerConfig(BaseModel):
    """
    Pydantic model for the overall SVG configuration.
    """

    banners: dict[str, dict[str, str]] = Field(
        ..., description="Banners configuration."
    )
    settings: SVGBannerSettings

    model_config = ConfigDict(strict=True, extra="forbid")


class SVGBannerGenerator:
    """
    Generate SVG banners for the README.md file.
    """

    def __init__(self, config_file: str) -> None:
        """Validate the configuration and load the SVG template."""
        file_handler = FileHandler()
        cwd = Path(__file__).parent.parent.parent
        raw_config = file_handler.read(cwd / config_file)
        self.config = SVGBannerConfig.model_validate(raw_config)
        self.svg_template = self.config.banners["svg"]["template"]

    def generate_svg(self, title: str) -> str:
        """Generate an SVG banner for the project name and tagline."""
        c = self.config.settings
        colors = generate_gradient_colors()
        svg_content = self.svg_template.format(
            width=c.width,
            height=c.height,
            color1=colors[0],
            color2=colors[1],
            color3=colors[2],
            shadow_dx=c.shadow_dx,
            shadow_dy=c.shadow_dy,
            shadow_blur=c.shadow_blur,
            shadow_opacity=c.shadow_opacity,
            pattern_size=c.pattern_size,
            pattern_opacity=c.pattern_opacity,
            border_radius=c.border_radius,
            width_08=c.width * 0.08,
            height_025=c.height * 0.25,
            height_015=c.height * 0.15,
            width_92=c.width * 0.92,
            height_075=c.height * 0.75,
            height_02=c.height * 0.2,
            width_2=c.width / 2,
            height_0125=c.height * 0.125,
            width_2_plus_height_025=c.width / 2 + c.height * 0.25,
            width_2_minus_height_025=c.width / 2 - c.height * 0.25,
            height_0375=c.height * 0.375,
            font_family=c.font_family,
            font_size=c.font_size,
            font_color=c.font_color,
            subtitle_size=c.subtitle_size,
            shape_opacity=c.shape_opacity,
            height_2=c.height / 2,
            height_0625=c.height * 0.75,
            title=title,
        )
        return svg_content
