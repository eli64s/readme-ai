"""
src/main.py
"""
import logging

import hydra
from omegaconf import DictConfig

import chatgpt_engine
import utils

logger = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    apikey = cfg.api.sk
    path = cfg.input.input_path

    utils.clone_codebase(path)

    # file_list = utils.parse_codebase()

    # summary_text = chatgpt_engine.annotate_file(apikey, file_list)

    # logger.info(f"{summary_text}")


if __name__ == "__main__":
    main()
