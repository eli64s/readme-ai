"""src/format.py
"""
import os
import subprocess
import tempfile

import git
import pandas as pd

from utils import FileFactory


def build(cfg, pkgs, url):
    pkgs.append("markdown")
        
    md_code = cfg.md.head
    md_body = cfg.md.body
    md_tree = cfg.md.tree
    md_modules = cfg.md.modules
    md_usage = cfg.md.usage

    json_path = cfg.paths.badges
    json_file = FileFactory(json_path).get_handler()
    badges = json_file.read_file()
    badges = get_badges(badges)
    name = url.split("/")[-1]

    md_badges = get_header(badges, pkgs)
    md_code = md_code.format(name, md_badges)
    md_code = f"{md_code}{md_body}{md_tree}"

    md_repo = get_tree(url)
    md_tables = get_tables(cfg.paths.docs)
    md_usage = md_usage.format(url, name)
    md_code = f"{md_code}{md_repo}{md_modules}{md_tables}{md_usage}"

    md_file = FileFactory(cfg.paths.md).get_handler()
    md_file.write_file(md_code)


def get_badges(icon_list):
    """_summary_

    Parameters
    ----------
    icon_list
            _description_

    Returns
    -------
            _description_
    """
    icon_map = {}
    idx = 0
    while True:
        try:
            row = icon_list["icons"][idx]
            icon_map[row["name"].lower()] = row
        except:
            break
        idx += 1
    return icon_map


def get_header(badges, pkgs):
    """_summary_

    Parameters
    ----------
    file_io
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
            if cnt % 4 == 0:
                header += "\n\n"
            header += f"![{pkg_name}]({badge})"
            cnt += 1
    return header


def get_tables(path):
    df = pd.read_csv(path)
    df[["path", "file"]] = df["module"].str.rsplit("/", n=1, expand=True)
    md_tables = []
    for index, group in df.groupby("path"):
        md_table = group[["file", "summary"]].to_markdown(index=False)
        md_tables.append(f"## {index}\n{md_table}")
    md_code = "\n".join(md_tables)
    return md_code


def get_tree(url) -> None:
    """_summary_

    Parameters
    ----------
    url
        _description_
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        git.Repo.clone_from(url, tmp_dir)
        output_bytes = subprocess.check_output(["tree", "-n", tmp_dir])
        output_str = output_bytes.decode("utf-8")
        markdown_str = f"```bash\n{output_str}```"
        return markdown_str
