from dataclasses import dataclass, field
from pathlib import Path
from string import Template
from typing import Optional

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import get_logger
from readmeai.extractors.models import QuickStart, RepositoryContext
from readmeai.utilities.importer import is_available

if is_available("tomllib"):  # pragma: no cover
    import tomllib
elif is_available("tomli"):  # pragma: no cover
    import tomli as tomllib

_logger = get_logger(__name__)


class QuickStartBuilder:
    """
    Dynamically construct the install, ssage, and testing Qucickstart guides.
    """

    def __init__(
        self, config_loader: ConfigLoader, repo_context: RepositoryContext
    ) -> None:
        self.config_loader = config_loader
        self.config = config_loader.config
        self.repo_context = repo_context
        self.git = self.config.git
        self.md = self.config.md
        self.user_guides = self._load_user_guides()

    def _load_user_guides(self) -> dict:
        """Load the user guide templates from the config file."""
        config_path = (
            Path(__file__).parent.parent
            / "config"
            / "settings"
            / self.config.files.quickstart_guides
        )
        with open(config_path, "rb") as f:
            return tomllib.load(f)

    def build(self) -> str:
        """Create the Installation, Usage, and Testing instructions."""
        repo_url = (
            f"../{self.git.name}"
            if self.git.host_domain.lower() == "local"
            else self.git.repository
        )
        usage_guides = QuickStartGenerator(self.config_loader).generate(
            self.repo_context.language_counts, self.repo_context.metadata
        )

        main_template = Template(self.user_guides["templates"]["main"])
        return main_template.safe_substitute(
            prerequisites_section=self._format_prerequisites(usage_guides),
            installation_section=self._format_installation(usage_guides, repo_url),
            usage_section=self._format_usage(usage_guides),
            testing_section=self._format_testing(usage_guides),
        )

    def _format_prerequisites(self, usage_guides: QuickStart) -> str:
        template = Template(self.user_guides["templates"]["prerequisites"])
        return template.safe_substitute(
            repo_name=self.git.name,
            system_requirements=self._format_system_requirements(usage_guides),
        )

    def _format_system_requirements(self, usage_guides: QuickStart) -> str:
        formatting = self.user_guides["formatting"]
        requirements = [
            formatting["system_requirements_prefix"].replace(
                "$key", "Programming Language"
            )
            + usage_guides.primary_language
        ]
        if usage_guides.package_managers:
            pkg_managers = ", ".join(
                tool.capitalize() for tool in usage_guides.package_managers
            )
            requirements.append(
                formatting["system_requirements_prefix"].replace(
                    "$key", formatting["package_managers_label"]
                )
                + pkg_managers
            )
        if usage_guides.containers:
            containers = ", ".join(
                tool.capitalize() for tool in usage_guides.containers
            )
            requirements.append(
                formatting["system_requirements_prefix"].replace(
                    "$key", formatting["containers_label"]
                )
                + containers
            )
        return "\n".join(requirements)

    def _format_installation(self, usage_guide: QuickStart, repo_url: str) -> str:
        template = Template(self.user_guides["templates"]["installation"])
        install_steps_template = Template(self.user_guides["install_steps"]["template"])

        install_steps = install_steps_template.safe_substitute(
            repo_name=self.git.name,
            repo_url=repo_url,
            install_commands=usage_guide.install_commands.strip()
            or self.config_loader.dev_setup["default"]["install"],
        )
        return template.safe_substitute(
            repo_name=self.git.name,
            header="Installation",
            install_steps=install_steps,
        )

    def _format_usage(self, usage_guides: QuickStart) -> str:
        template = Template(self.user_guides["templates"]["usage"])
        usage_commands = (
            usage_guides.usage_commands
            or self.config_loader.dev_setup["default"]["usage"]
        )
        usage_commands = usage_commands.strip()
        return template.safe_substitute(
            usage_instructions=f"""Run the project with:\n\n{usage_commands}"""
        )

    def _format_testing(self, usage_guides: QuickStart) -> str:
        template = Template(self.user_guides["templates"]["testing"])
        test_commands = (
            usage_guides.test_commands
            or self.config_loader.dev_setup["default"]["test"]
        )
        test_commands = test_commands.strip()
        return template.safe_substitute(
            test_instructions=(
                f"""{self.git.name.capitalize()} uses the {{__test_framework__}} """
                f"""test framework. Run the test suite with:\n\n{test_commands}"""
            )
        )


