#!/usr/bin/env python
import logging
from pathlib import Path

import hydra
import pandas as pd
from omegaconf import DictConfig

import gpt_model
import processor

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    """Main function for the program.

    Args:
        cfg: A dictionary of configuration parameters.

    Returns:
        None
    """
    output_dir = Path("data/output/file_docs.csv").resolve()
    path = cfg.input.input_path
    engine = cfg.api.engine

    dir = processor.clone_codebase(path)
    files = processor.parse_codebase(dir)

    file_summary = gpt_model.code_to_text(engine, files)

    cols = ["file", "summary"]
    df = pd.DataFrame(file_summary, columns=cols)
    df.to_csv(output_dir, index=False)


if __name__ == "__main__":
    main()
