from __future__ import annotations

from functools import cached_property
from typing import Literal, Tuple, Union

from pydantic import (
    AnyHttpUrl,
    BaseModel,
    ConfigDict,
    Field,
    FilePath,
    PositiveInt,
    computed_field,
)
from pydantic_extra_types.color import Color

from readmeai.config.constants import (
    BadgeStyleOptions,
    HeaderStyleOptions,
    ImageOptions,
    TocStyleOptions,
)


class BadgeSettings(BaseModel):
    """
    Badge icon and style settings.
    """

    color: Color = Field(default_factory=lambda: Color("blue"))
    style: BadgeStyleOptions = Field(
        default=BadgeStyleOptions.DEFAULT,
    )
    shields_io: str = ""
    skill_icons: str = ""
    tech_stack_icons: str = "{badges_tech_stack}"
    tech_stack_text: str = "<em>Tech Stack</em>"

    model_config = ConfigDict(
        frozen=True,
        use_enum_values=True,
    )

    @computed_field
    def hex_color(self) -> str:
        """Validate user input for color (hex or color name)."""
        try:
            return self.color.as_hex(format="long").lstrip("#")
        except ValueError:
            return Color("blue").as_hex(format="long").lstrip("#")


class HeaderSettings(BaseModel):
    """
    Header configuration settings.
    """

    align: Literal["left", "center", "right"] = "center"
    style: HeaderStyleOptions = Field(default=HeaderStyleOptions.CLASSIC)

    image: Union[AnyHttpUrl, FilePath, str] = Field(
        default=ImageOptions.BLUE,
        description="Project logo image",
    )
    image_width: str = Field(
        default="20%",
        description="Image width percentage",
    )

    model_config = ConfigDict(
        frozen=True,
        use_enum_values=True,
    )


class ContentSettings(BaseModel):
    """
    Content section settings.
    """

    overview: str = "❯ INSERT-OVERVIEW"
    features: str = "❯ INSERT-FEATURES"
    tagline: str = "❯ INSERT-TAGLINE"
    quickstart: str = ""
    contribute: str = ""
    project_index: str = ""
    tables: str = "❯ INSERT-TABLES"

    model_config = ConfigDict(frozen=True)


class StyleSettings(BaseModel):
    """
    Style and formatting settings.
    """

    emojis: bool = Field(
        default=False,
        description="Enable emoji prefixes",
    )
    placeholder: str = Field(
        default="<code>❯ REPLACE-ME</code>",
        description="Default placeholder text",
    )
    toc_style: TocStyleOptions = Field(
        default=TocStyleOptions.BULLET,
        description="Table of contents style",
    )

    model_config = ConfigDict(
        frozen=True,
        use_enum_values=True,
    )


class TreeSettings(BaseModel):
    """
    Project directory tree settings.
    """

    content: str = ""
    depth: PositiveInt = Field(
        default=2,
        ge=1,
        le=5,
        description="Maximum tree depth",
    )

    model_config = ConfigDict(frozen=True)


class MarkdownSettings(BaseModel):
    """
    Markdown configuration for README generation.
    """

    badges: BadgeSettings = Field(default_factory=BadgeSettings)
    header: HeaderSettings = Field(default_factory=HeaderSettings)
    content: ContentSettings = Field(default_factory=ContentSettings)
    style: StyleSettings = Field(default_factory=StyleSettings)
    tree: TreeSettings = Field(default_factory=TreeSettings)

    model_config = ConfigDict(
        frozen=True,
        arbitrary_types_allowed=True,
    )

    @computed_field
    def alignment(self) -> str:
        """Get content alignment."""
        return self.header.align

    @cached_property
    def has_emoji_headers(self) -> bool:
        """Check if emoji headers are enabled."""
        return self.style.emojis

    def get_section_content(self, section: str) -> str:
        """Get content for a specific section."""
        return getattr(self.content, section, self.style.placeholder)

    def get_badge_style(self) -> Tuple[str, str]:
        """Get badge color and style."""
        return self.badges.hex_color, self.badges.style

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
        validate_assignment=True,
        validate_default=True,
    )


# # Usage Example:
# if __name__ == "__main__":
#     settings = MarkdownSettings()

#     # Access settings in a clean, organized way
#     badge_color, badge_style = settings.get_badge_style()
#     overview_content = settings.get_section_content("overview")

#     print(f"Badge color: {badge_color}\n")
#     print(f"Badge style: {badge_style}\n")
#     print(f"Overview content: {overview_content}\n")

#     # Use computed fields
#     alignment = settings.alignment
#     uses_emojis = settings.has_emoji_headers

#     # Access nested settings directly
#     image_path = settings.header.image
#     tree_depth = settings.tree.depth

#     print(f"Alignment: {alignment}\n")
#     print(f"Uses emojis: {uses_emojis}\n")
#     print(f"Image path: {image_path}\n")
#     print(f"Tree depth: {tree_depth}\n")
