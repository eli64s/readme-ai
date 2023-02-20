"""src/format.py
"""
import os
import subprocess
import tempfile
import git
import pandas as pd

from utils import FileFactory


def build(cfg, pkgs, url):
    file_factory = FileFactory(".")
    badges = file_factory.read_json(cfg.paths.badges)
    badges = get_badges(badges)
    name = url.split("/")[-1]
    
    html_body = cfg.html.body
    html_tree = cfg.html.tree
    html_head = get_header(cfg, badges, name, pkgs)

    html_code = f"{html_head}{html_body}{html_tree}"
    file_factory.write_html(cfg.paths.html, html_code)
    
    html_setup = get_setup(cfg.html.setup, name, url)
    file_factory.write_html("docs/html/setup.html", html_setup)
    
    md_tables = get_tables(cfg.paths.docs)
    file_factory.write_md("docs/markdown/tables.md", md_tables)
    
    get_tree(url)
    
    return html_code


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


def get_header(cfg, badges, name, pkgs):
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
    pkgs.append("markdown")
    header = ""
    for pkg in pkgs:
        if pkg in badges:
            badge = badges[pkg.strip().lower()]["src"]
            header += f'<img src="{badge}">\n\t\t\t\t'

    header_html = f"""{cfg.html.head}<br><br>
    <h1>{name}</h1><br>
    <p>[insert-project-summary]</p>
    <br><p>{header}</p>
    </div>
    """
    return header_html


def get_setup(html, name, url):
    return html.format(url, name)


def get_tables(path):
    df = pd.read_csv(path)
    df[['path', 'file']] = df['module'].str.rsplit('/', n=1, expand=True)
    markdown_tables = []
    for index, group in df.groupby('path'):
        markdown_table = group[['file','summary']].to_markdown(index=False)
        markdown_tables.append(f'## {index}\n{markdown_table}')
    md_code = '\n'.join(markdown_tables)
    return md_code


def get_tree(url) -> None:
    """_summary_

    Parameters
    ----------
    url
        _description_
    """
    root_dir = os.getcwd()
    tree_path = f"{root_dir}/docs/markdown/tree.md"

    with tempfile.TemporaryDirectory() as tmp_dir:
        git.Repo.clone_from(url, tmp_dir)
        output_bytes = subprocess.check_output(["tree", "-n", tmp_dir])
        output_str = output_bytes.decode("utf-8")

        markdown_str = f"```bash\n{output_str}```"
        markdown_file = os.path.join(root_dir, "docs/markdown/tree.md")

        with open(markdown_file, "w") as f:
            f.write(markdown_str)
        with open(markdown_file, "r") as f:
            lines = f.readlines()
            lines.pop(1)
            lines.pop(-2)
        with open(tree_path, "w") as f:
            f.writelines(lines)