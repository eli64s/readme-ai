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
LOGGER = Logger("PydocsAI_logger")


def main() -> None:
    LOGGER.warning("PydocsAI processing has begun.")

    cwd_path = Path.cwd()
    conf_file = Path(CONF).resolve()
    toml_file = FileFactory(conf_file).get_handler()
    conf_dict = toml_file.read_file()
    conf = dacite.from_dict(AppConfig, conf_dict)

    dirs = conf.github.dirs
    url = conf.github.url
    files = processor.clone_codebase(cwd_path, dirs, url)
    packages = files["packages"] + files["extensions"]

    LOGGER.info(f"Total files to document: {len(files)}")
    LOGGER.info(f"Project dependencies: {packages}")

    engine = conf.api.engine
    LOGGER.info(f"OpenAI Engine: {engine}")
    code_docs = model.code_to_text(engine, files)
    LOGGER.info(f"OpenAI code summary: {code_docs}")

    csv_file = FileFactory(conf.paths.docs).get_handler()
    csv_file.write_file(code_docs)
    builder.build(conf, packages, url)
    
    LOGGER.warning("PydocsAI processing complete.")
    LOGGER.warning("Find your project readme docs ➡️ docs/*")


if __name__ == "__main__":
    main()
