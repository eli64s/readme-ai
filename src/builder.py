"""
src/format.py
"""
import subprocess
import tempfile

import git
import pandas as pd

from utils import FileFactory


def build(cfg: object, pkgs: list, url: str) -> None:
    """_summary_

    Parameters
    ----------
    cfg
        _description_
    pkgs
        _description_
    url
        _description_
    """
    pkgs.append("markdown")
    name = url.split("/")[-1]

    docs_path = cfg.paths.docs
    docs_df = pd.read_csv(docs_path)

    md = cfg.md.head
    md_body = cfg.md.body
    md_tree = cfg.md.tree
    md_modules = cfg.md.modules
    md_usage = cfg.md.usage

    json_path = cfg.paths.badges
    json_file = FileFactory(json_path).get_handler()

    badges = json_file.read_file()
    badges = get_badges(badges)
    md_badges = get_header(badges, pkgs)

    md = md.format(name, md_badges)
    md = f"{md}{md_body}{md_tree}"

    md_repo = get_tree(url)
    md_tables = get_tables(docs_df)
    md_usage = md_usage.format(name, url, name, name, name)

    md = f"{md}{md_repo}{md_modules}{md_tables}{md_usage}"
    md_file = FileFactory(cfg.paths.md).get_handler()
    md_file.write_file(md)


def get_badges(icon_dict):
    """_summary_

    Parameters
    ----------
    icon_dict
        _description_

    Returns
    -------
        _description_
    """
    icon_map = {}
    idx = 0
    while True:
        try:
            row = icon_dict["icons"][idx]
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
    cnt = 0
    header = ""
    for pkg in pkgs:
        if pkg in badges:
            pkg_name = pkg.strip().lower()
            badge = badges[pkg_name]["src"]
            header += f"![{pkg_name}]({badge})"
    return header


def get_tables(docs_df: pd.DataFrame) -> str:
    """_summary_

    Parameters
    ----------
    docs_df
        _description_

    Returns
    -------
        _description_
    """
    docs_df[["path", "file"]] = docs_df["module"].str.rsplit("/", n=1, expand=True)
    md_tables = []
    for idx, group in docs_df.groupby("path"):
        md_table = group[["file", "summary"]].to_markdown(index=False)
        md_tables.append(f"## {idx}\n{md_table}")
    md_code = "\n".join(md_tables)
    return md_code


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
        tree_md = f"```bash\n{tree_str}```"
        return tree_md
