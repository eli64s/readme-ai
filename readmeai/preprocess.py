"""Handles preprocessing of the input codebase."""

import tempfile
from pathlib import Path
from typing import Dict, Generator, List, Tuple

from . import conf, logger, parse, utils

logger = logger.Logger(__name__)


class RepositoryParserWrapper:
    """Wrapper class for the RepositoryParser."""

    def __init__(self, config: conf.AppConfig, conf_helper: conf.ConfigHelper):
        self.parser = RepositoryParser(
            config, conf_helper.language_names, conf_helper.language_setup
        )

    def get_unique_contents(self, contents: Dict, keys: List[str]) -> List[str]:
        """Extracts the unique contents from the list of dicts."""
        unique_contents = {data[key] for key in keys for data in contents}
        return list(unique_contents)

    def get_file_contents(self, contents: Dict) -> Dict[str, str]:
        """Extracts the file contents from the list of dicts."""
        return {content["path"]: content["content"] for content in contents}

    def get_dependencies(
        self, repository: str, is_remote: bool = True
    ) -> Tuple[List[str], Dict[str, str]]:
        """Extracts the dependencies of the user's repository."""
        contents = self.parser.analyze(repository, is_remote)
        dependencies = self.parser.get_dependency_file_contents(contents)
        attributes = ["extension", "language", "name"]
        dependencies.extend(self.get_unique_contents(contents, attributes))
        return list(set(dependencies)), self.get_file_contents(contents)


class RepositoryParser:
    """Analyzes a local or remote git repository."""

    def __init__(
        self,
        config: conf.AppConfig,
        language_names: Dict[str, str],
        language_setup: Dict[str, str],
    ):
        self.language_names = language_names
        self.language_setup = language_setup
        self.encoding_name = config.api.encoding

    def analyze(self, repo_path: str, is_remote: bool = False) -> List[Dict]:
        """Analyzes a local or remote git repository."""
        with tempfile.TemporaryDirectory() as temp_dir:
            if is_remote:
                utils.clone_repository(repo_path, temp_dir)
                repo_path = temp_dir
            contents = self.generate_contents(repo_path)
            contents = self.tokenize_content(contents)
            contents = self.process_language_mapping(contents)
        return contents

    def generate_contents(self, root_path: str) -> List[Dict]:
        """Generates a List of Dict of file information."""
        code_root = Path(root_path)
        data = list(self.generate_file_info(code_root))

        contents = []
        for name, path, content in data:
            extension = Path(name).suffix.lstrip(".")
            contents.append(
                {"name": name, "path": path, "content": content, "extension": extension}
            )
        return contents

    def get_dependency_file_contents(self, contents: List[Dict]) -> List[str]:
        """Extracts dependency file contents from the list of dicts."""
        file_parsers = self._get_file_parsers()
        dependency_files = [
            content
            for content in contents
            if any(file_name in content["name"] for file_name in file_parsers)
        ]

        parsed_contents = []
        for content in dependency_files:
            logger.info(f"Dependency file found: {content['name']}")
            # logger.info(f"Dependency file content: {content['content']}")
            parser = file_parsers[content["name"]]
            parsed_content = parser(content=content["content"])
            parsed_contents.append(parsed_content)

        return utils.flatten_list(parsed_contents)

    def generate_file_info(
        self, code_root: Path
    ) -> Generator[Tuple[str, Path, str], None, None]:
        """Generates a tuple of file information."""
        for file_path in code_root.rglob("*"):
            if file_path.is_file():
                if str(file_path.relative_to(code_root)).startswith(".git/"):
                    continue
                if ".github/workflows" in str(file_path.relative_to(code_root)):
                    yield "github actions", file_path.relative_to(code_root), ""
                try:
                    with file_path.open(encoding="utf-8") as file:
                        content = file.read()
                    relative_path = file_path.relative_to(code_root)
                    yield file_path.name, relative_path, content
                except UnicodeDecodeError:
                    continue

    def tokenize_content(self, contents: List[Dict]) -> List[Dict]:
        """Tokenizes the content of each file."""
        for content in contents:
            content["tokens"] = utils.get_token_count(
                content["content"], self.encoding_name
            )
        return contents

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

    @staticmethod
    def _get_file_parsers() -> Dict[str, callable]:
        """Returns a dictionary of callable file parser methods."""
        return {
            "build.gradle": parse.parse_gradle,
            "pom.xml": parse.parse_maven,
            "Cargo.toml": parse.parse_cargo_toml,
            "Cargo.lock": parse.parse_cargo_lock,
            "go.mod": parse.parse_go_mod,
            "go.sum": parse.parse_go_mod,
            "requirements.txt": parse.parse_requirements_file,
            "environment.yaml": parse.parse_conda_env_file,
            "environment.yml": parse.parse_conda_env_file,
            "Pipfile": parse.parse_pipfile,
            "Pipfile.lock": parse.parse_pipfile_lock,
            "poetry.lock": parse.parse_poetry_lock,
            "pyproject.toml": parse.parse_pyproject_toml,
            "package.json": parse.parse_package_json,
            "yarn.lock": parse.parse_yarn_lock,
            "package-lock.json": parse.parse_package_lock_json,
            "CMakeLists.txt": parse.parse_cmake,
            "Makefile.am": parse.parse_makefile_am,
            "configure.ac": parse.parse_configure_ac,
            "docker-compose.yaml": parse.parse_docker_compose,
        }
