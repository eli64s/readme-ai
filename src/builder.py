"""Builds the README Markdown file for your codebase."""

import subprocess
import tempfile
from pathlib import Path

import pandas as pd

import utils
from conf import AppConfig, ConfigHelper
from factory import FileHandler
from logger import Logger

LOGGER = Logger("readmeai_logger")


def build_readme(
    conf: AppConfig,
    conf_helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> None:
    """Builds the README Markdown file for your codebase."""
    readme_parts = create_readme_parts(conf, conf_helper, packages, summaries)
    readme_file = "\n".join(readme_parts)
    readme_path = Path.cwd() / conf.paths.readme
    FileHandler().write(readme_path, readme_file)
    LOGGER.info(f"README file generated at: {readme_path}")


def create_readme_parts(
    conf: AppConfig,
    conf_helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> list:
    """Creates each section of the README Markdown file."""
    name = conf.git.name
    repo = conf.git.repository
    cwd_path = Path.cwd()
    badges_path = cwd_path / conf.paths.badges
    badges_dict = FileHandler().read(badges_path)

    md_badges = get_badges(badges_dict, packages)
    md_repository = create_directory_tree(repo)
    summary_df = create_markdown_tables(summaries)
    md_tables = create_tables(summary_df, conf.md.dropdown)
    md_using = create_setup_guide(conf, conf_helper, summary_df)

    md_file_parts = [
        conf.md.header,
        conf.md.badges.format(md_badges),
        conf.md.toc,
        conf.md.intro,
        conf.md.tree,
        md_repository,
        conf.md.modules,
        md_tables,
        conf.md.setup.format(name, repo, *md_using),
        conf.md.ending,
    ]
    return md_file_parts


def get_badges(svg_icons: dict, dependencies: list) -> str:
    """Returns a list of badges for the project dependencies."""
    badges = [
        svg_icons[str(dependency).lower()]
        for dependency in dependencies
        if str(dependency).lower() in svg_icons
    ]
    # Sort badges by hex value (from light to dark color)
    badges.sort(
        key=lambda badge: int(badge[1], 16) if badge[1] else 0, reverse=True
    )
    badges = [badge[0] for badge in badges]

    return format_badges(badges)


def format_badges(badges: list) -> str:
    """Formats the svg icons into Markdown image tags."""
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
                f'<img src="{badge}" alt="{badge.split("/badge/")[1].split("-")[0]}" />'
                for badge in badges[i : i + badges_per_line]
            ]
        )
        badge_lines.append(line)

    return "\n\n".join([f"{line}" for line in badge_lines])


def create_markdown_tables(summaries: tuple) -> pd.DataFrame:
    """Formats the generated code summaries into a DataFrame."""
    summary_df = pd.DataFrame(summaries, columns=["Module", "Summary"])
    summary_df["Directory"] = summary_df["Module"].apply(
        lambda x: str(Path(x).parent)
    )
    summary_df["File"] = summary_df["Module"].apply(
        lambda x: str(Path(x).name)
    )
    return summary_df


def create_setup_guide(
    conf: AppConfig, conf_helper: ConfigHelper, summary_df: pd.DataFrame
):
    """Creates the 'Getting Started' section of the README file."""
    try:
        md_install = md_run = md_test = conf.md.default

        summary_df["Language"] = summary_df["Module"].apply(
            lambda x: Path(x).suffix[1:]
            if Path(x).suffix[1:] not in conf_helper.ignore_files
            else None
        )

        top_language = summary_df["Language"].value_counts().idxmax()
        language_name = conf_helper.language_names[top_language]
        language_setup = conf_helper.language_setup[language_name]
        LOGGER.info(f"Top language: {language_name.title()} (.{top_language})")
        LOGGER.info(f"{language_name} setup guide: {language_setup}")

        if language_setup:
            md_install = language_setup[0]
            md_run = language_setup[1]
            md_test = language_setup[2]

    except Exception as exc:
        LOGGER.debug(f"Error: {exc}\nUsing default setup: {md_run}")

    return (md_install, md_run, md_test)


def create_tables(df: pd.DataFrame, dropdown: str) -> str:
    """Creates Markdown tables for each sub-directory in the project."""
    df["Sub-Directory"] = df["Module"].apply(
        lambda x: str(x).split("/")[-2].capitalize()
        if "/" in str(x)
        else "Root"
    )
    tables = []
    for sub_dir_name, group in df.groupby("Sub-Directory"):
        table = group[["File", "Summary", "Module"]].to_markdown(index=False)
        table_wrappers = dropdown.format(sub_dir_name, table)
        tables.append(table_wrappers)
    return "\n".join(tables)


def create_directory_tree(url: str) -> str:
    """Creates a directory tree for the project."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        repo_path = Path(tmp_dir) / "repo"
        try:
            utils.clone_repository(url, repo_path)
            tree_str = run_tree_command(repo_path)
            return f"```bash\n{repo_path.name}\n{tree_str}```"
        except Exception as exc:
            LOGGER.warning(f"Error creating directory tree: {exc}")
            return ""


def run_tree_command(repo_path: Path) -> str:
    """Executes the 'tree' command to generate a directory tree."""
    try:
        tree_bytes = subprocess.check_output(["tree", "-n", repo_path])
        tree_str = tree_bytes.decode("utf-8")
        tree_lines = tree_str.split("\n")[1:]
        tree_str = "\n".join(tree_lines)
        return tree_str
    except subprocess.CalledProcessError as exc:
        raise (f"Error running 'tree' command: {exc}")
