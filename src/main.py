"""
src/main.py
"""
import dacite

import builder
import model
import processor
from conf import AppConfig
from logger import Logger
from utils import FileFactory


CONF = "conf/conf.toml"
LOGGER = Logger("PyDocsAI_logger")


def main() -> None:
    LOGGER.warning("PyDocsAI processing has begun.")

    file_factory = FileFactory(".")
    conf_dict = file_factory.read_toml(CONF)
    conf = dacite.from_dict(AppConfig, conf_dict)

    url = conf.github.url
    files = processor.clone_codebase(url)
    packages = files["packages"] + files["extensions"]

    LOGGER.info(f"Total files to document: {len(files)}")
    LOGGER.info(f"Project dependencies: {packages}")

    engine = conf.api.engine
    LOGGER.info(f"OpenAI Engine: {engine}")

    code_summary = model.code_to_text(engine, files)
    LOGGER.info(f"OpenAI code summary: {code_summary}")

    file_factory.write_csv(conf.paths.docs, code_summary)

    builder.build(conf, packages, url)
    LOGGER.warning("PyDocsAI processing complete.")
    LOGGER.warning("Find your project readme docs ➡️ docs/*")


if __name__ == "__main__":
    main()
