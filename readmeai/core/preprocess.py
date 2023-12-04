"""Preprocesses and extracts metadata from the user's repository."""

from pathlib import Path
from typing import Dict, Generator, List, Tuple

from readmeai.config import settings
from readmeai.core import logger, tokens
from readmeai.parsers.factory import parser_factory
from readmeai.utils import utils

logger = logger.Logger(__name__)

PARSERS = parser_factory()


class RepositoryParser:
    """Handles preprocessing of the input codebase."""

    def __init__(
        self,
        config: settings.AppConfig,
        conf_helper: settings.ConfigHelper,
    ):
        self.config = config
        self.config_helper = conf_helper
        self.language_names = conf_helper.language_names
        self.language_setup = conf_helper.language_setup
        self.encoding_name = config.api.encoding
        self.local_source = settings.GitHost.LOCAL.value

    def analyze(self, temp_dir: str) -> List[Dict]:
        """Analyzes a local or remote git repository."""
        contents = self.generate_contents(temp_dir)

        repo_source = self.config.git.source
        if repo_source != self.local_source:
            logger.info(f"Tokenizing content from source: {repo_source}")
            contents = self.tokenize_content(contents)

        contents = self.process_language_mapping(contents)

        return contents

    def generate_contents(self, repo_path: str) -> List[Dict]:
        """Generates a List of Dict of file information."""
        repo_path = Path(repo_path)

        data = list(self.generate_file_info(repo_path))

        contents = []
        for name, path, content in data:
            extension = Path(name).suffix.lstrip(".")
            contents.append(
                {
                    "name": name,
                    "path": path,
                    "content": content,
                    "extension": extension,
                }
            )
        return contents

    def get_dependency_file_contents(self, contents: List[Dict]) -> List[str]:
        """Extracts the dependency file contents using the factory pattern."""
        parsers = PARSERS

        filtered = [c for c in contents if c["name"] in parsers]
        if not filtered:
            return []

        parsed_contents = []
        for content in filtered:
            parser = parsers.get(content["name"])
            parsed_content = parser.parse(content=content["content"])
            parsed_contents.append(parsed_content)
            logger.info(
                f"Dependency file found: {content['name']} - {parsed_content}"
            )
        return utils.flatten_list(parsed_contents)

    def parse_content(content: Dict) -> List[str]:
        """Helper function to parse the content of a file."""
        parser = PARSERS.get(content["name"])
        if parser:
            return parser.parse(content["content"])
        return []

    def generate_file_info(
        self, repo_path: Path
    ) -> Generator[Tuple[str, Path, str], None, None]:
        """Generates a tuple of file information."""
        for file_path in repo_path.rglob("*"):
            if utils.should_ignore(self.config_helper, file_path):
                continue

            if file_path.is_file():
                if ".github/workflows" in str(
                    file_path.relative_to(repo_path)
                ):
                    yield "github actions", file_path.relative_to(
                        repo_path
                    ), ""
                try:
                    with file_path.open(encoding="utf-8") as file:
                        content = file.read()
                    relative_path = file_path.relative_to(repo_path)
                    yield file_path.name, relative_path, content
                except UnicodeDecodeError:
                    continue

    def get_file_contents(self, contents: Dict) -> Dict[str, str]:
        """Extracts the file contents from the list of dicts."""
        return {content["path"]: content["content"] for content in contents}

    def get_unique_contents(
        self, contents: Dict, keys: List[str]
    ) -> List[str]:
        """Extracts the unique contents from the list of dicts."""
        unique_contents = {data[key] for key in keys for data in contents}
        return list(unique_contents)

    def get_dependencies(
        self, temp_dir: str = None
    ) -> Tuple[List[str], Dict[str, str]]:
        """Extracts the dependencies of the user's repository."""
        contents = self.analyze(temp_dir)
        dependencies = self.get_dependency_file_contents(contents)
        attributes = ["extension", "language", "name"]
        dependencies.extend(self.get_unique_contents(contents, attributes))
        return list(set(dependencies)), self.get_file_contents(contents)

    def process_language_mapping(self, contents: List[Dict]) -> List[Dict]:
        """Maps file extensions to their programming languages."""
        for content in contents:
            content["language"] = self.language_names.get(
                content["extension"], ""
            ).lower()
            setup = self.language_setup.get(content["language"], "")
            setup = setup if isinstance(setup, list) else [None, None]
            while len(setup) < 3:
                setup.append(None)
            content["install"], content["run"], content["test"] = setup
        return contents

    def tokenize_content(self, contents: List[Dict]) -> List[Dict]:
        """Tokenizes the content of each file."""
        for content in contents:
            content["tokens"] = tokens.get_token_count(
                content["content"], self.encoding_name
            )
        return contents
