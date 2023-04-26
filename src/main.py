"""README-AI is a tool that generates a README.md file for your repository."""
import argparse
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

CONF = "conf/conf.toml"
LOGGER = Logger("readme_ai_logger")


def main() -> None:
    LOGGER.info("README-AI is now executing.")

    # Configuration
    conf_path = Path(CONF).resolve()
    handler = FileHandler()
    conf_dict = handler.read(conf_path)
    conf = dacite.from_dict(AppConf, conf_dict)
    conf_helper = load_conf_helper(conf)

    # Command line arguments
    parser = argparse.ArgumentParser(
        description="Generate a README.md file via OpenAI."
    )
    parser.add_argument("-k", "--api_key", type=str, help="OpenAI API key")
    parser.add_argument("-o", "--output", type=str, help="Output file path")
    parser.add_argument("-r", "--remote", type=str, help="Remote repository URL")
    parser.add_argument("-l", "--local", type=str, help="Local directory path")

    args = parser.parse_args()
    if args.api_key:
        openai.api_key = args.api_key
    if args.output:
        conf.paths.md = args.output
    if args.local:
        conf.github.local = args.local
    if args.remote:
        conf.github.remote = args.remote

    # GitHub API / Local Directory
    if args.local:
        LOGGER.info(f"Using local directory: {conf.github.local}")
        conf.github.path = conf.github.local
        repo_contents = preprocess.get_local_codebase(conf.github.local)
    else:
        LOGGER.info(f"Using GitHub remote repository: {conf.github.remote}")
        conf.github.path = conf.github.remote
        repo_contents = preprocess.clone_codebase(conf.github.remote)

    repo = conf.github.path
    name = preprocess.get_repo_name(repo)
    conf.github.name = name
    file_names = conf_helper.file_names
    dependencies = preprocess.get_project_dependencies(file_names)

    LOGGER.info(f"Creating README.md for the repo: {name}")
    LOGGER.info(f"Total files to document: {len(repo_contents)}")
    LOGGER.info(f"\nProject dependencies and tools list: {dependencies}\n")

    # OpenAI API
    prompt = conf.api.prompt_intro
    prompt_slogan = conf.api.prompt_slogan
    codebase_docs = model.code_to_text(repo_contents)
    introduction = model.generate_summary_text(prompt.format(repo))
    intro_slogan = model.generate_summary_text(prompt_slogan.format(name))
    conf.md.intro = conf.md.intro.format(introduction)
    documentation = pd.DataFrame(codebase_docs, columns=["Module", "Summary"])

    LOGGER.info(f"OpenAI generated codebase summaries: {documentation}")

    # Build README.md
    documentation.to_csv(conf.paths.docs, index=False)
    builder.build(conf, conf_helper, dependencies, documentation, intro_slogan)

    LOGGER.info("README-AI execution complete.")


if __name__ == "__main__":
    main()
