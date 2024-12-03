"""Pipeline that builds each markdown section of the README file."""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict, List, Protocol

from readmeai.config.constants import ImageOptions
from readmeai.config.settings import ConfigLoader
from readmeai.generators import tables
from readmeai.generators.badges import SVGBadgeGenerator
from readmeai.generators.emojis import ThemeManager
from readmeai.generators.headers import HeaderTemplate
from readmeai.generators.quickstart import QuickStartBuilder
from readmeai.generators.toc import TocTemplate
from readmeai.generators.tree import TreeGenerator
from readmeai.ingestion.models import RepositoryContext
from readmeai.logger import get_logger
from readmeai.readers.git.providers import GitHost

logger = get_logger(__name__)


class SectionType(Enum):
    """
    Available section types for README generation.
    """

    TOC = "table-of-contents"
    OVERVIEW = "overview"
    FEATURES = "features"
    PROJECT_STRUCTURE = "project-structure"
    PROJECT_INDEX = "project-index"
    GETTING_STARTED = "getting-started"
    PREREQUISITES = "prerequisites"
    INSTALLATION = "installation"
    USAGE = "usage"
    TESTING = "testing"
    ROADMAP = "roadmap"
    CONTRIBUTING = "contributing"
    LICENSE = "license"
    ACKNOWLEDGEMENTS = "acknowledgments"


class SectionBuilder(Protocol):
    """
    Protocol for section builders.
    """

    def build(self) -> str: ...


@dataclass
class MarkdownContext:
    """
    Context for markdown section building.
    """

    settings: ConfigLoader
    repo_context: RepositoryContext
    file_summaries: List[tuple[str, str]]
    temp_dir: Path

    def __post_init__(self):
        self.settings = self.settings
        self.config = self.settings.config
        self.md = self.config.md
        self.git = self.config.git
        self.deps = self.repo_context.dependencies
        self.repo_url = self._get_repo_url()

    def _get_repo_url(self) -> str:
        """Get repository URL based on host."""
        return (
            self.git.repository
            if self.git.host_domain != GitHost.LOCAL.name.lower()
            else f"../{self.git.name}"
        )


@dataclass
class HeaderConfig:
    """
    Configuration for README header template.
    """

    align: str
    image: str
    image_width: str
    placeholder: str
    tagline: str
    badges_tech_stack_text: str


class HeaderBuilder:
    """
    Builds the header section of the README.
    """

    def __init__(self, context: MarkdownContext):
        self.context = context
        self.config = context.config
        self.badge_generator = SVGBadgeGenerator(config=context.config)
        self.header_template = HeaderTemplate(context.md.header_style)

    def build(self) -> str:
        """Generate header with badges."""
        try:
            return self.header_template.render(self._prepare_header_data())
        except Exception as e:
            logger.error(f"Failed to build header: {e}")
            return self._generate_fallback_header()

    def _prepare_header_data(self) -> Dict[str, str]:
        """Prepare header template data with badges."""
        md_shields, md_badges = self._generate_badges()

        return {
            "align": self.context.md.align,
            "image": self.context.md.image,
            "image_width": self.context.md.image_width,
            "repo_name": self._get_repo_name(),
            "tagline": self.context.md.tagline,
            "shields_icons": md_shields,
            "badges_tech_stack_icons": md_badges,
            "badges_tech_stack_text": self.context.md.badges_tech_stack_text,
        }

    def _generate_badges(self) -> tuple[str, str]:
        """Generate appropriate badges based on configuration."""
        return self.badge_generator.generate_badges(
            dependencies=self.context.deps,
            full_name=str(self.context.git.full_name),
            git_host=str(self.context.git.host),
        )

    def _get_repo_name(self) -> str:
        """Get repository name with fallback."""
        return (
            self.context.git.name.upper()
            if self.context.git.name
            else self.context.md.placeholder
        )

    def _generate_fallback_header(self) -> str:
        """Generate minimal header in case of failure."""
        fallback_data = {
            "align": "center",
            "image": ImageOptions.BLUE.value,
            "image_width": "100",
            "repo_name": self._get_repo_name(),
            "tagline": self.config.md.placeholder,
            "shields_icons": self.config.md.placeholder,
            "badges_tech_stack_icons": self.config.md.placeholder,
            "badges_tech_stack_text": "Tech Stack",
        }
        return self.header_template.render(fallback_data)


