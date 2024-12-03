import colorsys
from typing import Any, Dict, List, Tuple

from readmeai.config.badges.models import (
    BadgeCache,
    BadgeGroup,
    BadgeMetric,
    BadgeProvider,
    BadgeSettings,
    BadgeTheme,
    BadgeType,
    TechBadge,
)
from readmeai.logger import get_logger
from readmeai.utils.file_handler import FileHandler

logger = get_logger(__name__)


class BadgeGenerator:
    """Enhanced badge generator with caching and multiple providers."""

    def __init__(self, settings: BadgeSettings):
        self.settings = settings
        self.file_handler = FileHandler()
        self.cache = BadgeCache(ttl=settings.cache_ttl)
        self._load_badge_definitions()

    def _load_badge_definitions(self) -> None:
        """Load badge definitions from configuration."""
        try:
            # Load shields.io badges
            if BadgeProvider.SHIELDS_IO in self.settings.providers:
                shields_data = self.file_handler.read(
                    "data/svg/shieldsio.json"
                )
                self._process_shields_badges(shields_data)

            # Load skillicons badges
            if BadgeProvider.SKILL_ICONS in self.settings.providers:
                skill_data = self.file_handler.read("data/svg/skillicons.json")
                self._process_skill_badges(skill_data)

        except Exception as e:
            logger.error(f"Error loading badge definitions: {e}")

    def _process_shields_badges(self, data: Dict[str, Any]) -> None:
        """Process shields.io badge definitions."""
        try:
            for category, badges in data.items():
                group = BadgeGroup(
                    name=category, type=BadgeType.TECH, badges=[]
                )

                for name, badge_data in badges.items():
                    if (
                        isinstance(badge_data, (list, tuple))
                        and len(badge_data) >= 2
                    ):
                        badge = TechBadge(
                            name=name,
                            svg_url=badge_data[0],
                            color=badge_data[1],
                            category=category,
                        )
                        group.badges.append(badge)

                self.settings.tech_groups.append(group)

        except Exception as e:
            logger.error(f"Error processing shields.io badges: {e}")

    def _process_skill_badges(self, data: Dict[str, Any]) -> None:
        """Process skillicons badge definitions."""
        try:
            icons = data.get("icons", {}).get("names", [])
            base_url = data.get("url", {}).get("base_url", "")

            group = BadgeGroup(name="Skills", type=BadgeType.TECH, badges=[])

            for icon in icons:
                badge = TechBadge(
                    name=icon,
                    svg_url=f"{base_url}{icon}",
                    color="",  # Skillicons use their own colors
                    category="Skills",
                )
                group.badges.append(badge)

            self.settings.tech_groups.append(group)

        except Exception as e:
            logger.error(f"Error processing skillicons badges: {e}")

    def generate_badges(
        self, dependencies: List[str], repo_info: Dict[str, Any]
    ) -> str:
        """Generate badge HTML with caching."""
        cache_key = f"{','.join(sorted(dependencies))}-{hash(frozenset(repo_info.items()))}"

        if self.settings.enable_cache:
            if cached := self.cache.get(cache_key):
                return cached

        try:
            # Generate metric badges
            metric_badges = self._generate_metric_badges(repo_info)

            # Generate tech stack badges
            tech_badges = self._generate_tech_badges(dependencies)

            # Combine and layout badges
            badges = []
            if metric_badges:
                badges.extend(metric_badges)
            if tech_badges:
                badges.extend(tech_badges)

            if not badges:
                return self._get_placeholder_badge("general")

            # Sort badges if using rainbow theme
            if self.settings.theme == BadgeTheme.RAINBOW:
                badges = self._sort_badges_by_rainbow(badges)

            # Format according to layout
            html = self.settings.layout.format_badges(badges)

            if self.settings.enable_cache:
                self.cache.set(cache_key, html)

            return html

        except Exception as e:
            logger.error(f"Error generating badges: {e}")
            return self._get_placeholder_badge("error")

    def _generate_metric_badges(self, repo_info: Dict[str, Any]) -> List[str]:
        """Generate repository metric badges."""
        badges = []

        for group in self.settings.metric_groups:
            for badge in group.badges:
                if isinstance(badge, BadgeMetric):
                    try:
                        url = badge.format(**repo_info)
                        html = f'<img src="{url}" alt="{badge.name}" />'
                        badges.append(html)
                    except Exception as e:
                        logger.warning(
                            f"Error generating metric badge {badge.name}: {e}"
                        )

        return badges

    def _generate_tech_badges(self, dependencies: List[str]) -> List[str]:
        """Generate technology stack badges."""
        # Find matching badges
        matched_badges = self.settings.find_badges(
            dependencies, badge_type=BadgeType.TECH
        )

        # Convert to HTML
        return [
            badge.html
            for badge in matched_badges
            if isinstance(badge, TechBadge)
        ]

    @staticmethod
    def _hex_to_hls(hex_color: str) -> Tuple[float, float, float]:
        """Convert hex color to HLS colorspace."""
        try:
            hex_color = hex_color.lstrip("#")
            rgb = tuple(
                int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4)
            )
            return colorsys.rgb_to_hls(*rgb)
        except (ValueError, AttributeError):
            return (0.0, 0.0, 0.0)

    def _sort_badges_by_rainbow(self, badges: List[str]) -> List[str]:
        """Sort badges by color in rainbow order."""

        def get_color(badge: str) -> str:
            """Extract color from badge URL."""
            try:
                parts = badge.split("badge/")[1].split("/")[0]
                return parts.split("-")[-1]
            except (IndexError, AttributeError):
                return ""

        def get_hue(badge: str) -> float:
            """Get hue value for sorting."""
            color = get_color(badge)
            h, _, _ = self._hex_to_hls(color)
            return h

        return sorted(badges, key=get_hue)

    @staticmethod
    def _get_placeholder_badge(error_type: str = "general") -> str:
        """Generate placeholder badge for errors."""
        messages = {
            "error": "Badge Generation Error",
            "network": "Network Error",
            "general": "Badges Unavailable",
        }
        colors = {"error": "red", "network": "orange", "general": "lightgrey"}

        message = messages.get(error_type, messages["general"])
        color = colors.get(error_type, colors["general"])

        url = (
            f"https://img.shields.io/badge/{message}-{color}"
            "?style=flat-square&logo=shields.io"
        )

        return f'<img src="{url}" alt="{message}" />'
