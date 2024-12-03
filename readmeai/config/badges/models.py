from enum import Enum
from typing import Dict, List, Optional, Set, Union

from pydantic import BaseModel, Field, computed_field
from pydantic_extra_types.color import Color


class BadgeProvider(str, Enum):
    """Supported badge providers."""

    SHIELDS_IO = "shields.io"
    SKILL_ICONS = "skillicons.dev"
    CUSTOM = "custom"


class BadgeType(str, Enum):
    """Types of badges."""

    METRIC = "metric"  # Repository metrics (stars, forks, etc.)
    TECH = "tech"  # Technology stack badges
    STATUS = "status"  # Build status, coverage, etc.
    SOCIAL = "social"  # Social links
    CUSTOM = "custom"  # Custom badges


class BadgeTheme(str, Enum):
    """Badge color themes."""

    RAINBOW = "rainbow"  # Sort by rainbow colors
    MONOCHROME = "mono"  # Single color variation
    BRAND = "brand"  # Use brand colors
    CUSTOM = "custom"  # Custom color scheme


class BadgeMetric(BaseModel):
    """Definition of a metric badge."""

    name: str
    icon: str
    color: str
    prefix: Optional[str] = None
    suffix: Optional[str] = None
    url_template: str

    def format(self, **kwargs) -> str:
        """Format badge URL with provided values."""
        try:
            return self.url_template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing required value for badge: {e}")


class TechBadge(BaseModel):
    """Definition of a technology badge."""

    name: str
    svg_url: str
    color: str
    category: Optional[str] = None
    aliases: Set[str] = Field(default_factory=set)

    @computed_field
    def html(self) -> str:
        """Generate HTML for badge."""
        return f'<img src="{self.svg_url}" alt="{self.name}" />'


class BadgeGroup(BaseModel):
    """Group of related badges."""

    name: str
    type: BadgeType
    badges: List[Union[BadgeMetric, TechBadge]]
    description: Optional[str] = None

    def filter_badges(
        self, terms: List[str]
    ) -> List[Union[BadgeMetric, TechBadge]]:
        """Filter badges by search terms."""
        terms = {term.lower() for term in terms}
        return [
            badge
            for badge in self.badges
            if any(
                term in badge.name.lower()
                or (
                    isinstance(badge, TechBadge)
                    and any(term in alias.lower() for alias in badge.aliases)
                )
                for term in terms
            )
        ]


class BadgeLayout(BaseModel):
    """Badge layout configuration."""

    max_per_line: int = 8
    spacing: str = "\t"
    new_line: bool = True
    center: bool = True

    def format_badges(self, badges: List[str]) -> str:
        """Format badges according to layout."""
        if not badges:
            return ""

        total = len(badges)
        badges_per_line = min(total, self.max_per_line)

        lines = []
        for i in range(0, total, badges_per_line):
            line_badges = badges[i : i + badges_per_line]
            line = self.spacing.join(line_badges)
            if self.new_line and i + badges_per_line < total:
                line += "\n"
            lines.append(line)

        content = "\n".join(lines)
        if self.center:
            content = f'<div align="center">\n{content}\n</div>'

        return content


class BadgeSettings(BaseModel):
    """Enhanced badge settings."""

    # Style configuration
    color: Color = Field(default_factory=lambda: Color("blue"))
    style: BadgeType = Field(default=BadgeType.TECH)
    theme: BadgeTheme = Field(default=BadgeTheme.RAINBOW)
    layout: BadgeLayout = Field(default_factory=BadgeLayout)

    # Provider configuration
    providers: List[BadgeProvider] = Field(default=[BadgeProvider.SHIELDS_IO])

    # Content configuration
    metric_groups: List[BadgeGroup] = Field(default_factory=list)
    tech_groups: List[BadgeGroup] = Field(default_factory=list)
    custom_groups: List[BadgeGroup] = Field(default_factory=list)

    # Cache configuration
    enable_cache: bool = True
    cache_ttl: int = 3600  # 1 hour

    @computed_field
    def hex_color(self) -> str:
        """Get validated hex color."""
        try:
            return self.color.as_hex(format="long").lstrip("#")
        except ValueError:
            return Color("blue").as_hex(format="long").lstrip("#")

    def get_badges_by_type(self, badge_type: BadgeType) -> List[BadgeGroup]:
        """Get badge groups by type."""
        return {
            BadgeType.METRIC: self.metric_groups,
            BadgeType.TECH: self.tech_groups,
            BadgeType.CUSTOM: self.custom_groups,
        }.get(badge_type, [])

    def find_badges(
        self, terms: List[str], badge_type: Optional[BadgeType] = None
    ) -> List[Union[BadgeMetric, TechBadge]]:
        """Find badges matching search terms."""
        groups = (
            self.get_badges_by_type(badge_type)
            if badge_type
            else self.metric_groups + self.tech_groups + self.custom_groups
        )

        matches = []
        for group in groups:
            matches.extend(group.filter_badges(terms))
        return matches


class BadgeCache(BaseModel):
    """Cache for badge generation."""

    content: Dict[str, str] = Field(default_factory=dict)
    timestamps: Dict[str, float] = Field(default_factory=dict)
    ttl: int = 3600  # 1 hour

    def get(self, key: str) -> Optional[str]:
        """Get cached content if valid."""
        import time

        if key not in self.content:
            return None

        timestamp = self.timestamps.get(key, 0)
        if time.time() - timestamp > self.ttl:
            del self.content[key]
            del self.timestamps[key]
            return None

        return self.content[key]

    def set(self, key: str, value: str) -> None:
        """Cache content with timestamp."""
        import time

        self.content[key] = value
        self.timestamps[key] = time.time()
