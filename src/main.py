"""
src/main.py
"""
import dacite
import toml

import builder
import logger
import model
import processor
import utils
from conf import AppConfig


logger = logger.setup_logger()


def main() -> None:
    conf_dict = toml.load("conf/conf.toml")
    conf_objs = dacite.from_dict(AppConfig, conf_dict)

    url = conf_objs.store.url
    file_io = utils.FileHandler(conf_objs)
    docs_path = conf_objs.paths.docs

    files = processor.clone_codebase(url)
    pkgs = files["packages"] + files["extensions"]

    logger.info(f"\nTotal files to document: {len(files)}\n")
    logger.info(f"Project dependencies:\n{pkgs}\n")

    # file_summary = model.code_to_text(engine, files)
    # docs = pd.DataFrame(file_summary, columns=["file", "summary"])

    name = url.split("/")[-1]
    badges = builder.create_header(file_io, pkgs)
    html_docs = builder.create_html(conf_objs, badges, name, docs_path)
    file_io.write_html(html_docs)

    logger.info("Markdown documentation complete.")


if __name__ == "__main__":
    main()
