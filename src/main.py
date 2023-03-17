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

    # Get config constants
    dirs = conf.github.dirs
    engine = conf.api.engine
    url = conf.github.url

    # Get project dependencies
    files = processor.clone_codebase(cwd_path, dirs, url)
    pkgs = files["packages"] + files["extensions"]

    LOGGER.info(f"Total files to document: {len(files)}")
    LOGGER.info(f"Project dependencies: {pkgs}")
    LOGGER.info(f"OpenAI Engine: {engine}")

    # OpenAI API call
    code_docs = model.code_to_text(engine, files)
    LOGGER.info(f"OpenAI code summary: {code_docs}")

    # Build Markdown file
    csv_file = FileFactory(conf.paths.docs).get_handler()
    csv_file.write_file(code_docs)
    builder.build(conf, pkgs, url)

    LOGGER.info("README-AI execution complete.")
    LOGGER.info("Find your project README.md ➡️ docs/*")


if __name__ == "__main__":
    main()
