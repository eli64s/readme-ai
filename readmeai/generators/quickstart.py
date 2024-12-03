"""Builds instruction sets for the 'Getting Started' README section."""

from dataclasses import dataclass, field
from enum import Enum
from string import Template
from typing import Dict, List, Optional

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import QuickStart, RepositoryContext
from readmeai.logger import get_logger

_logger = get_logger(__name__)


class ToolCategory(str, Enum):
    """Categories of development tools."""

    PACKAGE_MANAGER = "package_manager"
    BUILD_SYSTEM = "build_system"
    CONTAINER = "container"
    CI_CD = "ci_cd"
    CODE_QUALITY = "code_quality"
    API_DOCUMENTATION = "api_documentation"
    DATABASE = "database"
    MONITORING = "monitoring"
    SERVERLESS = "serverless"


@dataclass
class ToolConfig:
    """Configuration for a development tool."""

    name: str
    category: ToolCategory
    files: List[str]
    install_command: Optional[str] = None
    usage_command: Optional[str] = None
    test_command: Optional[str] = None
    shield_url: Optional[str] = None
    website_url: Optional[str] = None
    languages: List[str] = field(default_factory=list)

    def format_command(self, cmd_type: str, **kwargs) -> Optional[str]:
        """Format a specific command with given parameters."""
        cmd = getattr(self, f"{cmd_type}_command")
        if not cmd:
            return None

        try:
            # Apply any default replacements
            kwargs.setdefault("badge_style", "flat-square")
            formatted_cmd = cmd.format(**kwargs)

            if self.shield_url and self.website_url:
                shield = self.shield_url.format(
                    badge_style=kwargs.get("badge_style")
                )
                return f"""**With `{self.name}`** &nbsp; [<img align="center" src="{shield}" />]({self.website_url})\n\n```sh\n❯ {formatted_cmd}\n```"""
            return f"```sh\n❯ {formatted_cmd}\n```"
        except Exception as e:
            _logger.error(f"Error formatting command for {self.name}: {e}")
            return None


class QuickStartGenerator:
    """Generates QuickStart instructions based on repository analysis."""

    def __init__(self, settings: ConfigLoader):
        """Initialize with configuration settings."""
        self.settings = settings
        self.config = settings.config

    def generate(
        self,
        language_counts: Dict[str, int],
        metadata: Dict[str, Dict[str, str]],
    ) -> QuickStart:
        """Generate QuickStart instructions based on repository analysis."""
        try:
            primary_language = self._get_primary_language(language_counts)
            if not primary_language:
                _logger.warning(
                    f"No valid programming language detected in: {language_counts}"
                )
                return QuickStart()

            quickstart = QuickStart(
                primary_language=primary_language,
                language_counts=language_counts,
                package_managers=metadata.get("package_managers", {}),
                containers=metadata.get("containers", {}),
            )

            self._generate_commands(quickstart)
            return quickstart

        except Exception as e:
            _logger.error(f"Error generating QuickStart setup: {e}")
            return QuickStart()

    def _get_primary_language(self, counts: Dict[str, int]) -> Optional[str]:
        """Determine the primary programming language of the repository."""
        try:
            if not counts:
                return None

            # Get programming extensions from config
            programming_extensions = set(
                ext.lstrip(".")
                for ext in self.config.file_extensions.get("programming", [])
            )

            # Filter by known programming extensions
            valid_counts = {
                ext.lstrip("."): count
                for ext, count in counts.items()
                if ext.lstrip(".") in programming_extensions
            }

            if not valid_counts:
                return None

            primary_ext = max(valid_counts.items(), key=lambda x: x[1])[0]

            # Use language_map to get the proper language name
            return self.config.language_map.get(primary_ext)

        except Exception as e:
            _logger.error(f"Error determining primary language: {e}")
            return None

    def _generate_commands(self, quickstart: QuickStart) -> None:
        """Generate all commands for the quickstart guide."""
        if not quickstart.primary_language:
            return

        # Get language configuration
        lang_key = quickstart.primary_language.lower()
        lang_config = self.config.languages.get(lang_key, {})

        command_types = ["install", "usage", "test"]

        for cmd_type in command_types:
            commands = []

            # Add package manager commands
            if quickstart.package_managers:
                package_managers = lang_config.get("package_managers", {})
                for pm_name, file_path in quickstart.package_managers.items():
                    if pm_config := package_managers.get(pm_name, {}):
                        cmd = pm_config.get(f"{cmd_type}_command")
                        if cmd:
                            try:
                                formatted_cmd = cmd.format(file=file_path)
                                shield_url = pm_config.get("shield_url")
                                website_url = pm_config.get("website_url")

                                if shield_url and website_url:
                                    shield = shield_url.format(
                                        badge_style="flat-square"
                                    )
                                    commands.append(
                                        f"""**With `{pm_name}`** &nbsp; [<img align="center" src="{shield}" />]({website_url})\n\n```sh\n❯ {formatted_cmd}\n```"""
                                    )
                                else:
                                    commands.append(
                                        f"```sh\n❯ {formatted_cmd}\n```"
                                    )
                            except Exception as e:
                                _logger.error(
                                    f"Error formatting command for {pm_name}: {e}"
                                )

            # Add container commands
            if quickstart.containers:
                containers = self.config.tools.get("containers", {})
                for (
                    container_name,
                    image_name,
                ) in quickstart.containers.items():
                    if container_config := containers.get(container_name, {}):
                        cmd = container_config.get(f"{cmd_type}_command")
                        if cmd:
                            try:
                                formatted_cmd = cmd.format(
                                    image_name=image_name
                                )
                                shield_url = container_config.get("shield_url")
                                website_url = container_config.get(
                                    "website_url"
                                )

                                if shield_url and website_url:
                                    shield = shield_url.format(
                                        badge_style="flat-square"
                                    )
                                    commands.append(
                                        f"""**With `{container_name}`** &nbsp; [<img align="center" src="{shield}" />]({website_url})\n\n```sh\n❯ {formatted_cmd}\n```"""
                                    )
                                else:
                                    commands.append(
                                        f"```sh\n❯ {formatted_cmd}\n```"
                                    )
                            except Exception as e:
                                _logger.error(
                                    f"Error formatting command for {container_name}: {e}"
                                )

            setattr(quickstart, f"{cmd_type}_commands", "\n".join(commands))


