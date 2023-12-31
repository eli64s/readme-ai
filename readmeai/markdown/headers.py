"""Builds each section of the README Markdown file."""

__package__ = "readmeai"

import re
from typing import List

from readmeai.config.settings import AppConfig, ConfigHelper, GitService
from readmeai.core import factory, logger
from readmeai.markdown import badges, quickstart, tables
from readmeai.services import git_utilities as vcs

logger = logger.Logger(__name__)


def build_readme_md(
    conf: AppConfig,
    helper: ConfigHelper,
    deps: list,
    summaries: tuple,
) -> None:
    """Constructs each section of the README Markdown file."""
    markdown_sections = format_markdown_content(conf, helper, deps, summaries)
    readme_md_file = "\n".join(markdown_sections)
    factory.FileHandler().write(conf.files.output, readme_md_file)


def format_markdown_content(
    conf: AppConfig,
    helper: ConfigHelper,
    deps: list,
    summaries: tuple,
) -> List[str]:
    """Formats the README Markdown file contents for each section."""
    repo_url = conf.git.repository
    user_name, repo_name = vcs.get_remote_full_name(repo_url)
    full_name = f"{user_name}/{repo_name}"

    if conf.git.source == GitService.LOCAL.value:
        repo_path = f"../{repo_name}"
    else:
        repo_path = repo_url

    md_header = conf.md.header.format(
        alignment=conf.md.align,
        image=conf.md.image,
        repo_name=repo_name,
        slogan=conf.md.slogan,
    )
    if "skills" not in conf.md.badges_style:
        md_badges = badges.shields_icons(conf, deps, full_name)
    else:
        md_badges = badges.skill_icons(conf, deps)

    formatted_code_summaries = tables.format_code_summaries(
        conf.md.default,
        summaries,
    )
    md_code_summaries = tables.generate_markdown_tables(
        conf.md.modules_widget, formatted_code_summaries, full_name, repo_url
    )
    md_commands = quickstart.getting_started(conf, helper, deps, summaries)
    md_quick_start = conf.md.getting_started.format(
        repo_name=repo_name,
        repo_url=repo_path,
        install_command=md_commands[0],
        run_command=md_commands[1],
        test_command=md_commands[2],
    )
    md_contribute = conf.md.contribute.format(
        full_name=full_name, repo_name=repo_name
    )
    markdown_sections = [
        md_header,
        md_badges,
        conf.md.toc.format(repo_name),
        conf.md.overview,
        conf.md.features,
        conf.md.tree,
        conf.md.modules,
        md_code_summaries,
        md_quick_start,
        md_contribute,
    ]

    if conf.cli.emojis is False:
        return remove_emojis_from_headers(markdown_sections)

    return markdown_sections


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

    # Replace emojis for markdown lines starting with header symbols or in the ToC
    modified_content = []
    for section in content_list:
        lines = section.split("\n")
        for index, line in enumerate(lines):
            if line.startswith("#") or "Table of Contents" in section:
                lines[index] = emoji_pattern.sub("", line)
        modified_content.append("\n".join(lines))

    return modified_content
