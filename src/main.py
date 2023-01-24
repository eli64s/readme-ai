"""
src/main.py
"""
from pathlib import Path

import hydra
import pandas as pd
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
    pkgs_path = cfg.pkgs
    doc_path = cfg.docs

    files = processor.clone_codebase(url)

    files = processor.clone_codebase(url)
    logger.info(f"Total files to document: {len(files)}")

    # file_summary = model.code_to_text(engine, files)
    # docs = pd.DataFrame(file_summary, columns=["file", "summary"])

    name = url.split("/")[-1]
    pkgs = files["packages"] + files["extensions"]
    badges = builder.create_header(pkgs_path, pkgs)
    html_docs = builder.create_html(cfg, badges, name, doc_path)

    logger.info(f"Markdown documentation complete.")


if __name__ == "__main__":
    main()
