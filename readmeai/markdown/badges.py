"""Functions for building and formatting the badges in the README.md file."""

from typing import Dict, Tuple

from readmeai.config.enums import BadgeOptions
from readmeai.config.settings import AppConfig
from readmeai.core.factory import FileHandler
from readmeai.core.utils import get_resource_path
from readmeai.services.git_utils import GitService


def _read_badge_file(file_path: str) -> Dict[str, str]:
    """Reads the badges file and returns the SVG icons."""
    resource_path = get_resource_path(__package__, file_path)
    return FileHandler().read(resource_path)


def build_dependency_badges(
    dependencies: list[str], icons: dict[str, str], style: str
) -> str:
    """Build HTML badges for project dependencies."""
    badges = [
        icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in icons
    ]

    # Sort badges by hex value (from light to dark color)
    badges.sort(key=lambda b: int(b[1], 16) if b[1] else 0, reverse=True)
    badges = [badge[0].format(style) for badge in badges]
    return format_badges(badges)


def build_metadata_badges(config: AppConfig, full_name: str, host: str) -> str:
    """Build metadata badges using shields.io."""
    return config.md.badges_shields.format(
        host=host,
        full_name=full_name,
        badge_style=config.md.badge_style,
        badge_color=config.md.badge_color,
    )


def format_badges(badges: list[str]) -> str:
    """Format SVG badge icons as HTML."""
    len_icons = len(badges)
    if badges is None or len_icons == 0:
        return ""

    badges_per_line = (
        len_icons if len_icons < 9 else (len_icons // 2) + (len_icons % 2)
    )

    lines = []
    for i in range(0, len_icons, badges_per_line):
        line = "\n\t".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}">'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        lines.append(
            f"{line}\n\t<br>"
            if i + badges_per_line < len_icons
            else f"{line}\n"
        )

    return "\n\t".join(lines)


def shields_icons(
    conf: AppConfig, deps: list, full_name: str, git_host: str
) -> Tuple[str, str]:
    """
    Generates badges for the README using shields.io icons, referencing
    the repository - https://github.com/Aveek-Saha/GitHub-Profile-Badges.
    """
    badge_set = _read_badge_file(conf.files.shields_icons)

    metadata_badges = build_metadata_badges(conf, full_name, git_host)

    dependency_badges = build_dependency_badges(
        deps, badge_set, conf.md.badge_style
    )
    dependency_badges = conf.md.badges_dependencies.format(
        align=conf.md.align, badges=dependency_badges
    )

    if (
        conf.md.badge_style == BadgeOptions.DEFAULT.value
        and git_host != GitService.LOCAL
    ):
        return (
            metadata_badges,
            "<!-- default option, no dependency badges. -->\n",
        )

    if git_host == GitService.LOCAL:
        return (
            "<!-- local repository, no metadata badges. -->\n",
            dependency_badges,
        )

    return metadata_badges, dependency_badges


def skill_icons(conf: AppConfig, deps: list) -> str:
    """
    Generates badges for the README using skill icons, from the
    repository - https://github.com/tandpfun/skill-icons.
    """
    deps.extend(["md"])
    icons_dict = _read_badge_file(conf.files.skill_icons)
    icons_list = [
        icon for icon in icons_dict["icons"]["names"] if icon in deps
    ]
    skill_icons = ",".join(icons_list)
    # per_line = (len(skill_icons) + 2) // 2
    # icon_names = f"{icon_names}"  # &perline={per_line}"
    skill_icons = icons_dict["url"]["base_url"] + skill_icons

    if conf.md.badge_style == "skills-light":
        skill_icons = f"{skill_icons}&theme=light"

    conf.md.badges_skills = conf.md.badges_skills.format(skill_icons)
    dependency_badges = conf.md.badges_dependencies.format(
        align=conf.md.align, badges=conf.md.badges_skills
    )
    return dependency_badges
