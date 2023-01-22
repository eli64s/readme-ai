import os
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
    """Main function for the program."""
    url = cfg.input.url
    engine = cfg.api.engine
    html_path = Path(cfg.html_file).resolve()
    pkgs_path = Path(cfg.pkgs_file).resolve()
    text_path = Path(cfg.text_file).resolve()

    tmpdir = processor.clone_codebase(url)
    files = processor.parse_codebase(tmpdir)
    logger.info(f"Total files to document: {len(files)}")

    file_summary = model.code_to_text(engine, files)
    docs = pd.DataFrame(file_summary, columns=["file", "summary"])
    docs.to_csv(text_path, index=False)

    pkg_list = utils.get_pkgs_list()
    name = url.split('/')[-1]
    html_docs = builder.create_header(pkgs_path, pkg_list, name)
    utils.write_file(html_path, html_docs)
    
    logger.info(f"Markdown documentation complete.")


if __name__ == "__main__":
    main()