class ContentBuilder:
    """
    Builds each markdown section of the README file.
    """

    def __init__(self, context: MarkdownContext) -> None:
        self.context = context
        self.theme_manager = ThemeManager(config=context.config)
        self.theme_manager.set_theme(context.md.emojis)
        self.toc_template = TocTemplate(
            emoji_theme=context.md.emojis,
            style=context.md.toc_style,
        )
        self.quickstart_builder = QuickStartBuilder(
            context.settings, context.repo_context
        )

    def build_toc(self) -> str:
        """Builds table of contents template."""
        toc_data = self.theme_manager.generate_toc_data()
        return self.toc_template.render({"sections": toc_data})

    def build_project_structure(self) -> str:
        """Builds project directory tree structure."""
        project_tree = TreeGenerator(
            repo_name=self.context.git.name,
            root_dir=self.context.temp_dir,
            repo_url=self.context.repo_url,
            max_depth=self.context.md.tree_depth,
        ).generate(self.context.temp_dir)
        return self.context.md.tree.format(project_tree)

    def build_file_summaries(self) -> str:
        """Builds expandable markdown table to store the file summaries."""
        formatted_summaries = tables.format_code_summaries(
            self.context.md.placeholder,
            self.context.file_summaries,
        )
        return tables.generate_nested_module_tables(
            formatted_summaries,
            self.context.git.full_name,
            self.context.repo_url,
        )

    def build_contributing(self) -> str:
        """Builds the contributing section."""
        return self.context.md.contribute.format(
            host=self.context.git.host,
            host_domain=self.context.git.host_domain,
            full_name=self.context.git.full_name,
            repo_name=self.context.git.name,
            repo_url=self.context.repo_url,
        )


class MarkdownBuilder:
    """
    Formats and builds the complete README markdown file.
    """

    def __init__(
        self,
        settings: ConfigLoader,
        repo_context: RepositoryContext,
        file_summaries: List[tuple[str, str]],
        temp_dir: str,
    ) -> None:
        self.context = MarkdownContext(
            settings=settings,
            repo_context=repo_context,
            file_summaries=file_summaries,
            temp_dir=Path(temp_dir),
        )
        self.header_builder = HeaderBuilder(self.context)
        self.content_builder = ContentBuilder(self.context)
        self.markdown_template = settings.config.document_templates["standard"]

    def build(self) -> str:
        """Build all markdown sections."""
        try:
            headers = self.content_builder.theme_manager.get_headers()
            sections = self._build_section_headers(headers)
            content = self._build_section_content()
            template_vars = {**sections, **content}
        except Exception as e:
            logger.error(f"Error building README: {e!r}")
            template_vars = self._build_fallback_content()
        return self.markdown_template.format(**template_vars)

    def _build_fallback_content(self) -> Dict[str, str]:
        """Build fallback content in case of failure."""
        return {
            "HEADER": self.header_builder._generate_fallback_header(),
            "TOC_CONTENT": self.content_builder.build_toc(),
            "OVERVIEW_CONTENT": self.context.md.overview,
            "FEATURES_CONTENT": self.context.md.features,
            "PROJECT_STRUCTURE_CONTENT": self.content_builder.build_project_structure(),
            "PROJECT_INDEX_CONTENT": self.content_builder.build_file_summaries(),
            "PREREQUISITES_CONTENT": self.context.md.placeholder,
            "INSTALLATION_CONTENT": self.context.md.placeholder,
            "USAGE_CONTENT": self.context.md.placeholder,
            "TESTING_CONTENT": self.context.md.placeholder,
            "ROADMAP_CONTENT": self.context.md.roadmap,
            "CONTRIBUTING_CONTENT": self.context.md.contribute,
            "LICENSE_CONTENT": self.context.md.license,
            "ACKNOWLEDGEMENTS_CONTENT": self.context.md.acknowledgements,
        }

    def _build_section_headers(
        self, headers: Dict[str, str]
    ) -> Dict[str, str]:
        """Build section headers mapping."""
        return {
            f"{section.name}_HEADER": headers[section.value]
            for section in SectionType
        }

    def _build_section_content(self) -> Dict[str, str]:
        """Build section content mapping."""
        quickstart = self.content_builder.quickstart_builder

        return {
            "HEADER": self.header_builder.build(),
            "TOC_CONTENT": self.content_builder.build_toc(),
            "OVERVIEW_CONTENT": self.context.md.overview,
            "FEATURES_CONTENT": self.context.md.features,
            "PROJECT_STRUCTURE_CONTENT": self.content_builder.build_project_structure(),
            "PROJECT_INDEX_CONTENT": self.content_builder.build_file_summaries(),
            "PREREQUISITES_CONTENT": quickstart.build_prerequisites(),
            "INSTALLATION_CONTENT": quickstart.build_installation(),
            "USAGE_CONTENT": self.context.repo_context.quickstart.usage_commands,
            "TESTING_CONTENT": self.context.repo_context.quickstart.test_commands,
            "ROADMAP_CONTENT": self.context.md.roadmap,
            "CONTRIBUTING_CONTENT": self.content_builder.build_contributing(),
            "LICENSE_CONTENT": self.context.md.license.format(
                self.context.git.name.capitalize()
            ),
            "ACKNOWLEDGEMENTS_CONTENT": self.context.md.acknowledgements,
        }
