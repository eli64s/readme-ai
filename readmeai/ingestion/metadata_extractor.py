import fnmatch

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import FileContext


class MetadataExtractor:
    """
    Metadata extractor class to extract metadata from file contexts.
    """

    def __init__(self, config: ConfigLoader) -> None:
        self.config = config

    def extract_metadata(
        self, file_contexts: list[FileContext]
    ) -> dict[str, dict[str, str]]:
        """Extract metadata from file contexts, ensuring valid string values."""
        metadata_categories = {
            "cicd": "cicd",
            "containers": "containers",
            "documentation": "documentation",
            "package_managers": "package_managers",
        }
        return {
            category: self._convert_to_string(
                self._detect_tools(
                    file_contexts, self.config.tooling.get(tool_config, {})
                )
            )
            for category, tool_config in metadata_categories.items()
        }

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
        """
        Match a file path against a pattern.
        """
        if pattern.endswith("*"):
            return file_path.startswith(pattern.rstrip("*"))
        elif pattern.startswith("*"):
            return file_path.endswith(pattern[1:])
        elif "*" in pattern:
            return fnmatch.fnmatch(file_path, pattern)
        return file_path.endswith(pattern)

    def _convert_to_string(
        self, tool_files: dict[str, list[str]]
    ) -> dict[str, str]:
        """Convert detected tools list of file paths into a single string.

        - If multiple files are detected, join into a comma-separated string.
        """
        return {tool: ", ".join(files) for tool, files in tool_files.items()}
