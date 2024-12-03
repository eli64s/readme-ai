from pathlib import Path
from unittest.mock import patch

import pytest

from readmeai.config.settings import Settings
from readmeai.generators.builder import MarkdownBuilder
from readmeai.ingestion.models import RepositoryContext


@pytest.fixture
def markdown_builder(
    config_fixture: Settings,
    repository_context_fixture: RepositoryContext,
    file_summaries_fixture: list[tuple[str, str]],
    tmp_path: Path,
):
    return MarkdownBuilder(
        config=config_fixture,
        repo_context=repository_context_fixture,
        file_summaries=file_summaries_fixture,
        temp_dir=str(tmp_path),
    )


def test_build(markdown_builder: MarkdownBuilder):
    with (
        patch.object(
            MarkdownBuilder,
            "header_and_badges",
            new="Header and Badges",
        ),
        patch.object(
            MarkdownBuilder,
            "table_of_contents",
            new="Table of Contents",
        ),
        patch.object(
            MarkdownBuilder,
            "file_summaries",
            new="File Summaries",
        ),
        patch.object(MarkdownBuilder, "tree", new="Tree"),
        patch.object(
            MarkdownBuilder,
            "quickstart_guide",
            new="Quickstart Guide",
        ),
        patch.object(
            MarkdownBuilder,
            "contributing_guide",
            new="Contributing Guide",
        ),
        patch.object(markdown_builder.config.md, "overview", new="Overview"),
        patch.object(markdown_builder.config.md, "features", new="Features"),
        patch.object(
            markdown_builder.config.md, "project_index", new="Project Index"
        ),
        patch.object(markdown_builder.config.md, "emojis", new=False),
        patch(
            "readmeai.generators.emojis.remove_emojis", side_effect=lambda x: x
        ),
    ):
        result = markdown_builder.build()
        expected_output = "\n".join(
            [
                "Header and Badges",
                "Table of Contents",
                "Overview",
                "Features",
                "Tree",
                "Project Index",
                "File Summaries",
                "Quickstart Guide",
                "Contributing Guide",
            ]
        )
        assert result == expected_output
