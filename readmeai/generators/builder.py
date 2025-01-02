"""Generates the content of each section for the README.md document."""

from pathlib import Path
from typing import Dict

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import get_logger
from readmeai.extractors.models import RepositoryContext
from readmeai.generators import badges, tables, tree
from readmeai.generators.emojis import ThemeManager
from readmeai.generators.enums import BadgeStyles
from readmeai.generators.headers import HeaderRegistry, HeaderTemplate
from readmeai.generators.navigation import NavigationTemplate
from readmeai.generators.quickstart import QuickStartBuilder
from readmeai.retrievers.git.providers import GitHost

_logger = get_logger(__name__)


class MarkdownBuilder:
    """
    Generates each section for the README.md document.
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
        self.git = self.config.git
        self.md = self.config.md
        self.theme_map = self.config_loader.themes

        self.repo_url = str(
            self.git.repository
            if self.git.host_domain != GitHost.LOCAL.name.lower()
            else f"../{self.git.name}"
        )
        self.header_registry = HeaderRegistry(self.md.emojis, self.theme_map)
        self.header_template = HeaderTemplate(style=self.md.header_style)
        self.theme_manager = ThemeManager(self.config)
        self.toc_template = NavigationTemplate(
            style=self.md.navigation_style, header_registry=self.header_registry
        )
        self.thematic_break = self.md.thematic_break
        self.themed_headers = self._get_themed_headers()

    def _build_badges(self) -> tuple[str, str]:
        """Generate badge icon set to embed in the README header."""
        if BadgeStyles.SKILLS.value not in self.md.badge_style:
            code_metrics, tech_stack = badges.shieldsio(
                self.config,
                self.deps,
                self.git.full_name,
                self.git.host,
            )
        else:
            code_metrics = self.md.placeholder
            tech_stack = badges.skillicons(self.config, self.deps)
        return code_metrics, tech_stack

    def _build_header(self) -> str:
        """Build the README header with badge icons."""
        code_metrics, tech_stack = self._build_badges()
        header_data = {
            "align": self.md.align,
            "logo": self.md.logo,
            "logo_size": self.md.logo_size,
            "repo_name": self.git.name.upper()
            if self.git.name
            else self.md.placeholder,
            "tagline": self.md.tagline,
            "shields_icons": code_metrics,
            "tech_stack_icons": tech_stack,
            "tech_stack_description": self.md.tech_stack_description,
        }

        return self.header_template.render(header_data)

    def _get_themed_headers(self) -> Dict[str, str]:
        """Get themed versions of all section headers."""
        base_headers = [
            "Table of Contents",
            "Introduction",
            "Overview",
            "Features",
            "Project Structure",
            "Project Index",
            "Getting Started",
            "Prerequisites",
            "Installation",
            "Usage",
            "Testing",
            "Contributing",
            "Roadmap",
            "License",
            "Acknowledgment",
        ]
        headers = {}
        for header in base_headers:
            themed = self.theme_manager.apply_theme_to_section(header)
            headers[header] = themed
            if header.lower() == "acknowledgment":
                headers["Acknowledgments"] = themed
            snake_key = header.lower().replace(" ", "_")
            headers[snake_key] = themed
        return headers

    @property
    def header_and_badges(self) -> str:
        """Generate README header section with badges."""
        return self._build_header()

    @property
    def table_of_contents(self) -> str:
        toc_with_theme = self.theme_manager.get_themed_toc()
        _logger.debug(f"Table of Contents: {toc_with_theme}")
        return self.toc_template.render(toc_with_theme)

    @property
    def tree(self) -> str:
        """Generate the project directory tree structure."""
        project_tree = tree.TreeGenerator(
            repo_name=self.git.name,
            root_dir=self.temp_dir,
            repo_url=self.repo_url,
            max_depth=self.md.tree_max_depth,
        ).generate(self.temp_dir)
        return self.md.directory_structure.format(project_tree)

    @property
    def file_summaries(self) -> str:
        """Generate formatted tables containing file summaries."""
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
    def quickstart_guide(self) -> str:
        """Generate a themed quickstart guide with sections."""
        quickstart = QuickStartBuilder(self.config_loader, self.repo_context)
        content = quickstart.build()
        _logger.info(f"Quickstart (readmeai.generators): {content}")
        for section in [
            "Prerequisites",
            "Installation",
            "Usage",
            "Testing",
        ]:
            themed_header = self.theme_manager.apply_theme_to_section(
                "Getting Started",
                section,
            )
            content = content.replace(f"### {section}", f"### {themed_header}")

        return content

    @property
    def contributing_guide(self) -> str:
        """Generate a themed contributing guide."""
        return self.md.contribute.format(
            host=self.git.host,
            host_domain=self.git.host_domain,
            full_name=self.git.full_name,
            repo_name=self.git.name,
            repo_url=self.repo_url,
        )

    @property
    def license(self) -> str:
        """Generate the license section."""
        return self.md.license.format(self.git.name.capitalize())

    @property
    def acknowledgment(self) -> str:
        """Generate the acknowledgment section."""
        return self.md.acknowledgment

    def build(self) -> str:
        """Assembles each section of the README document in order."""
        sections = [
            # -- HEADER -------------------------------------
            self.md.top_anchor_markup,
            self._build_header(),
            # -- NAVIGATION ---------------------------------
            f"## {self.theme_manager.apply_theme_to_section('Table of Contents')}\n\n{self.table_of_contents}",
            self.thematic_break,
            # -- INTRODUCTION --------------------------------
            f"## {self.theme_manager.apply_theme_to_section('Overview')}\n\n{self.md.overview}\n",
            self.thematic_break,
            # -- FEATURES -----------------------------------
            f"## {self.theme_manager.apply_theme_to_section('Features')}\n\n{self.md.features}\n",
            self.thematic_break,
            # -- PROJECT STRUCTURE -------------------------
            f"## {self.theme_manager.apply_theme_to_section('Project Structure')}\n\n{self.tree}\n",
            f"### {self.theme_manager.apply_theme_to_section('Project Structure', 'Project Index')}\n\n{self.file_summaries}\n",
            self.thematic_break,
            # -- QUICKSTART GUIDE ----------------------------
            f"## {self.theme_manager.apply_theme_to_section('Getting Started')}\n\n{self.quickstart_guide}",
            self.thematic_break,
            # -- ROADMAP ------------------------------------
            f"## {self.theme_manager.apply_theme_to_section('Roadmap')}\n\n{self.md.roadmap}",
            self.thematic_break,
            # -- CONTRIBUTING --------------------------------
            f"## {self.theme_manager.apply_theme_to_section('Contributing')}\n\n{self.contributing_guide}",
            self.thematic_break,
            # -- LICENSE ------------------------------------
            f"## {self.theme_manager.apply_theme_to_section('License')}\n\n{self.license}",
            self.thematic_break,
            # -- ACKNOWLEDGMENTS -----------------------------
            f"## {self.theme_manager.apply_theme_to_section('Acknowledgment')}\n\n{self.acknowledgment}",
            # -- FOOTER -------------------------------------
            self.md.return_to_top_markup,
            self.thematic_break,
        ]
        return "\n".join(sections)
