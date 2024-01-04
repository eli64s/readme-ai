"""Builds each section of the README Markdown file."""

__package__ = "readmeai"

import re
from pathlib import Path
from typing import List

from readmeai.config.settings import (
    AppConfig,
    BadgeOptions,
    ConfigHelper,
    GitService,
)
from readmeai.core import factory
from readmeai.markdown import badges, tables
from readmeai.markdown.quickstart import getting_started
from readmeai.services.git_utilities import get_remote_full_name


def build_readme_md(
    conf: AppConfig,
    helper: ConfigHelper,
    deps: list,
    summaries: tuple,
) -> None:
    """Constructs each section of the README Markdown file."""
    readme_md_contents = format_readme_md(conf, helper, deps, summaries)
    readme_md_file = "\n".join(readme_md_contents)
    readme_path = Path(conf.files.output)
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    factory.FileHandler().write(readme_path, readme_md_file)


def format_readme_md(
    conf: AppConfig,
    helper: ConfigHelper,
    deps: list,
    summaries: tuple,
) -> List[str]:
    """Formats the README markdown contents."""
    repo_url = conf.git.repository
    user_name, repo_name = get_remote_full_name(repo_url)
    full_name = f"{user_name}/{repo_name}"
    if conf.git.source == GitService.LOCAL.value:
        repo_url = f"../{repo_name}"

    if BadgeOptions.SKILLS.value not in conf.md.badges_style:
        md_shields, md_badges = badges.shields_icons(conf, deps, full_name)
    else:
        md_shields = "<!-- Shields.io badges not used with skill icons. -->"
        md_badges = badges.skill_icons(conf, deps)

    md_header = conf.md.header.format(
        alignment=conf.md.align,
        image=conf.md.image,
        repo_name=repo_name.upper(),
        slogan=conf.md.slogan,
        badges_shields=md_shields,
        badges=md_badges,
    )

    formatted_code_summaries = tables.format_code_summaries(
        conf.md.default,
        summaries,
    )
    md_code_summaries = tables.generate_markdown_tables(
        conf.md.modules_widget, formatted_code_summaries, full_name, repo_url
    )

    project_setup = getting_started(conf, helper, summaries)
    md_project_setup = conf.md.getting_started.format(
        repo_name=repo_name,
        repo_url=repo_url,
        language_name=project_setup.top_language_full_name,
        install_command=project_setup.install_command,
        run_command=project_setup.run_command,
        test_command=project_setup.test_command,
    )

    readme_md_sections = [
        md_header,
        conf.md.toc.format(repo_name),
        conf.md.overview,
        conf.md.features,
        conf.md.tree,
        conf.md.modules,
        md_code_summaries,
        md_project_setup,
        conf.md.contribute.format(full_name=full_name, repo_name=repo_name),
    ]

    if conf.cli.emojis is False:
        return remove_emojis_from_headers(readme_md_sections)

    return readme_md_sections


def remove_emojis_from_headers(content_list: List[str]) -> List[str]:
    """Removes emojis from headers and ToC."""
    emoji_pattern = re.compile(
        pattern="["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # flags (iOS)
        "]+",
        flags=re.UNICODE,
    )

    # Replace emojis for markdown lines starting with header symbols or ToC
    modified_content = []

    for section in content_list:
        lines = section.split("\n")
        for index, line in enumerate(lines):
            if (
                line.startswith("#")
                or "Table of Contents" in section
                or "Quick Links" in section
            ):
                lines[index] = emoji_pattern.sub("", line)
        modified_content.append("\n".join(lines))

    return modified_content
