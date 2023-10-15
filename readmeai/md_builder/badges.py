"""Generate the style of badges for the README file."""

from pkg_resources import resource_filename

from readmeai.core import config, factory, logger
from readmeai.utils import utils

logger = logger.Logger(__name__)


def get_shieldsio_icons(
    conf: config.AppConfig, packages: list, user_repo: str
):
    """Generates the README badges using shields.io badges."""
    badges_path = resource_filename(
        __package__, f"{conf.paths.shieldsio_icons}"
    )
    badges_dict = factory.FileHandler().read(badges_path)
    shieldsio_icons = conf.md.badges.format(
        get_badges(badges_dict, packages).format(conf.md.badges_style),
        user_repo,
        conf.md.badges_style,
    )
    shieldsio_icons = (
        utils.remove_substring(shieldsio_icons)
        if "invalid" in user_repo.lower()
        else shieldsio_icons
    )
    return shieldsio_icons


def get_square_icons(conf: config.AppConfig, dependencies: list) -> str:
    """Generates the README badges using square iOS style badges."""
    conf.md.header = "<!---->\n"
    square_icons_path = resource_filename(
        __package__, f"{conf.paths.square_icons}"
    )
    icons_dict = factory.FileHandler().read(square_icons_path)
    filtered_icons = [
        icon for icon in icons_dict["icons"]["names"] if icon in dependencies
    ]
    filtered_icons.extend(["git", "github"])
    icon_names = ",".join(filtered_icons)
    # per_line = (len(filtered_icons) + 2) // 2
    # icon_names = f"{icon_names}"  # &perline={per_line}"
    square_icons = icons_dict["url"]["base_url"] + icon_names
    square_icons = conf.md.badges_alt.format(
        conf.git.name.upper(), conf.prompts.slogan, square_icons
    )
    return square_icons


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
