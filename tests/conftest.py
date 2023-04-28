"""Pytest configuration file for the tests directory."""

import tempfile

import pytest


@pytest.fixture
def config_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        f.write(
            """
            [api]
            api_key = "test_api_key"

            [github]
            local = "/path/to/local/codebase"
            remote = "https://github.com/username/repo"

            [md]
            close = "</details>"
            head = "# "
            intro = "# {0}\n"
            dropdown = "## Table of Contents\n\n{0}\n\n"
            modules = "## Modules\n\n{0}\n"
            setup = "## Setup\n\n{0}\n"
            toc = "<details>\n<summary>Table of Contents</summary>\n\n{0}\n\n</details>"
            tree = "## File Tree\n\n{0}\n"

            [paths]
            file_extensions = [".py"]
            file_names = []
            ignore_files = ["__init__.py"]
            setup_guide = "/path/to/setup/guide.md"
            badges = "/path/to/badges.md"
            docs = "/path/to/docs/README.md"
            md = "/path/to/md/file.md"
            """
        )
        f.flush()
        yield f.name
