"""
src/main.py
"""
import argparse
from pathlib import Path

import dacite
import openai
import pandas as pd

import builder
import model
import processor
from conf import AppConf, load_conf_helper
from file_factory import FileHandler
from logger import Logger

CONF = "conf/conf.toml"
CONF_HELPER = ["file_names.toml", "file_extensions.toml", "setup_guide.toml"]
LOGGER = Logger("readme_ai_logger")


def main() -> None:
    LOGGER.info("README-AI is now executing.")

    # Configuration
    conf_path = Path(CONF).resolve()
    handler = FileHandler()
    conf_dict = handler.read(conf_path)
    conf = dacite.from_dict(AppConf, conf_dict)
    conf_helper = load_conf_helper(CONF_HELPER)

    # Command line arguments
    parser = argparse.ArgumentParser(
        description="Generate a README.md file via OpenAI."
    )
    parser.add_argument("-k", "--api_key", type=str, help="Your OpenAI API key")
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    parser.add_argument("-u", "--url", type=str, help="URL for the repository")

    args = parser.parse_args()
    if args.api_key:
        openai.api_key = args.api_key
    if args.output:
        conf.paths.md = args.output
    if args.url:
        conf.github.url = args.url

    # GitHub API
    repo_url = conf.github.url
    repo_name = conf.github.repo_name
    file_names = conf_helper.file_names
    repo_contents = processor.fetch_github_repo_files_recursive(repo_url)
    dependencies = processor.create_dependency_list(file_names, repo_contents)

    LOGGER.info(f"Creating README.md for the repo: {repo_name}")
    LOGGER.info(f"Total files to document: {len(dependencies)}")
    LOGGER.info(f"Project dependencies and tools list: {dependencies}")

    # OpenAI API
    prompt = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan
    codebase_docs = model.code_to_text(repo_contents)
    introduction = model.generate_summary_text(prompt.format(repo_url))
    intro_slogan = model.generate_summary_text(prompt_slogan.format(repo_name))
    conf.md.intro = conf.md.intro.format(introduction)
    documentation = pd.DataFrame(codebase_docs, columns=["Module", "Summary"])

    LOGGER.info(f"OpenAI generated codebase summaries: {documentation}")

    # Build README.md
    documentation.to_csv(conf.paths.docs, index=False)
    builder.build(conf, conf_helper, dependencies, documentation, intro_slogan)

    LOGGER.info("README-AI execution complete.")


if __name__ == "__main__":
    main()
