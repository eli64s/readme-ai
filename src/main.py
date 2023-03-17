"""
src/main.py
"""
import argparse
from pathlib import Path

import dacite
import openai

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
    conf_file = Path(CONF).resolve()
    toml_file = FileFactory(conf_file).get_handler()
    conf_dict = toml_file.read_file()
    conf = dacite.from_dict(AppConfig, conf_dict)

    # Command line arguments
    parser = argparse.ArgumentParser(
        description="Generate a README.md file via OpenAI."
    )
    parser.add_argument(
        "-k", "--api_key", type=str, help="Provide your OpenAI API key."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Provide an output file path.",
        default=conf.paths.md,
    )

    args = parser.parse_args()
    openai.api_key = args.api_key
    if args.output != conf.paths.md:
        conf.paths.md = args.output

    # Get project dependencies
    repo_url = conf.github.url
    repo_full_name, repo_name = processor.extract_user_repo_from_url(repo_url)
    files = processor.fetch_github_folder_contents(repo_full_name)
    reqs = processor.dependencies_helper(repo_url)

    LOGGER.info(f"Total files to document: {len(files)}")
    LOGGER.info(f"Project dependencies: {reqs}")

    # OpenAI API
    prompt_feats = conf.api.prompt_features
    features_text = model.generate_readme_features(repo_url, prompt_feats)
    code_docs = model.code_to_text(files)

    LOGGER.info(f"OpenAI generated features: {features_text}")
    LOGGER.info(f"OpenAI generated documentation: {code_docs}")

    # Build README.md
    raw_docs = conf.paths.docs
    csv_file = FileFactory(raw_docs).get_handler()
    csv_file.write_file(code_docs)
    builder.build(conf, features_text, reqs, repo_name, repo_url)

    LOGGER.info("README-AI execution complete.")
    LOGGER.info("Find your project README.md ➡️ docs/*")


if __name__ == "__main__":
    main()
