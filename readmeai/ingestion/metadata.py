import fnmatch

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import FileContext

dev_tools = {
    "package_managers": {
        "pip": [
            "requirements.txt",
            "requirements-dev.txt",
            "requirements-prod.txt",
            "requirements.in",
            "requirements.test.txt",
        ],
        "conda": [
            "conda.yml",
            "conda.yaml",
            "environment.yml",
            "environment.yaml",
        ],
        "poetry": ["poetry.lock"],
        "pipenv": ["Pipfile", "Pipfile.lock"],
        "pdm": ["pdm.lock"],
        "flit": ["flit.ini"],
        "tox": ["tox.ini"],
    },
    "cicd": {
        "bitbucket_pipelines": [
            "bitbucket-pipelines.yml",
            "bitbucket-pipelines.yaml",
        ],
        "circleci": [".circleci/config.yml", ".circleci/config.yaml"],
        "github_actions": [
            ".github/workflows/*.yml",
            ".github/workflows/*.yaml",
        ],
        "gitlab_ci": [".gitlab-ci.yml", ".gitlab-ci.yaml"],
        "travisci": [".travis.yml", ".travis.yaml"],
        "jenkins": ["Jenkinsfile"],
    },
    "containers": {
        "docker": [
            "Dockerfile",
            "Dockerfile.*",
            "docker-compose.yml",
            "docker-compose.yaml",
            ".env",
        ],
        "podman": ["Containerfile", "Podfile", "Podfile.lock"],
        "singularity": ["Singularity"],
    },
}


class MetadataExtractor:
    """
    Extract metadata and dependencies from repository files.
    """

    def __init__(self, settings: ConfigLoader) -> None:
        self.settings = settings
        self.config = settings.config

    def extract_metadata(
        self, file_contexts: list[FileContext]
    ) -> dict[str, dict[str, str]]:
        """Extract metadata from file contexts, ensuring valid string values."""
        metadata_categories = {
            "prerequisites": "prerequisites",
            "cicd": "cicd",
            "containers": "containers",
            "documentation": "documentation",
            "package_managers": "package_managers",
        }
        return {
            category: self._convert_to_string(
                self._detect_tools(
                    file_contexts,
                    dev_tools.get(category_config, {}),
                )
            )
            for category, category_config in metadata_categories.items()
        }

    def _convert_to_string(
        self, tool_files: dict[str, list[str]]
    ) -> dict[str, str]:
        """Convert detected tools list of file paths into a single string.

        - If multiple files are detected, join into a comma-separated string.
        """
        return {tool: ", ".join(files) for tool, files in tool_files.items()}

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

    def normalize_dependencies(self, dependencies: list[str]) -> list[str]:
        """Normalize dependency names by removing special characters."""

        normalized = []
        seen = set()

        for dep in dependencies:
            dep = dep.lower().strip()
            dep = dep.split(".")[0]
            normalized_dep = (
                "".join(
                    char
                    for char in dep
                    if char.isalnum() or char in ("_", "-")
                )
                .replace("_", "")
                .replace("-", "")
            )
            if normalized_dep and normalized_dep not in seen:
                normalized.append(normalized_dep)
                seen.add(normalized_dep)

        return sorted(list(set(normalized)))
