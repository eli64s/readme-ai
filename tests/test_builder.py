"""Unit tests for the builder.py module."""

from pathlib import Path

import pandas as pd
import pytest

from src import builder


@pytest.fixture
def conf():
    class Conf:
        paths = type("", (), {"md": "README.md"})
        github = type(
            "", (), {"name": "my_project", "path": "https://github.com/me/my_project"}
        )
        md = type(
            "",
            (),
            {
                "head": "# {0}\n\n{1}\n\n{2}",
                "close": "\n\n---\n\n## Contributions\n\nAll contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.",
                "intro": "A brief introduction to my awesome project.",
                "dropdown": "<details>\n<summary>{0}</summary>\n\n{1}\n</details>\n",
                "modules": "## Modules\n\nThe following modules are included in this project:\n",
                "setup": "## Setup\n\n### Installing Dependencies\n\n{3}\n\n### Running the Project\n\n{5}\n",
            },
        )
        paths = type("", (), {"badges": "badges.json"})

    return Conf()


@pytest.fixture
def conf_helper():
    class ConfHelper:
        file_extensions = {
            "py": "Python",
            "r": "R",
            "jl": "Julia",
            "js": "JavaScript",
            "go": "Go",
        }
        setup = {
            "Python": [
                "pip install -r requirements.txt",
                "python main.py",
            ],
            "R": [
                "Rscript requirements.R",
                "Rscript main.R",
            ],
            "Julia": [
                "julia requirements.jl",
                "julia main.jl",
            ],
            "JavaScript": [
                "npm install",
                "npm start",
            ],
            "Go": [
                "go mod download",
                "go run main.go",
            ],
        }

    return ConfHelper()


@pytest.fixture
def dependencies():
    return ["pandas", "numpy", "matplotlib"]


@pytest.fixture
def df():
    return pd.DataFrame(
        {
            "Module": [
                "my_project/utils.py",
                "my_project/main.py",
                "my_project/data/load.py",
            ],
            "Summary": ["Utility functions", "Main script", "Data loading functions"],
        }
    )


@pytest.fixture
def intro():
    return "This is my awesome project."


def test_build(conf, conf_helper, dependencies, df, intro):
    builder(conf, conf_helper, dependencies, df, intro)

    md_path = Path.cwd() / conf.paths.md
    assert md_path.exists()

    with open(md_path, "r") as f:
        md_contents = f.read()

    assert "my_project" in md_contents
    assert "This is my awesome project." in md_contents
    assert "## Modules" in md_contents
    assert "my_project/utils.py" in md_contents
    assert "my_project/main.py" in md_contents
    assert "my_project/data/load.py" in md_contents
    assert "## Setup" in md_contents
    assert "Installing Dependencies" in md_contents
    assert "Running the Project" in md_contents
    assert "## Contributions" in md_contents
