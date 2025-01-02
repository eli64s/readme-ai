from collections import Counter
from pathlib import Path

from readmeai.config.settings import ConfigLoader
from readmeai.core.logger import get_logger
from readmeai.extractors.models import FileContext
from readmeai.parsers.factory import ParserFactory
from readmeai.preprocessor.document_cleaner import DocumentCleaner
from readmeai.preprocessor.file_filter import is_excluded

_logger = get_logger(__name__)


class FileProcessor:
    """
    File processor class to process files in a repository.
    """

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.document_cleaner = DocumentCleaner()
        self.ignore_list = config.ignore_list.get("ignore_list", [])
        self.language_names = config.language_map.get("languages", {})

    def process_files(self, repo_path: Path) -> list[FileContext]:
        """Generate file info for the given repository path."""
        return [
            self._create_file_context(file_path, repo_path)
            for file_path in repo_path.rglob("*")
            if file_path.is_file()
            and not is_excluded(self.ignore_list, file_path, repo_path)
        ]

    def count_languages(self, file_contexts: list[FileContext]) -> dict[str, int]:
        """Count the occurrences of each language."""
        return dict(Counter(file.ext for file in file_contexts if file.ext))

    def extract_dependencies(self, file_contexts: list[FileContext]) -> list[str]:
        """Extract all dependencies from file contexts."""

        return list(set().union(*(file.dependencies for file in file_contexts)))

    def extract_extensions(self, file_contexts: list[FileContext]) -> list[str]:
        """Extract all file extensions from file contexts."""
        return list(set(file.ext for file in file_contexts if file.ext))

    def _create_file_context(self, file_path: Path, repo_path: Path) -> FileContext:
        """Create a file context object for the given file path."""
        relative_path = str(file_path.relative_to(repo_path))
        content = file_path.read_text(errors="ignore")
        file_ext = file_path.suffix.lstrip(".")
        return FileContext(
            path=relative_path,
            name=file_path.name,
            ext=file_ext,
            content=self.document_cleaner.clean(content),
            language=self._map_language(file_ext, file_path.name),
            dependencies=self._parse_dependencies(relative_path, content),
        )

    def _map_language(self, file_ext: str, file_name: str) -> str:
        """Map the file extension to the programming language name."""
        return self.language_names.get(file_ext, file_name)

    def _parse_dependencies(self, file_path: str, content: str) -> list[str]:
        """Parse dependencies from the file content."""
        if parser := ParserFactory.create_parser(file_path):
            try:
                return parser.parse(content) or []
            except Exception as e:
                _logger.error(f"Error parsing dependency file {file_path}: {e}")
        return []
