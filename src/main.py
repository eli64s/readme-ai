"""
src/main.py
"""
import hydra
from omegaconf import DictConfig

import builder
import logger
import model
import processor
import utils


logger = logger.setup_logger()


@hydra.main(version_base=None, config_path="../conf", config_name="config")
def main(cfg: DictConfig) -> None:
    engine = cfg.driver.engine
    url = cfg.repository.url
    pkgs_path = cfg.pkgs_file
    doc_path = cfg.doc_file

    files = processor.clone_codebase(url)
    pkgs = files["packages"] + files["extensions"]

    logger.info(f"\n{pkgs}\n")
    logger.info(f"\n{exts}\n")
    logger.info(f"Total files to document: {len(files)}")

    # file_summary = model.code_to_text(engine, files)
    # docs = pd.DataFrame(file_summary, columns=["file", "summary"])

    name = url.split("/")[-1]
    badges = builder.create_header(pkgs_path, pkgs)
    html_docs = builder.create_html(cfg, badges, name, doc_path)
    utils.write_file(html_docs, cfg.html_file, cfg.md_file)

    logger.info(f"Markdown documentation complete.")


if __name__ == "__main__":
    main()
