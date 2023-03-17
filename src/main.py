"""
src/main.py
"""
from pathlib import Path

import dacite

import builder
import model
import processor
from conf import AppConfig
from logger import Logger
from utils import FileFactory


CONF = "conf/conf.toml"
LOGGER = Logger("my_logger")


def main() -> None:
    LOGGER.info("README-AI is now executing.")

    # Load config file
    cwd_path = Path.cwd()
    conf_file = Path(CONF).resolve()
    toml_file = FileFactory(conf_file).get_handler()
    conf_dict = toml_file.read_file()
    conf = dacite.from_dict(AppConfig, conf_dict)

    # Get project dependencies
    dirs = conf.github.dirs
    raw_docs = conf.paths.docs
    repo_url = conf.github.url
    files = processor.clone_codebase(cwd_path, dirs, repo_url)
    repo_name = processor.extract_repo_name(repo_url)
    repo_pkgs = files["packages"] + files["extensions"]

    LOGGER.info(f"Total files to document: {len(files)}")
    LOGGER.info(f"Project dependencies: {repo_pkgs}")

    # OpenAI API call
    prompt_feats = conf.api.prompt_features
    features = model.generate_readme_section(repo_url, prompt_feats)
    code_docs = model.code_to_text(files)

    LOGGER.info(f"OpenAI generated features: {features}")
    LOGGER.info(f"OpenAI generated documentation: {code_docs}")

    # Build Markdown file
    csv_file = FileFactory(raw_docs).get_handler()
    csv_file.write_file(code_docs)
    builder.build(conf, features, repo_pkgs, repo_name, repo_url)

    LOGGER.info("README-AI execution complete.")
    LOGGER.info("Find your project README.md ➡️ docs/*")


if __name__ == "__main__":
    main()
