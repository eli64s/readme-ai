from pathlib import Path

from readmeai.config.settings import ConfigLoader
from readmeai.generators.quickstart import QuickStartGenerator
from readmeai.ingestion.file_processor import FileProcessor
from readmeai.ingestion.metadata_extractor import MetadataExtractor
from readmeai.ingestion.models import RepositoryContext


class RepositoryProcessor:
    """
    Processes a repository to extract dependencies and metadata.
    """

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.file_processor = FileProcessor(config)
        self.metadata_extractor = MetadataExtractor(config)
        self.quickstart_generator = QuickStartGenerator(config)

    async def process_repository(
        self, repo_path: Path | str | None = None
    ) -> RepositoryContext:
        """Process the repository and extract metadata."""
        repo_path = Path(str(repo_path))

        file_contexts = self.file_processor.process_files(repo_path)

        metadata = self.metadata_extractor.extract_metadata(file_contexts)

        language_counts = self.file_processor.count_languages(file_contexts)

        dependencies = self.file_processor.extract_dependencies(file_contexts)

        language_names = list(
            {file.language for file in file_contexts if file.language}
        )
        quickstart = self.quickstart_generator.generate(
            language_counts, metadata
        )
        dependencies_and_tools = (
            [tool for tool_group in metadata.values() for tool in tool_group]
            + language_names
            + dependencies
        )
        return RepositoryContext(
            files=file_contexts,
            dependencies=dependencies_and_tools,
            languages=language_names,
            language_counts=language_counts,
            metadata=metadata,
            quickstart=quickstart,
        )


