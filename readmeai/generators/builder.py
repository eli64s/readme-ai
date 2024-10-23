from pathlib import Path

from readmeai.config.settings import BadgeStyleOptions, ConfigLoader
from readmeai.generators import badges, emojis, tables, tree
from readmeai.ingestion.models import RepositoryContext
from readmeai.readers.git.providers import GitHost
from readmeai.templates.header import HeaderTemplate
from readmeai.templates.quickstart import QuickStartBuilder
from readmeai.templates.table_of_contents import TocTemplate


class MarkdownBuilder:
    """
    Builds each section of the README Markdown file.
    """

    def __init__(
        self,
        config_loader: ConfigLoader,
        repo_context: RepositoryContext,
        file_summaries: list[tuple[str, str]],
        temp_dir: str,
    ):
        self.config_loader = config_loader
        self.config = config_loader.config
        self.deps = repo_context.dependencies
        self.repo_context = repo_context
        self.summaries = file_summaries
        self.temp_dir = Path(temp_dir)
        self.md = self.config.md
        self.git = self.config.git
        self.repo_url = (
            self.git.repository
            if self.git.host_domain != GitHost.LOCAL.name.lower()
            else f"../{self.git.name}"
        )
        self.header_template = HeaderTemplate(self.md.header_style)
        self.toc_template = TocTemplate(self.md.toc_style)

    @property
    def header_and_badges(self) -> str:
        """Generates the README header section."""
        if BadgeStyleOptions.SKILLS.value not in self.md.badge_style:
            md_shields, md_badges = badges.shieldsio_icons(
                self.config,
                self.deps,
                str(self.git.full_name),
                str(self.git.host),
            )
        else:
            md_shields = (
                "<!-- Shields.io badges disabled, using skill icons. -->"
            )
            md_badges = badges.skill_icons(self.config, self.deps)

        header_data = {
            "align": self.md.align,
            "image": self.md.image,
            "image_width": self.md.image_width,
            "repo_name": self.git.name.upper()
            if self.git.name
            else self.md.placeholder,
            "slogan": self.md.slogan,
            "shields_icons": md_shields,
            "badges_tech_stack": md_badges,
            "badges_tech_stack_text": self.md.badges_tech_stack_text,
        }
        return self.header_template.render(header_data)

    @property
    def table_of_contents(self) -> str:
        """Generates the README Table of Contents section."""
        headings = {
            "sections": [
                {"title": "📍 Overview"},
                {"title": "👾 Features"},
                {
                    "title": "📁 Project Structure",
                    "subsections": [
                        {"title": "📂 Project Index"},
                    ],
                },
                {
                    "title": "🚀 Getting Started",
                    "subsections": [
                        {"title": "☑️ Prerequisites"},
                        {"title": "⚙️ Installation"},
                        {"title": "🤖 Usage"},
                        {"title": "🧪 Testing"},
                    ],
                },
                {"title": "📌 Project Roadmap"},
                {"title": "🔰 Contributing"},
                {"title": "🎗 License"},
                {"title": "🙌 Acknowledgments"},
            ],
        }
        return self.toc_template.render(headings)

    @property
    def file_summaries(self) -> str:
        """Generates markdown tables that store repository module summaries."""
        formatted_summaries = tables.format_code_summaries(
            self.md.placeholder,
            self.summaries,
        )
        return tables.generate_nested_module_tables(
            formatted_summaries,
            self.git.full_name,
            self.repo_url,
        )

    @property
    def tree(self) -> str:
        """Generates the README directory tree structure."""
        project_tree = tree.TreeGenerator(
            repo_name=self.git.name,
            root_dir=self.temp_dir,
            repo_url=self.repo_url,
            max_depth=self.md.tree_depth,
        ).generate(self.temp_dir)
        return self.md.tree.format(project_tree)

    @property
    def quickstart_guide(self) -> str:
        """Generates the README Getting Started section."""
        return QuickStartBuilder(self.config_loader, self.repo_context).build()

    @property
    def contributing_guide(self) -> str:
        """Generates the README Contributing section."""
        return self.md.contribute.format(
            host=self.git.host,
            host_domain=self.git.host_domain,
            full_name=self.git.full_name,
            repo_name=self.git.name,
            repo_url=self.repo_url,
        )

    def build(self) -> str:
        """Builds each section of the README.md file."""
        readme_md_contents = [
            self.header_and_badges,
            self.table_of_contents,
            self.md.overview,
            self.md.features,
            self.tree,
            self.md.project_index,
            self.file_summaries,
            self.quickstart_guide,
            self.contributing_guide,
        ]

        if self.config.md.emojis is False:
            readme_md_contents = emojis.remove_emojis(readme_md_contents)

        return "\n".join(readme_md_contents)
