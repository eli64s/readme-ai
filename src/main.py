#!/usr/bin/env python
from pathlib import Path

import hydra
import pandas as pd
from markdownify import markdownify as md
from omegaconf import DictConfig

import builder
import logger
import model
import processor

logger = logger.setup_logger()


@hydra.main(version_base=None, config_path="../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    """Main function for the program."""
    url = cfg.input.url
    engine = cfg.api.engine
    outdir = Path(cfg.outdir).resolve()

    tmpdir = processor.clone_codebase(url)
    files = processor.parse_codebase(tmpdir)

    logger.info(f"Total files to document: {len(files)}")

    file_summary = model.code_to_text(engine, files)

    logger.info("code-to-text done.")

    df = pd.DataFrame(file_summary, columns=["file", "summary"])
    df.to_csv(outdir, index=False)

    html_docs = builder.create_html()
    md_docs = md(html_docs)
    with open("data/docs/markdown.html", "w") as file:
        file.write(html_docs)
    with open("data/docs/markdown.md", "w") as file:
        file.write(md_docs)

    logger.info("ChatGPT code-to-language model is complete.")


if __name__ == "__main__":
    main()
