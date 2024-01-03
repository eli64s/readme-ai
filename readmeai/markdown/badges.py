"""Functions for building and formatting the badges in the README.md file."""

from readmeai.config.settings import AppConfig, BadgeOptions, GitService
from readmeai.core.factory import FileHandler
from readmeai.utils import utils


def build_html_badges(
    dependencies: list,
    svg_icons: dict,
    style: str,
) -> str:
    """Returns a list of badges for the project dependencies."""
    badges = [
        svg_icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in svg_icons
    ]
    # Sort badges by hex value (from light to dark color)
    badges.sort(key=lambda b: int(b[1], 16) if b[1] else 0, reverse=True)
    badges = [badge[0].format(style) for badge in badges]
    return format_html_badges(badges)


def format_html_badges(badges: list) -> str:
    """Formats the SVG icons into HTML <img src=""> tags."""
    badge_lines = []
    total_badges = len(badges)
    if total_badges < 9:
        badges_per_line = total_badges
    else:
        badges_per_line = total_badges // 2 + (total_badges % 2)

    if badges_per_line == 0:
        return ""

    for i in range(0, total_badges, badges_per_line):
        line = "\n\t".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}">'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        badge_lines.append(line)

    return "\n\t<br>\n\t".join(badge_lines)


def shields_icons(conf: AppConfig, deps: list, full_name: str):
    """
    Generates badges for the README using shields icons, referencing the
    repository - https://github.com/Aveek-Saha/GitHub-Profile-Badges.
    """
    if conf.git.source == GitService.LOCAL.host:
        git_host = GitService.LOCAL.host
    else:
        git_host = GitService.extract_name_from_host(conf.git.source)

    metadata_badges = conf.md.badges_shields.format(
        git_host=git_host,
        full_name=full_name,
        badges_style=conf.md.badges_style,
    )

    if conf.md.badges_style == BadgeOptions.STANDARD.value:
        return metadata_badges

    badge_set = _read_badge_file(conf.files.shields_icons)
    dependency_badges = build_html_badges(
        deps,
        badge_set,
        conf.md.badges_style,
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


def _read_badge_file(file_path: str) -> dict:
    """Reads the badges file and returns the SVG icons."""
    resource_path = utils.get_resource_path(__package__, file_path)
    return FileHandler().read(resource_path)
