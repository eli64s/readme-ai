"""Builds the README.md file from the template and the data."""

import subprocess
import tempfile
from pathlib import Path

import git
import pandas as pd

from file_factory import FileHandler
from logger import Logger

LOGGER = Logger("readme_ai_logger")
IGNORE = [
    "lock",
    "pyc",
    "yml",
    "yaml",
    "config",
    "log",
    "ini",
    "cfg",
    "xml",
    "toml",
    "git",
    "idea",
    "__pycache__",
    "__init__",
    "requirements",
    "setup",
    "test",
]


def build(
    conf: object, conf_helper: object, dependencies: list, df: pd.DataFrame, intro: str
) -> None:
    name = conf.github.name
    url = conf.github.path

    md_file = conf.md.head
    md_close = conf.md.close
    md_intro = conf.md.intro
    md_dropdown = conf.md.dropdown
    md_modules = conf.md.modules
    md_setup = conf.md.setup
    md_toc = conf.md.toc
    md_tree = conf.md.tree

    cwd_path = Path.cwd()
    handler = FileHandler()
    json_path = cwd_path / conf.paths.badges
    json_dict = handler.read(json_path)

    df_cleaned = parse_pandas_cols(df)
    md_badges = get_badges(json_dict, dependencies)
    md_tables = create_tables(df_cleaned, md_dropdown)
    md_repo = create_directory_tree(url)
    md_setup = create_setup_guide(conf, conf_helper, df_cleaned)
    md_file = md_file.format(name, intro, md_badges)
    md_file = f"{md_file}{md_toc}{md_intro}{md_tree}{md_repo}"
    md_file = f"{md_file}{md_modules}{md_tables}{md_setup}{md_close}"

    md_path = cwd_path / conf.paths.md
    handler.write(md_path, md_file)

    LOGGER.info(f"README.md file created at: {md_path}")


def get_badges(data: dict, dependencies: list) -> str:
    badges = []
    icons_sorted = sorted(data["icons"], key=lambda x: x["color"])
    dependencies = list(set(dependencies))
    for dep in dependencies:
        for icon in icons_sorted:
            if dep.lower() == icon["name"].lower():
                badges.append(icon["src"])
                break  # found a match, move to the next dependency

    badge_lines = []
    total_badges = len(badges)
    if total_badges < 8:
        badges_per_line = total_badges
    else:
        badges_per_line = total_badges // 2 + (total_badges % 2)

    if badges_per_line == 0:
        return ""

    for i in range(0, total_badges, badges_per_line):
        line = "\n".join(
            [
                f'<img src="{badge}" alt="{dep}" />'
                for dep, badge in zip(
                    dependencies[i : i + badges_per_line],
                    badges[i : i + badges_per_line],
                )
            ]
        )
        badge_lines.append(line)

    return "\n\n".join([f"{line}" for line in badge_lines])


def create_setup_guide(conf: object, conf_helper: object, df: pd.DataFrame):
    install_guide = "[INSERT INSTALL GUIDE HERE]"
    run_guide = "[INSERT RUN GUIDE HERE]"

    name = conf.github.name
    path = conf.github.path

    df["Language"] = df["Module"].apply(
        lambda x: Path(x).suffix[1:] if Path(x).suffix[1:] not in IGNORE else None
    )
    top_language = df["Language"].value_counts().idxmax()

    try:
        language_name = conf_helper.file_extensions[top_language]
        language_setup = conf_helper.setup[language_name]

        LOGGER.info(f"Top language: {top_language}")
        LOGGER.info(f"Language name: {language_name}")
        LOGGER.info(f"Language setup: {language_setup}")

        if language_setup:
            install_guide = language_setup[0]
            run_guide = language_setup[1]

    except KeyError as ke:
        LOGGER.warning(f"KeyError: {ke}. Using default install and run guides.")

    md_setup_guide = conf.md.setup.format(
        name, path, name, install_guide, name, run_guide
    )

    return md_setup_guide


def create_directory_tree(url: str) -> str:
    with tempfile.TemporaryDirectory() as tmp_dir:
        git.Repo.clone_from(url, tmp_dir)
        output_bytes = subprocess.check_output(["tree", "-n", tmp_dir])
        tree_str = output_bytes.decode("utf-8")
        tree_lines = tree_str.split("\n")[1:]
        tree_str = "\n".join(tree_lines)
        tree_md = f"```bash\n.\n{tree_str}```"
        return tree_md


def create_tables(df: pd.DataFrame, dropdown: str) -> str:
    tables = []
    for dir_name, group in df.groupby("Directory"):
        table = group[["File", "Summary"]].to_markdown(index=False)
        table_wrapper = dropdown.format(dir_name.capitalize(), table)
        tables.append(table_wrapper)
    return "\n".join(tables)


def parse_pandas_cols(df: pd.DataFrame) -> pd.DataFrame:
    df["Directory"] = df["Module"].apply(lambda x: str(Path(x).parent))
    df["File"] = df["Module"].apply(lambda x: str(Path(x).name))
    return df
