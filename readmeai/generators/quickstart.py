from dataclasses import dataclass, field

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import QuickStart
from readmeai.logger import get_logger

_logger = get_logger(__name__)


@dataclass
class QuickStartGenerator:
    """
    Build the data model for generating the 'Quickstart' instructions.
    """

    config: ConfigLoader
    tools: dict = field(init=False)
    language_names: dict = field(init=False)
    default_commands: dict = field(init=False)

    def __post_init__(self):
        self.tools = self.config.tool_config
        self.language_names = self.config.languages.get("language_names", {})
        self.default_commands = self.tools.get("default", {})

    def generate(
        self,
        language_counts: dict[str, int],
        metadata: dict[str, dict[str, str]],
    ) -> QuickStart:
        """Get any relevant commands for the Quickstart instructions."""
        try:
            primary_language = self._get_primary_language(language_counts)
            quickstart = QuickStart(
                primary_language=primary_language,
                language_counts=language_counts,
                package_managers=metadata.get("package_managers", {}),
                containers=metadata.get("containers", {}),
            )
            self._generate_commands(quickstart, primary_language)
            return quickstart

        except Exception as e:
            _logger.error(
                f"Error generating QuickStart setup: {e}", exc_info=True
            )
            return QuickStart()

    def _get_primary_language(self, counts: dict[str, int]) -> str | None:
        """Determine the primary language of the repository."""
        if not counts:
            return None
        counts = {k: v for k, v in counts.items() if k not in ("yaml", "yml")}
        primary_lang = max(counts, key=counts.get)
        return self.language_names.get(
            primary_lang, self.language_names.get("default")
        )

    def _generate_commands(
        self, quickstart: QuickStart, primary_language: str
    ) -> None:
        """Generate install, usage, and test commands."""
        command_types = ["install", "usage", "test"]
        tool_types = ["package_managers", "containers"]
        for cmd_type in command_types:
            commands: list[str] = []
            for tool_type in tool_types:
                tools = getattr(quickstart, tool_type)
                commands.extend(
                    filter(
                        None,
                        [
                            self._format_command(
                                tool_name,
                                primary_language,
                                file_path,
                                cmd_type,
                                tool_type,
                            )
                            for tool_name, file_path in tools.items()
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
    ) -> str | None:
        """Format a command for the Quickstart instructions."""
        config = (
            self.tools.get(primary_language.lower(), {})
            .get(tool_type, {})
            .get(tool_name, {})
        ) or self.tools.get(tool_type, {}).get(tool_name, {})

        cmd = config.get(cmd_type, self.default_commands.get(cmd_type))
        if not cmd:
            return None

        if cmd_type == "install" and tool_type == "containers":
            cmd = cmd.replace("{image_name}", self.config.config.git.full_name)
        elif cmd_type in {"install", "test"}:
            cmd = cmd.replace("{file}", file_path)
        elif cmd_type == "usage":
            cmd = cmd.replace("{executable}", self.config.config.git.name)
        return f"""
**Using `{tool_name}`** &nbsp; [<img align="center" src="{config.get('shield', '')}" />]({config.get('website', '')})

```sh
❯ {cmd}
```
"""
