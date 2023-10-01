"""Generate the badges to display in the README file."""

from readmeai.core import logger

logger = logger.Logger(__name__)


def get_skill_icons(icons: dict, dependencies: list, repository: str) -> str:
    """Create HTML block of square logo icons for each dependency."""
    filtered_icons = [
        icon for icon in icons["icons"]["names"] if icon in dependencies
    ]
    filtered_icons.extend(["git", "github"])
    icon_names = ",".join(filtered_icons)
    # per_line = (len(filtered_icons) + 2) // 2
    # icon_names = f"{icon_names}"  # &perline={per_line}"
    return icons["url"]["base_url"] + icon_names


def get_badges(svg_icons: dict, dependencies: list) -> str:
    """Returns a list of badges for the project dependencies."""
    badges = [
        svg_icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in svg_icons
    ]
    # Sort badges by hex value (from light to dark color)
    badges.sort(key=lambda b: int(b[1], 16) if b[1] else 0, reverse=True)
    badges = [badge[0] for badge in badges]
    return format_badges(badges)


def format_badges(badges: list) -> str:
    """Formats the SVG icons into Markdown image tags."""
    badge_lines = []
    total_badges = len(badges)
    if total_badges < 8:
        badges_per_line = total_badges
    else:
        badges_per_line = total_badges // 2 + (total_badges % 2)

    if badges_per_line == 0:
        return ""

    for i in range(0, total_badges, badges_per_line):
        line = "\n".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}" />'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        badge_lines.append(line)

    return "\n\n".join(badge_lines)
