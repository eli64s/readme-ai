"""Logic for generating badges for the README file."""

from pkg_resources import resource_filename

from readmeai.config.settings import AppConfig, GitHost
from readmeai.core import factory, logger
from readmeai.utils import utils

logger = logger.Logger(__name__)


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


def get_badges_md_template(conf: AppConfig) -> str:
    """Return markdown template for badges"""
    if conf.git.source == GitHost.LOCAL.value:
        return conf.md.badges_offline
    else:
        return conf.md.badges


def get_shieldsio_icons(conf: AppConfig, packages: list, full_name: str):
    """Generates the README badges using shields.io badges."""
    md_template = get_badges_md_template(conf)

    badges_path = resource_filename(
        __package__, f"{conf.paths.shieldsio_icons}"
    )

    badges_dict = factory.FileHandler().read(badges_path)

    shieldsio_icons = md_template.format(
        get_badges(badges_dict, packages).format(conf.md.badge_style),
        full_name,
        conf.md.badge_style,
    )
    shieldsio_icons = (
        utils.remove_substring(shieldsio_icons)
        if "invalid" in full_name.lower()
        else shieldsio_icons
    )
    return shieldsio_icons


def get_app_icons(conf: AppConfig, dependencies: list) -> str:
    """Generates the README badges using app iOS style badges."""
    conf.md.header = "<!---->\n"

    app_icons_path = resource_filename(__package__, f"{conf.paths.app_icons}")

    icons_dict = factory.FileHandler().read(app_icons_path)

    filtered_icons = [
        icon for icon in icons_dict["icons"]["names"] if icon in dependencies
    ]
    filtered_icons.extend(["git", "github"])

    icon_names = ",".join(filtered_icons)
    # per_line = (len(filtered_icons) + 2) // 2
    # icon_names = f"{icon_names}"  # &perline={per_line}"

    app_icons = icons_dict["url"]["base_url"] + icon_names
    app_icons = conf.md.badges_alt.format(
        conf.git.name.upper(), conf.prompts.slogan, app_icons
    )

    return app_icons
