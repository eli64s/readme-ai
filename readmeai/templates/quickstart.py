from pathlib import Path
from string import Template

import tomllib

from readmeai.config.settings import ConfigLoader
from readmeai.generators.quickstart import QuickStartGenerator
from readmeai.ingestion.models import QuickStart, RepositoryContext


class QuickStartBuilder:
    """
    Build the 'Quickstart', or 'Getting Started' README section.
    """

    def __init__(
        self, config_loader: ConfigLoader, repo_context: RepositoryContext
    ):
        self.config_loader = config_loader
        self.config = config_loader.config
        self.repo_context = repo_context
        self.git = self.config.git
        self.md = self.config.md
        self.quickstart_config = self._load_quickstart_config()

    def _load_quickstart_config(self):
        config_path = (
            Path(__file__).parent.parent
            / "config"
            / "settings"
            / "quickstart_config.toml"
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

        main_template = Template(self.quickstart_config["templates"]["main"])
        return main_template.safe_substitute(
            prerequisites_section=self._format_prerequisites(usage_guides),
            installation_section=self._format_installation(
                usage_guides, repo_url
            ),
            usage_section=self._format_usage(usage_guides),
            testing_section=self._format_testing(usage_guides),
        )

    def _format_prerequisites(self, usage_guides: QuickStart) -> str:
        template = Template(
            self.quickstart_config["templates"]["prerequisites"]
        )
        return template.safe_substitute(
            repo_name=self.git.name,
            system_requirements=self._format_system_requirements(usage_guides),
        )

    def _format_system_requirements(self, usage_guides: QuickStart) -> str:
        formatting = self.quickstart_config["formatting"]
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

    def _format_installation(
        self, usage_guide: QuickStart, repo_url: str
    ) -> str:
        template = Template(
            self.quickstart_config["templates"]["installation"]
        )
        install_steps_template = Template(
            self.quickstart_config["install_steps"]["template"]
        )
        install_steps = install_steps_template.safe_substitute(
            repo_name=self.git.name,
            repo_url=repo_url,
            install_commands=usage_guide.install_commands
            or self.config_loader.tool_config.get("default", {}).get(
                "install", ""
            ),
        )
        return template.safe_substitute(
            repo_name=self.git.name,
            install_steps=install_steps,
        )

    def _format_usage(self, usage_guides: QuickStart) -> str:
        template = Template(self.quickstart_config["templates"]["usage"])
        usage_commands = (
            usage_guides.usage_commands
            or self.config_loader.tool_config.get("default", {}).get(
                "usage", ""
            )
        )
        return template.safe_substitute(
            usage_instructions=f"Run {self.git.name} using the following command:\n{usage_commands.lstrip()}"
        )

    def _format_testing(self, usage_guides: QuickStart) -> str:
        template = Template(self.quickstart_config["templates"]["testing"])
        test_commands = (
            usage_guides.test_commands
            or self.config_loader.tool_config.get("default", {}).get(
                "test", ""
            )
        )
        return template.safe_substitute(
            test_instructions=f"Run the test suite using the following command:\n{test_commands.lstrip()}"
        )
