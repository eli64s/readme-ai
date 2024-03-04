"""Builds each section of the README Markdown file."""

__package__ = "readmeai"

from pathlib import Path
from typing import List

from readmeai.cli.options import BadgeOptions
from readmeai.config.settings import ConfigLoader
from readmeai.generators import badges, tables, tree, utils
from readmeai.generators.quickstart import get_setup_data
from readmeai.services.git import GitHost


class MarkdownBuilder:
    """Builds each section of the README Markdown file."""

    def __init__(
        self,
        config_loader: ConfigLoader,
        dependencies: List[str],
        summaries: tuple,
        temp_dir: str,
    ):
        """Initializes the MarkdownBuilder class."""
        self.deps = dependencies
        self.summaries = summaries
        self.temp_dir = Path(temp_dir)
        self.config = config_loader.config
        self.config_loader = config_loader
        self.md = self.config.md
        self.git = self.config.git
        self.repo_url = (
            self.git.repository
            if self.git.host_domain != GitHost.LOCAL.name.lower()
            else f"../{self.git.name}"
        )

    @property
    def md_header(self) -> str:
        """Generates the README header section."""
        if BadgeOptions.SKILLS.value not in self.md.badge_style:
            md_shields, md_badges = badges.shields_icons(
                self.config, self.deps, self.git.full_name, self.git.host
            )
        else:
            md_shields = (
                "<!-- Shields.io badges not used with skill icons. -->"
            )
            md_badges = badges.skill_icons(self.config, self.deps)

        return self.md.header.format(
            alignment=self.md.alignment,
            image=self.md.image,
            width=self.md.width,
            repo_name=self.git.name.upper(),
            slogan=self.md.slogan,
            shields_icons=md_shields,
            badge_icons=md_badges,
        )

    @property
    def md_summaries(self) -> str:
        """Generates the README code summaries section."""
        summaries = tables.format_code_summaries(
            self.md.placeholder,
            self.summaries,
        )
        md_summaries = tables.generate_markdown_tables(
            self.md.modules_widget,
            summaries,
            self.git.full_name,
            self.repo_url,
        )
        return md_summaries

    @property
    def md_tree(self) -> str:
        """Generates the README directory tree structure."""
        md_tree = tree.TreeGenerator(
            repo_name=self.git.name,
            root_dir=self.temp_dir,
            repo_url=self.repo_url,
            max_depth=self.md.tree_depth,
        ).tree()
        return self.md.tree.format(md_tree)

    @property
    def md_quickstart(self) -> str:
        """Generates the README Getting Started section."""
        setup_data = get_setup_data(self.config_loader, self.summaries)
        return self.md.quickstart.format(
            repo_name=self.git.name,
            repo_url=self.repo_url,
            install_command=setup_data.install_command,
            run_command=setup_data.run_command,
            test_command=setup_data.test_command,
            system_requirements=setup_data.prerequisites,
        )

    @property
    def md_contributing(self) -> str:
        """Generates the README Contributing section."""
        return self.md.contribute.format(
            host=self.git.host,
            host_domain=self.git.host_domain,
            full_name=self.git.full_name,
            repo_name=self.git.name,
            repo_url=self.repo_url,
        )

    def build(self) -> str:
        """Builds the README Markdown file."""
        md_contents = [
            self.md_header,
            self.md.toc.format(repo_name=self.git.name),
            self.md.overview,
            self.md.features,
            self.md_tree,
            self.md.modules,
            self.md_summaries,
            self.md_quickstart,
            self.md_contributing,
        ]

        if self.config.md.emojis is False:
            md_contents = utils.remove_emojis(md_contents)

        return "\n".join(md_contents)
