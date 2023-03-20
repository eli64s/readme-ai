"""
src/format.py
"""
import subprocess
import tempfile

import git
import pandas as pd

import processor
from utils import FileFactory


def build(
    cfg: object, features: str, output_file: str, pkgs: list, name: str, url: str
) -> None:
    """_summary_

    Parameters
    ----------
    cfg
        _description_
    features
        _description_
    pkgs
        _description_
    name
        _description_
    url
        _description_
    """
    docs_path = cfg.paths.docs
    docs_df = pd.read_csv(docs_path)

    md = cfg.md.head
    md_body = cfg.md.body
    md_dropdown = cfg.md.dropdown
    md_modules = cfg.md.modules
    md_toc = cfg.md.toc
    md_tree = cfg.md.tree

    json_path = cfg.paths.badges
    json_file = FileFactory(json_path).get_handler()
    json_dict = json_file.read_file()
    badges = get_badges(json_dict)

    md_badges = get_header(badges, pkgs)
    md_body = md_body.format(features)
    md_instructions = processor.clone_repository_helper(cfg.md.instructions, name, url)
    md_repo = get_tree(url)
    md_tables = get_tables(docs_df, md_dropdown)
    md_toc = md_toc.format(name=name, name_lower=name.lower())

    md = md.format(name, md_badges)
    md = f"{md}{md_toc}{md_body}{md_tree}{md_repo}{md_modules}{md_tables}{md_instructions}"
    md_file = FileFactory(output_file).get_handler()
    md_file.write_file(md)


def get_badges(json_dict):
    """_summary_

    Parameters
    ----------
    json_dict
        _description_

    Returns
    -------
        _description_
    """
    icon_map = {}
    idx = 0
    while True:
        try:
            row = json_dict["icons"][idx]
            icon_map[row["name"].lower()] = row
        except:
            break
        idx += 1
    return icon_map


def get_header(badges, pkgs):
    """_summary_
    Parameters
    ----------
    badges
        _description_
    pkgs
        _description_
    Returns
    -------
        _description_
    """
    header = ""
    for pkg in pkgs:
        if pkg in badges:
            pkg_name = pkg.strip().lower()
            if not pkg_name:
                pkg_name = pkg.strip()
            badge = badges[pkg_name]["src"]
            header += f"\n> ![{pkg_name}]({badge})"
    return header


def get_tables(docs_df: pd.DataFrame, dropdown: str) -> str:
    """_summary_

    Parameters
    ----------
    docs_df
        _description_

    Returns
    -------
        _description_
    """
    docs_df = docs_df[~docs_df["Module"].isin(["extensions", "packages"])]
    docs_df[["Directory", "File Name"]] = docs_df["Module"].str.rsplit(
        "/", n=1, expand=True
    )
    tables = []
    for idx, group in docs_df.groupby("Directory"):
        table = group[["File Name", "Summary"]].to_markdown(index=False)
        table_wrapper = dropdown.format(idx.capitalize(), table)
        tables.append(table_wrapper)
    return "\n".join(tables)


def get_tree(url: str) -> str:
    """_summary_

    Parameters
    ----------
    url
        _description_

    Returns
    -------
        _description_
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        git.Repo.clone_from(url, tmp_dir)
        output_bytes = subprocess.check_output(["tree", "-n", tmp_dir])
        tree_str = output_bytes.decode("utf-8")
        tree_lines = tree_str.split("\n")[1:]
        tree_str = "\n".join(tree_lines)
        tree_md = f"```bash\n.\n{tree_str}```"
        return tree_md