class QuickStartBuilder:
    """Builds the 'Getting Started' section of the README."""

    def __init__(
        self, settings: ConfigLoader, repo_context: RepositoryContext
    ):
        self.settings = settings
        self.repo_context = repo_context
        self.config = settings.config
        self.git = self.config.git
        self.template = self.config.templates
        self._generator = QuickStartGenerator(settings)
        self._usage_guides: Optional[QuickStart] = None

    @property
    def usage_guides(self) -> QuickStart:
        """Lazy load and cache usage guides."""
        if self._usage_guides is None:
            self._usage_guides = self._generator.generate(
                self.repo_context.language_counts, self.repo_context.metadata
            )
        return self._usage_guides

    def build(self) -> str:
        """Create the complete Getting Started section."""
        return Template(self.template["templates"]["main"]).safe_substitute(
            prerequisites_section=self._build_prerequisites(),
            installation_section=self._build_installation(),
            usage_section=self._build_usage(),
            testing_section=self._build_testing(),
        )

    def _build_prerequisites(self) -> str:
        """Build prerequisites section."""
        template = Template(self.template["templates"]["prerequisites"])
        return template.safe_substitute(
            repo_name=self.git.name,
            system_requirements=self._format_system_requirements(),
        )

    def _build_installation(self) -> str:
        """Build installation section."""
        template = Template(self.template["templates"]["installation"])
        methods = self._get_install_methods()

        return template.safe_substitute(
            repo_name=self.git.name,
            install_steps="\n\n".join(
                f"**{m['name']}:**\n\n{m['steps']}" for m in methods
            ),
        )

    def _build_usage(self) -> str:
        """Build usage section."""
        template = Template(self.template["templates"]["usage"])
        usage_commands = (
            self.usage_guides.usage_commands
            or self.config.defaults.get("usage_command", "")
        )
        return template.safe_substitute(
            usage_instructions=f"Run `{self.git.name}` using the following command:\n\n{usage_commands.lstrip()}"
        )

    def _build_testing(self) -> str:
        """Build testing section."""
        template = Template(self.template["templates"]["testing"])
        test_commands = (
            self.usage_guides.test_commands
            or self.config.defaults.get("test_command", "")
        )
        return template.safe_substitute(
            test_instructions=f"Run the test suite using the following command:\n\n{test_commands.lstrip()}"
        )

    def _format_system_requirements(self) -> str:
        """Format system requirements as string."""
        formatting = self.template["formatting"]
        requirements = []

        if self.usage_guides.primary_language:
            requirements.append(
                f"{formatting['system_requirements_prefix'].replace('$key', 'Programming Language')}"
                f"{self.usage_guides.primary_language}"
            )

        for tool_type, label in [
            ("package_managers", formatting["package_managers_label"]),
            ("containers", formatting["containers_label"]),
        ]:
            if tools := getattr(self.usage_guides, tool_type, None):
                requirements.append(
                    f"{formatting['system_requirements_prefix'].replace('$key', label)}"
                    f"{', '.join(t.capitalize() for t in tools)}"
                )

        return "\n".join(requirements)

    def _get_install_methods(self) -> List[Dict[str, str]]:
        """Get all available installation methods."""
        methods = [
            {
                "name": "Build from source",
                "steps": self._format_source_install(),
            }
        ]

        install_commands = self.usage_guides.install_commands
        if install_commands:
            for tool_name in self.usage_guides.package_managers:
                methods.append(
                    {
                        "name": f"Install with {tool_name.capitalize()}",
                        "steps": install_commands,
                    }
                )

        return methods

    def _format_source_install(self) -> str:
        """Format the build from source installation steps."""
        repo_url = (
            f"../{self.git.name}"
            if self.git.host_domain.lower() == "local"
            else self.git.repository
        )

        install_steps_template = Template(
            self.template["install_steps"]["template"]
        )
        return install_steps_template.safe_substitute(
            repo_name=self.git.name,
            repo_url=repo_url,
            install_commands=self.usage_guides.install_commands
            or self.config.defaults.get("install_command", ""),
        )
