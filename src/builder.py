"""Builds the README Markdown file for your codebase."""

import subprocess
import tempfile
from pathlib import Path

import git
import pandas as pd

from conf import AppConfig, ConfigHelper
from factory import FileHandler
from logger import Logger

LOGGER = Logger("readmeai_logger")


def build(
    conf: AppConfig,
    conf_helper: ConfigHelper,
    packages: list,
    summaries: tuple,
) -> None:
    """Builds the README Markdown file for your codebase.

    Parameters
    ----------
    conf
        Configuration data class containing Markdown template strings.
    conf_helper
        Helper data class containing metadata to populate the README.
    packages
        List of project dependencies extracted from the user's repository.
    summaries
        Tuple of code summaries generated for each file in the repository.
    """
    name = conf.git.name
    repo = conf.git.repository
    cwd_path = Path.cwd()
    readme_path = cwd_path / conf.paths.readme
    badges_path = cwd_path / conf.paths.badges
    badges_dict = FileHandler().read(badges_path)

    md_badges = get_badges(badges_dict, packages)
    md_repository = create_directory_tree(repo)
    summary_df = format_markdown_table(summaries)
    md_tables = create_tables(summary_df, conf.md.dropdown)
    md_setup = create_setup_guide(conf.md.setup, conf_helper, summary_df)

    md_file_parts = [
        conf.md.header,
        conf.md.badges.format(md_badges),
        conf.md.toc,
        conf.md.intro,
        conf.md.tree,
        md_repository,
        conf.md.modules,
        md_tables,
        md_setup.format("{0}", "{1}", name, repo),
        conf.md.ending,
    ]
    md_file = "\n".join(md_file_parts)
    FileHandler().write(readme_path, md_file)
    LOGGER.info(f"README file generated at: {readme_path}")


def get_badges(svg_icons: dict, dependencies: list) -> str:
    """
    Generates badge icons for each dependency in the project.

    Parameters
    ----------
    svg_icons : dict
        Dictionary containing available icons and their src.
    ddependencies : list
        List of project dependencies.

    Returns
    -------
    str
        Formatted string containing badge icons for dependencies.
    """
    badges = []
    for dependency in dependencies:
        dependency = dependency.lower()
        if dependency in svg_icons:
            badges.append(svg_icons[dependency])

    LOGGER.info(f"SVG icons badges:\n\t{badges}")

    # Sort badges by hex value (from light to dark color)
    badges.sort(
        key=lambda badge: int(badge[1], 16) if badge[1] else 0, reverse=True
    )

    badges = [badge[0] for badge in badges]

    return format_badges(badges, dependencies)


def format_badges(badges: list, dependencies: list) -> str:
    """
    Formats the badges into a string with a maximum of 8 badges per line.

    Parameters
    ----------
    badges : list
        List of badge icons.
    dependencies : list
        List of project dependencies.

    Returns
    -------
    str
        Formatted string with badge icons arranged.
    """
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
                for dep, badge in zip(
                    dependencies[i : i + badges_per_line],
                    badges[i : i + badges_per_line],
                )
            ]
        )
        badge_lines.append(line)

    return "\n\n".join([f"{line}" for line in badge_lines])


def create_setup_guide(
    md_setup: str, conf_helper: ConfigHelper, summary_df: pd.DataFrame
):
    """
    Creates a setup guide for the project based on the top used language.

    Parameters
    ----------
    md_setup : str
        Markdown template string for the setup guide.
    conf_helper : object
        Configuration helper object containing file extensions and setup guide.
    summary_df : pd.DataFrame
        DataFrame containing parsed information from project files.

    Returns
    -------
    str
        Formatted string with setup guide.
    """
    try:
        md_install = md_run = "[📍 INSERT-INSTRUCTIONS_HERE]"

        summary_df["Language"] = summary_df["Module"].apply(
            lambda x: Path(x).suffix[1:]
            if Path(x).suffix[1:] not in conf_helper.ignore_files
            else None
        )

        top_language = summary_df["Language"].value_counts().idxmax()
        language_name = conf_helper.language_names[top_language]
        language_setup = conf_helper.language_setup[language_name]
        LOGGER.info(f"Top repository language: {top_language.upper()}")
        LOGGER.info(f"{language_name} setup guide: {language_setup}")

        if language_setup:
            md_install = language_setup[0]
            md_run = language_setup[1]

    except Exception as exc:
        LOGGER.debug(f"Error: {exc}\nUsing default setup: {md_run}")

    return md_setup.format("{2}", "{3}", md_install, md_run)


def create_directory_tree(url: str) -> str:
    """
    Creates a directory tree structure for the README.md
    file based on the provided repository path or URL.

    Parameters
    ----------
    url : str
        URL of the project's GitHub repository.

    Returns
    -------
    str
        Formatted string representing the project's directory tree structure.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        repo_path = Path(tmp_dir) / "repo"

        try:
            git.Repo.clone_from(url, repo_path)
            tree_bytes = subprocess.check_output(["tree", "-n", repo_path])
            tree_str = tree_bytes.decode("utf-8")
            tree_lines = tree_str.split("\n")[1:]
            tree_str = "\n".join(tree_lines)
            tree_md = f"```bash\n{repo_path.name}\n{tree_str}```"
            return tree_md

        except git.exc.GitCommandError as e:
            LOGGER.warning(f"Error cloning repository: {e}")
            return ""

        except subprocess.CalledProcessError as e:
            LOGGER.warning(f"Error running 'tree' command: {e}")
            return ""

        except Exception as e:
            LOGGER.warning(f"Error creating directory tree: {e}")
            return ""


def create_tables(df: pd.DataFrame, dropdown: str) -> str:
    """
    Creates markdown tables for each sub-directory in the project.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing parsed information from project files.
    dropdown : str
        Markdown template for a dropdown menu.

    Returns
    -------
    str
        Formatted string with markdown tables for each sub-directory.
    """

    df["Sub-Directory"] = df["Module"].apply(
        lambda x: str(x).split("/")[-2].capitalize()
        if "/" in str(x)
        else "Root"
    )
    groups = df.groupby("Sub-Directory")
    tables = [
        group[["File", "Summary", "Module"]].to_markdown(index=False)
        for _, group in groups
    ]
    table_wrappers = [
        dropdown.format(sub_dir_name, table)
        for sub_dir_name, table in zip(groups.groups.keys(), tables)
    ]
    return "\n".join(table_wrappers)


def format_markdown_table(summaries: tuple) -> pd.DataFrame:
    """
    Parses the Module field to create two additional DataFrame
    columns to be displayed in the README code summary tables.

    Parameters
    ----------
    summaries : tuple
        Tuple containing parsed information from project files.

    Returns
    -------
    pd.DataFrame
        Processed DataFrame with additional columns.
    """
    summary_df = pd.DataFrame(summaries, columns=["Module", "Summary"])
    summary_df["Directory"] = summary_df["Module"].apply(
        lambda x: str(Path(x).parent)
    )
    summary_df["File"] = summary_df["Module"].apply(
        lambda x: str(Path(x).name)
    )
    return summary_df
