"""Methods to build SVG badges for the README using shields.io icons."""

from typing import Sequence

from readmeai.config.settings import Settings
from readmeai.generators.colors.converters import hex_to_hls
from readmeai.generators.enums import BadgeStyles
from readmeai.retrievers.git.providers import GitHost
from readmeai.utilities.file_handler import FileHandler
from readmeai.utilities.resource_manager import build_resource_path

_comment = "<!-- default option, no dependency badges. -->\n"
_package = "readmeai"
_submodule = "assets/badges"


def build_code_metrics(
    config: Settings,
    full_name: str,
    host: str,
) -> str:
    """Build metadata badges using shields.io."""
    return config.md.shieldsio.format(
        host=host,
        full_name=full_name,
        badge_color=config.md.badge_color,
        badge_style=config.md.badge_style,
    )


def build_tech_stack(
    dependencies: list[str],
    icons: dict[str, str],
    style: str,
) -> str:
    """Build HTML badges for project dependencies."""
    badges = [
        icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in icons
    ]
    badges = sort_badges(badges)
    badges = [badge[0].format(style) for badge in badges]
    return format_badges(badges)


def format_badges(badges: list[str]) -> str:
    """Format SVG badge icons as HTML."""
    total = len(badges)
    if badges is None or total == 0:
        return ""

    badges_per_line = total if total < 9 else (total // 2) + (total % 2)

    lines = []
    for i in range(0, total, badges_per_line):
        line = "\n".join(
            [
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}">'
                for badge in badges[i : i + badges_per_line]
            ],
        )
        lines.append(
            f"{line}\n<br>" if i + badges_per_line < total else f"{line}\n",
        )

    return "\n".join(lines)


def sort_badges(badges: list[tuple[str, str]]) -> Sequence[tuple[str, str]]:
    """Sorts badges by color and then by name."""
    badges = [(badge[0], str(badge[1])) for badge in badges]
    badges = list(set(badges))
    return sorted(
        badges,
        key=lambda b: (*hex_to_hls(b[1]), b[0]) if b[1] else (float("inf"), 0, 0, ""),
    )


def shieldsio(
    conf: Settings,
    dependencies: list,
    full_name: str,
    git_host: str,
) -> tuple[str, str]:
    """Generates badges for the README using shields.io icons."""
    icons_path = build_resource_path(
        conf.files.shieldsio,
        _package,
        _submodule,
    )
    icons_dict = FileHandler().read(icons_path)

    default_icons = build_code_metrics(conf, full_name, git_host)

    tech_stack_icons = build_tech_stack(
        dependencies,
        icons_dict,
        conf.md.badge_style,
    )
    tech_stack_icons = conf.md.tech_stack_icons.format(
        align=conf.md.align,
        tech_stack_icons=tech_stack_icons,
    )

    if (
        conf.md.badge_style == BadgeStyles.DEFAULT.value
        and git_host != GitHost.LOCAL.name
    ):
        conf.md.tech_stack_description = _comment
        return (
            default_icons,
            _comment,
        )

    if git_host == GitHost.LOCAL.name:
        return (
            "<!-- local repository, no metadata badges. -->",
            tech_stack_icons,
        )

    return default_icons, tech_stack_icons


def skillicons(conf: Settings, dependencies: list) -> str:
    """Build tech stack icon set using skillicons."""
    dependencies.extend(["md"])

    icons_path = build_resource_path(
        conf.files.skillicons,
        _package,
        _submodule,
    )
    icons_dict = FileHandler().read(icons_path)

    icons = [icon for icon in icons_dict["icons"]["names"] if icon in dependencies]

    formatted_icons = icons_dict["url"]["base_url"] + ",".join(icons)

    if conf.md.badge_style == "skills-light":
        formatted_icons = f"{formatted_icons}&theme=light"

    conf.md.skillicons = conf.md.skillicons.format(formatted_icons)

    return conf.md.tech_stack_icons.format(
        align=conf.md.align,
        tech_stack_icons=conf.md.skillicons,
    )
