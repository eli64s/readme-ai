"""
Pre-processes the input repository files and extracts metadata.
"""

from collections.abc import Generator
from dataclasses import dataclass, field
from pathlib import Path

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import Logger
from readmeai.generators.builder import MarkdownBuilder
from readmeai.parsers.factory import parser_handler

_github_actions_path = ".github/workflows"


@dataclass
class FileContext:
    """
    Data class to store file contents and metadata.
    """

    file_path: Path
    file_name: str
    file_ext: str
    content: str
    language: str = field(init=False)
    dependencies: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Initializes the FileContext class."""
        self.file_ext = (
            self.file_name.split(".")[-1] if "." in self.file_name else ""
        )
        self.language = self.file_ext.lower()


class RepositoryProcessor:
    """Processes the repository files and generates FileContext list"""

    def __init__(self, config_loader: ConfigLoader):
        """Initializes the RepositoryProcessor class."""
        self._logger = Logger(__name__)
        self.config_loader = config_loader
        self.ignore_list = config_loader.ignore_list.get("ignore_list")
        self.commands = config_loader.commands
        self.languages = config_loader.languages.get("language_names")
        self.parser_files = config_loader.parsers.get("parsers")

    def create_file_data(
        self,
        file_info: tuple[str, Path, str],
    ) -> FileContext:
        """Creates a FileContext instance from the file information."""
        file_name, file_path, content = file_info
        return FileContext(
            file_name=file_name,
            file_path=file_path,
            content=content,
            file_ext="",
        )

    def extract_dependencies(self, file_data: FileContext) -> list[str]:
        """Extracts the dependency file contents using the factory pattern."""
        parsers = parser_handler()
        parser = parsers.get(file_data.file_name)
        if file_data.file_name not in parsers or parser is None:
            return []
        return parser.parse(content=file_data.content)

    def generate_contents(self, repo_path: Path | str) -> list[FileContext]:
        """Generates a List of Dict of file information."""
        if isinstance(repo_path, str):
            repo_path = Path(repo_path)
        return [file_data for file_data in self.generate_file_info(repo_path)]

    def generate_file_info(
        self,
        repo_path: Path,
    ) -> Generator[FileContext, None, None]:
        """
        Generates FileContext instances for each file in the repository.
        """
        for file_path in repo_path.rglob("*"):
            if self._filter_file(file_path):
                continue
            file_data = self._process_file_path(file_path, repo_path)
            if file_data:
                yield file_data

    def get_dependencies(self, contents: list[FileContext]) -> list[str]:
        """Returns a list of dependencies."""
        try:
            dependencies = set()
            parser_files = self.parser_files

            for file_data in contents:
                dependencies.update(file_data.dependencies)
                dependencies.add(file_data.language.lower())
                dependencies.add(file_data.file_ext)

                if file_data.file_name in parser_files["parsers"]:
                    dependencies.add(file_data.file_name)
                if _github_actions_path in str(file_data.file_path):
                    dependencies.add("github actions")

            return list(dependencies)

        except Exception as exc:
            self._logger.error(f"Error getting dependencies: {exc}")
            return []

    def _filter_file(self, file_path: Path) -> bool:
        """
        Determines if a file should be ignored based on configurations.
        """
        is_file_ignored = any(
            [
                file_path.name in self.ignore_list["files"],
                file_path.suffix.lstrip(".") in self.ignore_list["extensions"],
                any(
                    dir in file_path.parts
                    for dir in self.ignore_list["directories"]
                ),
            ],
        )
        if is_file_ignored and str(file_path.name) in self.parser_files:
            return False
        return not file_path.is_file() or is_file_ignored

    def _language_mapper(
        self,
        contents: list[FileContext],
    ) -> list[FileContext]:
        """Maps file extensions to their programming languages."""
        for content in contents:
            content.language = self.languages.get(content.file_ext, "").lower()
        return contents

    def _process_file_path(
        self,
        file_path: Path,
        repo_path: Path,
    ) -> FileContext:
        """
        Processes an individual file path and returns FileContext.
        """
        relative_path = file_path.relative_to(repo_path)
        if _github_actions_path in str(relative_path):
            return FileContext(
                file_path=relative_path,
                file_name="github actions",
                file_ext="",
                content="",
            )
        try:
            if file_path.is_dir():
                return FileContext(
                    file_path=relative_path,
                    file_name=file_path.name,
                    file_ext="",
                    content="",
                )
            with file_path.open(encoding="utf-8") as file:
                content = file.read()

            file_data = FileContext(
                file_path=relative_path,
                file_name=file_path.name,
                file_ext=file_path.suffix,
                content=content,
            )
            file_data.dependencies = self.extract_dependencies(file_data)
            return file_data

        except (OSError, UnicodeDecodeError) as exc:
            self._logger.warning(f"Error reading file {file_path}: {exc}")
            return FileContext(
                file_path=relative_path,
                file_name=file_path.name,
                file_ext="",
                content="",
            )


def preprocessor(conf: ConfigLoader, tmp_dir: str) -> tuple:
    """Processes the repository files and returns the context."""
    repo_processor = RepositoryProcessor(conf)
    repo_context = repo_processor.generate_contents(tmp_dir)
    repo_context = repo_processor._language_mapper(repo_context)
    deps = repo_processor.get_dependencies(repo_context)
    raw_files = [
        (str(context.file_path), context.content) for context in repo_context
    ]
    conf.config.md.tree = MarkdownBuilder(
        conf,
        deps,
        raw_files,
        tmp_dir,
    ).md_tree
    return deps, raw_files
