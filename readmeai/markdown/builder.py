"""Builds each section of the README Markdown file."""

__package__ = "readmeai"

import re
from pathlib import Path
from typing import List

from readmeai.config.enums import BadgeOptions
from readmeai.config.settings import AppConfig, ConfigHelper, GitService
from readmeai.core import factory
from readmeai.markdown import badges, tables, tree
from readmeai.markdown.quickstart import setup_guide


class ReadmeBuilder:
    """Builds each section of the README Markdown file."""

    def __init__(
        self,
        conf: AppConfig,
        helper: ConfigHelper,
        dependencies: List[str],
        summaries: tuple,
        temp_dir: str,
    ):
        """Initializes the ReadmeBuilder class."""
        self.conf = conf
        self.helper = helper
        self.deps = dependencies
        self.summaries = summaries
        self.temp_dir = temp_dir
        self.md = self.conf.md
        self.host = self.conf.git.host
        self.full_name = self.conf.git.full_name
        self.repo_name = self.conf.git.name
        self.repo_url = self.conf.git.repository
        if self.host == GitService.LOCAL:
            self.repo_url = f"../{self.repo_name}"

    @property
    def md_header(self) -> str:
        """Generates the README header section."""
        if BadgeOptions.SKILLS.value not in self.md.badge_style:
            md_shields, md_badges = badges.shields_icons(
                self.conf, self.deps, self.full_name, self.host
            )
        else:
            md_shields = (
                "<!-- Shields.io badges not used with skill icons. -->"
            )
            md_badges = badges.skill_icons(self.conf, self.deps)

        return self.md.header.format(
            align=self.md.align,
            image=self.md.image,
            repo_name=self.repo_name.upper(),
            slogan=self.md.slogan,
            badges_shields=md_shields,
            badges=md_badges,
        )

    @property
    def md_summaries(self) -> str:
        """Generates the README code summaries section."""
        formatted_summaries = tables.format_code_summaries(
            self.md.default,
            self.summaries,
        )
        md_summaries = tables.generate_markdown_tables(
            self.md.modules_widget,
            formatted_summaries,
            self.full_name,
            self.repo_url,
        )
        return md_summaries

    @property
    def md_tree(self) -> str:
        """Generates the README directory tree structure."""
        tree_generator = tree.TreeGenerator(
            conf_helper=self.helper,
            repo_name=self.repo_name,
            repo_url=self.repo_url,
            root_dir=self.temp_dir,
        )
        tree_structure = tree_generator.run()
        return self.md.tree.format(tree_structure)

    @property
    def md_quickstart(self) -> str:
        """Generates the README Getting Started section."""
        project_setup = setup_guide(self.conf, self.helper, self.summaries)
        md_project_setup = self.md.quickstart.format(
            repo_name=self.repo_name,
            repo_url=self.repo_url,
            requirements=project_setup.requirements,
            install_command=project_setup.install_command,
            run_command=project_setup.run_command,
            test_command=project_setup.test_command,
        )
        return md_project_setup

    def build(self) -> str:
        """Builds the README Markdown file."""
        readme_md_sections = [
            self.md_header,
            self.md.toc.format(repo_name=self.repo_name),
            self.md.overview,
            self.md.features,
            self.md_tree,
            self.md.modules,
            self.md_summaries,
            self.md_quickstart,
            self.md.contribute.format(
                host=self.host,
                full_name=self.full_name,
                repo_name=self.repo_name.capitalize(),
                repo_url=self.repo_url,
            ),
        ]

        if self.conf.cli.emojis is False:
            readme_md_sections = self.remove_emojis(readme_md_sections)

        return "\n".join(readme_md_sections)

    @staticmethod
    def remove_emojis(content_list: List[str]) -> List[str]:
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


def build_readme_md(
    conf: AppConfig,
    helper: ConfigHelper,
    dependencies: list,
    summaries: tuple,
    temp_dir: str,
) -> None:
    """Builds the README Markdown file."""
    builder = ReadmeBuilder(conf, helper, dependencies, summaries, temp_dir)
    readme_md_file = builder.build()
    readme_path = Path(conf.files.output)
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    factory.FileHandler().write(readme_path, readme_md_file)
