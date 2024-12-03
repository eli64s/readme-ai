from pathlib import Path

from readmeai.config.settings import ConfigLoader
from readmeai.generators.quickstart import QuickStartGenerator
from readmeai.ingestion.file_processor import FileProcessor
from readmeai.ingestion.metadata import MetadataExtractor
from readmeai.ingestion.models import RepositoryContext


class RepositoryProcessor:
    """
    Processes a repository to extract dependencies and metadata.
    """

    def __init__(self, settings: ConfigLoader) -> None:
        self.settings = settings
        self.config = settings.config
        self.file_processor = FileProcessor(settings=settings)
        self.metadata_extractor = MetadataExtractor(settings=settings)
        self.quickstart_generator = QuickStartGenerator(settings=settings)

    async def process_repository(
        self, repo_path: Path | str | None = None
    ) -> RepositoryContext:
        """Process the repository and extract metadata."""
        repo_path = Path(str(repo_path))
        file_contexts = self.file_processor.process_files(repo_path)
        metadata = self.metadata_extractor.extract_metadata(file_contexts)
        language_counts = self.file_processor.count_languages(file_contexts)
        dependencies = self.file_processor.extract_dependencies(file_contexts)
        extensions = list({file.ext for file in file_contexts if file.ext})
        languages = list(
            {file.language for file in file_contexts if file.language}
        )
        quickstart = self.quickstart_generator.generate(
            language_counts, metadata
        )
        technology_stack = (
            [tool for tool_group in metadata.values() for tool in tool_group]
            + dependencies
            + extensions
            + languages
        )
        # technology_stack = list(
        #     set(
        #         self.metadata_extractor.normalize_dependencies(
        #             technology_stack,
        #         )
        #     )
        # )

        return RepositoryContext(
            files=file_contexts,
            dependencies=technology_stack,
            languages=languages,
            language_counts=language_counts,
            metadata=metadata,
            quickstart=quickstart,
        )
