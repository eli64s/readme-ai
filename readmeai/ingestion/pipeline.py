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
