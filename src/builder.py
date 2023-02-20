"""src/format.py
"""
import subprocess
from pathlib import Path

import pandas as pd

from utils import FileFactory


def build(cfg, pkgs, url):
    file_factory = FileFactory(".")
    badges = file_factory.read_json(cfg.paths.badges)
    badges = get_badges(badges)
    name = url.split("/")[-1]

    html_head = get_header(cfg, badges, name, pkgs)
    html_body = get_body(cfg.html.body, cfg.paths.docs)
    html_tree = cfg.html.tree

    html_code = f"{html_head}{html_body}{html_tree}"
    file_factory.write_html(cfg.paths.html, html_code)

    html_setup = get_setup(cfg.html.setup, name, url)
    file_factory.write_html("docs/html/setup.html", html_setup)

    get_tree()

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
    pkgs.append("github")
    header = ""
    for pkg in pkgs:
        if pkg in badges:
            badge = badges[pkg.strip().lower()]["src"]
            header += f'<img src="{badge}">\n\t\t\t\t'

    header_html = f"""{cfg.html.head}<br><br>
    <h1>{name}</h1><br>
    <p>[insert-project-summary]</p>
    <br><h4>Software & Packages</h4>
    <p>{header}</p>
    </div>
    """
    return header_html


def get_body(body, path):
    data = pd.read_csv(path)

    prev_dir = None
    for i, j in data.iterrows():
        file = j[0].split("/")
        curr_dir = file[0]
        script = file[1]

        if prev_dir != curr_dir:
            body = f"""{body}<details closed>
            <summary>{curr_dir.upper()}</summary>"""

        tag = f"""
            <h5>{script}</h5>
            <p>{j[1].replace('"', '')}</p>
        """
        body = f"{body}{tag}"

        prev_dir = curr_dir
        if curr_dir != prev_dir:
            body = f"{body}<br></details><br>"
    # body = f"{body}<br></details><br>"
    return body


def get_setup(html, name, url):
    return html.format(url, name)


def get_tree() -> None:
    """_summary_"""
    cwd_path = Path.cwd()
    bash_path = f"{cwd_path}/scripts/build_md.sh"
    subprocess.call(["bash", bash_path])
