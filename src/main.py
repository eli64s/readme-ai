"""README-AI is a tool that generates a README.md file for your repository."""

import argparse
import asyncio
from pathlib import Path

import dacite
import openai
import pandas as pd

import builder
import model
import preprocess
from conf import AppConf, load_conf_helper
from file_factory import FileHandler
from logger import Logger

CONFIG_FILE = "conf/conf.toml"
LOGGER = Logger("readmeai_logger")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate a README.md file via OpenAI."
    )
    parser.add_argument("-k", "--api_key", type=str, help="OpenAI API key")
    parser.add_argument("-l", "--local", type=str, help="Local directory path")
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    parser.add_argument("-r", "--remote", type=str, help="Remote repository URL")
    return parser.parse_args()


def load_configuration(config_path):
    handler = FileHandler()
    conf_dict = handler.read(config_path)
    return dacite.from_dict(AppConf, conf_dict)


async def main() -> None:
    LOGGER.info("README-AI is now executing.")

    # Load configuration
    conf_path = Path(CONFIG_FILE).resolve()
    conf = load_configuration(conf_path)
    conf_helper = load_conf_helper(conf)

    # Parse command line arguments
    args = parse_arguments()
    if args.api_key:
        openai.api_key = args.api_key
    if args.output:
        conf.paths.md = args.output
    if args.local:
        conf.github.local = args.local
    if args.remote:
        conf.github.remote = args.remote

    # Process repository
    if args.local:
        LOGGER.info(f"Using local directory: {conf.github.local}")
        conf.github.path = conf.github.local
        repo_contents = preprocess.get_codebase_local(conf.github.local)
    else:
        LOGGER.info(f"Using GitHub remote repository: {conf.github.remote}")
        conf.github.path = conf.github.remote
        repo_contents = preprocess.get_codebase_remote(conf.github.remote)

    repo = conf.github.path
    name = preprocess.get_repo_name(repo)
    conf.github.name = name
    file_exts = conf_helper.file_extensions
    file_names = conf_helper.file_names
    ignore_files = conf_helper.ignore_files
    dependencies = preprocess.get_project_dependencies(repo, file_exts, file_names)

    LOGGER.info(f"Creating README.md for the repo: {name}")
    LOGGER.info(f"Total files to document: {len(repo_contents)}")
    LOGGER.info(f"\nProject dependencies and tools list: {dependencies}\n")

    # Use OpenAI API to generate documentation
    prompt_intro = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan
    codebase_docs = await model.code_to_text(ignore_files, repo_contents)
    introduction = model.generate_summary_text(prompt_intro.format(name))
    intro_slogan = model.generate_summary_text(prompt_slogan.format(name))
    conf.md.intro = conf.md.intro.format(introduction)
    documentation = pd.DataFrame(codebase_docs, columns=["Module", "Summary"])

    LOGGER.info(f"OpenAI generated codebase summaries:\n\n{documentation}\n")

    # Build README.md
    documentation.to_csv(conf.paths.docs, index=False)
    builder.build(conf, conf_helper, dependencies, documentation, intro_slogan)

    LOGGER.info("README-AI execution complete.\n")


if __name__ == "__main__":
    asyncio.run(main())
