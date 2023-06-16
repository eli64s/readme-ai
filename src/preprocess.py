"""Handles preprocessing of the input codebase."""

import shutil
import tempfile
from pathlib import Path
from typing import Dict, List

import pandas as pd
import tiktoken

import conf
import parse
import utils


class TempDirectory:
    """Creates a temporary directory."""

    def __enter__(self):
        self.temp_dir = tempfile.mkdtemp()
        return self.temp_dir

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.temp_dir)


class RepositoryParserWrapper:

    def __init__(self, conf: conf.AppConfig, conf_helper: conf.ConfigHelper):
        self.parser = RepositoryParser(
            conf,
            conf_helper.ignore_files["directories"],
            conf_helper.ignore_files["files"],
            conf_helper.ignore_files["extensions"],
            conf_helper.language_names,
            conf_helper.language_setup,
        )

    def get_unique_contents(self, contents, keys):
        unique_contents = [contents[key].unique().tolist() for key in keys]
        return list(set(utils.flatten_list(unique_contents)))

    def get_file_contents(self, contents):
        return contents.set_index("path")["content"].to_dict()

    def get_dependencies(self, repository, is_remote=True):
        contents = self.parser.analyze(repository, is_remote)
        dependencies = self.parser.get_dependency_file_contents(contents)
        attributes = ["extension", "language", "name"]
        dependencies.extend(self.get_unique_contents(contents, attributes))
        return dependencies, self.get_file_contents(contents)


class RepositoryParser:
    """Analyzes a local or remote git repository."""

    def __init__(
        self,
        conf: conf.AppConfig,
        ignore_dirs: set,
        ignore_filenames: set,
        ignore_extensions: set,
        language_names: dict,
        language_setup: dict,
    ):
        self.ignore_dirs = ignore_dirs
        self.ignore_filenames = ignore_filenames
        self.ignore_extensions = ignore_extensions
        self.language_names = language_names
        self.language_setup = language_setup
        self.encoding_name = conf.api.encoding

    def is_file_valid(self, path: Path) -> bool:
        """Checks if a file is valid for processing."""
        return (
            path.is_file() and
            all(idir not in path.parts for idir in self.ignore_dirs) and
            path.name not in self.ignore_filenames and
            path.suffix not in self.ignore_extensions
        )

    def generate_file_info(self, code_root: Path):
        """Generates a tuple of file information."""
        for p in code_root.rglob("*"):
            if p.is_file():
                if str(p.relative_to(code_root)).startswith(".git/"):
                    continue
                try:
                    with p.open(encoding="utf-8") as file:
                        content = file.read()
                    relative_path = p.relative_to(code_root)
                    yield p.name, relative_path, content
                except UnicodeDecodeError:
                    continue

    def num_tokens_from_string(self, string: str) -> int:
        """Returns the number of tokens in a string."""
        encoding = tiktoken.get_encoding(self.encoding_name)
        return len(encoding.encode(string))

    def tokenize_content(self, df):
        """Tokenizes the content of each file."""
        df["tokens"] = df["content"].map(self.num_tokens_from_string)
        return df

    def analyze(self, root_path: str, is_remote: bool = False) -> pd.DataFrame:
        """Analyzes a local or remote git repository."""
        with TempDirectory() as temp_dir:
            if is_remote:
                self.clone_remote_repo(root_path, temp_dir)
                root_path = temp_dir
            df = self.generate_dataframe(root_path)
            df = self.tokenize_content(df)
            df = self.process_language_mapping(df)
        return df

    def clone_remote_repo(self, remote_url, local_path):
        """Clone a remote git repository."""
        try:
            utils.clone_repository(remote_url, local_path)
        except Exception as exc:
            raise (f"Error cloning repository {remote_url}: {exc}")

    def generate_dataframe(self, root_path):
        """Generates a dataframe of file information."""
        code_root = Path(root_path)
        data = list(self.generate_file_info(code_root))
        df = pd.DataFrame(data, columns=["name", "path", "content"])
        df["extension"] = df["name"].map(lambda x: Path(x).suffix.lstrip("."))
        return df

    def process_language_mapping(self, df: pd.DataFrame) -> pd.DataFrame:
        """Maps file extensions to their programming languages."""
        language_map = pd.DataFrame.from_records(
            list(self.language_names.items()),
            columns=["extension", "language"],
        )
        language_map["language"] = language_map["language"].str.lower()
        language_setup = pd.DataFrame.from_records(
            list(self.language_setup.items()), columns=["language", "setup"]
        )
        language_setup["language"] = language_setup["language"].str.lower()

        df = df.merge(language_map, on="extension", how="left")
        df = df.merge(language_setup, on="language", how="left")
        df["setup"] = df["setup"].apply(
            lambda x: x if isinstance(x, list) else [None, None]
        )
        df[["install", "run", "test"]] = pd.DataFrame.from_records(
            df["setup"].to_list(), columns=["install", "run", "test"]
        )
        return df[[
            "name",
            "tokens",
            "content",
            "install",
            "run",
            "test",
            "extension",
            "language",
            "path",
        ]]

    def get_dependency_file_contents(self, df: pd.DataFrame) -> List[str]:
        """Extracts dependency file contents from the dataframe."""
        file_parsers = self._get_file_parsers()

        dependency_files = df[df["name"].str.contains("|".join(file_parsers.keys()))]

        parsed_contents = []
        for _, row in dependency_files.iterrows():
            parser = file_parsers[row["name"]]
            content = row["content"]
            parsed_content = parser(content)
            parsed_contents.append(parsed_content)

        return utils.flatten_list(parsed_contents)

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
            "pyproject.toml": parse.parse_pyproject_toml,
            "package.json": parse.parse_package_json,
            "yarn.lock": parse.parse_yarn_lock,
            "package-lock.json": parse.parse_package_lock_json,
            "CMakeLists.txt": parse.parse_cmake,
            "Makefile.am": parse.parse_makefile_am,
            "configure.ac": parse.parse_configure_ac,
            "docker-compose.yaml": parse.parse_docker_compose,
        }
