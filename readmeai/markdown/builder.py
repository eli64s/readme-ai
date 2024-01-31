"""Builds each section of the README Markdown file."""

__package__ = "readmeai"

from pathlib import Path
from typing import List

from readmeai.config.enums import BadgeOptions, GitService
from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.markdown import badges, tables, tree
from readmeai.markdown.quickstart import setup_guide
from readmeai.markdown.utilities import remove_emojis


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
        self.temp_dir = Path(temp_dir)
        self.md = self.conf.md
        self.full_name = self.conf.git.full_name
        self.host = self.conf.git.host
        self.host_domain = self.conf.git.host_domain
        self.repo_name = self.conf.git.name
        self.repo_url = self.conf.git.repository
        if self.host_domain == GitService.LOCAL:
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
        summaries = tables.format_code_summaries(
            self.md.default,
            self.summaries,
        )
        md_summaries = tables.generate_markdown_tables(
            self.md.modules_widget,
            summaries,
            self.full_name,
            self.repo_url,
        )
        return md_summaries

    @property
    def md_tree(self) -> str:
        """Generates the README directory tree structure."""
        md_tree = tree.TreeGenerator(
            repo_name=self.repo_name,
            root_dir=self.temp_dir,
            repo_url=self.repo_url,
            max_depth=self.md.tree_depth,
        ).tree()
        return self.md.tree.format(md_tree)

    @property
    def md_quickstart(self) -> str:
        """Generates the README Getting Started section."""
        project_setup = setup_guide(self.conf, self.helper, self.summaries)
        return self.md.quickstart.format(
            repo_name=self.repo_name,
            repo_url=self.repo_url,
            requirements=project_setup.requirements,
            install_command=project_setup.install_command,
            run_command=project_setup.run_command,
            test_command=project_setup.test_command,
        )

    @property
    def md_contributing(self) -> str:
        """Generates the README Contributing section."""
        return self.md.contribute.format(
            host=self.host_domain,
            full_name=self.full_name,
            repo_name=self.repo_name.capitalize(),
            repo_url=self.repo_url,
        )

    def build(self) -> str:
        """Builds the README Markdown file."""
        md_contents = [
            self.md_header,
            self.md.toc.format(repo_name=self.repo_name),
            self.md.overview,
            self.md.features,
            self.md_tree,
            self.md.modules,
            self.md_summaries,
            self.md_quickstart,
            self.md_contributing,
        ]

        if self.conf.md.emojis is False:
            md_contents = remove_emojis(md_contents)

        return "\n".join(md_contents)


def build_readme_md(
    conf: AppConfig,
    helper: ConfigHelper,
    dependencies: list,
    summaries: tuple,
    temp_dir: str,
) -> None:
    """Builds the README Markdown file."""
    builder = ReadmeBuilder(conf, helper, dependencies, summaries, temp_dir)
    markdown_sections = builder.build()
    return markdown_sections
