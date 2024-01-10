"""Processes the input repository files and extracts metadata."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, List, Tuple

from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.core.logger import Logger
from readmeai.core.tokens import token_counter
from readmeai.core.utils import should_ignore
from readmeai.markdown.builder import ReadmeBuilder
from readmeai.parsers.factory import parser_factory

logger = Logger(__name__)

GITHUB_WORKFLOWS_PATH = ".github/workflows"
PARSERS = parser_factory()


@dataclass
class FileData:
    """Data class to store repository file information."""

    path: Path
    name: str
    content: str
    extension: str
    language: str = field(init=False)
    tokens: int = 0
    dependencies: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Initializes the FileData class."""
        self.extension = self.name.split(".")[-1] if "." in self.name else ""
        self.language = self.extension.lower()


class RepoProcessor:
    """Processes the repository files and generates a list of FileData."""

    def __init__(
        self,
        config: AppConfig,
        conf_helper: ConfigHelper,
    ):
        """Initializes the RepoProcessor class."""
        self.config = config
        self.config_helper = conf_helper
        self.language_names = conf_helper.language_names
        self.language_setup = conf_helper.language_setup

    def create_file_data(self, file_info: Tuple[str, Path, str]) -> FileData:
        """Creates a FileData instance from the file information."""
        name, path, content = file_info
        return FileData(name=name, path=path, content=content, extension="")

    def extract_dependencies(self, file_data: FileData) -> List[str]:
        """Extracts the dependency file contents using the factory pattern."""
        parsers = PARSERS

        if file_data.name not in parsers:
            return []

        logger.info(
            f"Dependency file found: {file_data.name} - {file_data.content}"
        )
        parser = parsers.get(file_data.name)
        return parser.parse(content=file_data.content)

    def generate_contents(self, repo_path: str) -> List[FileData]:
        """Generates a List of Dict of file information."""
        if isinstance(repo_path, str):
            repo_path = Path(repo_path)

        return [file_data for file_data in self.generate_file_info(repo_path)]

    def generate_file_info(
        self, repo_path: Path
    ) -> Generator[FileData, None, None]:
        """
        Generates FileData instances for each file in the repository.
        Ignores files as per the `readmeai.settings.ignore_files.toml`
        configuration and handles special cases like GitHub workflows.
        """
        for file_path in repo_path.rglob("*"):
            dependency_files = self.config_helper.dependency_files.get(
                "dependency_files"
            )
            ignore = should_ignore(self.config_helper, file_path)
            if not file_path.is_file() or (
                ignore is True and str(file_path.name) not in dependency_files
            ):
                continue

            relative_path = file_path.relative_to(repo_path)
            relative_path_str = str(relative_path)

            if GITHUB_WORKFLOWS_PATH in relative_path_str:
                yield FileData(
                    name="github actions",
                    path=relative_path,
                    content="",
                    extension="",
                )
            else:
                try:
                    with file_path.open(encoding="utf-8") as file:
                        content = file.read()
                    file_data = FileData(
                        name=file_path.name,
                        path=relative_path,
                        content=content,
                        extension="",
                    )
                    file_data.dependencies = self.extract_dependencies(
                        file_data
                    )
                    yield file_data

                except (OSError, UnicodeDecodeError) as exc_info:
                    logger.warning(
                        f"Error reading file {file_path}: {exc_info}"
                    )
                    continue

    def language_mapper(self, contents: List[FileData]) -> List[FileData]:
        """Maps file extensions to their programming languages."""
        for content in contents:
            content.language = self.language_names.get(
                content.extension, ""
            ).lower()
        return contents

    def tokenize_content(self, contents: List[FileData]) -> List[FileData]:
        """Tokenize each file content and return the token count."""
        if self.config.cli.offline is True:
            return contents

        for content in contents:
            content.tokens = token_counter(
                content.content, self.config.llm.encoding
            )
        return contents

    def get_dependencies(self, contents: List[FileData]) -> List[str]:
        """Returns a list of dependencies."""
        try:
            dependencies = set()
            dependency_files = self.config_helper.dependency_files.get(
                "dependency_files"
            )

            for file_data in contents:
                dependencies.update(file_data.dependencies)
                dependencies.add(file_data.language)
                dependencies.add(file_data.extension)
                if file_data.name in dependency_files:
                    dependencies.add(file_data.name)
                if GITHUB_WORKFLOWS_PATH in str(file_data.path):
                    dependencies.add("github actions")

            return list(dependencies)

        except Exception as exc_info:
            logger.error(f"Error getting dependencies: {exc_info}")
            return []


def process_repository(
    config: AppConfig, config_helper: ConfigHelper, temp_dir: str
) -> Tuple[list, set, str]:
    """Processes the repository and returns the file context."""
    repo_processor = RepoProcessor(config, config_helper)
    file_context = repo_processor.generate_contents(temp_dir)
    file_context = repo_processor.language_mapper(file_context)
    file_context = repo_processor.tokenize_content(file_context)
    dependencies = repo_processor.get_dependencies(file_context)
    summaries = [(file.path, file.content) for file in file_context]
    config.md.tree = ReadmeBuilder(
        config, config_helper, dependencies, summaries, temp_dir
    ).md_tree
    return file_context, dependencies, summaries, config.md.tree
