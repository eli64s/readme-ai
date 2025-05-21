from typing import Any

from pydantic import BaseModel, Field


class BadgeInfo(BaseModel):
    """
    Model for storing badge information from repository files.
    """

    name: str
    description: str
    url: str | None = None


class RepositoryBadges(BaseModel):
    """
    Model for storing all badge information for a repository.
    """

    badges: list[BadgeInfo] = Field(default_factory=list)


class RepositoryContext(BaseModel):
    """
    Extended RepositoryContext model with badges support
    """

    files: list[FileContext]
    dependencies: list[str]
    languages: list[str]
    language_counts: dict[str, int]
    metadata: dict[str, Any] = Field(default_factory=dict)
    quickstart: QuickStart = Field(default_factory=QuickStart)
    badges: RepositoryBadges = Field(default_factory=RepositoryBadges)


class BadgeExtractor:
    """
    Badge extractor class to detect and generate badges based on repository files.
    """

    def __init__(self, config: ConfigLoader) -> None:
        self.config = config
        self._badge_definitions = {
            "prettier": {
                "files": [
                    ".prettierrc",
                    ".prettierrc.json",
                    ".prettierrc.js",
                    ".prettier.config.js",
                ],
                "description": "Code formatting with Prettier",
                "url": "https://prettier.io",
            },
            "eslint": {
                "files": [
                    ".eslintrc",
                    ".eslintrc.json",
                    ".eslintrc.js",
                    ".eslint.config.js",
                ],
                "description": "Code linting with ESLint",
                "url": "https://eslint.org",
            },
            "typescript": {
                "files": ["tsconfig.json"],
                "description": "TypeScript enabled",
                "url": "https://www.typescriptlang.org",
            },
            "docker": {
                "files": ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"],
                "description": "Docker containerization",
                "url": "https://www.docker.com",
            },
            "github-actions": {
                "files": [".github/workflows/*.yml", ".github/workflows/*.yaml"],
                "description": "GitHub Actions CI/CD",
                "url": "https://github.com/features/actions",
            },
        }

    def extract_badges(self, file_contexts: list[FileContext]) -> RepositoryBadges:
        """Extract badge information from file contexts."""
        badges = []
        file_paths = {file.path for file in file_contexts}

        for badge_name, badge_config in self._badge_definitions.items():
            if self._has_badge_files(file_paths, badge_config["files"]):
                badges.append(
                    BadgeInfo(
                        name=badge_name,
                        description=badge_config["description"],
                        url=badge_config["url"],
                    )
                )

        return RepositoryBadges(badges=badges)

    def _has_badge_files(self, file_paths: set[str], badge_patterns: list[str]) -> bool:
        """Check if any of the badge file patterns match the repository files."""
        for pattern in badge_patterns:
            if "*" in pattern:
                # Handle glob patterns
                base_path = pattern.split("*")[0]
                if any(path.startswith(base_path) for path in file_paths):
                    return True
            else:
                # Direct file match
                if pattern in file_paths:
                    return True
        return False


class RepositoryAnalyzer:
    """
    Extended RepositoryAnalyzer with badge support
    """

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.file_processor = FileProcessor(config)
        self.metadata_extractor = MetadataExtractor(config)
        self.quickstart_generator = QuickStartGenerator(config)
        self.badge_extractor = BadgeExtractor(config)

    async def process_repository(
        self, repo_path: Path | str | None = None
    ) -> RepositoryContext:
        """Process the repository and extract metadata including badges."""
        repo_path = Path(str(repo_path))

        file_contexts = self.file_processor.process_files(repo_path)
        metadata = self.metadata_extractor.extract_metadata(file_contexts)
        language_counts = self.file_processor.count_languages(file_contexts)
        dependencies = self.file_processor.extract_dependencies(file_contexts)
        extensions = self.file_processor.extract_extensions(file_contexts)
        language_names = list({
            file.language for file in file_contexts if file.language
        })

        # Extract badges
        badges = self.badge_extractor.extract_badges(file_contexts)

        quickstart = self.quickstart_generator.generate(language_counts, metadata)

        # Improve dependencies and tools extraction by including badge information
        dependencies_and_tools = (
            [tool for tool_group in metadata.values() for tool in tool_group]
            + language_names
            + [dep.split(".")[0] for dep in dependencies]
            + extensions
            + [badge.name for badge in badges.badges]  # Include badge names in tools
        )

        return RepositoryContext(
            files=file_contexts,
            dependencies=dependencies_and_tools,
            languages=language_names,
            language_counts=language_counts,
            metadata=metadata,
            quickstart=quickstart,
            badges=badges,
        )
