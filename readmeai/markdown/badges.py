"""Functions for building and formatting the badges in the README.md file."""

from typing import Dict, Tuple

from readmeai.config.settings import AppConfig, BadgeOptions
from readmeai.core.factory import FileHandler
from readmeai.core.utils import get_resource_path
from readmeai.services.git_utilities import GitService


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


def build_metadata_badges(
    config: AppConfig, host: str, repository: str
) -> str:
    """Build metadata badges using shields.io."""
    return config.md.badges_shields.format(
        git_host=host,
        full_name=repository,
        badges_style=config.md.badges_style,
    )


def format_badges(badges: list[str]) -> str:
    """Format SVG badge icons as HTML."""
    lines = []
    badges_per_line = len(badges) if len(badges) < 9 else (len(badges) % 2)

    if badges_per_line == 0:
        return ""

    for i in range(0, len(badges), badges_per_line):
        line = "\n\t".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}">'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        lines.append(line)

    return """\n\t<br>\n\t""".join(lines)


def shields_icons(
    conf: AppConfig, deps: list, full_name: str
) -> Tuple[str, str]:
    """
    Generates badges for the README using shields.io icons, referencing
    the repository - https://github.com/Aveek-Saha/GitHub-Profile-Badges.
    """
    badge_set = _read_badge_file(conf.files.shields_icons)
    git_host = GitService.extract_name_from_host(conf.git.source)

    metadata_badges = build_metadata_badges(conf, git_host, full_name)
    dependency_badges = build_dependency_badges(
        deps, badge_set, conf.md.badges_style
    )
    dependency_badges = conf.md.badges_dependencies.format(
        alignment=conf.md.align, badges=dependency_badges
    )

    if (
        conf.md.badges_style == BadgeOptions.DEFAULT.value
        and git_host != GitService.LOCAL.host
    ):
        return (
            metadata_badges,
            "<!-- default option, no dependency badges. -->\n",
        )

    if git_host == GitService.LOCAL.host:
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

    if conf.md.badges_style == "skills-light":
        skill_icons = f"{skill_icons}&theme=light"

    conf.md.badges_skills = conf.md.badges_skills.format(skill_icons)

    return conf.md.badges_skills