@dataclass
class QuickStartGenerator:
    """
    Generate Quickstart instructions for a repository.
    """

    config: ConfigLoader
    default_cmds: dict = field(init=False)
    language_names: dict = field(init=False)
    tool_names: dict = field(init=False)

    def __post_init__(self):
        self.default_cmds = self.config.dev_setup["default"]
        self.language_names = self.config.language_map.get("languages", {})
        self.tool_names = self.config.dev_setup

    def generate(
        self,
        language_counts: dict[str, int],
        metadata: dict[str, dict[str, str]],
    ) -> QuickStart:
        """Generate all user setup guides for the project."""
        try:
            primary_language = self._get_primary_language(language_counts)
            if not primary_language:
                primary_language = (
                    f"Error detecting primary_language: {language_counts}"
                )

            quickstart = QuickStart(
                primary_language=primary_language,
                language_counts=language_counts,
                package_managers=metadata.get("package_managers", {}),
                containers=metadata.get("containers", {}),
            )
            self._generate_commands(quickstart, primary_language)

        except Exception as e:
            _logger.warning(f"Error generating quickstart guide: {e!r}")
            quickstart = QuickStart()

        return quickstart

    def _get_primary_language(self, counts: dict[str, int]) -> str:
        """
        Determine the primary language of the project based on file extensions.

        Example
        -------
            Input counts = {'py': 10, 'txt': 5, 'json': 3, 'csv': 2}
            Output: 'Python' (csv, json, and txt are assumed to be data files)
        """
        default_language = self.language_names["unknown"]

        try:
            asset_files = {
                "png",
                "jpg",
                "jpeg",
                "gif",
                "svg",
                "ico",
                "ttf",
                "woff",
                "woff2",
                "eot",
            }
            config_files = {
                "yaml",
                "yml",
                "json",
                "toml",
                "ini",
                "cfg",
                "conf",
                "config",
                "properties",
            }
            data_files = {
                "txt",
                "csv",
                "tsv",
                "log",
                "md",
                "rst",
                "doc",
                "docx",
                "pdf",
                "xls",
                "xlsx",
            }
            excluded_extensions = config_files | data_files | asset_files

            valid_counts = {
                k: v
                for k, v in counts.items()
                if k.lower() not in excluded_extensions and v > 0
            }
            if not valid_counts:
                _logger.info("Failed to detect primary language of project.")
                top_lang = default_language
            else:
                top_lang = max(valid_counts, key=lambda k: valid_counts[k])

            _logger.info(
                f"Detected primary language: {top_lang} "
                f"from valid languages: {valid_counts}"
            )
            return self.language_names.get(top_lang, default_language)

        except Exception as e:
            _logger.error(f"Error detecting primary language of project: {e!r}")
            return default_language

    def _generate_commands(self, quickstart: QuickStart, top_language: str) -> None:
        """Generate install, usage, and test commands."""
        command_types = ["install", "usage", "test"]
        tool_types = ["containers", "package_managers", "documentation"]

        for cmd_type in command_types:
            commands: list[str] = []
            for tool_type in tool_types:
                tool_names = getattr(quickstart, tool_type, {})
                if not tool_names:
                    continue

                commands.extend(
                    filter(
                        None,
                        [
                            self._format_command(
                                tool_name=tool_name,
                                primary_language=top_language,
                                file_path=file_path,
                                cmd_type=cmd_type,
                                tool_type=tool_type,
                            )
                            for tool_name, file_path in tool_names.items()
                        ],
                    )
                )
            setattr(quickstart, f"{cmd_type}_commands", "\n".join(commands))

    def _format_command(
        self,
        tool_name: str,
        primary_language: str,
        file_path: str,
        cmd_type: str,
        tool_type: str,
    ) -> Optional[str]:
        """Format a command type for a specific tool/framework."""
        try:
            if not primary_language or not tool_name:
                return None

            lang_key = primary_language.lower()

            conf = (
                self.tool_names.get(lang_key, {}).get(tool_type, {}).get(tool_name, {})
            ) or self.tool_names.get(tool_type, {}).get(tool_name, {})

            shields = conf.get("shield", conf.get("default"))
            website = conf.get("website", conf.get("default"))

            cmd = conf.get(cmd_type, self.default_cmds.get(cmd_type))
            if not cmd:
                return None

            if cmd_type == "install" and tool_type == "containers":
                cmd = cmd.replace(
                    "{image_name}", self.config.config.git.full_name or ""
                )

            if cmd_type in {"install", "test"} and tool_type != "containers":
                cmd = cmd.replace("{file}", file_path or "")

            if cmd_type in {"usage", "test"}:
                cmd = cmd.replace("{executable}", self.config.config.git.name or "")
                return f"""**Using [{tool_name}]({website}):**\n```sh\n{cmd}\n```"""

            return f"""<!-- SHIELDS BADGE CURRENTLY DISABLED -->
    <!-- [![{tool_name}][{tool_name}-shield]][{tool_name}-link] -->
    <!-- REFERENCE LINKS -->
    <!-- [{tool_name}-shield]: {shields} -->
    <!-- [{tool_name}-link]: {website} -->

    **Using [{tool_name}]({website}):**

    ```sh
    ❯ {cmd}
    ```
    """.strip().replace("    ", "\t")

        except Exception as e:
            _logger.error(f"Error building {cmd_type} command: {e!r}")
            return conf.get("default")
