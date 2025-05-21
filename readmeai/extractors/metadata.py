import fnmatch
from pathlib import Path
from typing import List

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import get_logger
from readmeai.extractors.models import FileContext
from readmeai.parsers.factory import ParserFactory

_logger = get_logger(__name__)


class MetadataExtractor:
    """
    Enhanced metadata extractor class that uses the existing parser system.
    """

    def __init__(self, config: ConfigLoader) -> None:
        self.config = config

    def extract_metadata(
        self, file_contexts: list[FileContext]
    ) -> dict[str, dict[str, str | List[str]]]:
        """Extract metadata and dependencies from file contexts."""
        metadata_categories = {
            "cicd": "cicd",
            "containers": "containers",
            "documentation": "documentation",
            "package_managers": "package_managers",
        }

        # Get basic metadata
        metadata = {
            category: self._convert_to_string(
                self._detect_tools(
                    file_contexts, self.config.dev_tools.get(dev_setup, {})
                )
            )
            for category, dev_setup in metadata_categories.items()
        }

        # Extract dependencies using the parser system
        package_dependencies = self._extract_package_dependencies(
            metadata.get("package_managers", {}), file_contexts
        )

        if package_dependencies:
            metadata["dependencies"] = package_dependencies

        return metadata

    def _extract_package_dependencies(
        self, package_managers: dict[str, str], file_contexts: list[FileContext]
    ) -> dict[str, list[str]]:
        """Extract dependencies using the appropriate parser for each file."""
        dependencies: dict[str, set[str]] = {}

        for manager, files_str in package_managers.items():
            file_paths = [f.strip() for f in files_str.split(",")]

            for file_path in file_paths:
                file_name = Path(file_path).name
                file_content = next(
                    (f.content for f in file_contexts if f.path == file_path), None
                )

                if file_content:
                    parser = ParserFactory.create_parser(file_name)
                    parsed_deps = parser.parse(file_content)

                    if parsed_deps:
                        if manager not in dependencies:
                            dependencies[manager] = set()
                        dependencies[manager].update(parsed_deps)

        return {manager: sorted(list(deps)) for manager, deps in dependencies.items()}

    def _detect_tools(
        self, files: list[FileContext], tool_definitions: dict[str, list[str]]
    ) -> dict[str, list[str]]:
        """Detect tools based on file patterns."""
        detected_tools: dict[str, list[str]] = {}

        for file in files:
            for tool, patterns in tool_definitions.items():
                if matching_files := [
                    file.path
                    for pattern in patterns
                    if self._match_file_pattern(file.path, pattern)
                ]:
                    if tool not in detected_tools:
                        detected_tools[tool] = []
                    detected_tools[tool].extend(matching_files)

        return detected_tools

    def _match_file_pattern(self, file_path: str, pattern: str) -> bool:
        """Match a file path against a pattern."""
        if pattern.endswith("*"):
            return file_path.startswith(pattern.rstrip("*"))
        elif pattern.startswith("*"):
            return file_path.endswith(pattern[1:])
        elif "*" in pattern:
            return fnmatch.fnmatch(file_path, pattern)
        return file_path.endswith(pattern)

    def _convert_to_string(self, tool_files: dict[str, list[str]]) -> dict[str, str]:
        """Convert detected tools list of file paths into a single string."""
        return {tool: ", ".join(files) for tool, files in tool_files.items()}
