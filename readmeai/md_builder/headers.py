"""Builds the README Markdown file for your codebase."""

__package__ = "readmeai"

from pathlib import Path
from typing import List

from readmeai.core import factory, logger
from readmeai.core.config import AppConfig, ConfigHelper
from readmeai.md_builder import badges, setup_guides, tables
from readmeai.utils import git

logger = logger.Logger(__name__)


def build_readme_md(
    badges: str,
    conf: AppConfig,
    helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> None:
    """Constructs each section of the README Markdown file."""
    all_readme_sections = format_readme_md_contents(
        badges, conf, helper, packages, summaries
    )
    output_file = "\n".join(all_readme_sections)
    output_path = Path(conf.paths.output)
    factory.FileHandler().write(output_path, output_file)
    logger.info(f"README file generated at: {output_path}")


def format_readme_md_contents(
    badges_style: str,
    conf: AppConfig,
    helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> List[str]:
    """Formats the README Markdown file contents for each section."""
    repo_name = conf.git.name
    repository = conf.git.repository
    username, _ = git.get_user_repository_name(repository)
    user_repo = f"{username}/{repo_name}"

    if conf.api.offline_mode is False:
        md_tables = tables.create_markdown_tables(
            conf.md.default,
            summaries,
        )
        conf.md.tables = tables.create_tables(
            md_tables, conf.md.dropdown, repository, user_repo
        )

    if badges_style in ["default", "shields"]:
        badge_icons = badges.get_shieldsio_icons(conf, packages, user_repo)
    else:
        badge_icons = badges.get_square_icons(conf, packages)

    md_setup_guide = setup_guides.create_setup_guide(conf, helper, summaries)

    markdown_sections = [
        conf.md.header,
        badge_icons,
        conf.md.toc.format(repo_name),
        conf.md.intro,
        conf.md.tree,
        conf.md.modules,
        conf.md.tables,
        conf.md.setup.format(repo_name, repository, *md_setup_guide),
        conf.md.ending,
    ]
    return markdown_sections
