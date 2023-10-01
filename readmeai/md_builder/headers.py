"""Builds the README Markdown file for your codebase."""

__package__ = "readmeai"

from pathlib import Path
from typing import List

from pkg_resources import resource_filename

from readmeai.core import factory, logger
from readmeai.core.config import AppConfig, ConfigHelper
from readmeai.md_builder import badges, tables, usage
from readmeai.utils import github, utils

logger = logger.Logger(__name__)


def build(
    badges: str,
    conf: AppConfig,
    helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> None:
    """Builds the README Markdown file for your codebase."""
    readme_sections = insert_contents_and_join(
        badges, conf, helper, packages, summaries
    )
    output_file = "\n".join(readme_sections)
    output_path = Path(conf.paths.output)
    factory.FileHandler().write(output_path, output_file)
    logger.info(f"README file generated at: {output_path}")


def insert_contents_and_join(
    badges: str,
    conf: AppConfig,
    helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> List[str]:
    """Constructs each section of the README file."""
    name = conf.git.name
    repository = conf.git.repository
    user_repo = github.get_user_repository_name(repository)

    if conf.api.offline_mode is False:
        md_tables = tables.create_markdown_tables(conf.md.default, summaries)
        conf.md.tables = tables.create_tables(
            md_tables, conf.md.dropdown, repository, user_repo
        )

    md_usage_guides = usage.create_setup_guide(conf, helper, summaries)

    if badges == "shields":
        badge_icons = get_shields_icons(conf, packages, user_repo)
    else:
        skills_icons = get_skills_icons(conf, packages, repository)
        badge_icons = conf.md.badges_alt.format(
            name.upper(), conf.prompts.slogan, skills_icons
        )
        conf.md.header = "<!---->\n"

    markdown_sections = [
        conf.md.header,
        badge_icons,
        conf.md.toc.format(name),
        conf.md.intro,
        conf.md.tree,
        conf.md.modules,
        conf.md.tables,
        conf.md.setup.format(name, repository, *md_usage_guides),
        conf.md.ending,
    ]
    return markdown_sections


def get_shields_icons(conf: AppConfig, packages: list, user_repo: str):
    badges_path = resource_filename(__package__, f"{conf.paths.badge_icons}")
    badges_dict = factory.FileHandler().read(badges_path)
    shields_icons = conf.md.badges.format(
        badges.get_badges(badges_dict, packages), user_repo
    )
    shields_icons = (
        utils.remove_substring(shields_icons)
        if "invalid" in user_repo.lower()
        else shields_icons
    )
    return shields_icons


def get_skills_icons(conf: AppConfig, packages: list, repository: str) -> str:
    """Determines whether to use shields.io badges or skill icons."""
    skill_icons_path = resource_filename(
        __package__, f"{conf.paths.skill_icons}"
    )
    skill_icons_dict = factory.FileHandler().read(skill_icons_path)
    skill_icons = badges.get_skill_icons(
        skill_icons_dict, packages, repository
    )
    return skill_icons
