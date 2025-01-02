from readmeai.config.settings import ConfigLoader
from readmeai.extractors.models import QuickStart
from readmeai.generators.quickstart import QuickStartGenerator


def test_quickstart_generator_init(
    mock_config_loader: ConfigLoader,
    quickstart_generator: QuickStartGenerator,
):
    """Test QuickStartGenerator initialization"""
    assert quickstart_generator.config == mock_config_loader
    assert any(
        language_name in quickstart_generator.language_names
        for language_name in ["python", "sql", "shell", "cpp", "java"]
    )
    assert quickstart_generator.default_cmds == {
        "install": "echo 'INSERT-INSTALL-COMMAND-HERE'",
        "usage": "echo 'INSERT-RUN-COMMAND-HERE'",
        "test": "echo 'INSERT-TEST-COMMAND-HERE'",
        "shield": "https://img.shields.io/badge/Replace%20Me-999999?style=flat&logo=github&logoColor=white",
        "website": "https://img.shields.io/",
    }


def test_get_primary_language(quickstart_generator: QuickStartGenerator):
    """Test primary language detection"""
    # When multiple languages are present
    counts = {"py": 10, "sh": 2}
    primary_language = quickstart_generator._get_primary_language(counts)
    assert primary_language == "Python"

    # When no languages are present
    counts = {}
    primary_language = quickstart_generator._get_primary_language(counts)
    assert primary_language == "unknown"  # Returns 'unknown' instead of None


def test_format_command(quickstart_generator: QuickStartGenerator):
    """Test command formatting with current template style"""
    command = quickstart_generator._format_command(
        tool_name="pip",
        primary_language="Python",
        file_path="requirements.txt",
        cmd_type="install",
        tool_type="package_managers",
    )
    expected_command = """<!-- SHIELDS BADGE CURRENTLY DISABLED -->
\t<!-- [![pip][pip-shield]][pip-link] -->
\t<!-- REFERENCE LINKS -->
\t<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
\t<!-- [pip-link]: https://pypi.org/project/pip/ -->

\t**Using [pip](https://pypi.org/project/pip/):**

\t```sh
\t❯ pip install -r requirements.txt
\t```"""
    assert command.strip() == expected_command.strip()


def test_generate_commands(
    quickstart_fixture: QuickStart,
    quickstart_generator: QuickStartGenerator,
):
    """Test command generation for Python project"""
    quickstart_generator._generate_commands(quickstart_fixture, "Python")
    # Update assertions to match current template format
    assert (
        "<!-- SHIELDS BADGE CURRENTLY DISABLED -->"
        in quickstart_fixture.install_commands
    )
    assert (
        "**Using [pip](https://pypi.org/project/pip/):**"
        in quickstart_fixture.install_commands
    )
    assert "pip install -r requirements.txt" in quickstart_fixture.install_commands


def test_generate_quickstart(quickstart_generator: QuickStartGenerator):
    """Test complete quickstart generation"""
    language_counts = {"py": 10, "sh": 2}
    metadata = {
        "package_managers": {"pip": "requirements.txt"},
        "containers": {},
    }
    quickstart = quickstart_generator.generate(language_counts, metadata)
    assert quickstart.primary_language == "Python"
    assert quickstart.package_managers == {"pip": "requirements.txt"}
    assert "pip install -r requirements.txt" in quickstart.install_commands
    assert "python" in quickstart.usage_commands.lower()
    assert "pytest" in quickstart.test_commands.lower()


def test_generate_quickstart_empty_args(
    quickstart_generator: QuickStartGenerator,
):
    """Test quickstart generation with empty inputs"""
    quickstart = quickstart_generator.generate({}, {})
    # Should return 'unknown' for primary language with empty language counts
    assert quickstart.primary_language == "unknown"
    assert quickstart.install_commands == ""
    assert quickstart.usage_commands == ""
    assert quickstart.test_commands == ""


def test_format_command_invalid_inputs(quickstart_generator: QuickStartGenerator):
    """Test command formatting with invalid inputs"""
    command = quickstart_generator._format_command(
        tool_name="",
        primary_language="",
        file_path="",
        cmd_type="install",
        tool_type="package_managers",
    )
    assert command is None


def test_format_command_containers(quickstart_generator: QuickStartGenerator):
    """Test command formatting for containers"""
    command = quickstart_generator._format_command(
        tool_name="docker",
        primary_language="Python",
        file_path="Dockerfile",
        cmd_type="install",
        tool_type="containers",
    )
    assert "docker" in command.lower()
    assert "<!-- SHIELDS BADGE CURRENTLY DISABLED -->" in command
