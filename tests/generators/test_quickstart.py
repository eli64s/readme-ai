from readmeai.config.settings import ConfigLoader
from readmeai.generators.quickstart import QuickStartGenerator
from readmeai.ingestion.models import QuickStart


def test_quickstart_generator_init(
    config_loader_fixture: ConfigLoader,
    quickstart_generator: QuickStartGenerator,
):
    assert quickstart_generator.config == config_loader_fixture
    assert any(
        language_name in quickstart_generator.language_names
        for language_name in ["python", "sql", "shell", "cpp", "java"]
    )
    assert quickstart_generator.default_commands == {
        "install": "echo 'INSERT-INSTALL-COMMAND-HERE'",
        "usage": "echo 'INSERT-RUN-COMMAND-HERE'",
        "test": "echo 'INSERT-TEST-COMMAND-HERE'",
    }


def test_get_primary_language(quickstart_generator: QuickStartGenerator):
    # When multiple languages are present
    counts = {"py": 10, "sh": 2}
    primary_language = quickstart_generator._get_primary_language(counts)
    assert primary_language == "Python"

    # When no languages are present
    counts = {}
    primary_language = quickstart_generator._get_primary_language(counts)
    assert primary_language is None


def test_format_command(quickstart_generator: QuickStartGenerator):
    command = quickstart_generator._format_command(
        tool_name="pip",
        primary_language="Python",
        file_path="requirements.txt",
        cmd_type="install",
        tool_type="package_managers",
    )
    expected_command = """
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```
"""
    assert command.strip() == expected_command.strip()


def test_generate_commands(
    quickstart_fixture: QuickStart,
    quickstart_generator: QuickStartGenerator,
):
    quickstart_generator._generate_commands(quickstart_fixture, "Python")
    assert quickstart_fixture.install_commands.startswith("\n**Using `pip`**")
    assert quickstart_fixture.usage_commands.startswith("\n**Using `pip`**")
    assert quickstart_fixture.test_commands.startswith("\n**Using `pip`**")


def test_generate_quickstart(quickstart_generator: QuickStartGenerator):
    language_counts = {"py": 10, "sh": 2}
    metadata = {
        "package_managers": {"pip": "requirements.txt"},
        "containers": {},
    }
    quickstart = quickstart_generator.generate(language_counts, metadata)
    assert quickstart.primary_language == "Python"
    assert "install" in quickstart.install_commands
    assert "Using" in quickstart.usage_commands
    assert "test" in quickstart.test_commands


def test_generate_quickstart_empty_args(
    quickstart_generator: QuickStartGenerator,
):
    quickstart = quickstart_generator.generate({}, {})
    assert "Error detecting primary_language" in quickstart.primary_language
    assert quickstart.install_commands == ""
    assert quickstart.usage_commands == ""
    assert quickstart.test_commands == ""
