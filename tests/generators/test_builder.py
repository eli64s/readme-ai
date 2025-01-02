from pathlib import Path
from typing import Any, Generator
from unittest.mock import patch

import pytest
from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import RepositoryContext
from readmeai.generators.builder import MarkdownBuilder


@pytest.fixture
def mock_theme_manager() -> Generator[Any, None, None]:
    """Mock theme manager with proper parent/subsection handling."""
    with patch("readmeai.generators.emojis.ThemeManager") as mock:
        theme_manager = mock.return_value
        # Return subsection title if provided, otherwise return section title
        theme_manager.apply_theme_to_section.side_effect = (
            lambda section, subsection=None: subsection if subsection else section
        )
        theme_manager.get_themed_toc.return_value = "Themed TOC"
        yield theme_manager


@pytest.fixture
def mock_header_template() -> Generator[Any, None, None]:
    """Mock header template."""
    with patch("readmeai.generators.headers.HeaderTemplate") as mock:
        header_template = mock.return_value
        header_template.render.return_value = "Rendered Header"
        yield header_template


@pytest.fixture
def mock_toc_template() -> Generator[Any, None, None]:
    """Mock navigation template."""
    with patch("readmeai.generators.navigation.NavigationTemplate") as mock:
        toc_template = mock.return_value
        toc_template.render.return_value = "Rendered TOC"
        yield toc_template


@pytest.fixture
def mock_tree_generator() -> Generator[Any, None, None]:
    """Mock tree generator."""
    with patch("readmeai.generators.tree.TreeGenerator") as mock:
        tree_gen = mock.return_value
        tree_gen.generate.return_value = "Generated Tree"
        yield tree_gen


@pytest.fixture
def mock_quickstart_builder() -> Generator[Any, None, None]:
    """Mock quickstart builder."""
    with patch("readmeai.generators.quickstart.QuickStartBuilder") as mock:
        quickstart = mock.return_value
        quickstart.build.return_value = "Quickstart Guide"
        yield quickstart


@pytest.fixture
def markdown_builder(
    mock_config_loader: ConfigLoader,
    mock_repository_context: RepositoryContext,
    tmp_path: Path,
    mock_theme_manager: Any,
    mock_header_template: Any,
    mock_toc_template: Any,
):
    """Create markdown builder with mocked dependencies."""
    builder = MarkdownBuilder(
        config_loader=mock_config_loader,
        repo_context=mock_repository_context,
        file_summaries=[("file.py", "A test file")],
        temp_dir=str(tmp_path),
    )
    return builder


class TestMarkdownBuilder:
    """Test suite for MarkdownBuilder."""

    @pytest.fixture
    def test_builder(
        self,
        mock_config_loader: ConfigLoader,
        mock_repository_context: RepositoryContext,
        tmp_path: Path,
        mock_theme_manager: Any,
        mock_header_template: Any,
        mock_toc_template: Any,
    ):
        """Create a test builder with properly injected mocks."""
        with patch(
            "readmeai.generators.builder.ThemeManager", return_value=mock_theme_manager
        ):
            builder = MarkdownBuilder(
                config_loader=mock_config_loader,
                repo_context=mock_repository_context,
                file_summaries=[("file.py", "A test file")],
                temp_dir=str(tmp_path),
            )
            return builder

    def test_initialization(self, test_builder: MarkdownBuilder):
        """Test builder initialization."""
        assert test_builder.config is not None
        assert test_builder.theme_manager is not None
        assert test_builder.header_template is not None
        assert test_builder.toc_template is not None

    @patch("readmeai.generators.badges.shieldsio")
    def test_build_badges(self, mock_shieldsio, test_builder: MarkdownBuilder):
        """Test badge generation."""
        mock_shieldsio.return_value = ("code metrics", "tech stack")
        code_metrics, tech_stack = test_builder._build_badges()

        assert code_metrics == "code metrics"
        assert tech_stack == "tech stack"
        mock_shieldsio.assert_called_once()
