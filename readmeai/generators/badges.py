"""Generates badge icon sets that are embedded in the README file header."""

import colorsys
from typing import Dict, List, Set, Tuple

from readmeai.config.constants import BadgeStyleOptions
from readmeai.config.settings import Settings
from readmeai.logger import get_logger
from readmeai.readers.git.providers import GitHost
from readmeai.utils.file_handler import FileHandler

logger = get_logger(__name__)

ERROR_COMMENT = "<!-- Error occurred while generating badge sets. -->"
LOCAL_COMMENT = (
    "<!-- Shields.io metric badges are not supported for local projects. -->"
)
METRICS_COMMENT = "<!-- No badge-style selected. Shields.io metric badges included by default. -->"
SKILLICONS_COMMENT = "<!-- Skillicons.dev tech stack badge set. Shields.io metric badges excluded. -->"


class SVGBadgeGenerator:
    """
    Builds badge icon sets to embed in the README file header.
    """

    def __init__(self, config: Settings) -> None:
        self.config = config
        self.file_handler = FileHandler()
        self._seen_badges: Set[str] = set()
        self._shieldsio_cache: Dict[str, str] = self._shieldsio()
        self._skillicons_cache: Dict[str, str] = self._skillicons()

    def _shieldsio(self) -> Dict[str, str]:
        """Lazy load shields.io badge icons with fallback."""
        try:
            file_path = self.config.paths.data.shieldsio
            return self.file_handler.read(file_path)
        except Exception as e:
            logger.warning(f"Failed to load shields.io badges: {e!r}")
            return {}

    def _skillicons(self) -> Dict[str, str]:
        """Lazy load skillicons.dev badge icons with fallback."""
        try:
            file_path = self.config.paths.data.skillicons
            return self.file_handler.read(file_path)
        except Exception as e:
            logger.warning(f"Failed to load skillicons.dev badges: {e!r}")
            return {}

    def generate_badges(
        self,
        dependencies: List[str],
        full_name: str,
        git_host: str,
    ) -> Tuple[str, str]:
        """Build the badge icon sets for the README file header."""
        dependencies = list(set(dependencies))

        try:
            if self.config.md.badge_style in (
                BadgeStyleOptions.SKILLS,
                BadgeStyleOptions.SKILLS_LIGHT,
            ):
                return self._get_skillicons(
                    config=self.config,
                    dependencies=dependencies,
                    full_name=full_name,
                    git_host=git_host,
                )

            if git_host == GitHost.LOCAL.name:
                return LOCAL_COMMENT, self._build_tech_stack_badge_set(
                    dependencies
                )

            return (
                self._build_metric_badge_set(full_name, git_host),
                self._build_tech_stack_badge_set(dependencies),
            )
        except Exception as e:
            logger.error(f"Badge generation failed: {e}")
            return ERROR_COMMENT, get_placeholder_badge("network")

    def _build_metric_badge_set(self, full_name: str, host: str) -> str:
        """Builds the shields.io badge set for the repository metrics."""
        try:
            return self.config.md.shieldsio_icons.format(
                host=host,
                full_name=full_name,
                badge_color=self.config.md.badge_color,
                badge_style=self.config.md.badge_style,
            ).strip()
        except Exception as e:
            logger.warning(f"Error building shields.io metric badges: {e!r}")
            return self.config.md.shieldsio_icons.format(
                host=host,
                full_name=full_name,
                badge_color=self.config.md.badge_color,
                badge_style=self.config.md.badge_style,
            ).strip()

    def _build_tech_stack_badge_set(self, dependencies: List[str]) -> str:
        """Build HTML code blocks to structure badge sets."""
        try:
            # Reset seen badges for new generation
            self._seen_badges.clear()

            badges = self._get_unique_badges(dependencies)
            sorted_badges = self._sort_badges_by_rainbow(badges)

            formatted_badges = self._format_badges(sorted_badges)
            return self.config.md.badges_tech_stack.format(
                align=self.config.md.align,
                badges_tech_stack_icons=formatted_badges,
            ).strip()
        except Exception as e:
            logger.warning(f"Error building tech stack badge set: {e}")
            return METRICS_COMMENT

    def _get_unique_badges(
        self, dependencies: List[str]
    ) -> List[Tuple[str, str]]:
        """Get unique badges for dependencies, avoiding duplicates."""
        unique_badges = []
        seen_deps = set()

        for dep in dependencies:
            dep_lower = str(dep).lower()
            if (
                dep_lower not in seen_deps
                and dep_lower in self._shieldsio_cache
            ):
                badge_data = self._shieldsio_cache[dep_lower]
                if (
                    isinstance(badge_data, (list, tuple))
                    and len(badge_data) >= 2
                ):
                    unique_badges.append((badge_data[0], badge_data[1]))
                    seen_deps.add(dep_lower)

        return unique_badges

    def _format_badges(self, badges: List[str]) -> str:
        """Format SVG badge icons using HTML code blocks."""
        if not badges:
            return ""

        total = len(badges)
        badges_per_line = total if total < 9 else (total // 2) + (total % 2)

        lines = []
        for i in range(0, total, badges_per_line):
            line_badges = badges[i : i + badges_per_line]
            line = "\n\t".join(
                f'<img src="{badge}" alt="{self._get_badge_alt(badge)}">'
                for badge in line_badges
            )
            needs_break = i + badges_per_line < total
            lines.append(f"{line}\n\t<br>" if needs_break else f"{line}\n")

        return "\n\t".join(lines)

    def _sort_badges_by_rainbow(
        self, badges: List[Tuple[str, str]]
    ) -> List[str]:
        """Sort badges by color in rainbow order."""

        def get_hue(color: str) -> float:
            """Get hue value from color for rainbow sorting."""
            try:
                h, _, _ = self._hex_to_hls(color)
                return h
            except Exception:
                return 0.0

        sorted_badges = sorted(
            badges, key=lambda x: (get_hue(x[1]), x[0].lower())
        )

        return [
            badge[0].format(self.config.md.badge_style)
            for badge in sorted_badges
            if badge and badge[0]
        ]

    def _get_skillicons(
        self,
        config: Settings,
        dependencies: List[str],
        full_name: str,
        git_host: str,
    ) -> Tuple[str, str]:
        """Generate tech stack badge set using skillicons.dev icons."""
        try:
            if "github_actions" in dependencies:
                dependencies.extend(["githubactions"])

            deps_with_md = list({*dependencies, "md"})

            icons = {
                icon
                for icon in self._skillicons_cache.get("icons", {}).get(
                    "names", []
                )
                if icon in deps_with_md
            }

            if not icons:
                return ERROR_COMMENT, get_placeholder_badge("general")

            base_url = self._skillicons_cache.get("url", {}).get(
                "base_url", ""
            )
            formatted_icons = f"{base_url}{','.join(sorted(icons))}"

            if config.md.badge_style == BadgeStyleOptions.SKILLS_LIGHT:
                formatted_icons += "&theme=light"

            centered_html = f"""<a href="https://skillicons.dev">\n\t\t<img src="{formatted_icons}" alt="Tech Stack">\n\t</a>"""

            return SKILLICONS_COMMENT, centered_html

        except Exception as e:
            logger.error(f"Failed to generate skillicons badge set: {e!r}")
            return ERROR_COMMENT, get_placeholder_badge("network")

    @staticmethod
    def _hex_to_hls(hex_color: str) -> Tuple[float, float, float]:
        """Convert hex color to HLS colorspace."""
        try:
            hex_color = hex_color.lstrip("#")
            rgb = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))
            return colorsys.rgb_to_hls(
                rgb[0] / 255.0, rgb[1] / 255.0, rgb[2] / 255.0
            )
        except (ValueError, AttributeError):
            return (0.0, 0.0, 0.0)

    def _get_tech_stack_badges(self, dependencies: List[str]) -> List[str]:
        """Retrieve all relevant badge icons for a given project."""
        if not dependencies:
            return [get_placeholder_badge("general")]

        try:
            badges = [
                self.shieldsio.get(
                    dep.lower(), get_placeholder_badge("parsing")
                )
                for dep in dependencies
                if dep.lower() in self.shieldsio
            ]
            badges = [
                b if b else get_placeholder_badge("loading") for b in badges
            ]

            if not badges:
                return [get_placeholder_badge("general")]

            sorted_badges = self._sort_badges(badges)
            return [
                badge[0].format(self.config.md.badge_style)
                for badge in sorted_badges
                if badge and badge[0]
            ]
        except Exception:
            return [get_placeholder_badge("network")]

    @staticmethod
    def _get_badge_alt(badge: str) -> str:
        """Extract alt text from the badge icon URL."""
        try:
            return badge.split("/badge/")[1].split("-")[0]
        except (IndexError, AttributeError):
            return "badge"

    def _sort_badges(self, badges: list) -> List[Tuple[str, str]]:
        """Sort badge set to be ordered by color and name."""
        try:
            badges = [(badge[0], str(badge[1])) for badge in badges if badge]
            badges = list(set(badges))

            return sorted(
                badges,
                key=lambda b: (*self._hex_to_hls(b[1]), b[0])
                if b and b[1]
                else (float("inf"), 0, 0, ""),
            )
        except Exception as e:
            logger.warning(f"Error sorting badge set: {e!r}")
            return []


def get_placeholder_badge(error_type: str = "general") -> str:
    """Generate a visually consistent placeholder badge for error states."""
    error_messages = {
        "loading": "Badge%20Loading",
        "parsing": "Badge%20Parse%20Error",
        "network": "Network%20Error",
        "general": "Badge%20Unavailable",
    }
    error_colors = {
        "loading": "blue",
        "parsing": "orange",
        "network": "red",
        "general": "lightgrey",
    }
    message = error_messages.get(error_type, error_messages["general"])
    color = error_colors.get(error_type, error_colors["general"])
    return (
        f"https://img.shields.io"
        f"/badge/{message}-{color}"
        "?style=flat-square"
        "&logo=shields.io"
        "&logoColor=white"
    )
