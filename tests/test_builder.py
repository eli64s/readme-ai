"""Unit tests for the builder module."""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from readmeai.builder import (
    build_markdown_sections,
    build_readme_file,
    build_recursive_tables,
    create_markdown_tables,
    create_setup_guide,
    create_table,
    create_tables,
    format_badges,
    format_tree,
    generate_tree,
    get_badges,
)
from readmeai.conf import (
    ApiConfig,
    AppConfig,
    ConfigHelper,
    GitConfig,
    MarkdownConfig,
    PathsConfig,
    PromptsConfig,
)


@pytest.fixture
def config():
    return AppConfig(
        git=GitConfig(name="test", repository="https://github.com/test/test"),
        md=MarkdownConfig(
            badges="badges.toml",
            default="python setup.py install",
            dropdown="<details><summary>{}</summary>\n\n{}</details>",
            header="# Test",
            intro="This is a test project.",
            modules="## Modules",
            setup="## Getting Started\n\nTo get started, run the following commands:\n\n```sh\n$ {}\n$ {}\n$ {}\n```",
            tables="## Code Summary",
            toc="## Table of Contents\n\n- [Test](#test)\n",
            tree="## Project Structure",
            ending="## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.",
        ),
        api=ApiConfig(offline_mode=False),
        paths=PathsConfig(readme="README.md", badges="badges.toml"),
        prompts=PromptsConfig(),
    )


@pytest.fixture
def helper():
    return ConfigHelper()


@pytest.fixture
def packages():
    return ["pytest", "requests"]


@pytest.fixture
def code_summary():
    return [("test.py", "This is a test module")]


def test_build_readme_file(config, helper, packages, code_summary):
    with patch(
        "readmeai.build_markdown_sections"
    ) as mock_build_markdown_sections:
        mock_build_markdown_sections.return_value = [
            "# Test",
            "This is a test README file.",
        ]
        with patch("readmeai.factory.FileHandler.write") as mock_write:
            build_readme_file(config, helper, packages, code_summary)
            mock_build_markdown_sections.assert_called_once_with(
                config, helper, packages, code_summary
            )
            mock_write.assert_called_once_with(
                Path(config.paths.readme),
                "# Test\nThis is a test README file.",
            )


def test_build_markdown_sections(config, helper, packages, code_summary):
    with patch(
        "readmeai.get_user_repository_name"
    ) as mock_get_user_repository_name:
        mock_get_user_repository_name.return_value = "test/test"
        with patch("readmeai.create_setup_guide") as mock_create_setup_guide:
            mock_create_setup_guide.return_value = (
                "python setup.py install",
                "python run.py",
                "pytest",
            )
            with patch(
                "readmeai.create_markdown_tables"
            ) as mock_create_markdown_tables:
                mock_create_markdown_tables.return_value = [
                    ("test.py", "This is a test module")
                ]
                with patch("readmeai.create_tables") as mock_create_tables:
                    mock_create_tables.return_value = "## Code Summary"
                    sections = build_markdown_sections(
                        config, helper, packages, code_summary
                    )
                    assert sections == [
                        "# Test",
                        "Markdown badges",
                        "## Table of Contents\n\n- [Test](#test)\n",
                        "This is an introduction.",
                        "## Project Structure\n\n```sh\n└── test/\n    └── test.py\n```",
                        "## Modules",
                        "## Code Summary",
                        "## Getting Started\n\nTo get started, run the following commands:\n\n```sh\n$ python setup.py install\n$ python run.py\n$ pytest\n```",
                        "## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.",
                    ]


def test_get_badges():
    svg_icons = {"pytest": ("pytest.svg", "#3EAAAF")}
    dependencies = ["pytest", "requests"]
    badges = get_badges(svg_icons, dependencies)
    assert badges == '<img src="pytest.svg" alt="pytest" />'


def test_format_badges():
    badges = ["badge1.svg", "badge2.svg"]
    formatted_badges = format_badges(badges)
    assert (
        formatted_badges
        == '<img src="badge1.svg" alt="badge1" />\n<img src="badge2.svg" alt="badge2" />'
    )


def test_create_setup_guide(config, helper, code_summary):
    summary_list = [("test.py", "This is a test module")]
    setup_guide = create_setup_guide(config, helper, summary_list)
    assert setup_guide == (
        "python setup.py install",
        "python run.py",
        "pytest",
    )


def test_create_markdown_tables(config, code_summary):
    placeholder = "This is a placeholder."
    markdown_tables = create_markdown_tables(placeholder, code_summary)
    assert markdown_tables == [("test.py", "This is a test module")]


def test_create_tables():
    summary_list = [("test.py", "This is a test module")]
    dropdown = "<details><summary>{}</summary>\n\n{}</details>"
    user_repo_name = "test/test"
    tables = create_tables(summary_list, dropdown, user_repo_name)
    assert (
        tables
        == "<details><summary>Test</summary>\n\n| File | Summary |\n| --- | --- |\n| [test.py](https://github.com/test/test/blob/main/test.py) | This is a test module |\n</details>"
    )


def test_create_table():
    data = [("test.py", "This is a test module")]
    user_repo_name = "test/test"
    table = create_table(data, user_repo_name)
    assert (
        table
        == "| [test.py](https://github.com/test/test/blob/main/test.py) | This is a test module |"
    )


def test_build_recursive_tables():
    base_url = "https://github.com/test/test"
    directory = Path("test")
    placeholder = "This is a placeholder."
    markdown_tables = build_recursive_tables(base_url, directory, placeholder)
    assert markdown_tables == "| File | Summary |\n| --- | --- |\n"


def test_generate_tree():
    directory = Path("test")
    repo_url = "https://github.com/test/test"
    tree = generate_tree(directory, repo_url)
    assert tree == "└── test/"


def test_format_tree():
    name = "test"
    tree_str = "└── tmp/\n    └── test.py\n"
    formatted_tree = format_tree(name, tree_str)
    assert formatted_tree == "```sh\n└── test/\n    └── test.py\n```"