'''
import fnmatch
import os
from collections.abc import Generator
from pathlib import Path
from typing import Dict, List, Union

from readmeai.config.settings import ConfigLoader
from readmeai.ingestion.models import FileContext, RepositoryContext
from readmeai.logger import get_logger
from readmeai.parsers.factory import ParserFactory
from readmeai.preprocessor.document_cleaner import DocumentCleaner
from readmeai.preprocessor.file_filter import is_excluded

_logger = get_logger(__name__)


class RepositoryProcessor:
    """
    Processes a repository to extract dependencies and metadata.
    """

    def __init__(self, config: ConfigLoader):
        self.document_cleaner = DocumentCleaner()
        self.cicd = config.tooling.get("cicd", {})
        self.commands = config.commands.get("quickstart_guide", {})
        self.containers = config.tooling.get("containers", {})
        self.documentation = config.tooling.get("documentation", {})
        self.language_names = config.languages.get("language_names")
        self.ignore_list = config.ignore_list.get("ignore_list")
        self.package_managers = config.tooling.get("package_managers", {})
        self.parser_files = config.parsers.get("parsers", {})

    def build_file_context(
        self, repo_path: Path
    ) -> Generator[FileContext, None, None]:
        """
        Generate file info for the given repository path.
        """
        for file_path in repo_path.rglob("*"):
            if file_path.is_file() and not is_excluded(
                self.ignore_list,
                file_path,
                repo_path,
            ):
                _logger.debug(f"Processing file: {file_path}")
                yield self._create_file_context(file_path, repo_path)
            else:
                _logger.debug(f"Skipping file: {file_path}")

    def _create_file_context(
        self, file_path: Path, repo_path: Path
    ) -> FileContext:
        """
        Create a file context object for the given file path.
        """
        file_name = file_path.name
        file_ext = file_path.suffix.lstrip(".")
        file_format = self._map_language(file_ext)
        content = file_path.read_text(errors="ignore")
        cleaned_content = self.document_cleaner.clean(content)
        relative_path = str(file_path.relative_to(repo_path))

        try:
            dependencies = self.extract_dependencies(
                [
                    FileContext(
                        path=relative_path,
                        content=content,
                        name=file_name,
                        ext=file_ext,
                        language=file_format,
                        dependencies=[],
                    )
                ]
            )
        except Exception as e:
            _logger.error(
                f"Error extracting dependencies for file {file_path}: {e!s}"
            )
            dependencies = []

        return FileContext(
            path=relative_path,
            name=file_name,
            ext=file_ext,
            content=cleaned_content,
            language=file_format,
            dependencies=dependencies,
        )

    async def process_repository(
        self,
        repo_path: Union[Path, str, None] = None,
        repo_url: Union[str, None] = None,
        temp_dir: Union[str, None] = None,
    ) -> RepositoryContext:
        """
        Process the local repository contents.
        """
        file_contexts = list(self.build_file_context(Path(str(repo_path))))
        dependencies = set().union(
            *(file.dependencies for file in file_contexts)
        )
        languages = list(
            {file.language for file in file_contexts if file.language}
        )
        cicd = self.detect_cicd_tools(file_contexts)
        containers = self.detect_tools(file_contexts, self.containers)
        documentation = self.detect_documentation_tools(file_contexts)
        package_managers = self.detect_tools(
            file_contexts, self.package_managers
        )

        metadata = {
            "cicd": cicd,
            "containers": containers,
            "documentation": documentation,
            "package_managers": package_managers,
        }

        deps = list(
            set(
                [
                    dependency
                    for metadata in metadata.values()
                    for dependency in metadata
                ]
                + languages
                + list(dependencies)
            )
        )

        language_counts: Dict[str, int] = {}
        for file in file_contexts:
            if file.ext:
                language_counts[file.ext] = (
                    language_counts.get(file.ext, 0) + 1
                )
        language_counts = dict(
            sorted(
                language_counts.items(), key=lambda item: item[1], reverse=True
            )
        )

        return RepositoryContext(
            files=file_contexts,
            dependencies=list(set(deps)),
            languages=languages,
            language_counts=language_counts,
            metadata=metadata,
        )

    def extract_dependencies(self, files: List[FileContext]) -> List[str]:
        """
        Extract dependencies from the given list of files.
        """
        dependencies = []

        for file in files:
            parser = ParserFactory.create_parser(file.name)

            if parser:
                _logger.info(
                    f"Using {parser.__class__.__name__} parser for: {file.name}"
                )
                try:
                    parsed_deps = parser.parse(file.content)
                    if parsed_deps is not None:
                        dependencies.extend(parsed_deps)
                    else:
                        _logger.warning(
                            f"Parser returned None for file: {file.name}"
                        )
                except Exception as e:
                    _logger.error(
                        f"Error parsing dependency file {file.name}: {e!s}"
                    )
            else:
                _logger.info(f"No parser found for file: {file.name}")

        return dependencies

    def _match_file_pattern(self, file_path: str, pattern: str) -> bool:
        if pattern.endswith("*"):
            pattern_parts = pattern.rstrip("*").split("/")
            file_parts = file_path.split(os.path.sep)
            return (
                len(file_parts) >= len(pattern_parts)
                and file_parts[: len(pattern_parts)] == pattern_parts
            )
        elif pattern.startswith("*"):
            return file_path.endswith(pattern[1:])
        elif "*" in pattern:
            return self._match_glob_pattern(file_path, pattern)
        return file_path.endswith(pattern)

    def _match_glob_pattern(self, file_path: str, pattern: str) -> bool:
        return fnmatch.fnmatch(file_path, pattern)

    def detect_tools(
        self, files: List[FileContext], tool_definitions: Dict[str, List[str]]
    ) -> Dict[str, str]:
        detected_tools = {}
        for file in files:
            for tool, file_patterns in tool_definitions.items():
                for pattern in file_patterns:
                    if self._match_file_pattern(file.path, pattern):
                        _logger.debug(
                            f"Matched {tool} with pattern {pattern} for file {file.path}"
                        )
                        detected_tools[tool] = file.path
                    else:
                        _logger.debug(
                            f"No match for {tool} with pattern {pattern} for file {file.path}"
                        )
        return detected_tools

    def detect_cicd_tools(self, files: List[FileContext]) -> Dict[str, str]:
        return self.detect_tools(files, self.cicd)

    def detect_documentation_tools(
        self, files: List[FileContext]
    ) -> Dict[str, str]:
        return self.detect_tools(files, self.documentation)

    def _map_language(self, file_ext: str) -> str:
        """
        Map the file extension to the programming language name.
        """
        return self.language_names.get(
            file_ext.lstrip("."), self.language_names.get("default")
        )
'''
