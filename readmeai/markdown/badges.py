"""Functions for building and formatting the badges in the README.md file."""

from readmeai.config.settings import AppConfig, GitService
from readmeai.core.factory import FileHandler
from readmeai.core.logger import Logger
from readmeai.utils import utils

logger = Logger(__name__)


def badge_template(conf: AppConfig) -> str:
    """Return markdown template for badges"""
    if conf.git.source == GitService.LOCAL.value:
        return conf.md.badges_offline
    else:
        return conf.md.badges_shields


def build_html_badges(svg_icons: dict, dependencies: list) -> str:
    """Returns a list of badges for the project dependencies."""
    badges = [
        svg_icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in svg_icons
    ]
    # Sort badges by hex value (from light to dark color)
    badges.sort(key=lambda b: int(b[1], 16) if b[1] else 0, reverse=True)
    badges = [badge[0] for badge in badges]
    return format_html_badges(badges)


def format_html_badges(badges: list) -> str:
    """Formats the SVG icons into HTML <img src=""> tags."""
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
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}">'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        badge_lines.append(line)

    return "\n\n".join(badge_lines)


def shields_icons(conf: AppConfig, deps: list, full_name: str):
    """
    Generates badges for the README using shields icons, referencing the
    repository - https://github.com/Aveek-Saha/GitHub-Profile-Badges.
    """
    if conf.git.source == GitService.LOCAL.host:
        repo_host = GitService.LOCAL.host
    else:
        repo_host = GitService.extract_name_from_host(conf.git.source)

    resource_path = utils.get_resource_path(
        __package__, conf.files.shields_icons
    )

    md_badge_template = badge_template(conf)
    shields_dict = FileHandler().read(resource_path)
    shields_icons = md_badge_template.format(
        conf.md.align,
        build_html_badges(shields_dict, deps).format(conf.md.badges_style),
        repo_host,
        full_name,
        conf.md.badges_style,
    )
    return (
        utils.remove_substring(shields_icons)
        if "invalid" in full_name.lower()
        else shields_icons
    )


def skill_icons(conf: AppConfig, deps: list) -> str:
    """
    Generates badges for the README using skill icons, from the
    repository - https://github.com/tandpfun/skill-icons.
    """
    resource_path = utils.get_resource_path(
        __package__, conf.files.skill_icons
    )
    skill_icons_dict = FileHandler().read(resource_path)
    skill_icons = [
        icon for icon in skill_icons_dict["icons"]["names"] if icon in deps
    ]
    skill_icons.extend(["md", "github", "git"])
    icon_names = ",".join(skill_icons)
    # per_line = (len(skill_icons) + 2) // 2
    # icon_names = f"{icon_names}"  # &perline={per_line}"
    skill_icons = skill_icons_dict["url"]["base_url"] + icon_names

    if conf.md.badges_style == "skills-light":
        skill_icons = f"{skill_icons}&theme=light"

    return conf.md.badges_skills.format(
        alignment=conf.md.align,
        badges=skill_icons,
        image=conf.md.image,
        repo_name=conf.git.name.upper(),
        slogan=conf.md.slogan,
    )
