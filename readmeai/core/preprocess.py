"""Processes the input repository files and extracts metadata."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, List, Tuple

from readmeai.config.settings import AppConfig, ConfigHelper
from readmeai.core.logger import Logger
from readmeai.core.utils import is_file_ignored
from readmeai.llms.tokenize import count_tokens
from readmeai.markdown.builder import ReadmeBuilder
from readmeai.parsers.registry import parser_factory

logger = Logger(__name__)

GITHUB_WORKFLOWS_PATH = ".github/workflows"
PARSERS = parser_factory()


@dataclass
class FileContext:
    """Data class to store file contents and metadata."""

    file_path: Path
    file_name: str
    file_ext: str
    content: str
    tokens: int = 0
    language: str = field(init=False)
    dependencies: List[str] = field(default_factory=list)

    def __post_init__(self):
        """Initializes the FileContext class."""
        self.file_ext = (
            self.file_name.split(".")[-1] if "." in self.file_name else ""
        )
        self.language = self.file_ext.lower()


class RepoProcessor:
    """Processes the repository files and generates FileContext list"""

    def __init__(
        self,
        config: AppConfig,
        config_helper: ConfigHelper,
    ):
        """Initializes the RepoProcessor class."""
        self.config = config
        self.config_helper = config_helper
        self.dependency_files = self.config_helper.dependency_files.get(
            "dependency_files", []
        )
        self.language_names = config_helper.language_names
        self.language_setup = config_helper.language_setup

    def create_file_data(
        self, file_info: Tuple[str, Path, str]
    ) -> FileContext:
        """Creates a FileContext instance from the file information."""
        file_name, file_path, content = file_info
        return FileContext(
            file_name=file_name,
            file_path=file_path,
            content=content,
            file_ext="",
        )

    def extract_dependencies(self, file_data: FileContext) -> List[str]:
        """Extracts the dependency file contents using the factory pattern."""
        parsers = PARSERS

        if file_data.file_name not in parsers:
            return []

        parser = parsers.get(file_data.file_name)
        dependency_names = parser.parse(content=file_data.content)
        logger.info(
            f"Dependency file found: {file_data.file_name}:\n{dependency_names}"
        )
        return dependency_names

    def generate_contents(self, repo_path: str) -> List[FileContext]:
        """Generates a List of Dict of file information."""
        if isinstance(repo_path, str):
            repo_path = Path(repo_path)

        return [file_data for file_data in self.generate_file_info(repo_path)]

    def generate_file_info(
        self, repo_path: Path
    ) -> Generator[FileContext, None, None]:
        """
        Generates FileContext instances for each file in the repository.
        """
        for file_path in repo_path.rglob("*"):
            if self._is_file_ignored(file_path):
                continue
            file_data = self._process_file_path(file_path, repo_path)
            if file_data:
                yield file_data

    def get_dependencies(self, contents: List[FileContext]) -> List[str]:
        """Returns a list of dependencies."""
        try:
            dependency_dict = {}
            dependencies = set()
            dependency_files = self.config_helper.dependency_files.get(
                "dependency_files"
            )

            for file_data in contents:
                dependencies.update(file_data.dependencies)
                dependencies.add(file_data.language)
                dependencies.add(file_data.file_ext)

                if file_data.file_name in dependency_files:
                    dependencies.add(file_data.file_name)
                    dependency_dict[
                        file_data.file_name
                    ] = file_data.dependencies

                if GITHUB_WORKFLOWS_PATH in str(file_data.file_path):
                    dependencies.add("github actions")

            return list(dependencies), dependency_dict

        except Exception as exc:
            logger.error(f"Error getting dependencies: {exc}")
            return []

    def language_mapper(
        self, contents: List[FileContext]
    ) -> List[FileContext]:
        """Maps file extensions to their programming languages."""
        for content in contents:
            content.language = self.language_names.get(
                content.file_ext, ""
            ).lower()
        return contents

    def tokenize_content(
        self, contents: List[FileContext]
    ) -> List[FileContext]:
        """Tokenize each file content and return the token count."""
        if self.config.llm.offline is True:
            return contents

        for content in contents:
            content.tokens = count_tokens(
                content.content, self.config.llm.encoding
            )
        return contents

    def _is_file_ignored(self, file_path: Path) -> bool:
        """
        Determines if a file should be ignored based on configurations.
        """
        if (
            is_file_ignored(self.config_helper, file_path)
            and str(file_path.name) in self.dependency_files
        ):
            return False

        return not file_path.is_file() or is_file_ignored(
            self.config_helper, file_path
        )

    def _process_file_path(
        self, file_path: Path, repo_path: Path
    ) -> FileContext:
        """
        Processes an individual file path and returns FileContext.
        """
        relative_path = file_path.relative_to(repo_path)
        if GITHUB_WORKFLOWS_PATH in str(relative_path):
            return FileContext(
                file_path=relative_path,
                file_name="github actions",
                file_ext="",
                content="",
            )

        try:
            with file_path.open(encoding="utf-8") as file:
                content = file.read()
            file_data = FileContext(
                file_path=relative_path,
                file_name=file_path.name,
                file_ext="",
                content=content,
            )
            file_data.dependencies = self.extract_dependencies(file_data)
            return file_data

        except (OSError, UnicodeDecodeError) as exc:
            logger.warning(f"Error reading file {file_path}: {exc}")


def process_repository(
    config: AppConfig, config_helper: ConfigHelper, temp_dir: str
) -> Tuple[List[FileContext], List[str], List[Tuple[str, str]], str]:
    """Processes the repository files and returns the context."""
    repo_processor = RepoProcessor(config, config_helper)
    repo_context = repo_processor.generate_contents(temp_dir)
    repo_context = repo_processor.tokenize_content(repo_context)
    repo_context = repo_processor.language_mapper(repo_context)

    dependencies, dependency_dict = repo_processor.get_dependencies(
        repo_context
    )

    raw_files = [
        (str(context.file_path), context.content) for context in repo_context
    ]

    config.md.tree = ReadmeBuilder(
        config, config_helper, dependencies, raw_files, temp_dir
    ).md_tree

    return (
        repo_context,
        dependencies,
        raw_files,
        config.md.tree,
        dependency_dict,
    )
